import time
import aiohttp
import discord
import importlib
import textwrap
import re
import os
import json
import sys
import asyncio
from discord.ext import commands
from utility import http, default

START_CODE_BLOCK_RE = re.compile(r"^((```py)(?=\s)|(```))")


class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
        else:
            return m.id


class ActionReason(commands.Converter):
    async def convert(self, ctx, argument):
        ret = argument

        if len(ret) > 512:
            reason_max = 512 - len(ret) - len(argument)
            raise commands.BadArgument(f'reason is too long ({len(argument)}/{reason_max})')
        return ret


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_result = None

    @commands.command()
    async def reboot(self, ctx):
        if ctx.author.id == 314618320093577217:
            await ctx.send('Rebooting now...')
            time.sleep(1)
            sys.exit(0)
        else:
            await ctx.send(f'Only Shiro owner can use this command')

    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, message: str):
        if ctx.author.id == 314618320093577217:
            if not user:
                return await ctx.send(f"Could not find any UserID matching **{user}**")

            try:
                await user.send(message)
                await ctx.send(f"✉️ Отправил DM пользователю **{user.name}**")
            except discord.Forbidden:
                await ctx.send("Кажется у него отключеные личные сообщения или я заблокирован у него...")

    @commands.group()
    async def change(self, ctx):
        if ctx.author.id == 314618320093577217:
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))

    @change.command(name="username")
    async def change_username(self, ctx, *, name: str):
        if ctx.author.id == 314618320093577217:
            try:
                await self.client.user.edit(username=name)
                await ctx.send(f"Successfully changed username to **{name}**")
            except discord.HTTPException as err:
                await ctx.send(err)

    @change.command(name="nickname")
    async def change_nickname(self, ctx, *, name: str = None):
        if ctx.author.id == 314618320093577217:
            try:
                await ctx.guild.me.edit(nick=name)
                if name:
                    await ctx.send(f"Successfully changed nickname to **{name}**")
                else:
                    await ctx.send("Successfully removed nickname")
            except Exception as err:
                await ctx.send(err)

    @change.command(name="avatar")
    async def change_avatar(self, ctx, url: str = None):
        if ctx.author.id == 314618320093577217:
            if url is None and len(ctx.message.attachments) == 1:
                url = ctx.message.attachments[0].url
            else:
                url = url.strip('<>') if url else None

            try:
                bio = await http.get(url, res_method="read")
                await self.client.user.edit(avatar=bio)
                await ctx.send(f"Successfully changed the avatar. Currently using:\n{url}")
            except aiohttp.InvalidURL:
                await ctx.send("The URL is invalid...")
            except discord.InvalidArgument:
                await ctx.send("This URL does not contain a useable image")
            except discord.HTTPException as err:
                await ctx.send(err)
            except TypeError:
                await ctx.send("You need to either provide an image URL or upload one with the command")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):

        try:
            await member.kick(reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("kicked"))
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["nick"])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, name: str = None):
        try:
            await member.edit(nick=name, reason=default.responsible(ctx.author, "Changed by command"))
            message = f"Changed **{member.name}'s** nickname to **{name}**"
            if name is None:
                message = f"Reset **{member.name}'s** nickname"
            await ctx.send(message)
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["жалоба", "wrn", 'жб'])
    @commands.guild_only()
    async def warn(self, ctx, member: discord.Member, *, message: str):
        await ctx.channel.purge(limit=1)
        channel = self.client.get_channel(675742440245952520)
        author = ctx.message.author
        embed_warn = discord.Embed(
            color=discord.Colour.dark_purple(),
            timestamp=ctx.message.created_at
        )
        embed_warn.add_field(name='Жалоба', value=f'Жалоба на: {member.mention}\n От {author.mention} \n Содержание '
                                                  f'жалобы:\n ```{message}```')
        embed_warn.set_footer(text=f'warn {author.name} на {member.name}')
        await ctx.send('Ваша жалоба была отправлена на канал администрации! Ожидайте.')
        await channel.send(embed=embed_warn)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: MemberID, *, reason: str = None):
        m = ctx.guild.get_member(member)
        if m is not None and await permissions.check_priv(ctx, m):
            return

        try:
            await ctx.guild.ban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("banned"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, reason: ActionReason, *members: MemberID):
        try:
            for member_id in members:
                await ctx.guild.ban(discord.Object(id=member_id), reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("massbanned", mass=True))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: MemberID, *, reason: str = None):
        try:
            await ctx.guild.unban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unbanned"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):

        muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)

        if not muted_role:
            return await ctx.send(
                "Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.add_roles(muted_role, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("muted"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):

        muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)

        if not muted_role:
            return await ctx.send(
                "Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.remove_roles(muted_role, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unmuted"))
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["ar"])
    @commands.has_permissions(manage_roles=True)
    async def announcerole(self, ctx, *, role: discord.Role):
        if role == ctx.guild.default_role:
            return await ctx.send("To prevent abuse, I won't allow mentionable role for everyone/here role.")

        if ctx.author.top_role.position <= role.position:
            return await ctx.send(
                "It seems like the role you attempt to mention is over your permissions, therefor I won't allow you.")

        if ctx.me.top_role.position <= role.position:
            return await ctx.send("This role is above my permissions, I can't make it mentionable ;-;")

        await role.edit(mentionable=True, reason=f"[ {ctx.author} ] announcerole command")
        msg = await ctx.send(
            f"**{role.name}** is now mentionable, if you don't mention it within 30 seconds, I will revert the changes.")

        while True:
            def role_checker(m):
                if (role.mention in m.content):
                    return True
                return False

            try:
                checker = await self.client.wait_for('message', timeout=30.0, check=role_checker)
                if checker.author.id == ctx.author.id:
                    await role.edit(mentionable=False, reason=f"[ {ctx.author} ] announcerole command")
                    return await msg.edit(
                        content=f"**{role.name}** mentioned by **{ctx.author}** in {checker.channel.mention}")
                else:
                    await checker.delete()
            except asyncio.TimeoutError:
                await role.edit(mentionable=False, reason=f"[ {ctx.author} ] announcerole command")
                return await msg.edit(content=f"**{role.name}** was never mentioned by **{ctx.author}**...")

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def find(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @find.command(name="playing")
    async def find_playing(self, ctx, *, search: str):
        loop = []
        for i in ctx.guild.members:
            if i.activities and (not i.bot):
                for g in i.activities:
                    if g.name and (search.lower() in g.name.lower()):
                        loop.append(f"{i} | {type(g).__name__}: {g.name} ({i.id})")

        await default.prettyResults(
            ctx, "playing", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="username", aliases=["name"])
    async def find_name(self, ctx, *, search: str):
        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search.lower() in i.name.lower() and not i.bot]
        await default.prettyResults(
            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="nickname", aliases=["nick"])
    async def find_nickname(self, ctx, *, search: str):
        loop = [f"{i.nick} | {i} ({i.id})" for i in ctx.guild.members if i.nick if
                (search.lower() in i.nick.lower()) and not i.bot]
        await default.prettyResults(
            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="id")
    async def find_id(self, ctx, *, search: int):
        loop = [f"{i} | {i} ({i.id})" for i in ctx.guild.members if (str(search) in str(i.id)) and not i.bot]
        await default.prettyResults(
            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="discriminator", aliases=["discrim"])
    async def find_discriminator(self, ctx, *, search: str):
        if not len(search) == 4 or not re.compile("^[0-9]*$").search(search):
            return await ctx.send("You must provide exactly 4 digits")

        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search == i.discriminator]
        await default.prettyResults(
            ctx, "discriminator", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def prune(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            return await ctx.send(f'Слишком много сообщений задано. Лимит: ({limit}/2000)')

        if before is None:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after is not None:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden:
            return await ctx.send('Мне не разрешено удалять сообщения.')
        except discord.HTTPException as e:
            return await ctx.send(f'Ошибка: {e} (Попробуйте запрос поменьше?)')

        deleted = len(deleted)
        if message is True:
            await ctx.send(f'🚮 Успешно удалил {deleted}  {"сообщение" if deleted == 1 else "сообщений"}.')

    @prune.command()
    async def embeds(self, ctx, search=100):
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @prune.command()
    async def files(self, ctx, search=100):
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @prune.command()
    async def mentions(self, ctx, search=100):
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @prune.command()
    async def images(self, ctx, search=100):
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @prune.command(name='all')
    async def _remove_all(self, ctx, search=100):
        await self.do_removal(ctx, search, lambda e: True)

    @prune.command()
    async def user(self, ctx, member: discord.Member, search=100):
        await self.do_removal(ctx, search, lambda e: e.author == member)

    @prune.command()
    async def contains(self, ctx, *, substr: str):
        if len(substr) < 3:
            await ctx.send('The substring length must be at least 3 characters.')
        else:
            await self.do_removal(ctx, 100, lambda e: substr in e.content)

    @prune.command(name='bots')
    async def _bots(self, ctx, search=100, prefix=None):

        getprefix = prefix if prefix else self.config.prefix

        def predicate(m):
            return (m.webhook_id is None and m.author.client) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='users')
    async def _users(self, ctx, prefix=None, search=100):

        def predicate(m):
            return m.author.client is False

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='emojis')
    async def _emojis(self, ctx, search=100):
        custom_emoji = re.compile(r'<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]')

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='reactions')
    async def _reactions(self, ctx, search=100):

        if search > 2000:
            return await ctx.send(f'Too many messages to search for ({search}/2000)')

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()

        await ctx.send(f'Successfully removed {total_reactions} reactions.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sendrules(self, ctx):
        nsfw = self.client.get_channel(694617253752078427)
        spam = self.client.get_channel(694617026223931525)
        bots = self.client.get_channel(694617066455433326)
        casino = self.client.get_channel(694617109304705166)
        rules_embed = discord.Embed(
            description='**Текстовые и голосовые каналы сервера находятся под модерацией, да.** ⚜️\n'
                        '★ Для комфортного общения следует соблюдать правила   ★\n'
                        '\n**Общесерверные правила для всех каналов** ⚜️\n'
                        '\n★ ``#1`` - Соблюдайте '
                        'правила самого сообщества '
                        'Discord.\n☆ ``#2`` - '
                        'Запрещена реклама других '
                        'серверов, которая не была '
                        'согласована с '
                        'администраторами '
                        '**Imanity**\n★ ``#3`` - '
                        'Относитесь к остальным '
                        'участникам сообщества '
                        'сервера с пониманем и '
                        'уважением, независимо '
                        'администратор данный человек или '
                        f'просто участник. Этот '
                        f'пункт подразумевает '
                        f'наказание за оскорбления '
                        f'и прочее схожее, '
                        f'в т.ч. и троллинг\n☆ '
                        f'``#4`` - Порнографический '
                        f'контент разрешен только в '
                        f'{nsfw.mention}.\n'
                        f' ★ ``#5`` '
                        f'- Выяснение ваших личных '
                        f'отношений на сервере '
                        f'совсем не желательно '
                        f'видеть кому-либо, '
                        f'идите пожалуйста и '
                        f'ругайтесь в личных '
                        f'сообщениях.\n ☆ ``#6`` '
                        f'Здесь нет места флейму, '
                        f'троллингу, пингу людей '
                        f'без причины или спаму не '
                        f'в {spam.mention}\n ★ '
                        f'``#7`` Не провоцируйте '
                        f'конфликтные ситуации, '
                        f'а при их развитии не '
                        f'поддерживайте их.\n ☆ '
                        f'``#8`` - Используйте '
                        f'команды для ботов в '
                        f'соответствующих каналах. '
                        f'Список соответствующих '
                        f'каналов это: '
                        f'{spam.mention} '
                        f'{casino.mention} '
                        f'{bots.mention}\n ★ ``#9`` '
                        f'- Запрещено нарушение '
                        f'работы сервера в любом '
                        f'виде.',
            color=discord.Colour.dark_purple()
        )
        rules_embed_voice = discord.Embed(
            description='**Правила для голосовых каналов**'
                        '\n\n☆ ``#10`` - Общие голосовые каналы также подвергаются всем правилам выше, но только в '
                        'голосовой форме.'
                        '\n★ ``#11`` - Запрещено создавать специально громкие звуки и прерывать чужую дискуссию много '
                        'раз, специально перебивать друг друга.'
                        '\n☆ ``#12`` - Создаваемые лично пользователями голосовые каналы никаким образом не '
                        'подвергаются модерации, но однако если вы оказались в таком и вас просят уйти, то вы обязаны '
                        'выполнить данную просьбу, если же пользователь не соглашается, следует уведомить '
                        'администрацию. Мы заранее приносим глубочайшие извинения за подобные ситуации.',
            color=discord.Colour.dark_purple()
        )
        embed_photo = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_photo.set_image(url='https://cdn.discordapp.com/attachments/621005423335702528/681129883233026151/rules.png')
        await ctx.send(embed=embed_photo)
        await ctx.send(embed=rules_embed)
        await ctx.send(embed=rules_embed_voice)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sendinfo(self, ctx):
        member = ctx.author
        channel1 = self.client.get_channel(694608838065913939)
        channel2 = self.client.get_channel(694616568096620614)
        channel3 = self.client.get_channel(694616613978112061)
        channel5 = self.client.get_channel(694616683549163600)
        obshenie = self.client.get_channel(694616985857687552)
        nsfw = self.client.get_channel(694617253752078427)
        spam = self.client.get_channel(694617026223931525)
        bots = self.client.get_channel(694617066455433326)
        casino = self.client.get_channel(694617109304705166)
        suggest = self.client.get_channel(694617297704452217)
        art = self.client.get_channel(694617340163260457)
        embed_sender = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_sender.add_field(name='Приветик, очень рад тебя видеть, я - Тет и проведу тебе маленькую экскурсию по '
                                    'серверу, его каналам и ролям. Ага. ;)', value='**Начнем с каналов с '
                                                                                   'информацией**\n', inline=False)
        embed_sender.add_field(name='•Самая важная часть сервера - это правила, а вот и канал', value=f'{channel1.mention}', inline=False)
        embed_sender.add_field(name='•Команды ботов, чтобы с ними взаимодействовать, в том числе и со мной', value=f'{channel2.mention}', inline=False)
        embed_sender.add_field(name='•Ивенты, события, мероприятия нашего сервера', value=f'{channel3.mention}', inline=False)
        embed_sender.add_field(name='•Все вновь прибывшие и новоприбывшие здесь', value=f'{channel5.mention}', inline=False)
        embed_first_photo = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_first_photo.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681339608034050143/maxresdefault.png')
        await ctx.send(embed=embed_first_photo)
        await ctx.send(embed=embed_sender)
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681339597350764544/d7v5xie-14dece00-9e9b-482d-8d59-adadc5786ef0.png')
        await ctx.send(embed=embed)
        embed_desender = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_desender.add_field(name='А теперь о каналах, в которых все могут писать сообщения. Да, их время пришло.', value='_ _', inline=False)
        embed_desender.add_field(name='•Пользовательский чат', value=f'{obshenie.mention}', inline=False)
        embed_desender.add_field(name='•Пользовательская флудилка, здесь пользователи тоже могут общаться, но ``#5`` и '
                                      '``#6`` правила в этом канале не модерируются.', value=f'{spam.mention}', inline=False)
        embed_desender.add_field(name='•Для использования команд.', value=f'{bots.mention}', inline=False)
        embed_desender.add_field(name='•Азартный канал, в т.ч. и для использования команд', value=f'{casino.mention}', inline=False)
        embed_desender.add_field(name='•18+ чат, а также канал для 18+ артов', value=f'{nsfw.mention}', inline=False)
        embed_desender.add_field(name='•Канал для предложений по улучшению сервера, можете предложить здесь свои идеи', value=f'{suggest.mention}', inline=False)
        embed_desender.add_field(name='•Ваше и не только творчество', value=f'{art.mention}', inline=False)
        await ctx.send(embed=embed_desender)
        embed_moderation = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        role1 = discord.utils.get(member.guild.roles, name='真珠 | Shinju')
        role2 = discord.utils.get(member.guild.roles, name='グラス Gurasu')
        role3 = discord.utils.get(member.guild.roles, name='普通 Futsū')
        role4 = discord.utils.get(member.guild.roles, name='眩しい | Mabushii')
        role5 = discord.utils.get(member.guild.roles, name='明るい | Akarui')
        role6 = discord.utils.get(member.guild.roles, name='世界 Sekai')
        role7 = discord.utils.get(member.guild.roles, name='クリア Kuria')
        embed_moderation.add_field(name='**Основные роли сервера и их значение**', value='_ _', inline=False)
        embed_moderation.add_field(name='Старший Администратор', value=f'{role1.mention}', inline=False)
        embed_moderation.add_field(name='Администратор', value=f'{role2.mention}', inline=False)
        embed_moderation.add_field(name='Модератор', value=f'{role3.mention}', inline=False)
        embed_moderation.add_field(name='Бустер Сервера', value=f'{role6.mention}', inline=False)
        embed_moderation.add_field(name='Младший Модератор', value=f'{role4.mention}', inline=False)
        embed_moderation.add_field(name='Проводящий мероприятия', value=f'{role5.mention}\n\n(Все, кто выше, тоже '
                                                                        f'ответственны за проведение мероприятий, '
                                        'но имеют и другие возложенные на них обязанности, за искл. бустера)', inline=False)
        embed_moderation.add_field(name='Пользователь', value=f'{role7.mention}', inline=False)
        embed_moderation.add_field(name='Остальные роли', value=f'Остальные роли, которые вы видите возможно получить '
                                                                f'или купить у бота', inline=False)
        level1 = discord.utils.get(member.guild.roles, name='⚜️Level 1')
        level10 = discord.utils.get(member.guild.roles, name='⚜️Level 10')
        level20 = discord.utils.get(member.guild.roles, name='⚜️Level 20')
        level30 = discord.utils.get(member.guild.roles, name='⚜️Level 30')
        level40 = discord.utils.get(member.guild.roles, name='⚜️Level 40')
        level50 = discord.utils.get(member.guild.roles, name='⚜️Level 50')
        level60 = discord.utils.get(member.guild.roles, name='⚜️Level 60')
        embed_moderation.add_field(name='\n**Роли за уровень у Тет:**', value=f'_ _', inline=False)
        embed_moderation.add_field(name='**I**', value=f'{level1.mention}', inline=True)
        embed_moderation.add_field(name='**II**', value=f'{level10.mention}', inline=True)
        embed_moderation.add_field(name='**III**', value=f'{level20.mention}', inline=True)
        embed_moderation.add_field(name='**IV**', value=f'{level30.mention}', inline=True)
        embed_moderation.add_field(name='**V**', value=f'{level40.mention}', inline=True)
        embed_moderation.add_field(name='**VI**', value=f'{level50.mention}', inline=True)
        embed_moderation.add_field(name='**VII**', value=f'{level60.mention}', inline=True)
        await ctx.send(embed=embed_moderation)

    @commands.command(name='changeprefix')
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        with open('prefix.json', 'r') as file:
            prefixes = json.load(file)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefix.json', 'w') as file:
            json.dump(prefixes, file, indent=4)

        await ctx.send(f'Префикс команд был изменен на {prefix}')



def setup(client):
    client.add_cog(Admin(client))