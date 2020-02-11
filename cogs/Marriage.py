import discord
import asyncio
import json
from collections import OrderedDict
import random
import numpy as np
from collections import namedtuple
from discord.ext import commands


class Marriage(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open('marry.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('marry.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)


def setup(client):
    client.add_cog(Marriage(client))

