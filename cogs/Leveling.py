import discord
import asyncio
import json
from collections import OrderedDict
import random
import numpy as np
from collections import namedtuple
from discord.ext import commands


class Levels(commands.Cog):

    def __init__(self, client):
        self.bot = client

        self.bot.loop.create_task(self.save_users())

        with open(r'users.json', 'r') as f:
           self.users = json.load(f)

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r'users.json', 'w') as f:
                json.dump(self.users, f, indent=4)

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
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0



        self.users[author_id]['exp'] += 1

        if self.lvl_up(author_id):
            await message.channel.send(f"{message.author.mention} is now level {self.users[author_id]['level']}")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Level - {member}', icon_url=member.avatar_url)

            embed.add_field(name='Level', value=self.users[member_id]['level'])
            embed.add_field(name='XP', value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)

    @commands.command()
    async def lvl(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Level - {member}', icon_url=member.avatar_url)

            embed.add_field(name='Level', value=self.users[member_id]['level'])
            embed.add_field(name='XP', value=self.users[member_id]['exp'])

            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def toplevel(self, ctx):
        with open('users.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: (i[1]["level"], i[1]["exp"]))})
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        for index, element in enumerate(result):
            try:
                user = await self.bot.fetch_user(element)
                a = user.name
            except AttributeError:
                a = '?'
            embed.add_field(name=str(int(index+1)),
                            value=f"User - {a}       Level - {result[element]['level']}, Exp - {result[element]['exp']}",
                            inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def toplvl(self, ctx):
        with open('users.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: (i[1]["level"], i[1]["exp"]))})
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        for index, element in enumerate(result):
            try:
                user = await self.bot.fetch_user(element)
                a = user.name
            except AttributeError:
                a = '?'
            embed.add_field(name=str(int(index+1)),
                            value=f"User - {a}       Level - {result[element]['level']}, Exp - {result[element]['exp']}",
                            inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Levels(bot))