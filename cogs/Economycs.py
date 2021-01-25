import discord
from discord.ext import commands
import os
import json
import asyncio
import random
from functools import partial
from collections import OrderedDict
import requests
import random, sys
from typing import List

msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]


class Economycs(commands.Cog):

    def __init__(self, client):
        self.client = client

        with open(r'users.json', 'r') as f:
            self.users = json.load(f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.author.bot:
            return

        if not message.guild:
            return

        author_id = str(message.author.id)

        if len(message.content) > 15:
            if message.content != self.users[author_id]['last_msg']:
                await self.client.update_currency(author_id, random.randint(11, 30))

                self.users[author_id]['last_msg'] = message.content

                devil_number = (random.randint(1, 1000))
                if devil_number == 666:
                    embed_devil = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_devil.add_field(name='Ящик пандоры', value='С шансом 0.1% вы получили ящик Пандоры! '
                                                                     'Используйте .fortune чтобы воспользоваться им!')
                    await message.channel.send(embed=embed_devil)
                    await self.client.add_pandora(author_id, 1)

    @commands.command(name='setup_bot')
    @commands.cooldown(1, 31536000, commands.BucketType.guild)
    async def setup_bot(self, ctx):
        msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]
        guild = ctx.guild
        embedsetup = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedsetup.add_field(name='Setup :computer: ',
                             value=f'Setup is completed. You are welcome! Now all commands will work correctly! {random.choice(msgend)}')
        embedsetup.set_image(
            url='https://media1.tenor.com/images/54e8631b77e3612be9a217ed98961447/tenor.gif?itemid=9911334')
        embedsetup.set_footer(text='maybe correctly')
        await guild.create_role(name='💍', color=discord.Colour.dark_purple())
        await guild.create_role(name='Shiro lover', color=discord.Colour.magenta())
        await guild.create_role(name='Sempaii?', color=discord.Colour.dark_gold())
        await guild.create_role(name='N.E.E.T', color=discord.Colour.dark_grey())
        await guild.create_role(name='Loli', color=discord.Colour.dark_blue())
        await guild.create_role(name='🍃', color=discord.Colour.green())
        await guild.create_role(name='🍁', color=discord.Colour.gold())
        await guild.create_role(name='🍊', color=discord.Colour.orange())
        await guild.create_role(name='❄', color=discord.Colour.blue())
        await guild.create_role(name='🌙', color=discord.Colour.dark_orange())
        await guild.create_role(name='🍌', color=discord.Colour.gold())
        await guild.create_role(name='🍎', color=discord.Colour.red())
        await guild.create_role(name='💫', color=discord.Colour.gold())
        await guild.create_role(name='🌹', color=discord.Colour.red())
        await guild.create_role(name='🌌', color=discord.Colour.darker_grey())
        await guild.create_role(name='Is it was a great idea to spend all money on this role?',
                                color=discord.Colour.dark_green())
        await guild.create_role(name='Stranger', color=discord.Colour.lighter_grey())
        await ctx.send(embed=embedsetup)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_id = str(member.id)
        if not member_id in self.client.currency:
            self.client.currency[member_id] = {}
            self.client.currency[member_id]['money'] = 0
            self.client.currency[member_id]['box'] = 0
        role1 = discord.utils.get(member.guild.roles, name="クリア Kuria")
        role2 = discord.utils.get(member.guild.roles, name="⁣ ⁣ ⁣⁣⁣⁣⁣    ⁣  ⁣⁣⁣⁣⁣⁣    Уровень⁣  ⁣⁣⁣⁣⁣⁣       ⁣⁣⁣⁣⁣")
        role3 = discord.utils.get(member.guild.roles, name="⁣ ⁣ ⁣⁣⁣⁣⁣    ⁣  ⁣⁣⁣⁣⁣⁣    Игры⁣  ⁣⁣⁣⁣⁣⁣       ⁣⁣⁣⁣⁣")
        role4 = discord.utils.get(member.guild.roles, name="⁣ ⁣ ⁣⁣⁣⁣⁣    ⁣  ⁣⁣⁣⁣⁣⁣    Инфо  ⁣⁣⁣⁣⁣⁣       ⁣⁣⁣⁣⁣")
        role6 = discord.utils.get(member.guild.roles, name="⁣ ⁣ ⁣⁣⁣⁣⁣    ⁣  ⁣⁣⁣⁣⁣⁣    Клан  ⁣⁣⁣⁣⁣⁣       ⁣⁣⁣⁣⁣")
        role7 = discord.utils.get(member.guild.roles, name="⁣ ⁣ ⁣⁣⁣⁣⁣    ⁣  ⁣⁣⁣⁣⁣⁣      ⁣⁣⁣⁣⁣⁣       ⁣⁣⁣⁣⁣⁣ ⁣ ⁣⁣⁣⁣⁣  ")
        role5 = discord.utils.get(member.guild.roles, id=674969119069569044)
        await discord.Member.add_roles(member, role1)
        await discord.Member.add_roles(member, role2)
        await discord.Member.add_roles(member, role3)
        await discord.Member.add_roles(member, role4)
        await discord.Member.add_roles(member, role5)
        await discord.Member.add_roles(member, role6)
        await discord.Member.add_roles(member, role7)

    @commands.command(name='money', aliases=['баланс', 'balance', '$', 'карман', 'pocket', 'мани'])
    async def money(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.client.currency:
            await ctx.send("Вы пытаетесь определить бота или данного пользователя не существует в файлах хранения!")
            self.client.currency[member_id] = {}
            self.client.currency[member_id]['money'] = 0
            self.client.currency[member_id]['box'] = 0
        else:
            emoji = self.client.get_emoji(676803534758477845)

            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'  {member}', icon_url=member.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/621005423335702528/676802134875832350'
                                    '/doesnt_need_money_mokou.png')

            embed.add_field(name='Ваш счёт',
                            value=f"У тебя на счету: **{self.client.currency[member_id]['money']}** {emoji}\n ``(灬♥ω♥灬)`` \n")

            await ctx.send(embed=embed)

    @commands.command()
    async def admm(self, ctx, member: discord.Member, money_mum: int):
        if ctx.author.id == 314618320093577217:
            member_id = str(member.id)
            if not member_id in self.client.currency:
                self.client.currency[member_id] = {}
                self.client.currency[member_id]['money'] = 0
                self.client.currency[member_id]['box'] = 0

            await self.client.update_currency(member_id, money_mum)
        else:
            await ctx.send('You are not Shiro owner for using this command!')

    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.command(name='moneydaily', aliases=['daily', 'dailymoney', 'дневное', 'награда', 'timely', 'payday', 'daypay', 'н', 'денежка', 'pay'])
    async def moneydaily(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        embed_daily_money = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        member = ctx.author
        member_id = str(member.id)
        if not member_id in self.client.currency:
            self.client.currency[member_id] = {}
            self.client.currency[member_id]['money'] = 0
            self.client.currency[member_id]['box'] = 0
        premium = discord.utils.get(member.guild.roles, name='世界 Sekai')
        reward = 1000
        if premium in member.roles:
            reward = 3500
        embed_daily_money.add_field(name='Баланс', value=f'Вы получили + {reward} {emoji}')
        await self.client.update_currency(member_id, reward)

        await ctx.send(embed=embed_daily_money)

    @moneydaily.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Перезарядка',
                            value='Команда находится на перезарядке. Вы можете использовать её только раз в два часа :timer: \n Осталось: {:.2f}s'.format(
                                error.retry_after))
            embed.set_footer(text='Команда на перезарядке, перезвоните позже (✧ω✧)')
            await ctx.send(embed=embed)

    @commands.command(name='market', aliases=['магазин', 'маркет', 'shop', 'магаз'])
    async def market(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        member = ctx.author
        member_id = str(member.id)
        if not member_id in self.client.currency:
            self.client.currency[member_id] = {}
            self.client.currency[member_id]['money'] = 0
            self.client.currency[member_id]['box'] = 0
        embedmarket = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        role1 = discord.utils.get(member.guild.roles, name="Hentai")
        role2 = discord.utils.get(member.guild.roles, name="ecchi")
        role3 = discord.utils.get(member.guild.roles, name="🍌")
        role4 = discord.utils.get(member.guild.roles, name="Loli")
        role5 = discord.utils.get(member.guild.roles, name="🍃")
        role6 = discord.utils.get(member.guild.roles, name="🍁")
        role7 = discord.utils.get(member.guild.roles, name="🍊")
        role8 = discord.utils.get(member.guild.roles, name="❄")
        role9 = discord.utils.get(member.guild.roles, name="🌙")
        role10 = discord.utils.get(member.guild.roles, name="No Game")
        role11 = discord.utils.get(member.guild.roles, name="No Life")
        role12 = discord.utils.get(member.guild.roles, name="💫")
        role13 = discord.utils.get(member.guild.roles, name="🌹")
        role14 = discord.utils.get(member.guild.roles, name='鈍い | Nibui')
        role15 = discord.utils.get(member.guild.roles, name='灰色 Haiiro')
        role16 = discord.utils.get(member.guild.roles, name='スモーキー Sumōkī')
        role17 = discord.utils.get(member.guild.roles, name='ぼやけた Boyaketa')
        role18 = discord.utils.get(member.guild.roles, name='ダーク Dāku')
        embedmarket.set_author(name='Магазинчик')
        embedmarket.add_field(name='Роли', value=f'Магазин ролей, здесь вы можете купить роли за{emoji}',
                              inline=False)
        embedmarket.add_field(name='_ _',
                              value=f'``#1`` {role1.mention}\n``20000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#2`` {role2.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#3`` {role3.mention}\n``10000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#4`` {role4.mention}\n``10000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#5`` {role5.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#6`` {role6.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#7`` {role7.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#8`` {role8.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#9`` {role9.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#10`` {role10.mention}\n``10000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#11`` {role11.mention}\n``10000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#12`` {role12.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#13`` {role13.mention}\n``5000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#14`` {role14.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#15`` {role15.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#16`` {role16.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#17`` {role17.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.add_field(name='_ _',
                              value=f'``#18`` {role18.mention}\n``15000`` {emoji}', inline=True)
        embedmarket.set_image(url='https://i.pinimg.com/originals/01/1f/8b/011f8b4d0ebbae3c1c3c628258da5c2e.gif')
        await ctx.send(embed=embedmarket)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18')

            return inner_check

        msg = await self.client.wait_for('message', check=check(ctx.author), timeout=30)

        embednomoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

        embednomoney.set_author(name=f'Неуспешная покупка {member}', icon_url=member.avatar_url)

        embednomoney.add_field(name='Магазин', value='Не хватает денег для покупки')

        embednomoney.add_field(name='Баланс после покупки', value=f"{self.client.currency[member_id]['money']}{emoji}", inline=False)

        if msg.content == '1':
            if self.client.currency[member_id]['money'] - 20000 >= 0:
                await self.client.unupdate_currency(member_id, 20000)
                await discord.Member.add_roles(member, role1)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role1.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

        if msg.content == '2':
            if self.client.currency[member_id]['money'] - 15000 >= 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role2)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role2.mention}', inline=False)

                embed.add_field(name='Баланс после покупки', value=f"{self.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '3':
            if self.client.currency[member_id]['money'] - 10000 >= 0:
                await self.client.unupdate_currency(member_id, 10000)
                await discord.Member.add_roles(member, role3)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role3.mention}', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '4':
            if self.client.currency[member_id]['money'] - 10000 >= 0:
                await self.client.unupdate_currency(member_id, 10000)
                await discord.Member.add_roles(member, role4)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role4.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '5':
            if self.client.currency[member_id]['money'] - 5000 >= 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role5)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role5.mention}', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '6':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role6)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role6.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '7':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role7)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role7.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '8':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role8)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role8.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '9':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role9)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role9.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '10':
            if self.client.currency[member_id]['money'] - 10000 > 0:
                await self.client.unupdate_currency(member_id, 10000)
                await discord.Member.add_roles(member, role10)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role10.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '11':
            if self.client.currency[member_id]['money'] - 10000 > 0:
                await self.client.unupdate_currency(member_id, 10000)
                await discord.Member.add_roles(member, role11)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role11.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '12':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role12)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role12.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '13':
            if self.client.currency[member_id]['money'] - 5000 > 0:
                await self.client.unupdate_currency(member_id, 5000)
                await discord.Member.add_roles(member, role13)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role13.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '14':
            if self.client.currency[member_id]['money'] - 15000 > 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role14)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role14.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '15':
            if self.client.currency[member_id]['money'] - 15000 > 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role15)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role15.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '16':
            if self.client.currency[member_id]['money'] - 15000 > 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role16)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role16.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '17':
            if self.client.currency[member_id]['money'] - 15000 > 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role17)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role17.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '18':
            if self.client.currency[member_id]['money'] - 15000 > 0:
                await self.client.unupdate_currency(member_id, 15000)
                await discord.Member.add_roles(member, role18)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Успешная покупка {member}', icon_url=member.avatar_url)

                embed.add_field(name='Магазин', value=f'Вы успешно приобрели следующую роль: {role18.mention}!', inline=False)

                embed.add_field(name='Баланс после покупки',
                                value=f"{self.client.currency[member_id]['money']}{emoji}",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

    @commands.command(name='give', aliases=['send', 'отправить'], pass_context=True)
    async def moneygive(self, ctx, member: discord.Member, money_number: int):
        emoji = self.client.get_emoji(676803534758477845)
        author = ctx.message.author
        embedmoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embedmoney.add_field(name='Денежная операция',
                             value=f"{author.mention} отправил {money_number} {emoji} {member.mention}")
        member_id = str(member.id)
        author_id = str(author.id)
        if not member_id in self.client.currency:
            self.client.currency[member_id] = {}
            self.client.currency[member_id]['money'] = 0
            self.client.currency[member_id]['box'] = 0
        if author == member:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.add_field(name='Ошибка', value="Нельзя отправить деньги себе")
            await ctx.send(embed=embed)
        if money_number < 1:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.add_field(name='Ошибка', value=f"Вы можете отправить минимально 1 {emoji}")
            await ctx.send(embed=embed)
        if author != member:
            if money_number >= 1:
                if self.client.currency[author_id]['money'] - money_number > 0:
                    await self.client.unupdate_currency(author_id, money_number)
                    await self.client.update_currency(member_id, money_number)
                    await ctx.send(embed=embedmoney)
                else:
                    embednomoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                    embednomoney.set_author(name=f'Неудачная транзакция {author}', icon_url=author.avatar_url)

                    embednomoney.add_field(name='Ошибка', value='Не хватает денег для перевода')

                    embednomoney.add_field(name='Баланс', value=f"{self.client.currency[member_id]['money']} {emoji}",
                                           inline=False)
                    await ctx.send(embed=embednomoney)

    @commands.command(pass_context=True, no_pm=True)
    async def slot(self, ctx, bet: int):
        emoji = self.client.get_emoji(676803534758477845)
        bet = 1 if not bet else bet
        member_id = str(ctx.author.id)
        randomization = [":cherry_blossom:",
                         ":banana:",
                         ":cherries:",
                         ":diamonds:",
                         ":apple:",
                         ":sparkles:"]
        await self.client.unupdate_currency(member_id, bet)
        if self.client.currency[member_id]['money'] >= 0:
            line1 = f"{random.choice(randomization)} {random.choice(randomization)} {random.choice(randomization)}"
            slot1 = f"{random.choice(randomization)}"
            slot2 = f"{random.choice(randomization)}"
            slot3 = f"{random.choice(randomization)}"
            line3 = f"{random.choice(randomization)} {random.choice(randomization)} {random.choice(randomization)}"
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Slots', value=f" {line1}\n {slot1} {slot2} {slot3}\n {line3}")
            await ctx.send(embed=embed)
            if slot1 == ":cherry_blossom:" and slot2 == ":cherry_blossom:" and slot3 != ":cherry_blossom:" or slot1 != ":cherry_blossom:" and slot2 == ":cherry_blossom:" and slot3 == ":cherry_blossom:":
                bet_win = round(bet * 1.2)
                await ctx.send(f'You win {bet_win} {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":banana:" and slot2 == ":banana:" and slot3 != ":banana:" or slot1 != ":banana:" and slot2 == ":banana:" and slot3 == ":banana:":
                bet_win = round(bet * 1.4)
                await ctx.send(f' You win {bet_win}  :{emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":cherries:" and slot2 == ":cherries:" and slot3 != ":cherries:" or slot1 != ":cherries:" and slot2 == ":cherries:" and slot3 == ":cherries:":
                bet_win = round(bet * 1.3)
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":diamonds:" and slot2 == ":diamonds:" and slot3 != ":diamonds:" or slot1 != ":diamonds:" and slot2 == ":diamonds:" and slot3 == ":diamonds:":
                bet_win = round(bet * 1.6)
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":apple:" and slot2 == ":apple:" and slot3 != ":apple:" or slot1 != ":apple:" and slot2 == ":apple:" and slot3 == ":apple:":
                bet_win = round(bet * 1.1)
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":sparkles:" and slot2 == ":sparkles:" and slot3 != ":sparkles:" or slot1 != ":sparkles:" and slot2 == ":sparkles:" and slot3 == ":sparkles:":
                bet_win = round(bet * 1.7)
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":cherry_blossom:" and slot2 == ":cherry_blossom:" and slot3 == ":cherry_blossom:":
                bet_win = bet * 2
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":banana:" and slot2 == ":banana:" and slot3 == ":banana:":
                bet_win = bet * 2
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":cherries:" and slot2 == ":cherries:" and slot3 == ":cherries:":
                bet_win = bet * 3
                await ctx.send(f' You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":diamonds:" and slot2 == ":diamonds:" and slot3 == ":diamonds:":
                bet_win = bet * 10
                await ctx.send(f'Woah?!Oh. You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":apple:" and slot2 == ":apple:" and slot3 == ":apple:":
                bet_win = round(bet * 1.9)
                await ctx.send(f'You win {bet_win}  {emoji}')
                await self.client.update_currency(member_id, bet_win)
            if slot1 == ":sparkles:" and slot2 == ":sparkles:" and slot3 == ":sparkles:":
                bet_win = bet * 5
                await ctx.send(f'Not bad. You win {bet_win} {emoji}')
                await self.client.update_currency(member_id, bet_win)
        else:
            await self.client.update_currency(member_id, bet)
            await ctx.send(f"You have not enough {emoji} too play!")

    @slot.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Error', value='Your bet is required option!\n ```$slot 100```')
            await ctx.send(embed=embed)

    @commands.command(name='coin', aliases=['moneycoin', 'flip', 'cf', 'монетка'],
                      help=' - You flip a coin with 2 sides')
    async def moneycoin(self, ctx, bet: int, side=None):
        emoji = self.client.get_emoji(676803534758477845)
        author = ctx.author
        member_id = str(author.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    'орел', 'решка')

            return inner_check

        await self.client.unupdate_currency(member_id, bet)
        if self.client.currency[member_id]['money'] >= 0:
            if not side:
                await ctx.send('Выберите сторону и напишите в чат **орел** или **решка**')
                reply = await self.client.wait_for('message', check=check, timeout=30)
                author = ctx.message.author
                embedtails = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedhead = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                sides = ["tails", "heads"]
                embedtails.add_field(name='Монетка', value=f'{author.mention} выпал **орел**')
                embedtails.set_image(
                    url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
                embedhead.add_field(name='Монетка', value=f'{author.mention} выпала **решка**')
                embedhead.set_image(
                    url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
                if random.choice(sides) == 'tails':
                    await ctx.send(embed=embedtails)
                    if reply.content == 'орел':
                        await self.client.update_currency(member_id, bet * 2)
                        await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

                else:
                    await ctx.send(embed=embedhead)
                    if reply.content == 'решка':
                        await self.client.update_currency(member_id, bet * 2)
                        await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if side == 'орел' or side == 'о' or side == 'орёл':
                author = ctx.message.author
                embedtails = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedhead = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                sides = ["tails", "heads"]
                embedtails.add_field(name='Coin', value=f'{author.mention} выпал **орел**')
                embedtails.set_image(
                    url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
                embedhead.add_field(name='Coin', value=f'{author.mention} выпала **решка**')
                embedhead.set_image(
                    url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
                if random.choice(sides) == 'tails':
                    await ctx.send(embed=embedtails)
                    await self.client.update_currency(member_id, bet * 2)
                    await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
                else:
                    await ctx.send(embed=embedhead)
            if side == 'решка' or side == 'р' or side == 'p':
                author = ctx.message.author
                embedtails = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedhead = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                sides = ["tails", "heads"]
                embedtails.add_field(name='Coin', value=f'{author.mention} выпал **орел**')
                embedtails.set_image(
                    url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
                embedhead.add_field(name='Coin', value=f'{author.mention} выпала **решка**')
                embedhead.set_image(
                    url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
                if random.choice(sides) == 'heads':
                    await ctx.send(embed=embedhead)
                    await self.client.update_currency(member_id, bet * 2)
                    await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
                else:
                    await ctx.send(embed=embedtails)
        else:
            await ctx.send(f'Недостаточно {emoji} чтобы играть')
            await self.client.update_currency(member_id, bet)

    @moneycoin.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Ошибка', value='Ваша ставка это обязательная опция!\n ```.cf 200 о/р \n .cf 200```')
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def topmoney(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        kamo = ["(●♡∀♡)",
                "✿♥‿♥✿",
                "(♥ω♥ ) ~♪",
                "(｡･ω･｡)ﾉ♡",
                "(◍•ᴗ•◍)❤",
                "-ω(´•ω•｀)♡",
                "(◍•ᴗ•◍)♡ ✧*。",
                "( ◜◒◝ )♡",
                "(人 •͈ᴗ•͈)",
                "(´͈ ᵕ `͈ ♡°◌̊)",
                "(ღ˘⌣˘ღ)",
                "( ˘ ³˘)♥",
                "( ˘ ³˘)❤",
                "❣ (●❛3❛●)",
                "(っ˘з(˘⌣˘ )",
                "(◦˘ З(◦’ںˉ◦)♡",
                "(*-ω-)ω-*)"]
        with open('money.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: i[1]["money"])})
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        for index, element in enumerate(result):
            try:
                user = await self.client.fetch_user(element)
                a = user.name
            except AttributeError:
                a = '?'
            embed.add_field(name=str(int(index + 1)),
                            value=f"``{random.choice(kamo)}`` | {a} - {result[element]['money']} {emoji}",
                            inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='hangman', aliases=['hg'])
    async def hangman(self, ctx):
        author = ctx.author
        member_id = str(author.id)
        word_list = ['питон',
                     'анаконда',
                     'змея',
                     'сова',
                     'мышь',
                     'пчела',
                     'шершень',
                     'собака',
                     'хорек',
                     'кошка',
                     'афалина',
                     'баран',
                     'нерпа',
                     'бабуин',
                     'аплодонтия',
                     'вол',
                     'верблюд',
                     'ремнезуб',
                     'бегемот',
                     'барсук',
                     'белка',
                     'гиббон',
                     'белуха',
                     'медведь',
                     'бизон',
                     'бобер',
                     'муравьед',
                     'кенгуру',
                     'валлаби',
                     'бонго',
                     'буйвол',
                     'гиена',
                     'бурозубка',
                     'бурундук',
                     'викунья',
                     'мангуст',
                     'волк',
                     'вомбат',
                     'выхухоль',
                     'газель',
                     'гамадрил',
                     'гепард',
                     'геренук',
                     'мартышка',
                     'песец',
                     'кит',
                     'горилла',
                     'зебра',
                     'тапир',
                     'гринда',
                     'гуанако',
                     'горностай',
                     'дельфин',
                     'жираф',
                     'дикдик',
                     'кабан',
                     'дзерен',
                     'осел',
                     'динго',
                     'кенгуру',
                     'норка',
                     'долгопят',
                     'еж',
                     'зубр',
                     'ирбис',
                     'тигр',
                     'какомицли',
                     'капибара',
                     'игрунка',
                     'бегемот',
                     'кашалот',
                     'коала',
                     'козел',
                     'корова',
                     'свинья',
                     'косуля',
                     'крыса',
                     'лев',
                     'леопард',
                     'гепард',
                     'летяга',
                     'лось',
                     'лошадь',
                     'конь',
                     'морж',
                     'овца',
                     'ондатра',
                     'песчанка',
                     'пони',
                     'рысь',
                     'лисица',
                     'лиса',
                     'антилопа',
                     'сайгак',
                     'соня',
                     'ленивец',
                     'шимпанзе',
                     'ягуар',
                     'як',
                     'шиншилла',
                     'акула',
                     'чайка',
                     'скумбрия',
                     'змееящерица',
                     'ястреб',
                     'варан',
                     'журавль',
                     'лев',
                     'тигр',
                     'бабочка',
                     'геккон',
                     'барсук',
                     'щука',
                     'гепард',
                     'волк',
                     'буйвол',
                     'бурундук',
                     'снегирь',
                     'крыса',
                     'альбатрос',
                     'черепаха',
                     'акула',
                     'жаба',
                     'лягушка',
                     'пищуха',
                     'кряква',
                     'утка',
                     'утконос',
                     'пиранья',
                     'пиранга',
                     'аист',
                     'уж',
                     'сом',
                     'осетр',
                     'соня',
                     'жираф',
                     'дрозд',
                     'лемминг',
                     'пенелопа',
                     'свиристель',
                     'свистун',
                     'клещ',
                     'медведь',
                     'осел',
                     'газель',
                     'хамелеон',
                     'дикобраз',
                     'ястреб',
                     'голубь',
                     'воробей',
                     'ворона',
                     'сорока',
                     'рысь',
                     'пума',
                     'бабуин',
                     'стриж',
                     'тюлень',
                     'опоссум',
                     'орлан',
                     'попугай',
                     'певун',
                     'баклан',
                     'удод',
                     'тля',
                     'моль',
                     'выдра',
                     'колибри',
                     'гну',
                     'бизон',
                     'древолаз',
                     'шелкопряд',
                     'блоха',
                     'вошь',
                     'свинья',
                     'кабан',
                     'свин',
                     'хомяк',
                     'лань',
                     'кролик',
                     'антилопа',
                     'леопард',
                     'какаду',
                     'конь',
                     'муравьед',
                     'вилорог',
                     'сельдь',
                     'ослик',
                     'ночница',
                     'саламандра',
                     'филин',
                     'сова',
                     'гадюка',
                     'морж',
                     'дятел',
                     'петух',
                     'курица',
                     'осьминог',
                     'краб',
                     'креветка',
                     'лягушка',
                     'бабочка',
                     'глухарь',
                     'гусь',
                     'кенгуру',
                     'аноа',
                     'тритон',
                     'карась',
                     'аист',
                     'бык',
                     'дзерен',
                     'синица',
                     'удав',
                     'бегемот',
                     'суслик',
                     'шпрот',
                     'енот',
                     'трясогузка',
                     'медосос',
                     'окунь',
                     'нетопырь',
                     'цапля',
                     'кукушка',
                     'рогоклюв',
                     'фазан',
                     'сипуха',
                     'зубр',
                     'кит',
                     'игуана']
        guesses = 0
        word = random.choice(word_list)
        word_list = list(word)
        blanks = ("◆" * len(word))
        blanks_list = list(blanks)
        unbox_blank = (' '.join(blanks_list))
        new_blanks_list = list(blanks)
        guess_list = []
        guess_list_unbox = (', '.join(guess_list))
        embed_formatter = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_formatter.set_author(name='Виселица')
        hangman_picture_1 = """```
              _______
             |/      |
             |      
             |      
             |       
             |
             |
            _|___```"""

        hangman_picture_5 = """```
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |
             |
            _|___```"""
        hangman_picture_4 = """```
              _______
             |/      |
             |      (_)
             |      \|/
             |
             |
             |
            _|___```"""
        hangman_picture_3 = """```
              _______
             |/      |
             |      (_)
             |      \|
             |
             |
             |
            _|___```"""
        hangman_picture_2 = """```
              _______
             |/      |
             |      (_)
             |
             |
             |
             |
            _|___```"""
        hangman_picture_6 = """```
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      /
             |
            _|___```"""
        hangman_picture_7 = """```
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / \\
             |
            _|___```"""
        image = 'шо'

        embed_formatter.add_field(name='Животные', value=image)
        embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
        embed_formatter.set_footer(text=str(guess_list_unbox))
        while guesses < 7:
            embed_formatter.clear_fields()
            if guesses == 0:
                image = hangman_picture_1
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 1:
                image = hangman_picture_2
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 2:
                image = hangman_picture_3
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 3:
                image = hangman_picture_4
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 4:
                image = hangman_picture_5
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 5:
                image = hangman_picture_6
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            if guesses == 6:
                image = hangman_picture_7
                embed_formatter.add_field(name='Животные', value=image)
                embed_formatter.add_field(name='Информация', value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                embed_formatter.set_footer(text=str(guess_list_unbox))
            await ctx.send(embed=embed_formatter)

            russian_symbols = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                               'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ы', 'э', 'ю', 'я'}

            def check(author):
                def inner_check(message):
                    return message.author == author and message.content.casefold() in russian_symbols

                return inner_check

            guess = await self.client.wait_for('message', check=check(ctx.author), timeout=120)
            if len(guess.content) > 1 and guess.content != word:
                await ctx.send('Хватит жульничать')
                guesses -= 1
            if guess.content == " ":
                await ctx.send("Эй, ты не хочешь играть чтоле? Давай пиши подходящие буквы!")
            if guess.content in guess_list:
                await ctx.send(f"Ты уже использовал данный символ!")
            else:
                if len(guess.content) == 1:
                    guess.content = guess.content.casefold()
                    guess_list.append(guess.content)
                    guess_list_unbox = (', '.join(guess_list))
                i = 0
                while i < len(word):
                    if guess.content == word[i]:
                        new_blanks_list[i] = word_list[i]
                    i = i + 1

                if new_blanks_list == blanks_list:
                    guesses = guesses + 1

                if word_list != blanks_list:
                    blanks_list = new_blanks_list[:]
                    unbox_blank = (' '.join(blanks_list))

                    if word_list == blanks_list or guess.content.casefold() == word:
                        emoji = self.client.get_emoji(676803534758477845)
                        embed_formatter.clear_fields()
                        embed_formatter.add_field(name='Животные', value=image)
                        embed_formatter.add_field(name='Информация',
                                                  value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                        embed_formatter.set_footer(text=str(guess_list_unbox))
                        await ctx.send(embed=embed_formatter)
                        await self.client.update_currency(member_id, 1000)
                        await ctx.send(f'За победу в игре "Виселица" вы получаете + **1000** {emoji} на ваш счёт!')
                        break
        if guesses == 7:
            await ctx.send(f'Вы проиграли! Правильное слово: {word}')

    @commands.command(pass_context=True, aliases=['rockpaperscissors', 'rps', 'rcp', 'кнб', 'каменьножницыбумага'])
    async def rock_paper_scissors(self, ctx, bet: int):
        emoji = self.client.get_emoji(676803534758477845)
        author = ctx.author
        member_id = str(author.id)
        self.client.currency[member_id]['money'] -= bet
        if self.client.currency[member_id]['money'] >= 0:
            emote = ['🗿', '📄', "✂"]
            computer_choise = random.choice(emote)
            embedscis = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedscis.add_field(name='Камень ножницы Бумага',
                                value=f'Скорее сделайте вам выбор!Тет уже выбрал. {random.choice(msgend)}')
            embed_draw = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_draw.add_field(name='Камень ножницы Бумага',
                                 value=f'Тет выбирал: {computer_choise} Ничья!  Сыграем ещё раз? {random.choice(msgend)}')
            embed_shiro_win = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_shiro_win.add_field(name='Камень ножницы Бумага',
                                      value=f'Тет выбирал: {computer_choise} Тет победил! {random.choice(msgend)} ')
            embed_user_win = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_user_win.add_field(name='Камень ножницы Бумага',
                                     value=f'Тет выбирал: {computer_choise}  {author.mention} победил(а). {random.choice(msgend)}')
            message = await ctx.send(embed=embedscis)
            for e in emote:
                await message.add_reaction(e)

            def check(reaction, user):
                return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60)
            except asyncio.TimeoutError:
                await ctx.send("Время вышло")
                return
            if str(reaction) == '🗿' and computer_choise == '🗿':
                await ctx.send(embed=embed_draw)
                self.client.currency[member_id]['money'] += bet
            if str(reaction) == '🗿' and computer_choise == '📄':
                await ctx.send(embed=embed_shiro_win)
            if str(reaction) == '🗿' and computer_choise == '✂':
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '📄' and computer_choise == '🗿':
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '📄' and computer_choise == '📄':
                await ctx.send(embed=embed_draw)
                self.client.currency[member_id]['money'] += bet
            if str(reaction) == '📄' and computer_choise == '✂':
                await ctx.send(embed=embed_shiro_win)
            if str(reaction) == '✂' and computer_choise == '🗿':
                await ctx.send(embed=embed_shiro_win)
            if str(reaction) == '✂' and computer_choise == '📄':
                await ctx.send(embed=embed_user_win)
                self.client.currency[member_id]['money'] += bet * 2
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '✂' and computer_choise == '✂':
                await ctx.send(embed=embed_draw)
                await self.client.update_currency(member_id, bet)
        else:
            await ctx.send(f'Недостаточно {emoji} чтобы играть')
            self.client.currency[member_id]['money'] += bet

    @rock_paper_scissors.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Ошибка', value='Ваша ставка это обязательная опция!\n ```.кнб 5000```')
            await ctx.send(embed=embed)

    @commands.command()
    async def bkeytinfo(self, ctx):
        information_embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        information_embed.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                    value='Игра, которая основывается на стандартных "камень ножницы бумага", '
                                          'но однако является его аниме-стилизованной интерпретацией. Блок схема '
                                          '"кто-кого" бьёт прикрепляется к данному сообщению '
                                          '\n Эмодзи и их значение: \nКирпич - 🧱, Нож - 🔪,Компромат - 📋,Яндере - '
                                          '😈 ,Тентакли - 🐙 ')
        information_embed.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/678491112712830976/ae45770720efac14.png')
        await ctx.send(embed=information_embed)

    @commands.command(name='bkeyt', aliases=['кнкят'])
    async def bkeyt(self, ctx, bet: int):
        emoji = self.client.get_emoji(676803534758477845)
        author = ctx.author
        member_id = str(author.id)
        await self.client.unupdate_currency(member_id, bet)
        if self.client.currency[member_id]['money'] >= 0:
            emote = ['🧱', '🔪', "📋", '😈', '🐙']
            computer_choise = random.choice(emote)
            embedscis = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedscis.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                value=f'Скорее выбирай! Тет ужe сделал свой выбор. {random.choice(msgend)}')
            embed_draw = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_shiro_win = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_user_win = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            message = await ctx.send(embed=embedscis)

            for e in emote:
                await message.add_reaction(e)

            def check(reaction, user):
                return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60)

            except asyncio.TimeoutError:
                await ctx.send("Время закончилось")
                return
            # 1 - 5
            if str(reaction) == '🧱' and computer_choise == '🧱':
                embed_draw.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                     value='Кирпич на кирпич! Вау, строим дом. Ничья!')
                await ctx.send(embed=embed_draw)
                self.client.currency[member_id]['money'] += bet
            if str(reaction) == '🧱' and computer_choise == '🔪':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f'Кирпич и нож. Эй, ножик может ты хотя бы попробуешь? Нет? Тогда {author.mention} побеждает!')
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            if str(reaction) == '🧱' and computer_choise == '📋':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value="Кирпич и компромат. Прямо как камень и бумага! Тет победил!")
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '🧱' and computer_choise == '😈':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value="Кирпич и яндере. Новое оружие для яндере! Тет победил")
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '🧱' and computer_choise == '🐙':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Кирпич и тентакли. Тентакли ничего не могут сделать кирпичу!?  {author.mention}  побеждает!")
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            # 2 - 5
            if str(reaction) == '🔪' and computer_choise == '🧱':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f'Нож и кирпич. Эй, ножик может ты хотя бы попробуешь? Нет? Тогда Тет победил!')
                await ctx.send(embed=embed_shiro_win)
            if str(reaction) == '🔪' and computer_choise == '🔪':
                embed_draw.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                     value=f'Нож и нож. РЕЗАТЬ-РЕЗАТЬ-РЕЗАТЬ! Ничья!')
                await ctx.send(embed=embed_draw)
                await self.client.update_currency(member_id, bet)

            if str(reaction) == '🔪' and computer_choise == '📋':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Ножь и компромат. Компромату конец! {author.mention} побеждает!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            if str(reaction) == '🔪' and computer_choise == '😈':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value="Нож и яндере. Любимое оружие яндерки! Тет победил!")
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '🔪' and computer_choise == '🐙':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Нож и тентакли. Дорого-ой, сегодня у нас морская еда на ужин.  {author.mention} побеждает!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            # 3 - 5

            if str(reaction) == '📋' and computer_choise == '🧱':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Компромат и кирпич. Это больше похоже на камень и бумагу! {author.mention} побеждает!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '📋' and computer_choise == '🔪':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f'Компромат и нож. Компромату конец! Тет победил!')
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '📋' and computer_choise == '📋':
                embed_draw.add_field(name='Кирпич Нож Компромат Яндере Тентаклиs',
                                     value=f"Компромат и компромат. У яндере нет шансов! Ничья!")
                await ctx.send(embed=embed_draw)
                await self.client.update_currency(member_id, bet)

            if str(reaction) == '📋' and computer_choise == '😈':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Компромат и яндере. Сэмпай узнал правду :) {author.mention} побеждает!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            if str(reaction) == '📋' and computer_choise == '🐙':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f"Компромат и тентакли. Теперь это не компромат, а шарик бумаги! Тет побеждает!")
                await ctx.send(embed=embed_shiro_win)

            # 4 - 5
            if str(reaction) == '😈' and computer_choise == '🧱':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Яндере и кирпич.  Отличное оружие для яндерки! {author.mention} побеждает!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '😈' and computer_choise == '🔪':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Яндере и нож. Любимое оружие яндерки!! {author.mention} win!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            if str(reaction) == '😈' and computer_choise == '📋':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f"Яндере и компромат. Сэмпай узнал правду :)  Тет победил!")
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '😈' and computer_choise == '😈':
                embed_draw.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                     value=f"Яндере и яндере. Сэмпай! Сэмпай! Сэмпай! Ничья!")
                await ctx.send(embed=embed_draw)
                await self.client.update_currency(member_id, bet)

            if str(reaction) == '😈' and computer_choise == '🐙':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f"Яндере и тентакли. Уф...Это новый хентай? Тет победил!")
                await ctx.send(embed=embed_shiro_win)

            # 5 - 5

            if str(reaction) == '🐙' and computer_choise == '🧱':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f"Тентакли и кирпич. Тентакли не могут ничего сделать с кирпичом!? Тет победил!")
                await ctx.send(embed=embed_shiro_win)
            if str(reaction) == '🐙' and computer_choise == '🔪':
                embed_shiro_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                          value=f"Тентакли и нож.Дорого-ой, сегодня у нас морская еда на ужин. Тет победил!")
                await ctx.send(embed=embed_shiro_win)

            if str(reaction) == '🐙' and computer_choise == '📋':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Тентакли и компромат. Теперь это не компромат, а шарик бумаги! Тет побеждает! {author.mention}  win!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')

            if str(reaction) == '🐙' and computer_choise == '😈':
                embed_user_win.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                         value=f"Тентакли и яндере. Уф...Это новый хентай? {author.mention}  win!")
                await ctx.send(embed=embed_user_win)
                await self.client.update_currency(member_id, bet * 2)
                await ctx.send(f'Вы получаете {bet * 2}  {emoji}')
            if str(reaction) == '🐙' and computer_choise == '🐙':
                embed_draw.add_field(name='Кирпич Нож Компромат Яндере Тентакли',
                                     value=f"Тентакли на тентаклях. Тентакли на тентаклях тентакли в тентаклях у тентаклей под тентаклями за тентаклями! Ничья!")
                await ctx.send(embed=embed_draw)
                await self.client.update_currency(member_id, bet)
        else:
            await ctx.send(f'Недостаточно {emoji} чтобы играть')
            await self.client.update_currency(member_id, bet)

    @commands.command(name='thimble', aliases=['наперстки', 'thimbles'], help='thimbles with the baaaall')
    async def thimble(self, ctx, couple_of_thimbles: int, bet: int):
        embedsmall = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedsmall.add_field(name='Ошибка', value="С 1 наперстком нельзя играть! Укажите значение больше 1")
        if couple_of_thimbles > 1:
            emoji = self.client.get_emoji(676803534758477845)
            author = ctx.author
            member_id = str(author.id)
            await self.client.unupdate_currency(member_id, bet)
            if self.client.currency[member_id]['money'] >= 0:
                embedthimble = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedthimblerightguess = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedthimblewrongguess = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                number_of_thimble = random.randint(1, couple_of_thimbles)
                embedthimble.set_image(url='https://i.gifer.com/T0lP.gif')
                embedthimble.add_field(name='Наперстки',
                                       value=f'Какой из вы выберите? Напишите число от 1 до {couple_of_thimbles} и напишите его под сообшением!')
                embedthimblerightguess.set_image(
                    url='https://i.pinimg.com/originals/08/26/31/082631de583b33f19b18ec0949128014.gif')
                embedthimblerightguess.add_field(name='Да, вы правы!',
                                                 value=f'Ответ правильный! Шарик был под наперстком {number_of_thimble}')
                embedthimblewrongguess.set_image(
                    url='https://thumbs.gfycat.com/ImpassionedMildHowlermonkey-size_restricted.gif')
                embedthimblewrongguess.add_field(name='Нет ;)',
                                                 value=f'Нет, шарик был под наперстком {number_of_thimble}')
                await ctx.send(embed=embedthimble)
                reply = await self.client.wait_for('message', timeout=20)
                if not reply or reply.content == f'{number_of_thimble}':
                    await ctx.send(embed=embedthimblerightguess)
                    await self.client.update_currency(member_id, bet * couple_of_thimbles)
                    await ctx.send(f'Вы получаете {bet * couple_of_thimbles}  {emoji}')
                else:
                    await ctx.send(embed=embedthimblewrongguess)
            else:
                await ctx.send(f'Недостаточно {emoji} чтобы играть')
                await self.client.update_currency(member_id, bet)
        else:
            await ctx.send(embed=embedsmall)

    @thimble.error
    async def thimble_timeout(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedtimeout = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                                   value="Напишите правильное количество наперстков! Example: **.thimble 3 ставка**", inline=False)
            embedtimeout.set_image(url='https://i.pinimg.com/originals/3e/26/4d/3e264def78c771be662b97e51cbb1768.gif')
            await ctx.send(embed=embedtimeout)
        if isinstance(error, commands.CommandInvokeError):
            embedtimeout = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                                   value="Seems time is over. Don't worry and try to ask again!")
            embedtimeout.set_image(url='https://media3.giphy.com/media/uHJTtpE9WqfYc/source.gif')
            await ctx.send(embed=embedtimeout)

    @commands.command(name='wheel', aliases=['колесо', 'wheels'])
    async def wheel(self, ctx, bet: int):
        member_id = str(ctx.author.id)
        emoji = self.client.get_emoji(676803534758477845)
        await self.client.unupdate_currency(member_id, bet)
        if self.client.currency[member_id]['money'] >= 0:
            num_categorization = random.randint(1, 8)
            arrow = '↖️'
            if num_categorization == 1:
                arrow = '↖️'
                bet *= 0.5
                bet = int(bet)
            if num_categorization == 2:
                arrow = '⬆️️'
                bet *= 0.1
                bet = int(bet)
            if num_categorization == 3:
                arrow = '↗️'
                bet *= 0.3
                bet = int(bet)
            if num_categorization == 4:
                arrow = '➡️️'
                bet *= 1.2
                bet = int(bet)
            if num_categorization == 5:
                arrow = '↘️️'
                bet *= 1.5
                bet = int(bet)
            if num_categorization == 6:
                arrow = '⬇️️'
                bet *= 1.8
                bet = int(bet)
            if num_categorization == 7:
                arrow = '↙️️'
                bet *= 2.5
                bet = int(bet)
            if num_categorization == 8:
                arrow = '⬅️️'
                bet *= 0.2
                bet = int(bet)
            embed_wheel = discord.Embed(
                color=discord.Colour.dark_purple(),
                description=f'**Колесо удачи**\n{ctx.author.mention} получает {bet} {emoji}\n\n\n**♫|0.5  ♩|0.1  ♪|0.3**\n\n\n**♬|0.2  {arrow}  ♙|1.2**\n\n\n**♜|2.5  ♝|1.8  ♞|1.5**'
            )
            await self.client.update_currency(member_id, bet)
            await ctx.send(embed=embed_wheel)
        else:
            await self.client.update_currency(member_id, bet)
            embed_no = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_no.add_field(name='Баланс', value=f'Недостаточно {emoji} чтобы играть')
            await ctx.send(embed=embed_no)



def setup(client):
    client.add_cog(Economycs(client))
