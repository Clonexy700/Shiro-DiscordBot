import discord
import os
import youtube_dl
import requests as rq
from discord import opus
import asyncio
import functools
from functools import partial
import json
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
from discord.ext import commands
import random

msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]


class Tet(commands.AutoShardedBot):
    def __init__(self, *args, prefix=None, **kwargs):
        self._currency = None
        super().__init__(*args, **kwargs)

    @property
    def currency(self):
        if not self._currency:
            with open("money.json", "r") as ff:
                self._currency = json.load(ff)
        return self._currency

    async def update_currency(self, who: str, value: int):
        if not self._currency:
            with open("money.json", "r") as ff:
                self._currency = json.load(ff)
            if not who in self._currency:
                self._currency[who] = {}
                self._currency[who]['money'] = 0
                self._currency[who]['box'] = 0
        self._currency[who]["money"] += value
        await self.loop.run_in_executor(None,
                                        partial(json.dump, self._currency, open('money.json', 'w'), indent=4))

    async def unupdate_currency(self, who: str, value: int):
        if not self._currency:
            with open("money.json", "r") as ff:
                self._currency = json.load(ff)
            if not who in self._currency:
                self._currency[who] = {}
                self._currency[who]['money'] = 0
                self._currency[who]['box'] = 0
        self._currency[who]["money"] -= value
        await self.loop.run_in_executor(None,
                                        partial(json.dump, self._currency, open('money.json', 'w'), indent=4))

    async def add_pandora(self, who: str, value: int):
        if not self._currency:
            with open("money.json", "r") as ff:
                self._currency = json.load(ff)
            if not who in self._currency:
                self._currency[who] = {}
                self._currency[who]['money'] = 0
                self._currency[who]['box'] = 0
        self._currency[who]["box"] += value
        await self.loop.run_in_executor(None,
                                        partial(json.dump, self._currency, open('money.json', 'w'), indent=4))

    async def remove_pandora(self, who: str, value: int):
        if not self._currency:
            with open("money.json", "r") as ff:
                self._currency = json.load(ff)
            if not who in self._currency:
                self._currency[who] = {}
                self._currency[who]['money'] = 0
                self._currency[who]['box'] = 0
        self._currency[who]["box"] -= value
        await self.loop.run_in_executor(None,
                                        partial(json.dump, self._currency, open('money.json', 'w'), indent=4))

    async def on_ready(self):
        embed = discord.Embed(
            color=discord.Colour.dark_purple(),
            description=f'**Гендерные роли:**\nкликните на эмодзи для получения, чтобы убрать роль - уберите свой эмодзи'
        )
        print(f'{self.user} ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ! Я ВЕНТИЛЯТОР!')
        await self.change_presence(activity=discord.Game(name='.help'))
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                self.load_extension(f'cogs.{filename[:-3]}')

    async def on_raw_reaction_add(self, payload):
        member = self.get_guild(payload.guild_id).get_member(payload.user_id)
        if payload.channel_id != 674960193452376064:
            return
        if payload.emoji.name == '♂️':
            role = discord.utils.get(member.guild.roles, id=685764291760357401)
            await member.add_roles(role)
        if payload.emoji.name == '♀️':
            role = discord.utils.get(member.guild.roles, id=674968606811095050)
            await member.add_roles(role)
        if payload.emoji.id == 691522796970573856:
            role = discord.utils.get(member.guild.roles, id=674967605395718144)
            await member.add_roles(role)
        if payload.emoji.id == 691523294515429377:
            role = discord.utils.get(member.guild.roles, id=674968522111320088)
            await member.add_roles(role)
        if payload.emoji.id == 691523884675235960:
            role = discord.utils.get(member.guild.roles, id=685764351122210836)
            await member.add_roles(role)
        if payload.emoji.id == 691524275454345286:
            role = discord.utils.get(member.guild.roles, id=687927000790466563)
            await member.add_roles(role)
        if payload.emoji.id == 691525147445952583:
            role = discord.utils.get(member.guild.roles, id=687927006767087695)
            await member.add_roles(role)
        if payload.emoji.id == 691525387473125376:
            role = discord.utils.get(member.guild.roles, id=687927009921204265)
            await member.add_roles(role)
        if payload.emoji.id == 691525891100246027:
            role = discord.utils.get(member.guild.roles, id=687927014694322176)
            await member.add_roles(role)
        if payload.emoji.id == 691526165566980176:
            role = discord.utils.get(member.guild.roles, id=687927012756553728)
            await member.add_roles(role)
        if payload.emoji.id == 691526344919744513:
            role = discord.utils.get(member.guild.roles, id=687927004531916800)
            await member.add_roles(role)
        if payload.emoji.id == 691526943006523441:
            role = discord.utils.get(member.guild.roles, id=691531948606095392)
            await member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        member = self.get_guild(payload.guild_id).get_member(payload.user_id)
        if payload.channel_id != 674960193452376064:
            return
        if payload.emoji.name == '♂️':
            role = discord.utils.get(member.guild.roles, id=685764291760357401)
            await member.remove_roles(role)
        if payload.emoji.name == '♀️':
            role = discord.utils.get(member.guild.roles, id=674968606811095050)
            await member.remove_roles(role)
        if payload.emoji.id == 691522796970573856:
            role = discord.utils.get(member.guild.roles, id=674967605395718144)
            await member.remove_roles(role)
        if payload.emoji.id == 691523294515429377:
            role = discord.utils.get(member.guild.roles, id=674968522111320088)
            await member.remove_roles(role)
        if payload.emoji.id == 691523884675235960:
            role = discord.utils.get(member.guild.roles, id=685764351122210836)
            await member.remove_roles(role)
        if payload.emoji.id == 691524275454345286:
            role = discord.utils.get(member.guild.roles, id=687927000790466563)
            await member.remove_roles(role)
        if payload.emoji.id == 691525147445952583:
            role = discord.utils.get(member.guild.roles, id=687927006767087695)
            await member.remove_roles(role)
        if payload.emoji.id == 691525387473125376:
            role = discord.utils.get(member.guild.roles, id=687927009921204265)
            await member.remove_roles(role)
        if payload.emoji.id == 691525891100246027:
            role = discord.utils.get(member.guild.roles, id=687927014694322176)
            await member.remove_roles(role)
        if payload.emoji.id == 691526165566980176:
            role = discord.utils.get(member.guild.roles, id=687927012756553728)
            await member.remove_roles(role)
        if payload.emoji.id == 691526344919744513:
            role = discord.utils.get(member.guild.roles, id=687927004531916800)
            await member.remove_roles(role)
        if payload.emoji.id == 691526943006523441:
            role = discord.utils.get(member.guild.roles, id=691531948606095392)
            await member.remove_roles(role)

    async def on_guild_join(self, guild):
        with open('prefix.json', 'r') as file:
            prefixes = json.load(file)

        prefixes[str(guild.id)] = '.'

        with open('prefix.json', 'w') as file:
            json.dump(prefixes, file, indent=4)

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Приветик {member.name}, добро пожаловать на сервер **Imanity**! {random.choice(msgend)} Моё имя Тет! Сыграем? Лист команд - .help '
        )
        channel = self.get_channel(694616683549163600)

        avatar = BytesIO()
        await member.avatar_url.save(avatar)

        avatar = Image.open(avatar)
        avatar = avatar.resize((130, 130))
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('avatar.png')

        avatar = Image.open('avatar.png')
        fundo = Image.open('bemvindo.png')
        fonte1 = ImageFont.truetype('BebasNeue.otf', 22)
        fonte2 = ImageFont.truetype('ARIALUNI.TTF', 20)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(200, 120),
                      text=f'Добро пожаловать, {member.name}\nРады приветствовать \nи видеть тебя на Imanity!',
                      fill=(255, 255, 255), font=fonte2)
        fundo.paste(avatar, (40, 90), avatar)
        bv = BytesIO()
        fundo.save(bv, "PNG", quality=100)
        bv.seek(0)
        file = discord.File(bv, filename="bv.png")
        info = self.get_channel(694616508264874013)
        rules = self.get_channel(694608838065913939)
        message = discord.Embed(
            color=discord.Colour.dark_purple(),
            description=f'Приветик, {member.mention}!\n Ознакомься пожалуйста с правилами сервера, вот туточки {rules.mention}\n Подробная информация о сервере здесь {info.mention}'
        )
        await channel.send(embed=message)
        await channel.send(file=file)


f = open("token.txt", "r")
token = f.readline()
f.close()


client = Tet(command_prefix='!')

client.remove_command('help')

client.run('ODAwNzcwNDQyODc2NTUxMjEw.YAW9lw.r5SEBa0JW1bCkkxaHD1hpl3Orhc')