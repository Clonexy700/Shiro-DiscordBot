import discord
import asyncio
import json
from collections import OrderedDict
import random
import os
import numpy as np
import locale
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
from utility import utils
from collections import namedtuple
from discord.ext import commands


class Levels(commands.Cog):

    def __init__(self, client):
        self.bot = client

        self.bot.loop.create_task(self.save_users())

        with open(r'users.json', 'r') as f:
            self.users = json.load(f)
        with open(r'background.json', 'r') as ch:
            self.background = json.load(ch)

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open('users.json', 'w') as f:
                if self.users:
                    json.dump(self.users, f, indent=4)
            with open('background.json', 'w') as ch:
                if self.background:
                    json.dump(self.background, ch, indent=4)

            await asyncio.sleep(3)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((5 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_member_join(self, member):
        author_id = str(member.id)
        self.users[author_id] = {}
        self.users[author_id]['level'] = 1
        self.users[author_id]['exp'] = 0
        self.users[author_id]['last_msg'] = 0
        self.users[author_id]['bg_numerous'] = 0
        if not author_id in self.background:
            self.background[author_id] = {}
            self.background[author_id]['current_bg'] = 1
            self.background[author_id]['bg1'] = 1
            self.background[author_id]['bg2'] = 0
            self.background[author_id]['bg3'] = 0
            self.background[author_id]['bg4'] = 0
            self.background[author_id]['bg5'] = 0
            self.background[author_id]['bg6'] = 0
            self.background[author_id]['bg7'] = 0
            self.background[author_id]['bg8'] = 0
            self.background[author_id]['bg9'] = 0
            self.background[author_id]['bg10'] = 0
            self.background[author_id]['bg11'] = 0
            self.background[author_id]['bg12'] = 0
            self.background[author_id]['bg13'] = 0
            self.background[author_id]['bg14'] = 0
            self.background[author_id]['bg15'] = 0
            self.background[author_id]['bg16'] = 0
            self.background[author_id]['bg17'] = 0
            self.background[author_id]['bg18'] = 0
            self.background[author_id]['bg19'] = 0
            self.background[author_id]['bg20'] = 0
            self.background[author_id]['bg21'] = 0
            self.background[author_id]['bg22'] = 0
            self.background[author_id]['bg23'] = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.bot:
            return

        if not message.guild:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0
            self.users[author_id]['last_msg'] = 0

        if not author_id in self.background:
            self.background[author_id] = {}
            self.background[author_id]['current_bg'] = 1
            self.background[author_id]['bg1'] = 1
            self.background[author_id]['bg2'] = 0
            self.background[author_id]['bg3'] = 0
            self.background[author_id]['bg4'] = 0
            self.background[author_id]['bg5'] = 0
            self.background[author_id]['bg6'] = 0
            self.background[author_id]['bg7'] = 0
            self.background[author_id]['bg8'] = 0
            self.background[author_id]['bg9'] = 0
            self.background[author_id]['bg10'] = 0
            self.background[author_id]['bg11'] = 0
            self.background[author_id]['bg12'] = 0
            self.background[author_id]['bg13'] = 0
            self.background[author_id]['bg14'] = 0
            self.background[author_id]['bg15'] = 0
            self.background[author_id]['bg16'] = 0
            self.background[author_id]['bg17'] = 0
            self.background[author_id]['bg18'] = 0
            self.background[author_id]['bg19'] = 0
            self.background[author_id]['bg20'] = 0
            self.background[author_id]['bg21'] = 0
            self.background[author_id]['bg22'] = 0
            self.background[author_id]['bg23'] = 0

        if len(message.content) > 15:
            if message.content != self.users[author_id]['last_msg']:
                self.users[author_id]['exp'] += random.randint(13, 21)
                await self.bot.update_currency(author_id, random.randint(37, 99))
                self.users[author_id]['last_msg'] = message.content

        if self.lvl_up(author_id):
            embed_lvl_up = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_lvl_up.add_field(name='Уровень',
                                   value=f"{message.author.mention} достиг {self.users[author_id]['level']} уровня!\n "
                                         f"Умничка, продолжай в том же духе")
            embed_lvl_up.set_image(url='https://media.tenor.com/images/4ab61cccc28dc774c4f718c3080f8ccb/tenor.gif')
            await message.channel.send(embed=embed_lvl_up)
        if self.users[author_id]['level'] >= 1 and self.users[author_id]['level'] < 10:
            role1_id = 674969119069569044
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role1 = discord.utils.get(member.guild.roles, id=role1_id)
            await discord.Member.add_roles(member, role1)
        if self.users[author_id]['level'] >= 10 and self.users[author_id]['level'] < 20:
            role1_id = 674969119069569044
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role1 = discord.utils.get(member.guild.roles, id=role1_id)
            role2_id = 674967604686880805
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role2 = discord.utils.get(member.guild.roles, id=role2_id)
            await discord.Member.remove_roles(member, role1)
            await discord.Member.add_roles(member, role2)
        if self.users[author_id]['level'] >= 20 and self.users[author_id]['level'] < 30:
            role2_id = 674967604686880805
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role2 = discord.utils.get(member.guild.roles, id=role2_id)
            role3_id = 674968709038866442
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role3 = discord.utils.get(member.guild.roles, id=role3_id)
            await discord.Member.add_roles(member, role3)
            await discord.Member.remove_roles(member, role2)
        if self.users[author_id]['level'] >= 30 and self.users[author_id]['level'] < 40:
            role3_id = 674968709038866442
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role3 = discord.utils.get(member.guild.roles, id=role3_id)
            role4_id = 674968709940510748
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role4 = discord.utils.get(member.guild.roles, id=role4_id)
            await discord.Member.add_roles(member, role4)
            await discord.Member.remove_roles(member, role3)
        if self.users[author_id]['level'] >= 40 and self.users[author_id]['level'] < 50:
            role4_id = 674968709940510748
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role4 = discord.utils.get(member.guild.roles, id=role4_id)
            role5_id = 674968708300406784
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role5 = discord.utils.get(member.guild.roles, id=role5_id)
            await discord.Member.add_roles(member, role5)
            await discord.Member.remove_roles(member, role4)
        if self.users[author_id]['level'] >= 50 and self.users[author_id]['level'] < 60:
            role5_id = 674968708300406784
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role5 = discord.utils.get(member.guild.roles, id=role5_id)
            role6_id = 674968711769096223
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role6 = discord.utils.get(member.guild.roles, id=role6_id)
            await discord.Member.add_roles(member, role6)
            await discord.Member.remove_roles(member, role5)
        if self.users[author_id]['level'] >= 60:
            role6_id = 674968711769096223
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role6 = discord.utils.get(member.guild.roles, id=role6_id)
            role7_id = 674968707193241634
            memberid = message.author.id
            guild = self.bot.get_guild(674913512081850370)
            member = guild.get_member(memberid)
            role7 = discord.utils.get(member.guild.roles, id=role7_id)
            await discord.Member.add_roles(member, role7)
            await discord.Member.remove_roles(member, role6)

    @commands.command(name='level', aliases=['лвл', 'левел', 'lvl'])
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'- {member}', icon_url=member.avatar_url)

            embed.add_field(name='Уровень', value=self.users[member_id]['level'])
            embed.add_field(name='Опыт', value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def toplevel(self, ctx):
        with open('users.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict(
                {k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: (i[1]["level"], i[1]["exp"]))})
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
                            value=f"User - {a}       Level - {result[element]['level']}, Exp - {result[element]['exp']}",
                            inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def toplvl(self, ctx):
        with open('users.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict(
                {k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: (i[1]["level"], i[1]["exp"]))})
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
                            value=f"User - {a}       Level - {result[element]['level']}, Exp - {result[element]['exp']}",
                            inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='profile', aliases=['me', 'я', 'профиль', 'Я', 'Профиль', 'Me', 'ME'])
    @commands.guild_only()
    async def profile(self, ctx, user: discord.Member = None):
        async with ctx.channel.typing():

            locale.setlocale(locale.LC_TIME, "ru_RU")
            if user  is None:
                user = ctx.author
            embed = discord.Embed(
                colour=discord.Colour.dark_purple(),
                title=f"{user.name}'s Информация и  статистика."
            )
            embed.set_footer(text=f"ID: {user.id}")
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="__**Главное:**__", value=f"**Имя:\n** {user}\n"
                                                           f"**Аккаунт создан:**\n {user.created_at.strftime('%a, %d %b %Y %H:%M:%S')}\n")
            embed.add_field(name="__**Информация, связанная с сервером:**__", value=f"**Никнейм:** {user.nick}\n"
                                                                                    f"**Роли:** {' '.join([r.mention for r in user.roles[1:]])}")
            author_id = str(user.id)
            avatar = BytesIO()
            await user.avatar_url_as(format="png").save(avatar)

            avatar = Image.open(avatar)
            avatar = avatar.resize((130, 130))
            bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(avatar.size, Image.ANTIALIAS)
            avatar.putalpha(mask)

            output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.save('avatar.png')
            avatar = Image.open('avatar.png')
            fundo = Image.open('backgrounds/background1.png')
            if self.background[author_id]["current_bg"] == 1:
                fundo = Image.open('backgrounds/background1.png')
            if self.background[author_id]["current_bg"] == 2:
                fundo = Image.open('backgrounds/background2.png')
            if self.background[author_id]["current_bg"] == 3:
                fundo = Image.open('backgrounds/background3.png')
            if self.background[author_id]["current_bg"] == 4:
                fundo = Image.open('backgrounds/background4.png')
            if self.background[author_id]["current_bg"] == 5:
                fundo = Image.open('backgrounds/background5.png')
            if self.background[author_id]["current_bg"] == 6:
                fundo = Image.open('backgrounds/background6.png')
            if self.background[author_id]["current_bg"] == 7:
                fundo = Image.open('backgrounds/background7.png')
            if self.background[author_id]["current_bg"] == 8:
                fundo = Image.open('backgrounds/background8.png')
            if self.background[author_id]["current_bg"] == 9:
                fundo = Image.open('backgrounds/background9.png')
            if self.background[author_id]["current_bg"] == 10:
                fundo = Image.open('backgrounds/background10.png')
            if self.users[author_id]["bg_numerous"] == 11:
                fundo = Image.open('backgrounds/background11.png')
            if self.background[author_id]["current_bg"] == 12:
                fundo = Image.open('backgrounds/background12.png')
            if self.background[author_id]["current_bg"] == 13:
                fundo = Image.open('backgrounds/background13.png')
            if self.background[author_id]["current_bg"] == 14:
                fundo = Image.open('backgrounds/background14.png')
            if self.background[author_id]["current_bg"] == 15:
                fundo = Image.open('backgrounds/background15.png')
            if self.background[author_id]["current_bg"] == 16:
                fundo = Image.open('backgrounds/background16.png')
            if self.background[author_id]["current_bg"] == 17:
                fundo = Image.open('backgrounds/background17.png')
            if self.background[author_id]["current_bg"] == 18:
                fundo = Image.open('backgrounds/background18.png')
            if self.background[author_id]["current_bg"] == 19:
                fundo = Image.open('backgrounds/background19.png')
            if self.background[author_id]["current_bg"] == 20:
                fundo = Image.open('backgrounds/background20.png')
            if self.background[author_id]["current_bg"] == 21:
                fundo = Image.open('backgrounds/background21.png')
            if self.background[author_id]["current_bg"] == 22:
                fundo = Image.open('backgrounds/background22.png')
            if self.background[author_id]["current_bg"] == 23:
                fundo = Image.open('backgrounds/background23.png')
            if author_id == '602134789230821376':
                fundo = Image.open('backgrounds/backgroundwaifu.png')

            fonte2 = ImageFont.truetype('ARIALUNI.TTF', 18)
            escrever = ImageDraw.Draw(fundo)
            cur_xp = self.users[author_id]['exp']
            cur_lvl = self.users[author_id]['level']
            next_xp = round((5 * ((cur_lvl) ** 3)) / 5)
            with open('reputation.json', 'r') as f:
                self.reputation = json.load(f)
            escrever.text(xy=(250, 70),
                          text=f'   Уровень: {cur_lvl} \n   {cur_xp}/{next_xp} XP\n   Репутация: {self.reputation[author_id]["reputation"]}\n   Баланс: {self.bot.currency[author_id]["money"]}\n На сервер присоединился:\n {user.joined_at.strftime("%a, %d %b %Y %H:%M:%S")}\n',
                          fill=(255, 255, 255), font=fonte2)
            escrever.text(xy=(230, 24), text=f'Профиль: {user.name}', fill=(255, 255, 255),
                          font=fonte2)
            fundo.paste(avatar, (40, 90), avatar)
            bv = BytesIO()
            fundo.save(bv, "PNG", quality=100)
            bv.seek(0)
            file = discord.File(bv, filename="bv.png")
            await ctx.send(embed=embed, file=file)

    @commands.command(name='bgset',
                      aliases=['choosebg', 'backgroundchoose', 'setbg', 'bgchoose', 'wallpaperset', 'wallpaperchoose',
                               'wallpapershop', 'обоивыбор', 'выборобои', 'ов', 'mybg', 'моиобои', 'bgs'])
    async def bgset(self, ctx):
        checker = []
        embed_backgrounds = discord.Embed(color=discord.Colour.dark_purple(), timestamp=ctx.message.created_at)
        embed_backgrounds.add_field(name='**Все ваши обои**', value='У вас есть обои со следующими наименованиями:',
                                    inline=False)
        member_id = str(ctx.author.id)
        if not member_id in self.bot.currency:
            self.bot.currency[member_id] = {}
            self.bot.currency[member_id]['money'] = 0
            self.bot.currency[member_id]['box'] = 0
        if self.background[member_id]['bg1'] == 1:
            embed_backgrounds.add_field(name='1', value='_ _', inline=True)
            checker.append('1')
        if self.background[member_id]['bg2'] == 1:
            embed_backgrounds.add_field(name='2', value='_ _', inline=True)
            checker.append('2')
        if self.background[member_id]['bg3'] == 1:
            embed_backgrounds.add_field(name='3', value='_ _', inline=True)
            checker.append('3')
        if self.background[member_id]['bg4'] == 1:
            embed_backgrounds.add_field(name='4', value='_ _', inline=True)
            checker.append('4')
        if self.background[member_id]['bg5'] == 1:
            embed_backgrounds.add_field(name='5', value='_ _', inline=True)
            checker.append('5')
        if self.background[member_id]['bg6'] == 1:
            embed_backgrounds.add_field(name='6', value='_ _', inline=True)
            checker.append('6')
        if self.background[member_id]['bg7'] == 1:
            embed_backgrounds.add_field(name='7', value='_ _', inline=True)
            checker.append('7')
        if self.background[member_id]['bg8'] == 1:
            embed_backgrounds.add_field(name='8', value='_ _', inline=True)
            checker.append('8')
        if self.background[member_id]['bg9'] == 1:
            embed_backgrounds.add_field(name='9', value='_ _', inline=True)
            checker.append('9')
        if self.background[member_id]['bg10'] == 1:
            embed_backgrounds.add_field(name='10', value='_ _', inline=True)
            checker.append('10')
        if self.background[member_id]['bg11'] == 1:
            embed_backgrounds.add_field(name='11', value='_ _', inline=True)
            checker.append('11')
        if self.background[member_id]['bg12'] == 1:
            embed_backgrounds.add_field(name='12', value='_ _', inline=True)
            checker.append('12')
        if self.background[member_id]['bg13'] == 1:
            embed_backgrounds.add_field(name='13', value='_ _', inline=True)
            checker.append('13')
        if self.background[member_id]['bg14'] == 1:
            embed_backgrounds.add_field(name='14', value='_ _', inline=True)
            checker.append('14')
        if self.background[member_id]['bg15'] == 1:
            embed_backgrounds.add_field(name='15', value='_ _', inline=True)
            checker.append('15')
        if self.background[member_id]['bg16'] == 1:
            embed_backgrounds.add_field(name='16', value='_ _', inline=True)
            checker.append('16')
        if self.background[member_id]['bg17'] == 1:
            embed_backgrounds.add_field(name='17', value='_ _', inline=True)
            checker.append('17')
        if self.background[member_id]['bg18'] == 1:
            embed_backgrounds.add_field(name='18', value='_ _', inline=True)
            checker.append('18')
        if self.background[member_id]['bg19'] == 1:
            embed_backgrounds.add_field(name='19', value='_ _', inline=True)
            checker.append('19')
        if self.background[member_id]['bg20'] == 1:
            embed_backgrounds.add_field(name='20', value='_ _', inline=True)
            checker.append('20')
        if self.background[member_id]['bg21'] == 1:
            embed_backgrounds.add_field(name='21', value='_ _', inline=True)
            checker.append('21')
        if self.background[member_id]['bg22'] == 1:
            embed_backgrounds.add_field(name='22', value='_ _', inline=True)
            checker.append('22')
        if self.background[member_id]['bg23'] == 1:
            embed_backgrounds.add_field(name='23', value='_ _', inline=True)
            checker.append('23')
        await ctx.send(embed=embed_backgrounds)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in checker

            return inner_check

        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=120)

        if msg.content in checker:
            self.background[member_id]['current_bg'] = int(msg.content)
            await ctx.send('В ваш профиль установлены новые обои, наслаждайтесь!')

    @commands.command(name='bgshop',
                      aliases=['бгшоп', 'обои', 'магазобои', 'bgmarket', 'shopbg', 'marketbg', 'обоимагаз',
                               'wallpapers'])
    async def backgroundshop(self, ctx):
        member_id = str(ctx.author.id)
        if not member_id in self.bot.currency:
            self.bot.currency[member_id] = {}
            self.bot.currency[member_id]['money'] = 0
            self.bot.currency[member_id]['box'] = 0
        embed_bg = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        emoji = self.bot.get_emoji(676803534758477845)
        embed_bg.add_field(name='**Обои профиля**', value=f'Для покупки подходящих вам обоев профиля напишите цифру '
                                                          f'обоев, после того, как бот отправит сообщение со всеми '
                                                          f'картинками профиля и если у вас будет достаточно валюты в '
                                                          f'виде {emoji} , то обои станут вам доступны для установки в '
                                                          f'ваш профиль', inline=False)
        embed_bg.add_field(name='_ _',
                           value=f'``#1``\n``0`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#2``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#3``\n``30000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#4``\n``10000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#5``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#6``\n``15000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#7``\n``5000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#8``\n``5000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#9``\n``15000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#10``\n``18000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#11``\n``30000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#12``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#13``\n``15000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#14``\n``15000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#15``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#16``\n``30000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#17``\n``50000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#18``\n``50000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#19``\n``40000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#20``\n``30000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#21``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#22``\n``25000`` {emoji}', inline=True)
        embed_bg.add_field(name='_ _',
                           value=f'``#23``\n``30000`` {emoji}', inline=True)
        embed_bg.set_image(
            url='https://cdn.discordapp.com/attachments/621005423335702528/681874404212604945/84a9121cafbe74af.png')
        await ctx.send(embed=embed_bg)
        embed_bg1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_bg2 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_bg3 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_bg4 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_bg1.set_image(url='https://cdn.discordapp.com/attachments/621005423335702528/681874797721813084/2.png')
        embed_bg2.set_image(url='https://cdn.discordapp.com/attachments/621005423335702528/681875426162901008/3.png')
        embed_bg3.set_image(url='https://cdn.discordapp.com/attachments/621005423335702528/681875948211142661/4.png')
        embed_bg4.set_image(url='https://cdn.discordapp.com/attachments/621005423335702528/681876585858859025/4.png')
        await ctx.send(embed=embed_bg1)
        await ctx.send(embed=embed_bg2)
        await ctx.send(embed=embed_bg3)
        await ctx.send(embed=embed_bg4)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', '23')

            return inner_check

        member = ctx.author

        embednomoney = discord.Embed(color=discord.Colour.dark_purple())
        embednomoney.set_author(name=f'Неуспешная покупка {member}', icon_url=member.avatar_url)

        embednomoney.add_field(name='Магазин', value='Не хватает денег для покупки')

        embednomoney.add_field(name='Баланс', value=f"{self.bot.currency[member_id]['money']}{emoji}", inline=False)

        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=120)

        if msg.content == '1':
            if self.bot.currency[member_id]['money'] - 0 >= 0:
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'У вас уже есть эти обои {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Эти обои у вас есть!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

        if msg.content == '2':
            if self.bot.currency[member_id]['money'] - 25000 >= 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки', value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg2'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '3':
            if self.bot.currency[member_id]['money'] - 30000 >= 0:
                await self.bot.unupdate_currency(member_id, 30000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg3'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '4':
            if self.bot.currency[member_id]['money'] - 10000 >= 0:
                await self.bot.unupdate_currency(member_id, 10000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg4'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '5':
            if self.bot.currency[member_id]['money'] - 25000 >= 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg5'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '6':
            if self.bot.currency[member_id]['money'] - 15000 > 0:
                await self.bot.unupdate_currency(member_id, 15000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg6'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '7':
            if self.bot.currency[member_id]['money'] - 5000 > 0:
                await self.bot.unupdate_currency(member_id, 5000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg7'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '8':
            if self.bot.currency[member_id]['money'] - 5000 > 0:
                await self.bot.unupdate_currency(member_id, 5000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg8'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '9':
            if self.bot.currency[member_id]['money'] - 15000 > 0:
                await self.bot.unupdate_currency(member_id, 15000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg9'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '10':
            if self.bot.currency[member_id]['money'] - 18000 > 0:
                await self.bot.unupdate_currency(member_id, 18000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg10'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '11':
            if self.bot.currency[member_id]['money'] - 30000 > 0:
                await self.bot.unupdate_currency(member_id, 30000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg11'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '12':
            if self.bot.currency[member_id]['money'] - 25000 > 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg12'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '13':
            if self.bot.currency[member_id]['money'] - 15000 > 0:
                await self.bot.unupdate_currency(member_id, 15000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg13'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '14':
            if self.bot.currency[member_id]['money'] - 15000 > 0:
                await self.bot.unupdate_currency(member_id, 15000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg14'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '15':
            if self.bot.currency[member_id]['money'] - 25000 > 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg15'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '16':
            if self.bot.currency[member_id]['money'] - 30000 > 0:
                await self.bot.unupdate_currency(member_id, 30000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg16'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '17':
            if self.bot.currency[member_id]['money'] - 50000 > 0:
                await self.bot.unupdate_currency(member_id, 50000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg17'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '18':
            if self.bot.currency[member_id]['money'] - 50000 > 0:
                await self.bot.unupdate_currency(member_id, 50000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg18'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '19':
            if self.bot.currency[member_id]['money'] - 40000 > 0:
                await self.bot.unupdate_currency(member_id, 40000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg19'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '20':
            if self.bot.currency[member_id]['money'] - 30000 > 0:
                await self.bot.unupdate_currency(member_id, 30000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg20'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '21':
            if self.bot.currency[member_id]['money'] - 25000 > 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg21'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '22':
            if self.bot.currency[member_id]['money'] - 25000 > 0:
                await self.bot.unupdate_currency(member_id, 25000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg22'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '23':
            if self.bot.currency[member_id]['money'] - 30000 > 0:
                await self.bot.unupdate_currency(member_id, 30000)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели данные обои', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.bot.currency[member_id]['money']}{emoji}",
                                inline=False)
                self.background[member_id]['bg23'] = 1
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

    @commands.command(name='boxbuy', aliases=['boxshop', 'pandorashop', 'lootbuy', 'buyloot', 'lootshop', 'fortuneshop','buyfortune', 'fortunashop', 'shopfortuna', 'buybox'])
    async def buyfortune(self, ctx, box_num: int = 1):
        member_id = str(ctx.author.id)
        if not member_id in self.bot.currency:
            self.bot.currency[member_id] = {}
            self.bot.currency[member_id]['money'] = 0
            self.bot.currency[member_id]['box'] = 0
        if self.bot.currency[member_id]['money'] - 18000 * box_num >= 0:
            await self.bot.unupdate_currency(member_id, 18000 * box_num)
            embed_bought = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_bought.add_field(name='Магазин', value=f'Вы купили {box_num} коробок пандоры!')
            await ctx.send(embed=embed_bought)
            await self.bot.add_pandora(member_id, box_num)
        else:
            embed_no_money = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_no_money.add_field(name='Баланс', value='Недостаточно средств на счете пользователя, чтобы реализовать покупку')
            await ctx.send(embed=embed_no_money)
    @commands.command(name='fortunafree', aliases=['freefortune', 'getfortune', 'getfortuna', 'dailyfortune', 'fortunedaily', 'paybox', 'boxpay', 'getbox', 'boxget', 'boxfree', 'freebox'])
    @commands.cooldown(1, 259200, commands.BucketType.user)
    async def freefortuna(self, ctx):
        member_id = str(ctx.author.id)
        if not member_id in self.bot.currency:
            self.bot.currency[member_id] = {}
            self.bot.currency[member_id]['money'] = 0
            self.bot.currency[member_id]['box'] = 0
        await self.bot.add_pandora(member_id, 1)
        embed_added = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_added.add_field(name='Фортуна', value='На ваш аккаунт была добавлена бесплатная коробка фортуны! Теперь ждите 3 дня до следующей!')
        await ctx.send(embed=embed_added)

    @commands.command(name='fortune',
                      aliases=['pandora', 'lootbox', 'коробка', 'пандора', 'фортуна', 'лутбокс', 'лут', 'loot', 'openbox', 'boxopen'])
    async def fortune(self, ctx):

        emoji = self.bot.get_emoji(676803534758477845)
        member_id = str(ctx.author.id)
        if not member_id in self.bot.currency:
            self.bot.currency[member_id] = {}
            self.bot.currency[member_id]['money'] = 0
            self.bot.currency[member_id]['box'] = 0
        if self.bot.currency[member_id]['box'] - 1 >= 0:
            await self.bot.remove_pandora(member_id, 1)
            fortunaizer = [
                1, 1, 1, 2, 2, 2, 1, 2, 1, 5, 5, 3, 4, 4, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1,
                1, 1, 1, 2, 2, 2, 5, 2, 1, 1, 1, 5, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2,
                1, 2, 1, 5, 5, 5, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 5, 5, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1,
                1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 5, 5, 1, 1, 1, 2, 2, 1, 1, 2]
            member = ctx.author
            random_item = random.choice(fortunaizer)
            if random_item == 1:
                money_random_selector = random.randint(500, 25001)
                await self.bot.update_currency(member_id, money_random_selector)
                embed = discord.Embed(color=discord.Colour.dark_purple())
                embed.add_field(name='Фортуна',
                                value=f'Ящик пандоры открылся и вы получили...\n + ``{money_random_selector}`` {emoji}')
                await ctx.send(embed=embed)
            if random_item == 2:
                role5 = discord.utils.get(member.guild.roles, name="🍃")
                role6 = discord.utils.get(member.guild.roles, name="🍁")
                role7 = discord.utils.get(member.guild.roles, name="🍊")
                role8 = discord.utils.get(member.guild.roles, name="❄")
                role9 = discord.utils.get(member.guild.roles, name="🌙")
                role12 = discord.utils.get(member.guild.roles, name="💫")
                role13 = discord.utils.get(member.guild.roles, name="🌹")
                role_revoker = [5, 6, 7, 8, 9, 12, 13]
                role_revoker_answer = random.choice(role_revoker)
                if role_revoker_answer == 5:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role5.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role5)
                if role_revoker_answer == 6:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role6.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role6)
                if role_revoker_answer == 7:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role7.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role7)
                if role_revoker_answer == 8:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role8.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role8)
                if role_revoker_answer == 9:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role9.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role9)
                if role_revoker_answer == 12:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role12.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role12)
                if role_revoker_answer == 13:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + {role13.mention}')
                    await ctx.send(embed=embed)
                    await discord.Member.add_roles(ctx.author, role13)
            if random_item == 3:
                embed = discord.Embed(color=discord.Colour.dark_purple())
                embed.add_field(name='Фортуна',
                                value=f'Ящик пандоры открылся и вы получили...\n + ваш собственный полностью '
                                      f'настраиваемый голосовой канал. Обратитесь к администраторам для его создания')
                await ctx.send(embed=embed)
            if random_item == 4:
                embed = discord.Embed(color=discord.Colour.dark_purple())
                embed.add_field(name='Фортуна',
                                value=f'Ящик пандоры открылся и вы получили...\n + ваш собственный клан. Обратитесь к '
                                      f'администраторам для его создания')
                await ctx.send(embed=embed)
            if random_item == 5:
                background = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                background_choose = random.choice(background)
                if background_choose == 2:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 2')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg2'] = 1
                if background_choose == 3:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 3')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg3'] = 1
                if background_choose == 4:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 4')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg4'] = 1
                if background_choose == 5:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 5')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg5'] = 1
                if background_choose == 6:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 6')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg6'] = 1
                if background_choose == 7:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 7')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg7'] = 1
                if background_choose == 8:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 8')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg8'] = 1
                if background_choose == 9:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 9')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg9'] = 1
                if background_choose == 10:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 10')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg10'] = 1
                if background_choose == 11:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 11')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg11'] = 1
                if background_choose == 12:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 12')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg12'] = 1
                if background_choose == 13:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 13')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg13'] = 1
                if background_choose == 14:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 14')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg14'] = 1
                if background_choose == 15:
                    embed = discord.Embed(color=discord.Colour.dark_purple())
                    embed.add_field(name='Фортуна',
                                    value=f'Ящик пандоры открылся и вы получили...\n + обои для вашего профиля под номером 15')
                    await ctx.send(embed=embed)
                    self.background[member_id]['bg15'] = 1
        else:
            embed_no_box = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_no_box.add_field(name='Ошибка', value='Недостаточно коробок пандоры для использования команды')
            await ctx.send(embed=embed_no_box)

    @freefortuna.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Перезарядка',
                            value='Команда находится на перезарядке. Вы можете использовать её только раз в три дня :timer: \n Осталось: {:.2f}s'.format(
                                error.retry_after))
            embed.set_footer(text='Команда на перезарядке, перезвоните позже (✧ω✧)')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Levels(bot))