import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

from io import BytesIO
from discord.ext import commands
from utility import http


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        await ctx.send(r[endpoint])

    @commands.command(aliases=['color'])
    async def colour(self, ctx, colour: str):
        if colour == "random":
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if colour[:1] == "#":
            colour = colour[1:]

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")

        try:
            r = await http.get(f"https://api.alexflipnote.dev/colour/{colour}", res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        embed = discord.Embed(colour=discord.Colour.dark_purple())
        embed.set_thumbnail(url=r["image"])
        embed.set_image(url=r["image_gradient"])

        embed.add_field(name="HEX", value=r['hex'], inline=True)
        embed.add_field(name="RGB", value=r['rgb'], inline=True)
        embed.add_field(name="Int", value=r['int'], inline=True)
        embed.add_field(name="Brightness", value=r['brightness'], inline=True)

        await ctx.send(embed=embed, content=f"{ctx.invoked_with.title()} name: **{r['name']}**")

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        async with ctx.channel.typing():
            url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")

            if url is None:
                return await ctx.send("I think the API broke...")

            if not len(url['list']):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

            await ctx.send(f":bookmark:  Definitions for **{result['word']}**```fix\n{definition}```")

def setup(client):
    client.add_cog(Info(client))
