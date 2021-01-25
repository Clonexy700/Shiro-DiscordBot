import asyncio
import functools
import itertools
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

# Silence bug report messages
youtube_dl.utils.bug_reports_message = lambda: ''


# youtube-dl is a command line program used to download videos from sites
class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': False,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def swap(self, x: int, y: int):
        temp = self._queue[x]
        self._queue[x] = self._queue[y]
        self._queue[y] = temp
        return

    def shuffle(self):
        random.shuffle(self._queue)

    def get_title(self, index: int):
        return self._queue[index].source.title

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 5 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(300):  # 5 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    # Joins the sender's voice channel
    @commands.command(name='join', aliases=['connect'])
    async def _join(self, ctx: commands.Context):

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    # Clears the queue and leaves the voice channel
    @commands.command(name='leave', aliases=['disconnect'])
    async def _leave(self, ctx: commands.Context):
        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    # Sets the volume of the player
    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing is currently being played')
        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')
        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    # Displays the currently playing audio
    @commands.command(name='now', aliases=['np', 'current', 'playing'])
    async def _now(self, ctx: commands.Context):
        if not ctx.voice_state.voice.is_playing():
            return await ctx.send('Nothing is currently being played')
        await ctx.send(embed=ctx.voice_state.current.create_embed())

    # Pauses the currently playing audio
    @commands.command(name='pause')
    async def _pause(self, ctx: commands.Context):
        if ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.send('Audio player has been paused')

    # Resumes a currently paused audio
    @commands.command(name='resume', aliases=['continue'])
    async def _resume(self, ctx: commands.Context):
        if ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.send('Audio player has resumed')

    # Skips the current audio
    @commands.command(name='skip', aliases=['s'])
    async def _skip(self, ctx: commands.Context):
        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing is currently being played')

        ctx.voice_state.skip()
        await ctx.send(f'Skipped **{ctx.voice_state.current.source.title}**')

    # Skips the current audio and plays specified index if it exists
    @commands.command(name='skipto')
    async def _skipto(self, ctx: commands.Context, index: int):
        try:
            i = int(index)
        except ValueError:
            return await ctx.send(f'Index must be an integer')

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing is currently being played')

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Audio playlist is empty')

        # Move entry at index to front of queue
        song = ctx.voice_state.songs._queue[i - 1]
        ctx.voice_state.songs.remove(i - 1)
        ctx.voice_state.songs._queue.appendleft(song)

        ctx.voice_state.skip()
        await ctx.send(f'Skipped **{ctx.voice_state.current.source.title}**')

    # Stops playing audio and clears the queue
    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        ctx.voice_state.songs.clear()
        ctx.voice_state.voice.stop()
        await ctx.send('Audio player has stopped')

    # Shows the audio playlist
    @commands.command(name='queue', aliases=['playlist'])
    async def _queue(self, ctx: commands.Context):
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Audio playlist is empty')

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs, start=0):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue)))
        await ctx.send(embed=embed)

    # Shuffles the audio playlist
    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Audio playlist is empty')

        ctx.voice_state.songs.shuffle()
        await ctx.send('Audio playlist has been shuffled')

    # Swaps two entries in audio paylist
    @commands.command(name='swap', aliases=['switch'])
    async def _swap(self, ctx: commands.Context, x, y):
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return await ctx.send(f'Indices must be integers')

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Audio playlist is empty')

        ctx.voice_state.songs.swap(x - 1, y - 1)
        await ctx.send(f'Swapped entries of indices **{x}** and **{y}**')

    # Removes a song from the playlist at a given index
    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index):
        try:
            i = int(index)
        except ValueError:
            response = (f'Index must be an integer')
            return await ctx.send(response)

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Audio playlist is empty')

        title = ctx.voice_state.songs.get_title(i - 1)
        ctx.voice_state.songs.remove(i - 1)
        await ctx.send(f'Removed **{title}** from the playlist')

    # Adds a song to the end of playlist
    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))

    # Verifies the audio player's voice state
    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Already in a voice channel')

def setup(bot):
    bot.add_cog(Music(bot))