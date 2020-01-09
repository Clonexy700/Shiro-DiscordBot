import discord
import asyncio
from collections import OrderedDict
import time
import json
from discord.ext import commands

class Clickercoin(commands.Cog):

    def __init__(self, client):

        self.client = client

        self.client.loop.create_task(self.save_users())

        with open('click.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('click.json', 'w') as f:
                json.dump(self.users, f, indent=4)



            await asyncio.sleep(1)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        author_id = str(message.author.id)

        member_id = author_id

        if not member_id in self.users:
            self.users[member_id] = {}
            self.users[member_id]['shiro_coin'] = 0
            self.users[member_id]['shiro1'] = 0
            self.users[member_id]['shiro2'] = 0
            self.users[member_id]['shiro3'] = 0
            self.users[member_id]['shiro4'] = 0
            self.users[member_id]['shiro5'] = 0


        income1 = self.users[member_id]['shiro1'] * 5
        income2 = self.users[member_id]['shiro2'] * 13
        income3 = self.users[member_id]['shiro3'] * 28
        income4 = self.users[member_id]['shiro4'] * 50
        income5 = self.users[member_id]['shiro5'] * 100
        income = income1 + income2 + income3 + income4 + income5

        self.users[member_id]['shiro_coin'] += income

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_id = str(member.id)
        self.users[member_id] = {}
        self.users[member_id]['shiro_coin'] = 0
        self.users[member_id]['shiro1'] = 0
        self.users[member_id]['shiro2'] = 0
        self.users[member_id]['shiro3'] = 0
        self.users[member_id]['shiro4'] = 0
        self.users[member_id]['shiro5'] = 0

    @commands.command()
    async def clicker(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Please write it again")
            self.users[member_id] = {}
            self.users[member_id]['shiro_coin'] = 0
            self.users[member_id]['shiro1'] = 0
            self.users[member_id]['shiro2'] = 0
            self.users[member_id]['shiro3'] = 0
            self.users[member_id]['shiro4'] = 0
            self.users[member_id]['shiro5'] = 0
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Shiro Clicker - {member}', icon_url=member.avatar_url)

            embed.add_field(name='Values', value=f" Shiro coins - {self.users[member_id]['shiro_coin']} :fleur_de_lis: \n About game - ``$clickerinfo``"
                                                 f"\n Miko {self.users[member_id]['shiro1']} | Jibril {self.users[member_id]['shiro2']} | Schwi Dola {self.users[member_id]['shiro3']} | Izuna {self.users[member_id]['shiro4']} | Shiro {self.users[member_id]['shiro5']}" )


            await ctx.send(embed=embed)



    @commands.command()
    async def clickerinfo(self, ctx):
        embed_info = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_info.add_field(name='Information about game', value=f"Shiro Clicker is a game where you need to click on your own and register commands to click, as well as buy objects that will click for you. All this will bring you currency - Shiro Coin, for which you can buy even more objects. Become a Tycoon of Shiro Coin and the best in the list of players!"
                                                                  "\n ``$clicker - displays main clicker info`` \n ``$clickerinfo - displays this message`` \n ``$click - enable some games where you must click or type!`` \n ``$clickershop - shop for buying objects!`` \n ``$clickertop-Top users by shiro coins``")
        await ctx.send(embed=embed_info)


    @commands.command()
    async def clickershop(self, ctx):
        author = ctx.author
        member_id = str(author.id)
        embed_shop1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        cost1 = 100 + self.users[member_id]['shiro1'] * 100
        cost2 = 500 + self.users[member_id]['shiro2'] * 500
        cost3 = 2000 + self.users[member_id]['shiro3'] * 2000
        cost4 = 3500 + self.users[member_id]['shiro4'] * 3500
        cost5 = 5000 + self.users[member_id]['shiro5'] * 5000
        embed_shop1.add_field(name='Shop', value=f'1) Miko {cost1} ⚜| 5 coins every message\n 2) Jibril {cost2} ⚜| 13 coins every message \n 3) Schwi Dola {cost3} ⚜| 28 coins every message \n 4) Izuna {cost4} ⚜| 50 coins every message \n 5) Shiro {cost5} ⚜| 100 coins every message')
        emote = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']
        message = await ctx.send(embed=embed_shop1)

        for e in emote:
            await message.add_reaction(e)

        def check(reaction, user):
            return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)
        try:
            reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Timed out")
            return
        if str(reaction) == '1️⃣':
            self.users[member_id]['shiro_coin'] -= cost1
            if self.users[member_id]['shiro_coin'] < 0:
                self.users[member_id]['shiro_coin'] += cost1
                await ctx.send('Not enough coins')
            else:
                embed_buy = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_buy.add_field(name='Market', value='Successful buy!')
                embed_buy.set_image(url='https://vignette.wikia.nocookie.net/no-game-no-life/images/1/13/Miko.png/revision/latest/top-crop/width/360/height/450?cb=20140808200747&path-prefix=ru')
                self.users[member_id]['shiro1'] += 1
                await ctx.send(embed=embed_buy)

        if str(reaction) == '2️⃣':
            self.users[member_id]['shiro_coin'] -= cost2
            if self.users[member_id]['shiro_coin'] < 0:
                self.users[member_id]['shiro_coin'] += cost2
                await ctx.send('Not enough coins')
            else:
                embed_buy = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_buy.add_field(name='Market', value='Successful buy!')
                embed_buy.set_image(
                    url='https://em.wattpad.com/51f6d9038a80a2bfe78b0952cbeeff0a4376fd99/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6a5631334d4e3742775a632d4f673d3d2d32352e313533393564616131636666326331623837353531363230353932342e6a7067?s=fit&w=720&h=720')
                self.users[member_id]['shiro2'] += 1
                await ctx.send(embed=embed_buy)

        if str(reaction) == '3️⃣':
            self.users[member_id]['shiro_coin'] -= cost3
            if self.users[member_id]['shiro_coin'] < 0:
                self.users[member_id]['shiro_coin'] += cost3
                await ctx.send('Not enough coins')
            else:
                embed_buy = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_buy.add_field(name='Market', value='Successful buy!')
                embed_buy.set_image(
                    url='https://images6.alphacoders.com/905/thumb-1920-905429.png')
                self.users[member_id]['shiro3'] += 1
                await ctx.send(embed=embed_buy)

        if str(reaction) == '4️⃣':
            self.users[member_id]['shiro_coin'] -= cost4
            if self.users[member_id]['shiro_coin'] < 0:
                self.users[member_id]['shiro_coin'] += cost4
                await ctx.send('Not enough coins')
            else:
                embed_buy = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_buy.add_field(name='Market', value='Successful buy!')
                embed_buy.set_image(
                    url='https://vignette.wikia.nocookie.net/no-game-no-life/images/9/9e/Hatsuse_Izuna.png/revision/latest?cb=20170323163109')
                self.users[member_id]['shiro4'] += 1
                await ctx.send(embed=embed_buy)

        if str(reaction) == '5️⃣':
            self.users[member_id]['shiro_coin'] -= cost5
            if self.users[member_id]['shiro_coin'] < 0:
                self.users[member_id]['shiro_coin'] += cost5
                await ctx.send('Not enough coins')
            else:
                embed_buy = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_buy.add_field(name='Market', value='Successful buy!')
                embed_buy.set_image(
                    url='https://vsthemes.ru/uploads/posts/2019-05/1731776569.jpg')
                self.users[member_id]['shiro5'] += 1
                await ctx.send(embed=embed_buy)

    @commands.command()
    async def click(self, ctx):
        def is_me(m):
            return m.author == self.client.user
        member = ctx.author
        member_id = str(member.id)
        embed_shop1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_shop1.set_image(
            url='https://vignette.wikia.nocookie.net/nogamenolife/images/c/cc/Shiro_card_edit.jpg/revision/latest?cb=20150402213911&path-prefix=ru')
        emote = ['⚜', '❌']
        for i in range(1, 10**1000000):
            message = await ctx.send(embed=embed_shop1)

            for e in emote:
                await message.add_reaction(e)

            def predicate(reaction, user):
                return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

            try:
                reaction, user = await self.client.wait_for('reaction_add', check=predicate, timeout=60)
            except asyncio.TimeoutError:
                await ctx.send("Timed out")
                return
            if str(reaction) == '⚜':
                self.users[member_id]['shiro_coin'] += 1
                embed_balance = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_balance.set_author(name=f'Shiro Clicker - {member}', icon_url=member.avatar_url)
                embed_balance.add_field(name='Coin Balance', value=f"{self.users[member_id]['shiro_coin']} ⚜️")
                await ctx.send(embed=embed_balance)
                asyncio.sleep(2)
                await ctx.channel.purge(limit=2, check=is_me)
            if str(reaction) == '❌':
                await ctx.send('Stopped')
                break

    @commands.command()
    async def clickertop(self, ctx):
        with open('click.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: i[1]["shiro_coin"])})
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        for index, element in enumerate(result):
            try:
                user = await self.client.fetch_user(element)
                a = user.name
            except AttributeError:
                a = '?'
            embed.add_field(name=str(int(index+1)),
                            value=f"User - {a} Shiro coin - {result[element]['shiro_coin']} :fleur_de_lis: ",
                            inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Clickercoin(client))