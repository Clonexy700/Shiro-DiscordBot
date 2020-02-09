import time
import aiohttp
import discord
import importlib
import os
import sys
from discord.ext import commands


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

def setup(client):
    client.add_cog(Admin(client))
