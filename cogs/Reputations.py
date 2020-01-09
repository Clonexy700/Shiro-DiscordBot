import discord
import json
import asyncio
from collections import OrderedDict
from discord.ext import commands

class Reputations(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open('reputation.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('reputation.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    @commands.command()
    async def rep(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("Can't identify a member")
            member_id = str(member.id)
            self.users[member_id] = {}
            self.users[member_id]['reputation'] = 0
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f'Reputation of {member}', icon_url=member.avatar_url)

            embed.add_field(name='Reputation', value=f"{self.users[member_id]['reputation']} :sparkles: ")

            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_id = str(member.id)
        self.users[member_id] = {}
        self.users[member_id]['reputation'] = 0

    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.command()
    async def addrep(self, ctx, member: discord.Member):
        author = ctx.author
        member_id = str(member.id)
        embed_reputation = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        if member == ctx.author:
            await ctx.send("You can't give reputation to yourself!")
        else:
            embed_reputation.add_field(name='Reputation', value=f'{author.mention} added 1 reputation to {member.mention}')
            self.users[member_id]['reputation'] += 1
            await ctx.send(embed=embed_reputation)

    @addrep.error
    async def addrep_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Cooldown', value='Command is on cooldown. You can use it once in 2 hours :timer: \n Remaining time: {:.2f}s'.format(error.retry_after))
            await ctx.send(embed=embed)

    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.command()
    async def removerep(self, ctx, member: discord.Member):
        author = ctx.author
        member_id = str(member.id)
        embed_reputation = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        if member == ctx.author:
            await ctx.send("You can't remove reputation from yourself!")
        else:
            embed_reputation.add_field(name='Reputation', value=f'{author.mention} removed 1 reputation from {member.mention}')
            self.users[member_id]['reputation'] -= 1
            await ctx.send(embed=embed_reputation)

    @addrep.error
    async def removerep_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed.add_field(name='Cooldown', value='Command is on cooldown. You can use it once in 2 hours :timer: \n Remaining time: {:.2f}s'.format(error.retry_after))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def toprep(self, ctx):
        with open(r'C:\Users\conex_000\PycharmProjects\DiscordShiro\reputation.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: i[1]["reputation"])})
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
                            value=f"User - {a}      Reputation - {result[element]['reputation']}",
                            inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reputations(client))