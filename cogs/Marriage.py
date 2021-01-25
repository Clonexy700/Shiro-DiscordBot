import discord
import asyncio
import json
from collections import OrderedDict
import random
import numpy as np
from functools import partial
from discord.utils import get
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
                if self.users:
                    json.dump(self.users, f, indent=4)

            await asyncio.sleep(3)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        author_id = str(member.id)
        self.users[author_id] = {}
        self.users[author_id]['couple_id'] = 'None'
        self.users[author_id]['price'] = 1
        self.users[author_id]['gift1'] = 'None'
        self.users[author_id]['gift2'] = 'None'
        self.users[author_id]['gift3'] = 'None'
        self.users[author_id]['gift4'] = 'None'
        self.users[author_id]['gift5'] = 'None'
        self.users[author_id]['gift6'] = 'None'
        self.users[author_id]['gift7'] = 'None'
        self.users[author_id]['gift8'] = 'None'
        self.users[author_id]['gift9'] = 'None'
        self.users[author_id]['gift10'] = 'None'
        self.users[author_id]['gift11'] = 'None'
        self.users[author_id]['gift12'] = 'None'
        self.users[author_id]['gift13'] = 'None'
        self.users[author_id]['gift14'] = 'None'
        self.users[author_id]['gift15'] = 'None'
        self.users[author_id]['gift16'] = 'None'
        self.users[author_id]['gift17'] = 'None'
        self.users[author_id]['gift18'] = 'None'
        self.users[author_id]['gift19'] = 'None'
        self.users[author_id]['gift20'] = 'None'
        self.users[author_id]['gift21'] = 'None'
        self.users[author_id]['divorce_num'] = 0

    @commands.Cog.listener()
    async def on_message(self, message):

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['couple_id'] = 'None'
            self.users[author_id]['price'] = 1
            self.users[author_id]['gift1'] = 'None'
            self.users[author_id]['gift2'] = 'None'
            self.users[author_id]['gift3'] = 'None'
            self.users[author_id]['gift4'] = 'None'
            self.users[author_id]['gift5'] = 'None'
            self.users[author_id]['gift6'] = 'None'
            self.users[author_id]['gift7'] = 'None'
            self.users[author_id]['gift8'] = 'None'
            self.users[author_id]['gift9'] = 'None'
            self.users[author_id]['gift10'] = 'None'
            self.users[author_id]['gift11'] = 'None'
            self.users[author_id]['gift12'] = 'None'
            self.users[author_id]['gift13'] = 'None'
            self.users[author_id]['gift14'] = 'None'
            self.users[author_id]['gift15'] = 'None'
            self.users[author_id]['gift16'] = 'None'
            self.users[author_id]['gift17'] = 'None'
            self.users[author_id]['gift18'] = 'None'
            self.users[author_id]['gift19'] = 'None'
            self.users[author_id]['gift20'] = 'None'
            self.users[author_id]['gift21'] = 'None'
            self.users[author_id]['divorce_num'] = 0

    @commands.command(name='marry', pass_context=True)
    async def marry(self, ctx, member: discord.Member):
        author_id = str(ctx.message.author.id)
        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['couple_id'] = 'None'
            self.users[author_id]['price'] = 1
            self.users[author_id]['gift1'] = 'None'
            self.users[author_id]['gift2'] = 'None'
            self.users[author_id]['gift3'] = 'None'
            self.users[author_id]['gift4'] = 'None'
            self.users[author_id]['gift5'] = 'None'
            self.users[author_id]['gift6'] = 'None'
            self.users[author_id]['gift7'] = 'None'
            self.users[author_id]['gift8'] = 'None'
            self.users[author_id]['gift9'] = 'None'
            self.users[author_id]['gift10'] = 'None'
            self.users[author_id]['gift11'] = 'None'
            self.users[author_id]['gift12'] = 'None'
            self.users[author_id]['gift13'] = 'None'
            self.users[author_id]['gift14'] = 'None'
            self.users[author_id]['gift15'] = 'None'
            self.users[author_id]['gift16'] = 'None'
            self.users[author_id]['gift17'] = 'None'
            self.users[author_id]['gift18'] = 'None'
            self.users[author_id]['gift19'] = 'None'
            self.users[author_id]['gift20'] = 'None'
            self.users[author_id]['gift21'] = 'None'
            self.users[author_id]['divorce_num'] = 0
        member_id = str(member.id)
        if not member_id in self.users:
            self.users[member_id] = {}
            self.users[member_id]['couple_id'] = 'None'
            self.users[member_id]['price'] = 1
            self.users[member_id]['gift1'] = 'None'
            self.users[member_id]['gift2'] = 'None'
            self.users[member_id]['gift3'] = 'None'
            self.users[member_id]['gift4'] = 'None'
            self.users[member_id]['gift5'] = 'None'
            self.users[member_id]['gift6'] = 'None'
            self.users[member_id]['gift7'] = 'None'
            self.users[member_id]['gift8'] = 'None'
            self.users[member_id]['gift9'] = 'None'
            self.users[member_id]['gift10'] = 'None'
            self.users[member_id]['gift11'] = 'None'
            self.users[member_id]['gift12'] = 'None'
            self.users[member_id]['gift13'] = 'None'
            self.users[member_id]['gift14'] = 'None'
            self.users[member_id]['gift15'] = 'None'
            self.users[member_id]['gift16'] = 'None'
            self.users[member_id]['gift17'] = 'None'
            self.users[member_id]['gift18'] = 'None'
            self.users[member_id]['gift19'] = 'None'
            self.users[member_id]['gift20'] = 'None'
            self.users[member_id]['gift21'] = 'None'
            self.users[author_id]['divorce_num'] = 0
        role = discord.utils.get(member.guild.roles, name="💍")
        author = ctx.message.author
        embedmarry = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedyee = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embednii = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedalreadymarried = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedyoucantmarryyourselflmaoidiot = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedmarry.add_field(name='Свадьба :heart_exclamation: ',
                             value=f'{author.mention} предлагает вам свою руку и сердце! {member.mention}',
                             inline=False)
        embedmarry.add_field(name='Каков будет ваш ответ? :question: :thinking:  ',
                             value='Вы можете ответить с помощью **да** или **нет**, у вас есть целая минута, чтобы принять '
                                   'решение!',
                             inline=False)
        embedmarry.set_image(
            url='https://media1.tenor.com/images/69dbcb02b724d26644228a38e367d017/tenor.gif?itemid=14444888')
        embedyee.add_field(name='Удачная свадьба :heart:',
                           value=f'{author.mention} женился на {member.mention} ! Мои поздравления! ;) ')
        embedyee.set_image(
            url='https://cdn.discordapp.com/attachments/624296774747553808/642210564571004929/2c4259204e631b3e70cbd248331ac1e2.gif' or 'https://media1.tenor.com/images/ed8113a52d8517b31b4073b9ee9db314/tenor.gif?itemid=11767932')
        embednii.add_field(name='Свадьба неудачна :broken_heart: ',
                           value=f"{member.mention} отказалась(ся). Не плачь {author.mention} , найдешь кого-нибудь другого")
        embednii.set_image(
            url='https://cdn.discordapp.com/attachments/624296774747553808/642209594130694163/0caba0318aa667572c0ae30f34ecf8b62896aee5_hq.gif')
        embedalreadymarried.add_field(name='Вы уже женаты!',
                                      value=f'{author.mention} Вы уже женаты!')
        embedyoucantmarryyourselflmaoidiot.add_field(name='Свадьба неудачна :thinking:  :thinking: ',
                                                     value=f"Хмм?..На себе нельзя жениться, ты чего?")
        embedyoucantmarryyourselflmaoidiot.set_image(url='https://media1.giphy.com/media/GstlqgmrVgpuE/source.gif')

        if member == author:
            await ctx.send(embed=embedyoucantmarryyourselflmaoidiot)

        if self.users[author_id]['couple_id'] == member_id:
            await ctx.send(embed=embedalreadymarried)
        if (self.users[member_id]['couple_id'] != 'None' or self.users[author_id]['couple_id'] != 'None') and \
                self.users[author_id]['couple_id'] != member_id:
            await ctx.send('Сперва сделайте развод со своими партнерами')

        if role not in author.roles and role not in member.roles:
            if member != author:
                if self.users[author_id]['couple_id'] != member_id:
                    await ctx.send(embed=embedmarry)

                def check(message):
                    return message.content in (
                        'да', 'нет', 'Да', 'дА', 'ДА', 'Нет', 'нЕт', 'неТ', 'НЕт', 'НеТ', 'нЕТ', 'НЕТ')

                reply = await self.client.wait_for('message', check=check, timeout=30)
                if not reply or reply.content.casefold() == 'нет':
                    await ctx.send(embed=embednii)
                if not reply or reply.content.casefold() == 'да':
                    await ctx.send(embed=embedyee)
                    await discord.Member.add_roles(member, role)
                    await discord.Member.add_roles(author, role)
                    self.users[author_id]['couple_id'] = member_id
                    self.users[member_id]['couple_id'] = author_id

    @marry.error
    async def marry_timeout(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embedtimeout = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedtimeout.add_field(name='Оууууууууууу! :interrobang: ',
                                   value="Время свадьбы закончилось. Не беспокойтесь и попробуйте ещё раз!")
            embedtimeout.set_image(url='https://media3.giphy.com/media/uHJTtpE9WqfYc/source.gif')
            await ctx.send(embed=embedtimeout)
        if isinstance(error, commands.MissingRequiredArgument):
            embedmarryerror = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedmarryerror.add_field(name='Ошибка',
                                      value=f' Укажите на ком хотите жениться. .marry @ \n Пример:')
            await ctx.send(embed=embedmarryerror)
            await ctx.send('```.marry @Clonexy700#3767```')

    @commands.command(pass_context=True)
    async def divorce(self, ctx):
        author_id = str(ctx.message.author.id)
        member = ctx.guild.get_member(int(self.users[author_id]['couple_id']))
        role = discord.utils.get(member.guild.roles, name="💍")
        author = ctx.message.author
        embeddivorce = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embeddivorce.add_field(name='Развод :broken_heart:  :broccoli: ',
                               value=f'{author.mention} теперь больше не женаты с {member.mention}')
        embeddivorce.set_image(url="https://rabujoi.files.wordpress.com/2017/02/fuu62.jpg")
        embeddivorcefail = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embeddivorcefail.add_field(name='Развод :broccoli:',
                                   value=f'{author.mention} не получилось развестись! Кажется ты или {member.mention} уже не женаты! ')
        embeddivorcefail.set_image(url='https://i.gifer.com/BtGB.gif')
        if role in author.roles and role in member.roles:
            await discord.Member.remove_roles(author, role)
            await discord.Member.remove_roles(member, role)
            member_id = self.users[author_id]['couple_id']
            self.users[member_id]['couple_id'] = 'None'
            self.users[author_id]['couple_id'] = 'None'
            self.users[author_id]['divorce_num'] += 1
            await ctx.send(embed=embeddivorce)
        else:
            await ctx.send(embed=embeddivorcefail)

    @commands.command(name='hentai', aliases=['ласкать', 'хентай'])
    async def hentai(self, ctx, member: discord.Member):
        msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]
        author = ctx.message.author
        author_id = str(ctx.message.author.id)
        member_id = str(member.id)
        if self.users[author_id]['couple_id'] == member_id:
            embedhentai = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            hentaigifs = [
                "https://66.media.tumblr.com/e5921dae5876c00e1c3fcc0540ecab12/tumblr_opnxbzZbYT1sghvvyo1_500.gif",
                "https://i.pinimg.com/originals/fc/fa/b1/fcfab1d1656f5e9f859744ce999b35d5.gif",
                "https://ci.memecdn.com/1394312.gif",
                "https://lh3.googleusercontent.com/proxy/4N3f_aUCbDjN7Dcbvbd0xi1Fx1VNJsW_U4givReTfGarUG4S5-SFBAfpLa1BH0UaGbdQItlwQgqaErtORYcCmsUAtIYU9Z1xPw",
                "https://userdisk.webry.biglobe.ne.jp/020/046/94/N000/000/000/126525418193816203746_dat1265220059955.gif",
                "https://psv4.userapi.com/c610925/u259174237/docs/5e23102a51fa/3f74a54545774160611b83983fe8020c.gif?extra=xsXm8TuVauL_efYWOtBq1fhNRhqMvHTrxoauN58As_O2Nup80jf4VVVdB-z_6AflVR-bQRIO-U351o8_MauFbTRFbskG5jQbg073yy9tSDb1fEtF169xFrWq-fFoJz_1KVsOLxqrrdS8Zf8_QhMTpuA",
                "https://66.media.tumblr.com/32f890680919d5edb248cf6de10cd1cb/tumblr_nrdtcvHEhl1trw883o1_1280.gif",
                "https://x.imagefapusercontent.com/u/bvelasco/5823564/1635151298/gOqBNfD.gif",
                "https://66.media.tumblr.com/2bd84e6dcd5fcb76dbc0448ce7211cc1/tumblr_o5zxbaSKjE1rv1jano1_540.gif",
                "https://66.media.tumblr.com/3779148a1def9b5484ce33b873b02272/tumblr_nwjlolOMea1sz111so2_540.gif",
                "https://66.media.tumblr.com/05454f06a749373d72065dbdceadb50a/tumblr_ohbvseGCp81vkkt9ro1_1280.gif",
                "https://lh3.googleusercontent.com/proxy/vStpimmvo0WAaK6nk1SwgMtp7LlXPuleXsjuln82K80K3ZJ3SBOkz6F1u-KkmO1DKsJZs6k9ndgQ4aDmDcxUA84Lbh1vsODFjieODT_JzneyMAxD_RbpMpcdauaziRRlYBbvCMuv9FCyFbxrT3biqyN1WVv05swGG22wpSY3uQ",
                "https://lh3.googleusercontent.com/proxy/VFCSlrNEErwdJhkFVO5Sk9P3R-SWYcejlDrkQgwRmCqp5MJZCgqrmWS2Uah-WzMDgl80w0ljAYU-yiNqZJ2mYtg6lF03bjbZGkLE9rC2qKBAup_dtj3pM24kxI6M_Jife_ar45BtROxtq6MhJhPY1b0OiV8YGZFYKbFuusafuoaDtxtt",
                "https://2gifs.ru/images/p49.media.tumblr.com/544299c4e63878310a02957b5e5a133c/tumblr_nyw1ejWY2E1tlb937o1_500.gif",
                "https://cs6.pikabu.ru/images/big_size_comm_an/2014-05_3/14001629958442.gif",
                "https://img-4.poringa.net/poringa/img/8/1/E/1/B/E/FrankFolla/789.gif",
                "https://pbs.twimg.com/profile_images/855027348386701313/YIgX4cok_400x400.jpg",
                "https://lh3.googleusercontent.com/proxy/rNRpnzLDcrOdqA5UmT5BGXH0Wqhv-iE1bvB3D1bbhjRWesgyW8t6_RLvQhSOjMnJW77S_Xqyt_W-47ubVJgV668G7efQmvVcdqFPxdRBXJjnI10EWrOoepav3RdWhIYFKnQsPbA6YQ",
                "https://i.imgur.com/xuZ4dHi.gif"]
            embedhentai.add_field(name="Любовь :heart:",
                                  value=f"У {author.mention} и {member.mention} любовь. :heart: {random.choice(msgend)}")
            embedhentai.set_image(url=random.choice(hentaigifs))
            await ctx.send(embed=embedhentai)
        else:
            await ctx.send('Вы не женаты с данным человеком, поэтому не можете использовать данную команду')

    @commands.command(name='waifu', aliases=['вайфу', 'пара', 'жена'])
    async def waifu(self, ctx, member: discord.Member = None):
        emoji = self.client.get_emoji(676803534758477845)
        loli = self.client.get_emoji(680064619385192515)
        author = ctx.author if not member else member
        member_id = str(author.id)
        price = self.users[member_id]['price']
        if self.users[member_id]["couple_id"] == 'None':
            pair = 'None'
        else:
            pair = ctx.guild.get_member(int(self.users[member_id]['couple_id']))
            pair = pair.name
        waifu_menu = discord.Embed(
            color=discord.Colour.dark_purple(),
            timestamp=ctx.message.created_at,
            description=f'**Цена**\n{price}{emoji}\nВайфу {author.name}\n**Вместе с**\n{pair}\n Разводов {self.users[member_id]["divorce_num"]} :broken_heart:\n __**Подарки вайфу**__:'
        )
        waifu_menu.set_author(name=f'Вайфу {author.name}', icon_url=author.avatar_url)
        waifu_menu.set_thumbnail(url=author.avatar_url)
        gifts = 'Список всех ваших подарков: \n '
        if self.users[member_id]["gift1"] != 'None':
            waifu_menu.add_field(name='Трусы ', value=f':briefs: \n • {self.users[member_id]["gift1"]}', inline=True)
        if self.users[member_id]["gift2"] != 'None':
            waifu_menu.add_field(name='Лифчик ', value=f'🩱 \n • {self.users[member_id]["gift2"]}', inline=True)
        if self.users[member_id]["gift3"] != 'None':
            waifu_menu.add_field(name='Сапоги ', value=f'🥾 \n • {self.users[member_id]["gift3"]}', inline=True)
        if self.users[member_id]["gift4"] != 'None':
            waifu_menu.add_field(name='Котик ', value=f'🐱 \n • {self.users[member_id]["gift4"]}', inline=True)
        if self.users[member_id]["gift16"] != 'None':
            waifu_menu.add_field(name='Собачка ', value=f'🐶 \n • {self.users[member_id]["gift16"]}', inline=True)
        if self.users[member_id]["gift5"] != 'None':
            waifu_menu.add_field(name='Дом ', value=f'🏠 \n • {self.users[member_id]["gift5"]}', inline=True)
        if self.users[member_id]["gift6"] != 'None':
            waifu_menu.add_field(name='Манго ', value=f'🥭 \n • {self.users[member_id]["gift6"]}', inline=True)
        if self.users[member_id]["gift7"] != 'None':
            waifu_menu.add_field(name='Шарфик ', value=f'🧣 \n • {self.users[member_id]["gift7"]}', inline=True)
        if self.users[member_id]["gift17"] != 'None':
            waifu_menu.add_field(name='Носки ', value=f'🧦 \n • {self.users[member_id]["gift17"]}', inline=True)
        if self.users[member_id]["gift8"] != 'None':
            waifu_menu.add_field(name='Чулки ', value=f'🧦 \n • {self.users[member_id]["gift8"]}', inline=True)
        if self.users[member_id]["gift9"] != 'None':
            waifu_menu.add_field(name='Неко-уши ', value=f'👙 \n • {self.users[member_id]["gift9"]}', inline=True)
        if self.users[member_id]["gift10"] != 'None':
            waifu_menu.add_field(name='Хвостик ', value=f'👙 \n • {self.users[member_id]["gift10"]}', inline=True)
        if self.users[member_id]["gift11"] != 'None':
            waifu_menu.add_field(name='Кимоно ', value=f'👘 \n • {self.users[member_id]["gift11"]}', inline=True)
        if self.users[member_id]["gift18"] != 'None':
            waifu_menu.add_field(name='Костюм горничной ', value=f'👘 \n • {self.users[member_id]["gift18"]}',
                                 inline=True)
        if self.users[member_id]["gift12"] != 'None':
            waifu_menu.add_field(name='Ошейник ', value=f'👙 \n • {self.users[member_id]["gift12"]}', inline=True)
        if self.users[member_id]["gift13"] != 'None':
            waifu_menu.add_field(name='Очки ', value=f':eyeglasses: \n • {self.users[member_id]["gift13"]}',
                                 inline=True)
        if self.users[member_id]["gift14"] != 'None':
            waifu_menu.add_field(name='Лоли ', value=f'{loli} \n • {self.users[member_id]["gift14"]}', inline=True)
        if self.users[member_id]["gift15"] != 'None':
            waifu_menu.add_field(name='Чупа-Чупс ', value=f'🍭 \n • {self.users[member_id]["gift15"]}', inline=True)
        if self.users[member_id]["gift19"] != 'None':
            waifu_menu.add_field(name='Мишка ', value=f'🧸 \n • {self.users[member_id]["gift19"]}', inline=True)
        if self.users[member_id]["gift20"] != 'None':
            waifu_menu.add_field(name='Вино ', value=f':wine_glass: \n • {self.users[member_id]["gift20"]}', inline=True)
        if self.users[member_id]["gift21"] != 'None':
            waifu_menu.add_field(name='Торт ', value=f':birthday: \n • {self.users[member_id]["gift21"]}', inline=True)
        waifu_menu.set_footer(text=f'Запросил {ctx.author.name} \n (♥ω♥ ) ~♪')
        await ctx.send(embed=waifu_menu)

    @commands.command(name='gifts', aliases=['подарки', 'giftlist', 'мп', 'giftshop', 'пм'])
    async def gifts(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        loli = self.client.get_emoji(680064619385192515)
        embed_gifts = discord.Embed(color=discord.Colour.dark_purple(), timestamp=ctx.message.created_at)
        embed_gifts.set_author(name='Подарки для вашей вайфу')
        embed_gifts.add_field(name='Трусы ', value=f':briefs: \n > 50 {emoji}', inline=True)
        embed_gifts.add_field(name='Лифчик', value=f'🩱 \n > 70 {emoji}', inline=True)
        embed_gifts.add_field(name='Сапоги', value=f'🥾 \n > 90 {emoji}', inline=True)
        embed_gifts.add_field(name='Кот', value=f'🐱 \n > 5000 {emoji}', inline=True)
        embed_gifts.add_field(name='Собака', value=f'🐶 \n > 5000 {emoji}', inline=True)
        embed_gifts.add_field(name='Дом', value=f'🏠 \n > 50000 {emoji}', inline=True)
        embed_gifts.add_field(name='Манго', value=f'🥭 \n > 20 {emoji}', inline=True)
        embed_gifts.add_field(name='Шарфик', value=f'🧣 \n > 60 {emoji}', inline=True)
        embed_gifts.add_field(name='Носки', value=f'🧦 \n > 300 {emoji}', inline=True)
        embed_gifts.add_field(name='Чулки', value=f'👙 \n > 600 {emoji}', inline=True)
        embed_gifts.add_field(name='Неко-уши', value=f'👙 \n > 800 {emoji}', inline=True)
        embed_gifts.add_field(name='Хвостик', value=f'👙 \n > 800 {emoji}', inline=True)
        embed_gifts.add_field(name='Кимоно', value=f'👘 \n > 1200 {emoji}', inline=True)
        embed_gifts.add_field(name='Костюм горничной', value=f'👘 \n > 2400 {emoji}', inline=True)
        embed_gifts.add_field(name='Ошейник', value=f'👙 \n > 2000 {emoji}', inline=True)
        embed_gifts.add_field(name='Очки', value=f':eyeglasses:  \n > 4000 {emoji}', inline=True)
        embed_gifts.add_field(name='Лоли', value=f'{loli} \n > 100000 {emoji}', inline=True)
        embed_gifts.add_field(name='Чупа-чупс', value=f'🍭 \n > 10 {emoji}', inline=True)
        embed_gifts.add_field(name='Мишка', value=f'🧸 \n > 2500 {emoji}', inline=True)
        embed_gifts.add_field(name='Вино', value=f':wine_glass: \n > 250 {emoji}', inline=True)
        embed_gifts.add_field(name='Торт', value=f':birthday: \n > 500 {emoji}', inline=True)
        embed_gifts.set_image(
            url='https://66.media.tumblr.com/c704b54b4390f2b2eef8d85c50d35dfd/tumblr_ofb1vtxYrF1th93f0o3_400.gif')
        embed_gifts.set_footer(text=f'запросил {ctx.author.name}')
        await ctx.send(embed=embed_gifts)

    @commands.command(name='gift', aliases=['подарить', 'гифт', 'п', 'подарок'])
    async def gift(self, ctx, member: discord.Member, gift=None, n: int = 1):
        loli = self.client.get_emoji(680064619385192515)
        member_id = str(member.id)
        author_id = str(ctx.author.id)
        embed_reply = discord.Embed(color=discord.Colour.dark_purple())
        gift = gift.casefold()

        if gift is None:
            def check(author):
                def inner_check(message):
                    return message.author == ctx.author and message.casefold().content in (
                        'трусы', 'лифчик', 'сапоги', 'кот', 'Собака', 'Дом', 'Манго', 'Шарфик', 'Носки', 'Чулки',
                        'Неко-уши', 'Хвостик', 'Кимоно', 'Ошейник', 'Лоли', 'Чупа-чупс', 'Костюм горничной', 'Очки', 'Мишка', 'Вино', 'Торт')

                return inner_check

            await ctx.send('Уточните пожалуйста подарок, который вы хотите отправить!')
        else:
            if gift == 'трусы':
                if self.client.currency[author_id]["money"] - 50 * n >= 0:
                    await self.client.unupdate_currency(author_id, 50 * n)
                    if self.users[member_id]["gift1"] == 'None':
                        self.users[member_id]["gift1"] = 0
                    self.users[member_id]["gift1"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 50 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Трусики '
                                                                    f':briefs:!')
            if gift == 'лифчик':
                if self.client.currency[author_id]["money"] - 70 * n >= 0:
                    await self.client.unupdate_currency(author_id, 70 * n)
                    if self.users[member_id]["gift2"] == 'None':
                        self.users[member_id]["gift2"] = 0
                    self.users[member_id]["gift2"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 70 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Лифчик '
                                                                    f'🩱!')
            if gift == 'сапоги':
                if self.client.currency[author_id]["money"] - 90 * n >= 0:
                    await self.client.unupdate_currency(author_id, 90 * n)
                    if self.users[member_id]["gift3"] == 'None':
                        self.users[member_id]["gift3"] = 0
                    self.users[member_id]["gift3"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 90 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Сапоги '
                                                                    f'🥾!')
            if gift == 'кот':
                if self.client.currency[author_id]["money"] - 5000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 5000 * n)
                    if self.users[member_id]["gift4"] == 'None':
                        self.users[member_id]["gift4"] = 0
                    self.users[member_id]["gift4"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 5000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Котика '
                                                                    f'🐱!')
            if gift == 'собака':
                if self.client.currency[author_id]["money"] - 5000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 5000 * n)
                    if self.users[member_id]["gift16"] == 'None':
                        self.users[member_id]["gift16"] = 0
                    self.users[member_id]["gift16"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 5000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Cобачку '
                                                                    f'🐶!')
            if gift == 'дом':
                if self.client.currency[author_id]["money"] - 50000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 50000 * n)
                    if self.users[member_id]["gift5"] == 'None':
                        self.users[member_id]["gift5"] = 0
                    self.users[member_id]["gift5"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 50000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Дом '
                                                                    f'🏠!')
            if gift == 'манго':
                if self.client.currency[author_id]["money"] - 20 * n >= 0:
                    await self.client.unupdate_currency(author_id, 20 * n)
                    if self.users[member_id]["gift6"] == 'None':
                        self.users[member_id]["gift6"] = 0
                    self.users[member_id]["gift6"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 20 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Манго '
                                                                    f'🥭!')
            if gift == 'шарфик':
                if self.client.currency[author_id]["money"] - 60 * n >= 0:
                    await self.client.unupdate_currency(author_id, 60 * n)
                    if self.users[member_id]["gift7"] == 'None':
                        self.users[member_id]["gift7"] = 0
                    self.users[member_id]["gift7"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 60 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Шарфик '
                                                                    f'🧣!')
            if gift == 'носки':
                if self.client.currency[author_id]["money"] - 300 * n >= 0:
                    await self.client.unupdate_currency(author_id, 300 * n)
                    if self.users[member_id]["gift17"] == 'None':
                        self.users[member_id]["gift17"] = 0
                    self.users[member_id]["gift17"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 300 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Носочки '
                                                                    f'🧦!')
            if gift == 'чулки':
                if self.client.currency[author_id]["money"] - 600 * n >= 0:
                    await self.client.unupdate_currency(author_id, 600 * n)
                    if self.users[member_id]["gift8"] == 'None':
                        self.users[member_id]["gift8"] = 0
                    self.users[member_id]["gift8"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 600 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Чулочки '
                                                                    f'👙!')
            if gift == 'неко-уши':
                if self.client.currency[author_id]["money"] - 800 * n >= 0:
                    await self.client.unupdate_currency(author_id, 800 * n)
                    if self.users[member_id]["gift9"] == 'None':
                        self.users[member_id]["gift9"] = 0
                    self.users[member_id]["gift9"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 800 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Неко-уши '
                                                                    f'👙!')
            if gift == 'хвостик':
                if self.client.currency[author_id]["money"] - 800 * n >= 0:
                    await self.client.unupdate_currency(author_id, 800 * n)
                    if self.users[member_id]["gift10"] == 'None':
                        self.users[member_id]["gift10"] = 0
                    self.users[member_id]["gift10"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 800 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Хвостик '
                                                                    f'👙!')
            if gift == 'кимоно':
                if self.client.currency[author_id]["money"] - 1200 * n >= 0:
                    await self.client.unupdate_currency(author_id, 1200 * n)
                    if self.users[member_id]["gift11"] == 'None':
                        self.users[member_id]["gift11"] = 0
                    self.users[member_id]["gift11"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 1200 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Кимоно '
                                                                    f'👘 !')
            if gift == 'костюм горничной':
                if self.client.currency[author_id]["money"] - 2400 * n >= 0:
                    await self.client.unupdate_currency(author_id, 2400 * n)
                    if self.users[member_id]["gift18"] == 'None':
                        self.users[member_id]["gift18"] = 0
                    self.users[member_id]["gift18"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 2400 * n
                    embed_reply.add_field(name='Вы подарили',
                                          value=f'{ctx.author.mention} подарил {member.mention} Костюм горничной '
                                                f'👘 !')
            if gift == 'ошейник':
                if self.client.currency[author_id]["money"] - 2000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 2000 * n)
                    if self.users[member_id]["gift12"] == 'None':
                        self.users[member_id]["gift12"] = 0
                    self.users[member_id]["gift12"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 2000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Ошейник '
                                                                    f'👙!')
            if gift == 'очки':
                if self.client.currency[author_id]["money"] - 4000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 4000 * n)
                    if self.users[member_id]["gift13"] == 'None':
                        self.users[member_id]["gift13"] = 0
                    self.users[member_id]["gift13"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 4000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Очечки '
                                                                    f':eyeglasses:!')
            if gift == 'лоли':
                if self.client.currency[author_id]["money"] - 100000 * n >= 0:
                    await self.client.unupdate_currency(author_id, 100000 * n)
                    if self.users[member_id]["gift14"] == 'None':
                        self.users[member_id]["gift14"] = 0
                    self.users[member_id]["gift14"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 100000 * n
                    embed_reply.add_field(name='Вы подарили', value=f'{ctx.author.mention} подарил {member.mention} Лольку '
                                                                    f'{loli}!')
            if gift == 'чупа-чупс':
                if self.client.currency[author_id]["money"] - 10 * n >= 0:
                    await self.client.unupdate_currency(author_id, 10 * n)
                    if self.users[member_id]["gift15"] == 'None':
                        self.users[member_id]["gift15"] = 0
                    self.users[member_id]["gift15"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 10 * n
                    embed_reply.add_field(name='Вы подарили',
                                          value=f'{ctx.author.mention} подарил {member.mention} Чупа-чупс 🍭!')
            if gift == 'мишка':
                if self.client.currency[author_id]["money"] - 2500 * n >= 0:
                    await self.client.unupdate_currency(author_id, 2500 * n)
                    if self.users[member_id]["gift19"] == 'None':
                        self.users[member_id]["gift19"] = 0
                    self.users[member_id]["gift19"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 2500 * n
                    embed_reply.add_field(name='Вы подарили',
                                          value=f'{ctx.author.mention} подарил {member.mention} Плюшевого мишку :teddy_bear: !')
            if gift == 'вино':
                if self.client.currency[author_id]["money"] - 250 * n >= 0:
                    await self.client.unupdate_currency(author_id, 250 * n)
                    if self.users[member_id]["gift20"] == 'None':
                        self.users[member_id]["gift20"] = 0
                    self.users[member_id]["gift20"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 250 * n
                    embed_reply.add_field(name='Вы подарили',
                                          value=f'{ctx.author.mention} подарил {member.mention} Винишко :wine_glass: !')
            if gift == 'торт':
                if self.client.currency[author_id]["money"] - 500 * n >= 0:
                    await self.client.unupdate_currency(author_id, 500 * n)
                    if self.users[member_id]["gift21"] == 'None':
                        self.users[member_id]["gift21"] = 0
                    self.users[member_id]["gift21"] += n
                    if self.users[member_id]["price"] == 1:
                        self.users[member_id]["price"] -= 1
                    self.users[member_id]["price"] += 500 * n
                    embed_reply.add_field(name='Вы подарили',
                                          value=f'{ctx.author.mention} подарил {member.mention} Тортик :birthday: !')
            await ctx.send(embed=embed_reply)

    @commands.command(name='ship', aliases=['шип', 'ебитес'], help=' ship 1st person with 2nd person')
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        role = discord.utils.get(member1.guild.roles, name="💍")
        empedship = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        empedship.add_field(name=':heart_eyes:  Ship :heart: ',
                            value=f' Шипперим {member1.mention} и {member2.mention} :smirk: ', inline=False)
        LovePossibility = random.randint(0, 100)
        LoveSymbolic = ["Между ними нет любви. ",
                        "▄ █ ",
                        "▄ █ █ ▄",
                        "▄ █ █ ▄ ▄ █",
                        "▄ █ █ ▄ ▄ █ ▄ █",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▆ ▅",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▆ ▅ ▃",
                        "▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▆ ▅ ▃ ▂"]
        if member1 == member2:
            empedship.add_field(name=f'Ммм... Я думаю тут проблемка.',
                                value=f"Ты не можешь шипперить двух одинаковых людей.")
        if member1 != member2:
            if member2 or member1 != discord.User.bot:
                author_id = str(member1.id)
                member_id = str(member2.id)
                if role not in member1.roles or role not in member2.roles or self.users[author_id][
                    'couple_id'] != member_id:
                    if LovePossibility <= 5:
                        empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                            value=f'{LoveSymbolic[0]} {LovePossibility} % :broken_heart: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/2d432485a60674319ef423b643877ee4/tenor.gif?itemid=11302966')
                    if LovePossibility >= 6:
                        if LovePossibility <= 10:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[1]} __**{LovePossibility}%**__ :broken_heart: ',
                                                inline=False)
                            empedship.set_image(url='https://cdn42.picsart.com/171043668003202.gif?c256x256')
                    if LovePossibility >= 11:
                        if LovePossibility <= 19:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[2]} __**{LovePossibility}%**__ :black_heart: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/e375857e0f78c321b83040514b21a420/tenor.gif?itemid=13802170')
                    if LovePossibility >= 20:
                        if LovePossibility <= 29:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[3]} __**{LovePossibility}%**__ :black_heart: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/93f5876e82ae575a6c4b4613d57f6e29/tenor.gif?itemid=13665536')
                    if LovePossibility >= 30:
                        if LovePossibility <= 39:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[4]} __**{LovePossibility}%**__ :brown_heart: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/f0479ee873f30213a7a5579cc18da5d0/tenor.gif?itemid=12165912')
                    if LovePossibility >= 40:
                        if LovePossibility <= 49:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[5]} __**{LovePossibility}%**__ :hearts: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/93f5876e82ae575a6c4b4613d57f6e29/tenor.gif?itemid=13665536')
                    if LovePossibility >= 50:
                        if LovePossibility <= 59:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[6]} __**{LovePossibility}%**__ :heart_decoration: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/f0479ee873f30213a7a5579cc18da5d0/tenor.gif?itemid=12165912')
                    if LovePossibility >= 60:
                        if LovePossibility <= 69:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[7]} __**{LovePossibility}%**__ :blue_heart: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/4490d35d5950b90df2b7bccaf4f79922/tenor.gif?itemid=3478319')
                    if LovePossibility >= 70:
                        if LovePossibility <= 79:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[8]} __**{LovePossibility}%**__ :heartbeat: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/fb1aa76944c156acc494fff37ebdbcfa/tenor.gif?itemid=14521920')
                    if LovePossibility >= 80:
                        if LovePossibility <= 89:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[9]} __**{LovePossibility}%**__ :heart_exclamation: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/62a43e567137edec0d5231d5ec4b814b/tenor.gif?itemid=8955295')
                    if LovePossibility >= 90:
                        if LovePossibility <= 100:
                            empedship.add_field(name=f'Вероятность любви между {member1} и {member2} это :',
                                                value=f'{LoveSymbolic[10]} _**{LovePossibility}%**_ :heartpulse: ',
                                                inline=False)
                            empedship.set_image(
                                url='https://media1.tenor.com/images/8cab4f4c73547d077c56066461c40a5e/tenor.gif?itemid=12873196')
                author_id = str(member1.id)
                member_id = str(member2.id)
                if self.users[author_id]['couple_id'] == member_id:
                    if role in member1.roles and role in member2.roles:
                        empedship.add_field(name=f' {member1} и {member2} в любовных отношениях:',
                                            value=f"▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▆ ▅ ▃ ▂ _ **100%** :heartpulse: _\nОни "
                                                  f"женаты! Конечно "
                                                  f"же это любовь!")
                        empedship.set_image(
                            url='https://media1.tenor.com/images/8cbe0edadc12ca1056d5eb685a4c27f6/tenor.gif?itemid=14518537')
                await ctx.send(embed=empedship)

    @ship.error
    async def shiperror(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedmarryerror = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedmarryerror.add_field(name='Ошибка синтаксиса команды',
                                      value=f' Пожалуйста идентифицируйте 1-го и 2-го пользователей. .ship @ @\n Пример:')
            await ctx.send(embed=embedmarryerror)
            await ctx.send('```.ship @Clonexy#3767 .Shiro ♣#9014```')

    @commands.command(name='waifunull', aliases=['waifureset', 'сбросвайфу', 'resetwaifu'])
    async def waifureset(self, ctx):
        author = ctx.author
        member_id = str(author.id)
        self.users[member_id]['price'] = 1
        self.users[member_id]['gift1'] = 'None'
        self.users[member_id]['gift2'] = 'None'
        self.users[member_id]['gift3'] = 'None'
        self.users[member_id]['gift4'] = 'None'
        self.users[member_id]['gift5'] = 'None'
        self.users[member_id]['gift6'] = 'None'
        self.users[member_id]['gift7'] = 'None'
        self.users[member_id]['gift8'] = 'None'
        self.users[member_id]['gift9'] = 'None'
        self.users[member_id]['gift10'] = 'None'
        self.users[member_id]['gift11'] = 'None'
        self.users[member_id]['gift12'] = 'None'
        self.users[member_id]['gift13'] = 'None'
        self.users[member_id]['gift14'] = 'None'
        self.users[member_id]['gift15'] = 'None'
        self.users[member_id]['gift16'] = 'None'
        self.users[member_id]['gift17'] = 'None'
        self.users[member_id]['gift18'] = 'None'
        self.users[member_id]['gift19'] = 'None'
        self.users[member_id]['gift20'] = 'None'
        self.users[member_id]['gift21'] = 'None'
        null = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        null.add_field(name='Ваша статистика',
                       value='Ваша статистика Вайфу была успешно обнулена по-вашему запросу, проверьте её с помощью команды .waifu !')
        await ctx.send(embed=null)

    @commands.command(name='waifutop', aliases=['топвайфу', 'вайфутоп', 'твайфу', 'лучшиевайфу', 'topwaifu'])
    async def waifutop(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        kamo = ["(●♡∀♡)",
                "✿♥‿♥✿",
                "(♥ω♥ ) ~♪",
                "(｡･ω･｡)ﾉ♡",
                "(◍•ᴗ•◍)❤",
                "-ω(´•ω•｀)♡",
                "(◍•ᴗ•◍)♡ ✧*。",
                "( ◜◒◝ )♡",
                "(人 •͈ᴗ•͈)",
                "(´͈ ᵕ `͈ ♡°◌̊)",
                "(ღ˘⌣˘ღ)",
                "( ˘ ³˘)♥",
                "( ˘ ³˘)❤",
                "❣ (●❛3❛●)",
                "(っ˘з(˘⌣˘ )",
                "(◦˘ З(◦’ںˉ◦)♡",
                "(*-ω-)ω-*)"]
        with open('marry.json') as json_data:
            d = json.load(json_data)
            result = OrderedDict({k: v for k, v in sorted(d.items(), reverse=True, key=lambda i: i[1]["price"])})
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
                            value=f"``{random.choice(kamo)}`` | {a} - {result[element]['price']} {emoji}",
                            inline=False)
        await ctx.send(embed=embed)


    @commands.command(name='emojitest')
    async def testetetetetetetete(self, ctx):
        msg = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        msg.add_field(name='Игровые роли:', value='_ _')
        msg = await ctx.send(embed=msg)
        reactions = [691522796970573856, 691523294515429377, 691523884675235960, 691524275454345286, 691525147445952583, 691525387473125376, 691525891100246027, 691526165566980176, 691526344919744513, 691526943006523441]
        for emoji_id in reactions:
            emoji = self.client.get_emoji(emoji_id)
            await msg.add_reaction(emoji)


def setup(client):
    client.add_cog(Marriage(client))