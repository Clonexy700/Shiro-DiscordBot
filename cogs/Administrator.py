import time
import aiohttp
import discord
import importlib
import os
import sys
from discord.ext import commands
from utility import http, default


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
    async def dm(self, ctx, user_id: int, *, message: str):
        if ctx.author.id == 314618320093577217:
            user = self.client.get_user(user_id)
            if not user:
                return await ctx.send(f"Could not find any UserID matching **{user_id}**")

            try:
                await user.send(message)
                await ctx.send(f"✉️ Sent a DM to **{user_id}**")
            except discord.Forbidden:
                await ctx.send("This user might be having DMs blocked or it's a bot account...")

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

def setup(client):
    client.add_cog(Admin(client))
