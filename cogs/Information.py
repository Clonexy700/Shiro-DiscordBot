import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

import base64
import binascii
import codecs
import discord
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
from discord.ext import commands
from utility import http, argparser, default

msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        await ctx.send(r[endpoint])

    async def api_img_creator(self, ctx, url, filename, content=None):
        async with ctx.channel.typing():
            req = await http.get(url, res_method="read")

            if req is None:
                return await ctx.send("I couldn't create the image ;-;")

            bio = BytesIO(req)
            bio.seek(0)
            await ctx.send(content=content, file=discord.File(bio, filename=filename))

    @commands.command(aliases=['color'])
    async def colour(self, ctx, colour: str):
        if colour == "random":
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if colour[:1] == "#":
            colour = colour[1:]

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")

        try:
            r = await http.get(f"https://api.alexflipnote.dev/colour/{colour}", res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        embed = discord.Embed(colour=discord.Colour.dark_purple())
        embed.set_thumbnail(url=r["image"])
        embed.set_image(url=r["image_gradient"])

        embed.add_field(name="HEX", value=r['hex'], inline=True)
        embed.add_field(name="RGB", value=r['rgb'], inline=True)
        embed.add_field(name="Int", value=r['int'], inline=True)
        embed.add_field(name="Brightness", value=r['brightness'], inline=True)

        await ctx.send(embed=embed, content=f"{ctx.invoked_with.title()} name: **{r['name']}**")

    @commands.command()
    async def urban(self, ctx, *, search: str):
        async with ctx.channel.typing():
            url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")

            if url is None:
                return await ctx.send("I think the API broke...")

            if not len(url['list']):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

            embed_urban = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_urban.add_field(name=f"Meaning of: {result['word']}", value=f':bookmark: \n```\n{definition}```')
            await ctx.send(embed=embed_urban)

    @commands.command(name='reverse', aliases=['переверни', 'реверс'])
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        embed_reversion = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_reversion.add_field(name='Reverse 🔁', value=t_rev)
        await ctx.send(embed=embed_reversion)

    @commands.command(name='пароль', aliases=['password'])
    async def password(self, ctx, nbytes: int = 18):
        if nbytes not in range(3, 401):
            return await ctx.send("Я принимаю значения между 3-400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Отправляю твой пароль тебе в личные сообщения ;) **{ctx.author.name}**")
        embed_password = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_password.add_field(name='Пароль :lock: ', value=f"``Ваш пароль:``\n{secrets.token_urlsafe(nbytes)}")
        await ctx.author.send(embed=embed_password)

    @commands.command()
    async def supreme(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        parser = argparser.Arguments()
        parser.add_argument('input', nargs="+", default=None)
        parser.add_argument('-d', '--dark', action='store_true')
        parser.add_argument('-l', '--light', action='store_true')

        args, valid_check = parser.parse_args(text)
        if not valid_check:
            return await ctx.send(args)

        inputText = urllib.parse.quote(' '.join(args.input))
        if len(inputText) > 500:
            return await ctx.send(f"**{ctx.author.name}**, Лимит это 500 символов,  простите.")

        darkorlight = ""
        if args.dark:
            darkorlight = "dark=true"
        if args.light:
            darkorlight = "light=true"
        if args.dark and args.light:
            return await ctx.send(f"**{ctx.author.name}**, you can't define both --dark and --light, sorry..")

        await self.api_img_creator(ctx, f"https://api.alexflipnote.dev/supreme?text={inputText}&{darkorlight}", "supreme.png")

    @commands.group()
    async def encode(self, ctx):
        if ctx.invoked_subcommand is None:
            embed_decode = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_decode.add_field(name='Decode \n Commands: ', value='ascii85: ``Encode in ASCII85``\n base32:  '
                                                                      '``Encode in '
                                                                      'base32``\n base64:``Encode in base64``\n '
                                                                      'base85:  ``Encode '
                                                                      ' in base85``\n hex: ``Encode in hex``\n rot13:  '
                                                                      '``Encode in rot13``\n ')
            await ctx.send(embed=embed_decode)

    @commands.group()
    async def decode(self, ctx):
        if ctx.invoked_subcommand is None:
            embed_decode = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_decode.add_field(name='Decode \n Commands: ', value='ascii85: ``Decode in ASCII85``\n base32:  '
                                                                      '``Decode in '
                                                                      'base32``\n base64:``Decode in base64``\n '
                                                                      'base85:  ``Decode '
                                                                      ' in base85``\n hex: ``Decode in hex``\n rot13:  '
                                                                      '``Decode in rot13``\n ')
            await ctx.send(embed=embed_decode)

    async def detect_file(self, ctx):
        if ctx.message.attachments:
            file = ctx.message.attachments[0].url

            if not file.endswith(".txt"):
                raise BadArgument(".txt files only")

        try:
            content = await http.get(file, no_cache=True)
        except Exception:
            raise BadArgument("Invalid .txt file")

        if not content:
            raise BadArgument("File you've provided is empty")
        return content

    async def encryptout(self, ctx, convert, input):
        if not input:
            return await ctx.send(f"Aren't you going to give me anything to encode/decode **{ctx.author.name}**")

        async with ctx.channel.typing():
            if len(input) > 1900:
                try:
                    data = BytesIO(input.encode('utf-8'))
                except AttributeError:
                    data = BytesIO(input)

                try:
                    return await ctx.send(
                        content=f"📑 **{convert}**",
                        file=discord.File(data, filename=default.timetext("Encryption"))
                    )
                except discord.HTTPException:
                    return await ctx.send(f"The file I returned was over 8 MB, sorry {ctx.author.name}...")

            try:
                await ctx.send(f"📑 **{convert}**```fix\n{input.decode('UTF-8')}```")
            except AttributeError:
                await ctx.send(f"📑 **{convert}**```fix\n{input}```")

    @encode.command(name="base32", aliases=["b32"])
    async def encode_base32(self, ctx, *, input: commands.clean_content = None):
        """ Encode in base32 """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base32", base64.b32encode(input.encode('UTF-8'))
        )

    @decode.command(name="base32", aliases=["b32"])
    async def decode_base32(self, ctx, *, input: commands.clean_content = None):
        """ Decode in base32 """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base32 -> Text", base64.b32decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base32...")

    @encode.command(name="base64", aliases=["b64"])
    async def encode_base64(self, ctx, *, input: commands.clean_content = None):
        """ Encode in base64 """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base64", base64.urlsafe_b64encode(input.encode('UTF-8'))
        )

    @decode.command(name="base64", aliases=["b64"])
    async def decode_base64(self, ctx, *, input: commands.clean_content = None):
        """ Decode in base64 """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base64 -> Text", base64.urlsafe_b64decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base64...")

    @encode.command(name="rot13", aliases=["r13"])
    async def encode_rot13(self, ctx, *, input: commands.clean_content = None):
        """ Encode in rot13 """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> rot13", codecs.decode(input, 'rot_13')
        )

    @decode.command(name="rot13", aliases=["r13"])
    async def decode_rot13(self, ctx, *, input: commands.clean_content = None):
        """ Decode in rot13 """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "rot13 -> Text", codecs.decode(input, 'rot_13'))
        except Exception:
            await ctx.send("Invalid rot13...")

    @encode.command(name="hex")
    async def encode_hex(self, ctx, *, input: commands.clean_content = None):
        """ Encode in hex """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> hex",
            binascii.hexlify(input.encode('UTF-8'))
        )

    @decode.command(name="hex")
    async def decode_hex(self, ctx, *, input: commands.clean_content = None):
        """ Decode in hex """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "hex -> Text", binascii.unhexlify(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid hex...")

    @encode.command(name="base85", aliases=["b85"])
    async def encode_base85(self, ctx, *, input: commands.clean_content = None):
        """ Encode in base85 """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base85",
            base64.b85encode(input.encode('UTF-8'))
        )

    @decode.command(name="base85", aliases=["b85"])
    async def decode_base85(self, ctx, *, input: commands.clean_content = None):
        """ Decode in base85 """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base85 -> Text", base64.b85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base85...")

    @encode.command(name="ascii85", aliases=["a85"])
    async def encode_ascii85(self, ctx, *, input: commands.clean_content = None):
        """ Encode in ASCII85 """
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> ASCII85",
            base64.a85encode(input.encode('UTF-8'))
        )

    @decode.command(name="ascii85", aliases=["a85"])
    async def decode_ascii85(self, ctx, *, input: commands.clean_content = None):
        """ Decode in ASCII85 """
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "ASCII85 -> Text", base64.a85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid ASCII85...")

    @commands.command(name='say', help=' bot will say that u say to say')
    async def say(self, ctx, *, message: str):
        author = ctx.message.author
        await ctx.channel.purge(limit=1)
        embed_say = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_say.add_field(name='Тет', value=message)
        embed_say.set_footer(text=f'запросил {author.name}')
        await ctx.send(embed=embed_say)

    @commands.command(name='ping', aliases=['пинг'], help=' - shows my ping')
    async def ping(self, ctx):
        embedping = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedping.add_field(name='Задержка',
                            value=f'Понг!Задержка ровно в {round(self.client.latency * 1000)}ms {random.choice(msgend)}')
        await ctx.send(embed=embedping)

    @commands.command(help=' - test command')
    async def test(self, ctx):
        await ctx.send(
            "1234567890ё-=йцукенгшщзхъфывапролдэячсмитьбю.`123456790-=qwertyuiop[]asdfghjkl;'zxcvbnm,./?.!@№#$;%^:&?*("
            ")_-+=\/|")

    @commands.command(name='avatar', help='sends avatar image')
    async def avatar(self, ctx, member: discord.Member):
        author = ctx.message.author
        embedavatar = discord.Embed(
            color=discord.Colour.dark_purple(), timestamp=ctx.message.created_at
        )
        embedavatar.set_image(url='{}'.format(member.avatar_url))
        embedavatar.add_field(name=f'Аватарка {member.display_name}', value=f'запросил {author.mention}')
        await ctx.send(embed=embedavatar)

    @commands.command(name='8шар', aliases=['8ball', '8ш'], help='ваш вопрос - вы получаете магический ответ от шара')
    async def ball8ru(self, ctx, question):
        embedball8 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        responses = ["Это точно.",
                     "Да, это так.",
                     "Без сомнений.",
                     "Да - точно.",
                     "Можешь быть уверен в этом.",
                     "Как мне кажется...Да.",
                     "Вообщем-то.... Угу.",
                     "НЕ, НЕ, НЕ, НЕ.",
                     "Ага.",
                     "Звёзды говорят - да.",
                     "Точно - нет.",
                     "Не знаю.",
                     "Тебе лучше не знать это.",
                     "Не могу сказать сейчас точно.",
                     "Спросите попозже.",
                     "Даже не рассчитывай на ответ на этот вопрос.",
                     "Мне надо подумать над ответом.",
                     "Мой ответ - нет.",
                     "Мои тайные источники говорят - нет.",
                     "Врятли.",
                     "Сомневаюсь."]
        embedball8.add_field(name='Шар Предсказаний', value=' :8ball:  ', inline=False)
        embedball8.add_field(name='Предсказание', value=f'{random.choice(responses)} {random.choice(msgend)}')
        embedball8.set_image(url='https://static.zerochan.net/Wizard.Cookie.full.2415740.jpg')
        await ctx.send(embed=embedball8)

    @commands.command(name='github')
    async def github(self, ctx):
        embed = discord.Embed(color=discord.Colour.dark_purple(), timestamp=ctx.message.created_at)

        embed.set_author(name=f'Shiro ♣', icon_url=self.client.user.avatar_url)

        embed.add_field(name='Link', value=f"https://github.com/Clonexy700/DiscordShiro")

        await ctx.send(embed=embed)

    @commands.command(name='dice', help='number of dice  number of sides - Simulates rolling dice.')
    async def roll(self, ctx, number_of_sides: int = None, number_of_dice: int = None):
        number_of_dice = 1 if not number_of_dice else number_of_dice
        number_of_sides = 6 if not number_of_sides else number_of_sides
        embeddice = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        embeddice.add_field(name=':game_die: Dice', value=', '.join(dice) + f' <-- Results {random.choice(msgend)}')
        embeddice.set_image(url='https://media1.giphy.com/media/3ohjUS2N88LGAjLypO/giphy.gif')
        await ctx.send(embed=embeddice)

    @commands.command()
    async def servers(self, ctx):
        guilds = list(self.client.guilds)
        await ctx.send(f"Connected on {str(len(guilds))} servers:")
        await ctx.send('\n'.join(guild.name for guild in guilds))

    @commands.command(name='google')
    async def google(self, ctx, *, search: str):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Google',
                        value=f"[Клик \"{search}\"](https://www.google.com/search?q={search.replace(' ', '+')})")
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Info(client))