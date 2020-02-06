import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

from io import BytesIO
from discord.ext import commands
from utility import http, argparser


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

    async def api_img_creator(self, ctx, url, filename, content=None):
        async with ctx.channel.typing():
            req = await http.get(url, res_method="read")

            if req is None:
                return await ctx.send("I couldn't create the image ;-;")

            bio = BytesIO(req)
            bio.seek(0)
            await ctx.send(content=content, file=discord.File(bio, filename=filename))

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

            embed_urban = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_urban.add_field(name=f"Meaning of: {result['word']}", value=f':bookmark: \n```\n{definition}```')
            await ctx.send(embed=embed_urban)

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        embed_reversion = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_reversion.add_field(name='Reverse 🔁', value=t_rev)
        await ctx.send(embed=embed_reversion)

    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        embed_password = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_password.add_field(name='Password generation :lock: ', value=f"``Here is your password:``\n{secrets.token_urlsafe(nbytes)}")
        await ctx.author.send(embed=embed_password)

    @commands.command()
    async def supreme(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        parser = argparser.Arguments()
        parser.add_argument('input', nargs="+", default=None)
        parser.add_argument('-d', '--dark', action='store_true')
        parser.add_argument('-l', '--light', action='store_true')

        args, valid_check = parser.parse_args(text)
        if not valid_check:
            return await ctx.send(args)

        inputText = urllib.parse.quote(' '.join(args.input))
        if len(inputText) > 500:
            return await ctx.send(f"**{ctx.author.name}**, the Supreme API is limited to 500 characters, sorry.")

        darkorlight = ""
        if args.dark:
            darkorlight = "dark=true"
        if args.light:
            darkorlight = "light=true"
        if args.dark and args.light:
            return await ctx.send(f"**{ctx.author.name}**, you can't define both --dark and --light, sorry..")

        await self.api_img_creator(ctx, f"https://api.alexflipnote.dev/supreme?text={inputText}&{darkorlight}", "supreme.png")


def setup(client):
    client.add_cog(Info(client))
