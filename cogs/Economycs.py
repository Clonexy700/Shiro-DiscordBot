import discord
from discord.ext import commands
import os
import json
import asyncio
import random
from collections import OrderedDict
import requests
import random, sys
from typing import List


class Economycs(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open('money.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('money.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['money'] = 0

        self.users[author_id]['money'] += 1

    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Balance - {member}', icon_url=member.avatar_url)

            embed.add_field(name='Money', value=f"{self.users[member_id]['money']} :diamonds:")

            await ctx.send(embed=embed)

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
        self.users[member_id] = {}
        self.users[member_id]['money'] = 0

    @commands.command()
    async def money(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Balance - {member}', icon_url=member.avatar_url)

            embed.add_field(name='Money', value=f"{self.users[member_id]['money']} :diamonds:")

            await ctx.send(embed=embed)

    @commands.command()
    async def moneybylonexyset(self, ctx, member: discord.Member, money_mum: int):
        if ctx.author.id == 314618320093577217:
            member_id = str(member.id)
            if not member_id in self.users:
                self.users[member_id] = {}
                self.users[member_id]['money'] = 0

            self.users[member_id]['money'] = money_mum
        else:
            await ctx.send('You are not Shiro owner for using this command!')

    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.command(name='moneydaily', aliases=['daily', 'dailymoney'])
    async def moneydaily(self, ctx):
        embed_daily_money = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_daily_money.add_field(name='Balance', value='You got 1000 :diamonds:')
        member = ctx.author
        member_id = str(member.id)
        if not member_id in self.users:
            self.users[member_id] = {}
            self.users[member_id]['money'] = 0

        self.users[member_id]['money'] += 1000

        await ctx.send(embed=embed_daily_money)

    @moneydaily.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Cooldown',
                            value='Command is on cooldown. You can use it once in 2 hours :timer: \n Remaining time: {:.2f}s'.format(
                                error.retry_after))
            await ctx.send(embed=embed)

    @commands.command()
    async def market(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        if not member_id in self.users:
            self.users[member_id] = {}
            self.users[member_id]['money'] = 0
        embedmarket = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedmarket.set_author(name='Market')
        embedmarket.add_field(name='All roles', value='Here you can buy roles for your :moneybag: :diamonds:',
                              inline=False)
        embedmarket.add_field(name='------------', value='1 Shiro lover     20000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='2 Sempaii?     15000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='3 N.E.E.T     10000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='4 Loli     10000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='5 🍃     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='6 🍁     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='7 🍊     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='8 ❄     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='9 🌙     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='10 🍌     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='11 🍎     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='12 💫     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='13 🌹     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------', value='14 🌌     5000 :diamonds:', inline=False)
        embedmarket.add_field(name='------------',
                              value='15 Is it was a great idea to spend all money on this role?      1000000 :diamonds:',
                              inline=False)
        await ctx.send(embed=embedmarket)
        role1 = discord.utils.get(member.guild.roles, name="Shiro lover")
        role2 = discord.utils.get(member.guild.roles, name="Sempaii?")
        role3 = discord.utils.get(member.guild.roles, name="N.E.E.T")
        role4 = discord.utils.get(member.guild.roles, name="Loli")
        role5 = discord.utils.get(member.guild.roles, name="🍃")
        role6 = discord.utils.get(member.guild.roles, name="🍁")
        role7 = discord.utils.get(member.guild.roles, name="🍊")
        role8 = discord.utils.get(member.guild.roles, name="❄")
        role9 = discord.utils.get(member.guild.roles, name="🌙")
        role10 = discord.utils.get(member.guild.roles, name="🍌")
        role11 = discord.utils.get(member.guild.roles, name="🍎")
        role12 = discord.utils.get(member.guild.roles, name="💫")
        role13 = discord.utils.get(member.guild.roles, name="🌹")
        role14 = discord.utils.get(member.guild.roles, name="🌌")
        role15 = discord.utils.get(member.guild.roles, name='Is it was a great idea to spend all money on this role?')

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')

            return inner_check

        msg = await self.client.wait_for('message', check=check(ctx.author), timeout=30)

        embednomoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

        embednomoney.set_author(name=f'Unsuccessful purchase by {member}', icon_url=member.avatar_url)

        embednomoney.add_field(name='Market', value='Not enough money for purchase')

        embednomoney.add_field(name='Balance', value=f"{self.users[member_id]['money']}:diamonds:", inline=False)

        if msg.content == '1':
            if self.users[member_id]['money'] - 20000 > 0:
                self.users[member_id]['money'] -= 20000
                await discord.Member.add_roles(member, role1)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "Shiro Lover"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

        if msg.content == '2':
            if self.users[member_id]['money'] - 15000 > 0:
                self.users[member_id]['money'] -= 15000
                await discord.Member.add_roles(member, role2)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "Sempaii?"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '3':
            if self.users[member_id]['money'] - 10000 > 0:
                self.users[member_id]['money'] -= 10000
                await discord.Member.add_roles(member, role3)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "N.E.E.T"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '4':
            if self.users[member_id]['money'] - 10000 > 0:
                self.users[member_id]['money'] -= 10000
                await discord.Member.add_roles(member, role4)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "Loli"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '5':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role5)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🍃"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '6':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role6)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🍁"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '7':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role7)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🍊"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '8':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role8)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "❄"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '9':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role9)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🌙"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '10':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role10)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🍌"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '11':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role11)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🍎"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '12':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role12)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "💫"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '13':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role13)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🌹"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '14':
            if self.users[member_id]['money'] - 5000 > 0:
                self.users[member_id]['money'] -= 5000
                await discord.Member.add_roles(member, role14)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market', value='You successfully purchased role "🌌"!', inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)
        if msg.content == '15':
            if self.users[member_id]['money'] - 1000000 > 0:
                self.users[member_id]['money'] -= 1000000
                await discord.Member.add_roles(member, role15)
                embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                embed.set_author(name=f'Successful purchase by {member}', icon_url=member.avatar_url)

                embed.add_field(name='Market',
                                value='LMAOOOOO AYYYY. SOMEBODY BOUGHT IT? Congratulations from Clonexy700#3767 - Shiro Developer! You bought "Is it was a great idea to spend all money on this role?"!',
                                inline=False)

                embed.add_field(name='Balance after purchase', value=f"{self.users[member_id]['money']}:diamonds:",
                                inline=False)

                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embednomoney)

    @commands.command(pass_context=True)
    async def moneygive(self, ctx, member: discord.Member, money_number: int):
        author = ctx.message.author
        embedmoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embedmoney.add_field(name='Money operaton',
                             value=f"{author.mention} sent {money_number} :diamonds: to {member.mention}")
        member_id = str(member.id)
        author_id = str(author.id)
        if not member_id in self.users:
            self.users[member_id] = {}
            self.users[member_id]['money'] = 0
        if author == member:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.add_field(name='Error', value="You can't send money to yourself")
            await ctx.send(embed=embed)
        if money_number < 1:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.add_field(name='Error', value="You need to send at least 1 :diamonds:")
            await ctx.send(embed=embed)
        if author != member:
            if money_number >= 1:
                if self.users[author_id]['money'] - money_number > 0:
                    self.users[author_id]['money'] -= money_number
                    self.users[member_id]['money'] += money_number
                    await ctx.send(embed=embedmoney)
                else:
                    embednomoney = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

                    embednomoney.set_author(name=f'Unsuccessful Transfer by {author}', icon_url=author.avatar_url)

                    embednomoney.add_field(name='Error', value='Not enough money for transfer')

                    embednomoney.add_field(name='Balance', value=f"{self.users[member_id]['money']}:diamonds:",
                                           inline=False)
                    await ctx.send(embed=embednomoney)

    @commands.command(pass_context=True, no_pm=True)
    async def slot(self, ctx, bet: int):
        bet = 1 if not bet else bet
        member_id = str(ctx.author.id)
        randomization = [":cherry_blossom:",
                         ":banana:",
                         ":cherries:",
                         ":diamonds:",
                         ":apple:",
                         ":sparkles:"]
        self.users[member_id]['money'] -= bet
        if self.users[member_id]['money'] >= 0:
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
                await ctx.send(f'You win {bet_win} :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":banana:" and slot2 == ":banana:" and slot3 != ":banana:" or slot1 != ":banana:" and slot2 == ":banana:" and slot3 == ":banana:":
                bet_win = round(bet * 1.4)
                await ctx.send(f' You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":cherries:" and slot2 == ":cherries:" and slot3 != ":cherries:" or slot1 != ":cherries:" and slot2 == ":cherries:" and slot3 == ":cherries:":
                bet_win = round(bet * 1.3)
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":diamonds:" and slot2 == ":diamonds:" and slot3 != ":diamonds:" or slot1 != ":diamonds:" and slot2 == ":diamonds:" and slot3 == ":diamonds:":
                bet_win = round(bet * 1.6)
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":apple:" and slot2 == ":apple:" and slot3 != ":apple:" or slot1 != ":apple:" and slot2 == ":apple:" and slot3 == ":apple:":
                bet_win = round(bet * 1.1)
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":sparkles:" and slot2 == ":sparkles:" and slot3 != ":sparkles:" or slot1 != ":sparkles:" and slot2 == ":sparkles:" and slot3 == ":sparkles:":
                bet_win = round(bet * 1.7)
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win

            if slot1 == ":cherry_blossom:" and slot2 == ":cherry_blossom:" and slot3 == ":cherry_blossom:":
                bet_win = bet * 2
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win

            if slot1 == ":banana:" and slot2 == ":banana:" and slot3 == ":banana:":
                bet_win = bet * 2
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win

            if slot1 == ":cherries:" and slot2 == ":cherries:" and slot3 == ":cherries:":
                bet_win = bet * 3
                await ctx.send(f' You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win

            if slot1 == ":diamonds:" and slot2 == ":diamonds:" and slot3 == ":diamonds:":
                bet_win = bet * 10
                await ctx.send(f'Woah?!Oh. You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win

            if slot1 == ":apple:" and slot2 == ":apple:" and slot3 == ":apple:":
                bet_win = round(bet * 1.9)
                await ctx.send(f'You win {bet_win}  :diamonds:')
                self.users[member_id]['money'] += bet_win
            if slot1 == ":sparkles:" and slot2 == ":sparkles:" and slot3 == ":sparkles:":
                bet_win = bet * 5
                await ctx.send(f'Not bad. You win {bet_win} :diamonds:')
                self.users[member_id]['money'] += bet_win
        else:
            self.users[member_id]['money'] += bet
            await ctx.send(f"You have not enough :diamonds: too play!")

    @slot.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Error', value='Your bet is required option!\n ```$slot 100```')
            await ctx.send(embed=embed)

    @commands.command(name='moneycoin', help=' - You flip a coin with 2 sides')
    async def moneycoin(self, ctx, bet: int):
        author = ctx.author
        member_id = str(author.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    'tails', 'heads')

            return inner_check

        self.users[member_id]['money'] -= bet
        if self.users[member_id]['money'] >= 0:
            await ctx.send('Choose the side and write in chat **tails** or **heads **')
            reply = await self.client.wait_for('message', check=check, timeout=30)
            author = ctx.message.author
            embedtails = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedhead = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            sides = ["tails", "heads"]
            embedtails.add_field(name='Coin', value=f'{author.mention} flipped **tails**')
            embedtails.set_image(
                url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
            embedhead.add_field(name='Coin', value=f'{author.mention} flipped **heads**')
            embedhead.set_image(
                url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
            if random.choice(sides) == 'tails':
                await ctx.send(embed=embedtails)
                if reply.content == 'tails':
                    self.users[member_id]['money'] += bet * 2
                    await ctx.send(f'You win {bet * 2}  :diamonds:')

            else:
                await ctx.send(embed=embedhead)
                if reply.content == 'heads':
                    self.users[member_id]['money'] += bet * 2
                    await ctx.send(f'You win {bet * 2}  :diamonds:')
        else:
            await ctx.send('You have not enough :diamonds: to play')
            self.users[member_id]['money'] += bet

    @moneycoin.error
    async def moneydaily_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Error', value='Your bet is required option!\n ```$moneycoin 100```')
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def topmoney(self, ctx):
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
                            value=f"User - {a} Money - {result[element]['money']} :diamonds:",
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
                     'шиншилла']
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
             |      |
             |
            _|___```"""
        hangman_picture_7 = """```
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      | |
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
            guess = await self.client.wait_for('message', timeout=120)
            if len(guess.content) > 1 and guess.content != word:
                await ctx.send('Хватит жульничать')
                guesses -= 1
            if guess.content == " ":
                await ctx.send("Эй, ты не хочешь играть чтоле? Давай пиши подходящие буквы!")
            if guess.content in guess_list:
                await ctx.send(f"Ты уже использовал данный символ!")
            else:
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
                    unbox_blank = (', '.join(blanks_list))

                    if word_list == blanks_list or guess.content == word:
                        embed_formatter.clear_fields()
                        embed_formatter.add_field(name='Животные', value=image)
                        embed_formatter.add_field(name='Информация',
                                                  value=f'\n Попыток: {guesses} \n ```{unbox_blank}```')
                        embed_formatter.set_footer(text=str(guess_list_unbox))
                        await ctx.send(embed=embed_formatter)
                        self.users[member_id]['money'] += 1000
                        await ctx.send('За победу в игре "Виселица" вы получаете 1000 :diamonds: на ваш счёт!')
                        break
        if guesses == 7:
            await ctx.send(f'Вы проиграли! Правильное слово: {word}')

    @hangman.error
    async def hangman_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embedtimeout = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                                   value="Seems time is over. Don't worry and try to ask again!")
            embedtimeout.set_image(url='https://media3.giphy.com/media/uHJTtpE9WqfYc/source.gif')
            await ctx.send(embed=embedtimeout)

def setup(client):
    client.add_cog(Economycs(client))
