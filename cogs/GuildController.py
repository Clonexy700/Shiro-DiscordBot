import discord
import asyncio
import time
from collections import OrderedDict
import json
from discord.ext import commands
from functools import partial


class Clans(commands.Cog):

    def __init__(self, client):

        self.users = None
        self.client = client

    async def update_guild(self, man_id: str, name: str, guild_role_value: int):
        if not self.users:
            with open("guilds.json", "r") as ff:
                self.users = json.load(ff)
            if not man_id in self.users:
                self.users[man_id] = {}
                self.users[man_id]['guildname'] = 0
                self.users[man_id]['value'] = 0
                self.users[man_id]['imgurl'] = 0
                self.users[man_id]['guildmoney'] = 0
                self.users[man_id]['guildlvl'] = 1
                self.users[man_id]['skillpoint'] = 0
                self.users[man_id]['skill1'] = 0
                self.users[man_id]['skill2'] = 0
                self.users[man_id]['skill3'] = 0
                self.users[man_id]['skill4'] = 0
                self.users[man_id]['memberlimit'] = 6
                self.users[man_id]['guild_url'] = 0
        self.users[man_id]["guildname"] = name
        self.users[man_id]['value'] = guild_role_value
        await self.client.loop.run_in_executor(None,
                                        partial(json.dump, self.users, open('guilds.json', 'w'), indent=4))

    async def update_guild_url(self, man_id: str, guild_url: str):
        if not self.users:
            with open("guilds.json", "r") as ff:
                self.users = json.load(ff)
        self.users[man_id]["guild_url"] = guild_url
        await self.client.loop.run_in_executor(None,
                                        partial(json.dump, self.users, open('guilds.json', 'w'), indent=4))

    async def update_guildmoney(self, man_id: str, guild_money_amount: int):
        if not self.users:
            with open("guilds.json", "r") as ff:
                self.users = json.load(ff)
        self.users[man_id]["guildmoney"] += guild_money_amount
        await self.client.loop.run_in_executor(None,
                                        partial(json.dump, self.users, open('guilds.json', 'w'), indent=4))

    async def lvl_up(self, author_id):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        cur_xp = self.users[author_id]['guildmoney']
        cur_lvl = self.users[author_id]['guildlvl']

        if cur_xp >= cur_lvl * 200000 + 100000:
            self.users[author_id]['guildlvl'] += 1
            self.users[author_id]['skillpoint'] += 1
            self.users[author_id]['guildmoney'] -= cur_lvl * 200000 + 100000
            await self.client.loop.run_in_executor(None,
                                                   partial(json.dump, self.users, open('guilds.json', 'w'), indent=4))
        cur_xp = self.users[author_id]['guildmoney']
        cur_lvl = self.users[author_id]['guildlvl']

        if cur_xp >= cur_lvl * 200000 + 100000:
            self.users[author_id]['guildlvl'] += 1
            self.users[author_id]['skillpoint'] += 0
            self.users[author_id]['guildmoney'] -= cur_lvl * 200000 + 100000
            await self.client.loop.run_in_executor(None,
                                                   partial(json.dump, self.users, open('guilds.json', 'w'), indent=4))

    @commands.command(name='createclan', aliases=['guildcreate', 'createguild', 'clancreate'])
    async def guildcreation(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        price = 1000000
        premium = discord.utils.get(ctx.author.guild.roles, name='世界 Sekai')
        if premium in ctx.author.roles:
            price = 750000
        embed_creation = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_creation.add_field(name='Создание клана', value=f'Создание клана недешевое удовольствие, которое лично для вас обойдется в сумму размером:\n ``{price}`` {emoji}\n Если вы согласны с столь деликатной ценой данного вопроса, то напишите ниже: **да**')
        await ctx.send(embed=embed_creation)

        def check(author):
            def inner_check(message):
                return message.author == author

            return inner_check
        member_id = str(ctx.author.id)
        message = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
        if message.content.casefold() == 'да':
            await self.client.unupdate_currency(member_id, price)
            if self.client.currency[member_id]['money'] >= 0:
                embed_clan_creation_progress = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_clan_creation_progress.add_field(name='Меню создания', value='Прямо сейчас вы создаете клан. '
                                                                                   'Напишите желаемое название клана '
                                                                                   'в сообщении ниже. Оно может быть '
                                                                                   'любым, соответствующим правилам '
                                                                                   'сервера. Максимальная длина названия - 18 символов')
                await ctx.send(embed=embed_clan_creation_progress)
                i = 0
                while i == 0:
                    message = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
                    if len(message.content) <= 18:
                        i = 1
                    else:
                        embed_try_again = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        embed_try_again.add_field(name='Ошибка', value='Введите название ещё раз ниже, оно должно быть максимум 18 символов!')
                        await ctx.send(embed=embed_try_again)
                membership = await ctx.guild.create_role(name=message.content)
                category = await ctx.guild.create_category(name=message.content)
                await discord.Member.add_roles(ctx.author, membership)
                await ctx.guild.create_text_channel(name='правила', category=category)
                await ctx.guild.create_text_channel(name='чат', category=category)
                await ctx.guild.create_voice_channel(name='голосовой канал', category=category)
                await self.update_guild(member_id, message.content, 3)
            if self.client.currency[member_id]['money'] < 0:
                embed_not_enough_money = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_not_enough_money.add_field(name='Баланс', value=f'Для осуществления покупки недостаточно {emoji}')
                await ctx.send(embed=embed_not_enough_money)
                await self.client.update_currency(member_id, price)

    @commands.command(name='claninfo', aliases=['infoguild', 'infoclan', 'myclan', 'myguild'])
    async def guildinfo(self, ctx):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        author_id = str(ctx.author.id)
        embed_guild_info = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_guild_info.add_field(name='Клан', value=f"{self.users[author_id]['guildname']}", inline=False)
        embed_guild_info.add_field(name='Деньги гильдии', value=f"``{self.users[author_id]['guildmoney']}``", inline=True)
        embed_guild_info.add_field(name='Уровень гильдии', value=f"``{self.users[author_id]['guildlvl']}``", inline=True)
        embed_guild_info.add_field(name='Лидер гильдии:', value=f"{ctx.author.mention}", inline=True)
        member_counter = 0
        for member in ctx.guild.members:
            for role in member.roles:
                if role.name == self.users[author_id]['guildname']:
                    member_counter += 1
        embed_guild_info.add_field(name='Человек в гильдии:', value=f"``{member_counter}``", inline=True)
        embed_guild_info.add_field(name='Члены гильдии:', value="_ _", inline=False)
        for member in ctx.guild.members:
            for role in member.roles:
                if role.name == self.users[author_id]['guildname']:
                    embed_guild_info.add_field(name='_ _', value=f"{member.name}", inline=False)
        embed_guild_info.add_field(name='Умения гильдии:', value='_ _', inline=False)
        if self.users[author_id]['skill1'] == 0:
            embed_guild_info.add_field(name='Скидка на роли', value='Не изучено', inline=True)
        if self.users[author_id]['skill1'] == 1:
            embed_guild_info.add_field(name='Скидка на роли', value='Изучено', inline=True)
        if self.users[author_id]['skill2'] == 0:
            embed_guild_info.add_field(name='Скидка на подарки', value='Не изучено', inline=True)
        if self.users[author_id]['skill2'] == 1:
            embed_guild_info.add_field(name='Скидка на подарки', value='Изучено', inline=True)
        if self.users[author_id]['skill3'] == 0:
            embed_guild_info.add_field(name='Скидка на обои', value='Не изучено', inline=True)
        if self.users[author_id]['skill3'] == 1:
            embed_guild_info.add_field(name='Скидка на обои', value='Изучено', inline=True)
        if self.users[author_id]['skill4'] == 0:
            embed_guild_info.add_field(name='Увеличение лимита участников с 6 до 12', value='Не изучено', inline=True)
        if self.users[author_id]['skill4'] == 1:
            embed_guild_info.add_field(name='Увеличение лимита участников с 6 до 12', value='Изучено', inline=True)
        embed_guild_info.add_field(name='_ _', value=f"``Значок вашей гильдии:``", inline=False)
        if self.users[author_id]['guild_url'] != 0:
            embed_guild_info.set_image(url=self.users[author_id]['guild_url'])
        await ctx.send(embed=embed_guild_info)

    @commands.command(name='setclanimg', aliases=['setguildimg', 'setclanpng', 'setguildpng', 'clanimgset', 'guildimgset', 'guildpngset', 'clanpngset', 'clanimg', 'clanpng', 'guildimg'])
    async def setclanimg(self, ctx, url: str):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        author_id = str(ctx.author.id)
        if self.users[author_id]['value'] == 3:
            embed_set = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_set.add_field(name='Вы установили следующий герб клана:', value='_ _')
            embed_set.set_image(url=url)
            await self.update_guild_url(author_id, url)
            await ctx.send(embed=embed_set)

    @commands.command(name='guilddeposit', aliases=['clandeposit', 'guildeposit', 'guildmoneyadd', 'clanmoneyadd', 'moneyguildadd', 'moneyclanadd'])
    async def guilddeposit(self, ctx, guild_deposit: int):
        emoji = self.client.get_emoji(676803534758477845)
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        member_id = str(ctx.author.id)
        author_id = member_id
        if self.users[author_id]['value'] == 3:
            if self.client.currency[member_id]['money'] - guild_deposit >= 0:
                await self.client.unupdate_currency(member_id, guild_deposit)
                embed_set = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_set.add_field(name='Депозит в клан', value=f'Вы внесли {guild_deposit} {emoji}')
                lvl_ago = self.users[author_id]['guildlvl']
                await self.update_guildmoney(member_id, guild_deposit)
                await ctx.send(embed=embed_set)
                await self.lvl_up(author_id)
                lvl_future = self.users[author_id]['guildlvl']
                if lvl_future > lvl_ago:
                    embed_lvl_up = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_lvl_up.add_field(
                        name='Уровень гильдии повышен!Поздравляем, деньги гильдии были сняты со счета по данной причине.',
                        value='_ _')
                    await ctx.send(embed=embed_lvl_up)
            else:
                embed_not_enough = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_not_enough.add_field(name='Баланс', value=f'Недостаточно {emoji} для депозита')
                await ctx.send(embed=embed_not_enough)

    @commands.command(name='claninvite', aliases=['guildinvite'])
    async def claninvite(self, ctx, user: discord.Member):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        author_id = str(ctx.author.id)
        if self.users[author_id]['value'] == 3:
            embed_invitation = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_invitation.add_field(name='Приглашение',
                                       value=f"{user.mention}!\nВас приглашают в гильдию **{self.users[author_id]['guildname']}**, если вы принимаете данный запрос, то ответьте ниже: **да** ")

            def check(author):
                def inner_check(message):
                    return message.author == author

                return inner_check
            await ctx.send(embed=embed_invitation)

            message = await self.client.wait_for('message', check=check(user), timeout=120)
            if message.content.casefold() == 'да':
                member_counter = 0
                for member in ctx.guild.members:
                    for role in member.roles:
                        if role.name == self.users[author_id]['guildname']:
                            member_counter += 1
                if member_counter < self.users[author_id]['memberlimit']:
                    embed_hooray = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_hooray.add_field(name='Добро пожаловать!', value=f"{user.mention} вступил в гильдию **{self.users[author_id]['guildname']}**")
                    role1 = discord.utils.get(user.guild.roles, name=self.users[author_id]['guildname'])
                    await user.add_roles(role1)
                    await ctx.send(embed=embed_hooray)
                if member_counter > self.users[author_id]['memberlimit']:
                    embed_limitation = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_limitation.add_field(name='Лимит', value='Лимит участников гильдии достигнут, мы не можем добавить вас в гильдию')

    @commands.command(name='guildskills', aliases=['clanskills', 'clanskilltree', 'clanskill', 'guildskill'])
    async def guildskillingtree(self, ctx):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        author_id = str(ctx.author.id)
        if self.users[author_id]['value'] == 3:
            emoji = self.client.get_emoji(676803534758477845)
            skill_tree = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            skill_tree.add_field(name='Древо умений гильдии', value='_ _')
            if self.users[author_id]['skill1'] == 0:
                skill_tree.add_field(name='1)Скидка на роли\n',
                                     value=f'Постоянная скидка на все роли для членов гильдии в виде 2500 {emoji} \n``Не изучено``',
                                     inline=False)
            if self.users[author_id]['skill1'] == 1:
                skill_tree.add_field(name='1)Скидка на роли',
                                     value=f'Постоянная скидка на все роли для членов гильдии в виде 2500 {emoji} \n``Изучено``',
                                     inline=False)
            if self.users[author_id]['skill2'] == 0:
                skill_tree.add_field(name='2)Скидка на подарки',
                                     value=f'Постоянная скидка на подарки для вайфу в размере 10% от стоимости подарка для всех членов гильдии!\n``Не изучено``',
                                     inline=False)
            if self.users[author_id]['skill2'] == 1:
                skill_tree.add_field(name='2)Скидка на подарки',
                                     value='Постоянная скидка на подарки для вайфу в размере 10% от стоимости подарка для всех членов гильдии!\n``Изучено``',
                                     inline=False)
            if self.users[author_id]['skill3'] == 0:
                skill_tree.add_field(name='3)Скидка на обои',
                                     value='Постоянная скидка на подарки для вайфу в размере 25% от стоимости обоев для всех членов гильдии!\n``Не изучено``',
                                     inline=False)
            if self.users[author_id]['skill3'] == 1:
                skill_tree.add_field(name='3)Скидка на обои',
                                     value='Постоянная скидка на подарки для вайфу в размере 25% от стоимости обоев для всех членов гильдии!\n``Изучено``',
                                     inline=False)
            if self.users[author_id]['skill4'] == 0:
                skill_tree.add_field(name='4)Увеличение лимита участников с 6 до 12', value='``Не изучено``',
                                     inline=False)
            if self.users[author_id]['skill4'] == 1:
                skill_tree.add_field(name='4)Увеличение лимита участников с 6 до 12', value='``Изучено``', inline=False)
            skill_tree.add_field(name='Введите номер умения, которое собираетесь изучать', value='_ _')
            await ctx.send(embed=skill_tree)

            def check(author):
                def inner_check(message):
                    return message.author == author

                return inner_check
            message = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
            if message.content.casefold() == '1':
                if self.users[author_id]['skillpoint'] >= 1:
                    self.users[author_id]['skill1'] = 1
                    self.users[author_id]['skillpoint'] -= 1
                    embed_skill = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_skill.add_field(name='Скидка на роли', value=f"Теперь гильдия {self.users[author_id]['guildname']} изучила это умение!")
                    await ctx.send(embed=embed_skill)
                    await self.client.loop.run_in_executor(None,
                                                           partial(json.dump, self.users, open('guilds.json', 'w'),
                                                                   indent=4))
            if message.content.casefold() == '2':
                if self.users[author_id]['skillpoint'] >= 1:
                    self.users[author_id]['skill2'] = 1
                    self.users[author_id]['skillpoint'] -= 1
                    embed_skill = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_skill.add_field(name='Скидка на подарки', value=f"Теперь гильдия {self.users[author_id]['guildname']} изучила это умение!")
                    await ctx.send(embed=embed_skill)
                    await self.client.loop.run_in_executor(None,
                                                           partial(json.dump, self.users, open('guilds.json', 'w'),
                                                                   indent=4))
            if message.content.casefold() == '3':
                if self.users[author_id]['skillpoint'] >= 1:
                    self.users[author_id]['skill3'] = 1
                    self.users[author_id]['skillpoint'] -= 1
                    embed_skill = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_skill.add_field(name='Скидка на обои',
                                          value=f"Теперь гильдия {self.users[author_id]['guildname']} изучила это умение!")
                    await ctx.send(embed=embed_skill)
                    await self.client.loop.run_in_executor(None,
                                                           partial(json.dump, self.users, open('guilds.json', 'w'),
                                                                   indent=4))
            if message.content.casefold() == '4':
                if self.users[author_id]['skillpoint'] >= 1:
                    self.users[author_id]['skill4'] = 1
                    self.users[author_id]['skillpoint'] -= 1
                    self.users[author_id]['memberlimit'] = 12
                    embed_skill = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_skill.add_field(name='Увеличение лимита участников с 6 до 12',
                                          value=f"Теперь гильдия {self.users[author_id]['guildname']} увеличила лимит участников с 6 до целых 12!")
                    await ctx.send(embed=embed_skill)
                    await self.client.loop.run_in_executor(None,
                                                           partial(json.dump, self.users, open('guilds.json', 'w'),
                                                                   indent=4))
            if self.users[author_id]['skillpoint'] <= 0:
                embed_skill_not_enough = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_skill_not_enough.add_field(name='Недостаточно очков!',
                                                 value='Недостаточно очков умений гильдии для того, чтобы изучить умение!')
                await ctx.send(embed=embed_skill_not_enough)

    @commands.command(name='guilddelete', aliases=['deleteguild', 'clandelete', 'deleteclan'])
    async def clandelition(self, ctx):
        with open("guilds.json", "r") as ff:
            self.users = json.load(ff)
        author_id = str(ctx.author.id)
        if self.users[author_id]['value'] == 3:
            def check(author):
                def inner_check(message):
                    return message.author == author

                return inner_check

            embed_guild_want_1 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_guild_want_1.add_field(name='Удаление гильдии', value='Вы уверены в том, что хотите безвозвратно удалить гильдию? Ничего возвращено не будет. Если вы уверены в данном действии, то напишите **да**')
            await ctx.send(embed=embed_guild_want_1)

            message = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
            if message.content.casefold() == 'да':
                embed_guild_want_2 = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_guild_want_2.add_field(name='Удаление гильдии',
                                             value='Вы ТОЧНО уверены в том, что хотите БЕЗВОЗВРАТНО удалить гильдию? '
                                                   'Ничего возвращено не будет. После этого сообщения данный процесс '
                                                   'НЕВОЗМОЖНО отменить. Если ВЫ УВЕРЕНЫ в данном действии, '
                                                   'то напишите название вашей гильдии ниже')
                await ctx.send(embed=embed_guild_want_2)
                message = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
                if message.content.casefold() == self.users[author_id]['guildname']:
                    for member in ctx.guild.members:
                        for role in member.roles:
                            if role.name == self.users[author_id]['guildname']:
                                await member.remove_roles(role)
                    del self.users[author_id]
                    embed_delition = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_delition.add_field(name='Удаление клана',  value='Процесс удаления клана был завершен')
                    await ctx.send(embed=embed_delition)
                    await self.client.loop.run_in_executor(None,
                                                           partial(json.dump, self.users, open('guilds.json', 'w'),
                                                                   indent=4))

    @commands.command(name='clantop', aliases=['guildtop'])
    async def topclan(self, ctx):
        with open('guilds.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict(
                {k: v for k, v in
                 sorted(d.items(), reverse=True, key=lambda i: (i[1]["guildlvl"], i[1]["guildmoney"]))})
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        for index, element in enumerate(result):
            try:
                user = await self.bot.fetch_user(element)
                a = user.name
            except AttributeError:
                a = '?'
            embed.add_field(name=str(int(index + 1)),
                            value=f" Guild - {result[element]['guildname']}, Guild Level - {result[element]['guildlvl']}, Guild Money - {result[element]['guildmoney']}",
                            inline=False)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Clans(client))