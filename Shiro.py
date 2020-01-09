import discord
import os
import youtube_dl
import requests as rq
from discord import opus
import asyncio
import json
from discord.ext import commands
import random

client = commands.Bot(command_prefix='$')
client.remove_command('help')

f = open("token.txt", "r")
token = f.readline()
f.close()


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Cog loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Cog unloaded')


@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send('Cog reloaded')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! I want to play a game!')
    await client.change_presence(activity=discord.Game(name='$help'))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! {random.choice(msgend)} My name is Shiro! Play with me, please. <3 My command list is - $help '
    )
    role = discord.utils.get('Stranger')
    await discord.Member.add_roles(member, role)


@client.command(name='help', pass_context=True)
async def help(ctx):
    author = ctx.message.author

    eset = discord.Embed(
        color=discord.Colour.dark_purple()
    )

    embed_categories = discord.Embed(
        color=discord.Colour.dark_purple()
    )

    eset.add_field(name='USE THIS COMMAND IF YOU USE SHIRO FIRST TIME ON YOUR SERVER!',
                   value="$setup_bot - setups all Shiro's commands and they will work correctly! ")
    await ctx.send(embed=eset)

    embed_categories.set_author(name='Help')
    embed_categories.add_field(name='Categories',
                               value='Choose category and write name of category through $ Example:```$Main```')
    embed_categories.add_field(name='Emotions', value='``sends help menu about emotions``:laughing:', inline=False)
    embed_categories.add_field(name='Games', value='``sends help menu about games``:game_die:', inline=False)
    embed_categories.add_field(name='Info',
                               value='``sends help menu about commands for getting info``:information_source:',
                               inline=False)
    embed_categories.add_field(name='Fun / Social / Main',
                               value='``sends help menu about main, funny and social commands``:people_holding_hands:',
                               inline=False)
    embed_categories.add_field(name='Economy', value='``sends help menu about money commands``:moneybag:', inline=False)
    embed_categories.add_field(name='Reputation', value='``sends help menu about reputation``:heavy_plus_sign:',
                               inline=False)
    embed_categories.add_field(name='RPG', value='``sends help menu about RPG!``:crossed_swords:', inline=False)
    embed_categories.add_field(name='clickerinfo', value='``sends Shiro clicker information menu!``:fleur_de_lis:  ',
                               inline=False)
    embed_categories.add_field(name='Music', value='``sends help menu about music`` :musical_note:',
                               inline=False)
    embed_categories.add_field(name='Эмоции', value='``отправляет меню с командами эмоций на русском``:flag_ru: :cry: ',
                               inline=False)
    embed_categories.add_field(name='Игры',
                               value='``отправляет меню с командами игр на русском``:flag_ru: :video_game: ',
                               inline=False)
    await ctx.send(embed=embed_categories)


@client.command(name='emotions', pass_context=True)
async def emotions(ctx):
    embed = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed.set_author(name='Help Emotions')
    embed.add_field(name='$kiss @id', value='``Sends kiss emotion``', inline=True)
    embed.add_field(name='$lewd ', value='``Sends lewd emotion``')
    embed.add_field(name='$tickle @id', value='``Sends tickle emotion``', inline=True)
    embed.add_field(name='$hug @id', value='``Sends hug emotion``', inline=True)
    embed.add_field(name='$wink', value='``Sends wink emotion``', inline=True)
    embed.add_field(name='$pat @id', value='``Sends pat emotion``', inline=True)
    embed.add_field(name='$nyan', value='``Sends nyan emotion``', inline=True)
    embed.add_field(name='$lick @id', value='``Sends lick emotion``', inline=True)
    embed.add_field(name='$handhold @id', value='``Sends handhold emotion``', inline=True)
    embed.add_field(name='$blush', value='``Sends blush emotion``', inline=True)
    embed.add_field(name='$punch @id', value='``Sends punch emotion``', inline=True)
    embed.add_field(name='$pout', value='``Sends pout emotion``', inline=True)
    embed.add_field(name='$cry', value='``Sends cry emotion``', inline=True)
    embed.add_field(name='$bite @id', value='``Sends bite emotion``', inline=True)
    embed.add_field(name='$offend', value='``Sends offend emotion``', inline=True)
    embed.add_field(name='$spank @id', value='``Sends spank emotion``', inline=True)
    embed.add_field(name='$laugh', value='``Sends laugh emotion``', inline=True)
    embed.add_field(name='$yandere', value='``Sends yandere emotion``', inline=True)
    embed.add_field(name='$facepalm', value='``Sends facepalm emotion``', inline=True)
    embed.add_field(name='$wtf', value='``Sends surprised emotion``', inline=True)
    embed.add_field(name='$dance', value='``Sends dancing emotion``', inline=True)
    embed.add_field(name='$poke @id', value='``Sends poke emotion``', inline=True)
    embed.add_field(name='$F', value='``Sends pay respect emotion``', inline=True)
    embed.add_field(name='$scared', value='``Sends scare emotion``', inline=True)

    embedemotions = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedemotions.add_field(name='$idk', value="``Sends idk emotion``", inline=True)
    embedemotions.add_field(name='$run', value="``Sends run emotion``", inline=True)
    embedemotions.add_field(name='$shy', value="``Sends shy emotion``", inline=True)
    embedemotions.add_field(name='$thinking', value="``Sends think emotion``", inline=True)
    embedemotions.add_field(name='$spy @id', value="``Sends spy emotion``", inline=True)
    embedemotions.add_field(name='$disgust', value="``Sends disgust emotion``", inline=True)
    embedemotions.add_field(name='$yawn', value="``Sends yawn emotion``", inline=True)

    await ctx.send(embed=embed)
    await ctx.send(embed=embedemotions)


@client.command(name='Emotions', pass_context=True)
async def Emotions(ctx):
    embed = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed.set_author(name='Help Emotions')
    embed.add_field(name='$kiss @id', value='``Sends kiss emotion``', inline=True)
    embed.add_field(name='$lewd ', value='``Sends lewd emotion``')
    embed.add_field(name='$tickle @id', value='``Sends tickle emotion``', inline=True)
    embed.add_field(name='$hug @id', value='``Sends hug emotion``', inline=True)
    embed.add_field(name='$wink', value='``Sends wink emotion``', inline=True)
    embed.add_field(name='$pat @id', value='``Sends pat emotion``', inline=True)
    embed.add_field(name='$nyan', value='``Sends nyan emotion``', inline=True)
    embed.add_field(name='$lick @id', value='``Sends lick emotion``', inline=True)
    embed.add_field(name='$handhold @id', value='``Sends handhold emotion``', inline=True)
    embed.add_field(name='$blush', value='``Sends blush emotion``', inline=True)
    embed.add_field(name='$punch @id', value='``Sends punch emotion``', inline=True)
    embed.add_field(name='$pout', value='``Sends pout emotion``', inline=True)
    embed.add_field(name='$cry', value='``Sends cry emotion``', inline=True)
    embed.add_field(name='$bite @id', value='``Sends bite emotion``', inline=True)
    embed.add_field(name='$offend', value='``Sends offend emotion``', inline=True)
    embed.add_field(name='$spank @id', value='``Sends spank emotion``', inline=True)
    embed.add_field(name='$laugh', value='``Sends laugh emotion``', inline=True)
    embed.add_field(name='$yandere', value='``Sends yandere emotion``', inline=True)
    embed.add_field(name='$facepalm', value='``Sends facepalm emotion``', inline=True)
    embed.add_field(name='$wtf', value='``Sends surprised emotion``', inline=True)
    embed.add_field(name='$dance', value='``Sends dancing emotion``', inline=True)
    embed.add_field(name='$poke @id', value='``Sends poke emotion``', inline=True)
    embed.add_field(name='$F', value='``Sends pay respect emotion``', inline=True)
    embed.add_field(name='$scared', value='``Sends scare emotion``', inline=True)

    embedemotions = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedemotions.add_field(name='$idk', value="``Sends idk emotion``", inline=True)
    embedemotions.add_field(name='$run', value="``Sends run emotion``", inline=True)
    embedemotions.add_field(name='$shy', value="``Sends shy emotion``", inline=True)
    embedemotions.add_field(name='$thinking', value="``Sends think emotion``", inline=True)
    embedemotions.add_field(name='$spy @id', value="``Sends spy emotion``", inline=True)
    embedemotions.add_field(name='$disgust', value="``Sends disgust emotion``", inline=True)
    embedemotions.add_field(name='$yawn', value="``Sends yawn emotion``", inline=True)
    embedemotions.add_field(name='$awoo', value="``Sends awooo emotion``", inline=True)
    embedemotions.add_field(name='$uwu', value="``Sends uwu emotion``", inline=True)
    embedemotions.add_field(name='$jojo', value="``Sends jojo emotion``", inline=True)

    await ctx.send(embed=embed)
    await ctx.send(embed=embedemotions)


@client.command(name='Games', pass_context=True)
async def Games(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Games')
    embed1.add_field(name='$coin', value='``Flips coin``', inline=False)
    embed1.add_field(name='$rockpaperscissors $rcp $rps', value='``Rock paper scissors game``', inline=False)
    embed1.add_field(name='$bkeyt',
                     value='``brick - knife - evidence - yandere - tentacles game, print $bkeytinfo for more information``')
    embed1.add_field(name='$8ball question', value='``Magic answer from ball``', inline=False)
    embed1.add_field(name='$dice # #', value='# sides # dices``Rolls dice``', inline=False)
    embed1.add_field(name='$thimble #', value='#thimbles ``the thimble game!``', inline=False)
    embed1.add_field(name='$fortune', value='``sends you prediction from fortune cookie``', inline=False)
    await ctx.send(embed=embed1)


@client.command(name='games', pass_context=True)
async def games(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Games')
    embed1.add_field(name='$coin', value='``Flips coin``', inline=False)
    embed1.add_field(name='$rockpaperscissors $rcp $rps', value='``Rock paper scissors game``', inline=False)
    embed1.add_field(name='$bkeyt',
                     value='``brick - knife - evidence - yandere - tentacles game, print $bkeytinfo for more information``')
    embed1.add_field(name='$8ball question', value='``Magic answer from ball``', inline=False)
    embed1.add_field(name='$dice # #', value='# sides # dices``Rolls dice``', inline=False)
    embed1.add_field(name='$thimble #', value='#thimbles ``the thimble game!``', inline=False)
    embed1.add_field(name='$fortune', value='``sends you prediction from fortune cookie``', inline=False)
    await ctx.send(embed=embed1)


@client.command(name='info', pass_context=True)
async def info(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Info')
    embed1.add_field(name='$ping', value='``sends ping value of bot``')
    embed1.add_field(name='$help', value='``sends help message``', inline=False)
    embed1.add_field(name='$avatar @id', value='``sends avatar of specified user``', inline=False)
    embed1.add_field(name='$level $lvl', value='``sends level and exp of user``', inline=False)
    embed1.add_field(name='$toplevel $toplvl', value='``sends users with highest level and exp ``', inline=False)
    embed1.add_field(name='$google search', value='``search in google specified search ``', inline=False)
    embed1.add_field(name='$github', value='``Send Shiro github link ``', inline=False)
    await ctx.send(embed=embed1)


@client.command(name='Info', pass_context=True)
async def info(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Info')
    embed1.add_field(name='$ping', value='``sends ping value of bot``')
    embed1.add_field(name='$help', value='``sends help message``', inline=False)
    embed1.add_field(name='$avatar @id', value='``sends avatar of specified user``', inline=False)
    embed1.add_field(name='$level $lvl', value='``sends level and exp of user``', inline=False)
    embed1.add_field(name='$toplevel $toplvl', value='``sends users with highest level and exp ``', inline=False)
    embed1.add_field(name='$google search', value='``search in google specified search ``', inline=False)
    embed1.add_field(name='$github', value='``Send Shiro github link ``', inline=False)
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['fun', 'social', 'main', 'Fun', 'Social', 'Main', 'funny', 'Funny'])
async def funnySocial(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Social Funny Main')
    embed1.add_field(name='$marry @id', value='``sends marry propose to specified user``', inline=False)
    embed1.add_field(name='$divorce @id', value='``divorce with person which you married``', inline=False)
    embed1.add_field(name='$ship @id @id', value='``ship first specified person with second specified person``',
                     inline=False)
    embed1.add_field(name='$changenick @id nick', value='``changes nickname for specified person``', inline=False)
    embed1.add_field(name='$clear amount', value='``clear amount of specified messages``', inline=False)
    embed1.add_field(name='$fortune', value='``sends you prediction from fortune cookie``', inline=False)

    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['Economy', 'economy'])
async def economycs(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Money')
    embed1.add_field(name='$balance $money', value='``sends value of your money``')
    embed1.add_field(name='$moneydaily', value='``one use per 2 hours. Give you 1000 money.``', inline=False)
    embed1.add_field(name='$market', value='``spend your money here``', inline=False)
    embed1.add_field(name='$moneygive $id', value='``send money to specified user``', inline=False)
    embed1.add_field(name='$slot bet', value='``bet your money and play slots game``', inline=False)
    embed1.add_field(name='$moneycoin bet', value='``bet your money and flip a coin``', inline=False)
    embed1.add_field(name='$topmoney', value='``sends users with biggest value of money ``', inline=False)
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['Reputation'])
async def reputation(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Reputation')
    embed1.add_field(name='$rep', value='``sends value of your reputation``')
    embed1.add_field(name='$addrep @id', value='``add 1 reputation to specified user``', inline=False)
    embed1.add_field(name='$removerep @id', value='``remove 1 reputation from specified user``', inline=False)
    embed1.add_field(name='$toprep', value='``sends users with biggest reputation ``', inline=False)
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['RPG', 'Rpg', 'rPg', 'rgp', 'rpG', 'rPG', 'RPg', 'RpG', 'RGP'])
async def rpg(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help RPG')
    embed1.add_field(name='$charactercreate', value='``create your rpg character menu``')
    embed1.add_field(name='$rpgstorystart', value='``start RPG for new character``', inline=False)
    embed1.add_field(name='$rpgplay', value='``continue RPG playing from last save point``', inline=False)
    embed1.add_field(name='$rpgheal', value='``Town nurse``', inline=False)
    embed1.add_field(name='$rpgshop', value='``Town shop``', inline=False)
    embed1.add_field(name='$rpgblacksmith', value='``Town blacksmith``', inline=False)
    embed1.add_field(name='$rpgmagic', value='``Magic learning menu``', inline=False)
    embed1.add_field(name='$rpginfo', value='``shows information about your character``', inline=False)
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['Music', 'musik', 'Musik', 'musicc', 'musi'])
async def music(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Music')
    embed1.add_field(name='SomeInfo',
                     value='``Music have custom emoji controller and some commands equivalent to controller buttons``',
                     inline=False)
    embed1.add_field(name='$join $connect',
                     value='``Connect Shiro to voice channel``',
                     inline=False)
    embed1.add_field(name='$play song_name/url',
                     value='``Request Shiro to play specified song and add it in queue``',
                     inline=False)
    embed1.add_field(name='$skip $s ',
                     value='``Request Shiro to skip song playing now``',
                     inline=False)
    embed1.add_field(name='$pause $stop',
                     value='``Request Shiro to pause song playing now``',
                     inline=False)
    embed1.add_field(name='$resume $continue',
                     value='``Request Shiro to continue song playing now``',
                     inline=False)
    embed1.add_field(name='$np $nowplaying',
                     value='``Request Shiro to show the song playing now and buttons menu``',
                     inline=False)
    embed1.add_field(name='$leave $disconnect',
                     value='``Request Shiro to leave voice channel``',
                     inline=False)
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['mathematics', 'Math', 'mat', 'matan', 'mathe', 'maths', 'Maths'])
async def math(ctx):
    embed1 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed1.set_author(name='Help Math')
    embed1.add_field(name='Trigonometric',
                     value='``$sin # $cos # $tan #\n$sinh # $cosh # $tanh #\n$asin # $acos # $atan #\n$asinh # $acosh # $atanh``')
    embed1.add_field(name='Standart',
                     value='``$sqrt # $factorial #``')
    await ctx.send(embed=embed1)


@client.command(pass_context=True, aliases=['эмоции', 'Эмоции', 'эмоцыи', 'емоции', 'Емоции'])
async def emotionsru(ctx):
    embedru = discord.Embed(
        colour=discord.Colour.dark_purple()
    )

    embedru.set_author(name='Эмоции')
    embedru.add_field(name='$цем @id', value='``Поцелуй``', inline=True)
    embedru.add_field(name='$кусь @id', value='``Кусь``', inline=True)
    embedru.add_field(name='$обнять @id', value='``Обнимашки``', inline=True)
    embedru.add_field(name='$ударить @id', value='``Удар``', inline=True)
    embedru.add_field(name='$шлеп @id', value='``Шлеп по попке``', inline=True)
    embedru.add_field(name='$лизь @id', value='``Лизнуть кого-то``', inline=True)
    embedru.add_field(name='$лол', value='``Смех``', inline=True)
    embedru.add_field(name='$смущение', value='``Эмоция смущения``', inline=True)
    embedru.add_field(name='$втф', value='``Удивление``', inline=True)
    embedru.add_field(name='$тык @id', value='``Тыкнуть кого-то``', inline=True)
    embedru.add_field(name='$испуг', value='``Эмоция страха, испуга.``', inline=True)
    embedru.add_field(name='$хз', value="``Эмоция незнания``", inline=True)
    embedru.add_field(name='$хмм', value="``Эмоция задумвчивости``", inline=True)
    await ctx.send(embed=embedru)


@client.command(pass_context=True, aliases=['игры', 'игори', 'Игари', 'Игори', 'Игры'])
async def gamessru(ctx):
    embedru = discord.Embed(
        colour=discord.Colour.dark_purple()
    )
    embedru.add_field(name='$8шар вопрос', value='``Магический ответ от шара предсказаний``', inline=True)
    embedru.add_field(name='$монетка', value='``Вы подбрасываете монетку и получаете один из двух результатов``',
                      inline=True)
    await ctx.send(embed=embedru)
    await ctx.send(embed=embedsetup)


client.marriage_active = False


@client.command(pass_context=True)
async def marry(ctx, member: discord.Member):
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
    embedmarry.add_field(name='Marriage :heart_exclamation: ',
                         value=f'{author.mention} want to marry you! {member.mention}', inline=False)
    embedmarry.add_field(name='What is your answer right now :question: :thinking:  ',
                         value='You can answer with __yes__ or __no__ (without $ ) You have 30 seconds to answer.',
                         inline=False)
    embedmarry.set_image(
        url='https://media1.tenor.com/images/69dbcb02b724d26644228a38e367d017/tenor.gif?itemid=14444888')
    embedyee.add_field(name='Marriage successful :heart:',
                       value=f'{author.mention} now married on {member.mention} ! My congratulations ;) ')
    embedyee.set_image(
        url='https://cdn.discordapp.com/attachments/624296774747553808/642210564571004929/2c4259204e631b3e70cbd248331ac1e2.gif' or 'https://media1.tenor.com/images/ed8113a52d8517b31b4073b9ee9db314/tenor.gif?itemid=11767932')
    embednii.add_field(name='Marriage unsuccessful :broken_heart: ',
                       value=f"{member.mention} rejected. Don't cry {author.mention} you will find another ")
    embednii.set_image(
        url='https://cdn.discordapp.com/attachments/624296774747553808/642209594130694163/0caba0318aa667572c0ae30f34ecf8b62896aee5_hq.gif')
    embedalreadymarried.add_field(name='You are already married', value=f'{author.mention} you are already married!')
    embedyoucantmarryyourselflmaoidiot.add_field(name='Marriage unsuccesful :thinking:  :thinking: ',
                                                 value=f"Huh?...You can't marry yourself, lul")
    embedyoucantmarryyourselflmaoidiot.set_image(url='https://media1.giphy.com/media/GstlqgmrVgpuE/source.gif')
    if client.marriage_active:
        return  # Do nothing
    client.marriage_active = True

    if member == author:
        await ctx.send(embed=embedyoucantmarryyourselflmaoidiot)

    if role not in author.roles and role not in member.roles:
        if member != author:
            await ctx.send(embed=embedmarry)

            def check(message):
                return message.content in ('yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES', 'no', 'NO', 'No')

            reply = await client.wait_for('message', check=check, timeout=30)
            if not reply or reply.content == 'no':
                await ctx.send(embed=embednii)
            if not reply or reply.content == 'NO':
                await ctx.send(embed=embednii)
            if not reply or reply.content == 'No':
                await ctx.send(embed=embednii)
            if not reply or reply.content == 'Yes':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'yes':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'yEs':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'yeS':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'YEs':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'YeS':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'YES':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
            if not reply or reply.content == 'yES':
                await ctx.send(embed=embedyee)
                await discord.Member.add_roles(member, role)
                await discord.Member.add_roles(author, role)
    else:
        await ctx.send(embed=embedalreadymarried)
    client.marriage_active = False


@marry.error
async def marry_timeout(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embedtimeout = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                               value="Seems marriage time is over. Don't worry and try to ask again!")
        embedtimeout.set_image(url='https://media3.giphy.com/media/uHJTtpE9WqfYc/source.gif')
        await ctx.send(embed=embedtimeout)
    if isinstance(error, commands.MissingRequiredArgument):
        embedmarryerror = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedmarryerror.add_field(name='Marry command error',
                                  value=f' Please indicate a member for marrying. $marry @id \n Example:')
        await ctx.send(embed=embedmarryerror)
        await ctx.send('```$marry @Clonexy700#3767```')


@client.command(name='say', help=' bot will say that u say to say')
async def say(ctx, *, message: str):
    await ctx.send(message)


@client.command(name='clear', pass_context=True)
async def clear(ctx, amount: int = None):
    if ctx.message.author.guild_permissions.manage_messages:
        amount = 3 if not amount else amount
        await ctx.channel.purge(limit=amount)
        embedclear = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedclear.add_field(name='Clear', value=f'{amount} messages was deleted!')
        await ctx.send(embed=embedclear)
    else:
        await ctx.send("Not enough permissions to clear!")


@client.command(pass_context=True, aliases=['rockpaperscissors', 'rps', 'rcp'])
async def rock_paper_scissors(ctx):
    author = ctx.author
    emote = ['🗿', '📄', "✂"]
    computer_choise = random.choice(emote)
    embedscis = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedscis.add_field(name='Rock Paper Scissors',
                        value=f'Choose your option! Shiro made her choice. {random.choice(msgend)}')
    embed_draw = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed_draw.add_field(name='Rock Paper Scissors',
                         value=f'Shiro choose was a {computer_choise} Draw!  Shall we play again? {random.choice(msgend)}')
    embed_shiro_win = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed_shiro_win.add_field(name='Rock Paper Scissors',
                              value=f'Shiro choose was a {computer_choise} Shiro win. {random.choice(msgend)} ')
    embed_user_win = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed_user_win.add_field(name='Rock Paper Scissors',
                             value=f'Shiro choose was a {computer_choise}  {author.mention} win. {random.choice(msgend)} ')
    message = await ctx.send(embed=embedscis)
    for e in emote:
        await message.add_reaction(e)

    def check(reaction, user):
        return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

    try:
        reaction, user = await client.wait_for('reaction_add', check=check, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Timed out")
        return
    if str(reaction) == '🗿' and computer_choise == '🗿':
        await ctx.send(embed=embed_draw)
    if str(reaction) == '🗿' and computer_choise == '📄':
        await ctx.send(embed=embed_shiro_win)
    if str(reaction) == '🗿' and computer_choise == '✂':
        await ctx.send(embed=embed_user_win)
    if str(reaction) == '📄' and computer_choise == '🗿':
        await ctx.send(embed=embed_user_win)
    if str(reaction) == '📄' and computer_choise == '📄':
        await ctx.send(embed=embed_draw)
    if str(reaction) == '📄' and computer_choise == '✂':
        await ctx.send(embed=embed_shiro_win)
    if str(reaction) == '✂' and computer_choise == '🗿':
        await ctx.send(embed=embed_shiro_win)
    if str(reaction) == '✂' and computer_choise == '📄':
        await ctx.send(embed=embed_user_win)
    if str(reaction) == '✂' and computer_choise == '✂':
        await ctx.send(embed=embed_draw)


@client.command()
async def bkeytinfo(ctx):
    information_embed = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    information_embed.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                value='Based on standart rock paper scissors game, but more likely anime edition and have features and 5 options. Option block scheme is attached to this message'
                                      '\n Emojis and their meaning: \nBrick - 🧱, Knife - 🔪,Evidence - 📋,Yandere - 😈 ,Tentacles - 🐙 ')
    information_embed.set_image(
        url='https://cdn.discordapp.com/attachments/635409942118924291/662890429192208405/a0532d853a21fe70.png')
    await ctx.send(embed=information_embed)


@client.command()
async def bkeyt(ctx):
    author = ctx.author
    emote = ['🧱', '🔪', "📋", '😈', '🐙']
    computer_choise = random.choice(emote)
    embedscis = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedscis.add_field(name='Brick Knife Evidence Yandere Tentacles',
                        value=f'Choose your option! Shiro already made her choice. {random.choice(msgend)}')
    embed_draw = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed_shiro_win = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed_user_win = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    message = await ctx.send(embed=embedscis)

    for e in emote:
        await message.add_reaction(e)

    def check(reaction, user):
        return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

    try:
        reaction, user = await client.wait_for('reaction_add', check=check, timeout=60)

    except asyncio.TimeoutError:
        await ctx.send("Timed out")
        return
    # 1 - 5
    if str(reaction) == '🧱' and computer_choise == '🧱':
        embed_draw.add_field(name='Brick Knife Evidence Yandere Tentacles',
                             value='Brick on other brick. Wow, we can build a house! Draw.')
        await ctx.send(embed=embed_draw)
    if str(reaction) == '🧱' and computer_choise == '🔪':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f'Brick and knife.Hey knife, maybe at least you will try? No? Okay, it means that {author.mention}  win!')
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '🧱' and computer_choise == '📋':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value="Brick and evidence. It's more likely like rock and paper! Shiro win!")
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '🧱' and computer_choise == '😈':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value="Brick and yandere. Good new weapon for yandere! Shiro win!")
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '🧱' and computer_choise == '🐙':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Brick and tentacles. Tentacles can't do something with brick!?  {author.mention}  win!")
        await ctx.send(embed=embed_user_win)

    # 2 - 5
    if str(reaction) == '🔪' and computer_choise == '🧱':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f'Knife and brick.Hey knife, maybe at least you will try? No? Okay, it means that Shiro win!')
        await ctx.send(embed=embed_shiro_win)
    if str(reaction) == '🔪' and computer_choise == '🔪':
        embed_draw.add_field(name='Brick Knife Evidence Yandere Tentacles',
                             value=f'Knife and knife. CHOP CHOP CHOP CHOP! Draw!')
        await ctx.send(embed=embed_draw)

    if str(reaction) == '🔪' and computer_choise == '📋':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Knife and evidence. Evidence meet its end! {author.mention} win!")
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '🔪' and computer_choise == '😈':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value="Knife and yandere. Good new weapon for yandere! Shiro win!")
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '🔪' and computer_choise == '🐙':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Knife and tentacles. Honey, we have seafood today for lunch.  {author.mention}  win!")
        await ctx.send(embed=embed_user_win)

    # 3 - 5

    if str(reaction) == '📋' and computer_choise == '🧱':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Evidence and brick. It's more likely like paper and rock! {author.mention}")
        await ctx.send(embed=embed_user_win)
    if str(reaction) == '📋' and computer_choise == '🔪':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f'Evidence and knife. Evidence meet its end! Shiro win!')
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '📋' and computer_choise == '📋':
        embed_draw.add_field(name='Brick Knife Evidence Yandere Tentacles',
                             value=f"Evidence and evidence. Yandere have no chances now! Draw!")
        await ctx.send(embed=embed_draw)

    if str(reaction) == '📋' and computer_choise == '😈':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Evidence and yandere. Her sempai will know the truth! {author.mention}!")
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '📋' and computer_choise == '🐙':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f"Evidence and tentacles. Now this is not an evidence, but just a ball of paper! Shiro  win!")
        await ctx.send(embed=embed_shiro_win)

    # 4 - 5
    if str(reaction) == '😈' and computer_choise == '🧱':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Yandere and brick.  Good new weapon for yandere! {author.mention} win!")
        await ctx.send(embed=embed_user_win)
    if str(reaction) == '😈' and computer_choise == '🔪':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Yandere and knife. Good new weapon for yandere! {author.mention} win!")
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '😈' and computer_choise == '📋':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f"Yandere and evidence. Her sempai will know the truth! Shiro win!")
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '😈' and computer_choise == '😈':
        embed_draw.add_field(name='Brick Knife Evidence Yandere Tentacles',
                             value=f"Yandere and yandere. SEMPAI! SEMPAI! SEMPAI! Draw!")
        await ctx.send(embed=embed_draw)

    if str(reaction) == '😈' and computer_choise == '🐙':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f"Yandere and tentacles. Oof...Is it new hentai? Shiro  win!")
        await ctx.send(embed=embed_shiro_win)

    # 5 - 5

    if str(reaction) == '🐙' and computer_choise == '🧱':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f"Tentacles and brick.  Tentacles can't do something with brick!? Shiro win!")
        await ctx.send(embed=embed_shiro_win)
    if str(reaction) == '🐙' and computer_choise == '🔪':
        embed_shiro_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                  value=f"Tentacles and knife. Honey, we have seafood today for lunch. Shiro win!")
        await ctx.send(embed=embed_shiro_win)

    if str(reaction) == '🐙' and computer_choise == '📋':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Tentacles and evidence. Now this is not an evidence, but just a ball of paper! {author.mention}  win!")
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '🐙' and computer_choise == '😈':
        embed_user_win.add_field(name='Brick Knife Evidence Yandere Tentacles',
                                 value=f"Tentacles and yandere. Oof...Is it new hentai? {author.mention}  win!")
        await ctx.send(embed=embed_user_win)

    if str(reaction) == '🐙' and computer_choise == '🐙':
        embed_draw.add_field(name='Brick Knife Evidence Yandere Tentacles',
                             value=f"Tentacles and tentacles. Tentacles in tentacles on tentacles with tentacles under tentacles above tentacles and below tentacles! Draw!")
        await ctx.send(embed=embed_draw)


@client.command(name='fortune', help='fortune cookie')
async def fortune(ctx):
    embedfortune = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    quotes = ["Today it's up to you to create the peacefulness you long for.",
              "A friend asks only for your time not your money.",
              "If you refuse to accept anything but the best, you very often get it.",
              "A smile is your passport into the hearts of others.",
              "Change can hurt, but it leads a path to something better.",
              "Hard work pays off in the future, laziness pays off now.",
              "Hidden in a valley beside an open stream- This will be the type of place where you will find your dream.",
              "A chance meeting opens new doors to success and friendship.",
              "You learn from your mistakes... You will learn a lot today.",
              "Be on the lookout for coming events; They cast their shadows beforehand.",
              "You cannot love life until you live the life you love.",
              "Our deeds determine us, as much as we determine our deeds.",
              "A dream you have will come true.",
              "Meeting adversity well is the source of your strength.",
              "You already know the answer to the questions lingering inside your head.",
              "You must try, or hate yourself for not trying.",
              "The love of your life is stepping into your planet this summer.",
              "Serious trouble will bypass you.",
              "Adversity is the parent of virtue.",
              "A stranger, is a friend you have not spoken to yet.",
              "Keep your eye out for someone special.",
              "You will travel to many exotic places in your lifetime.",
              "You are very talented in many ways.",
              "A new voyage will fill your life with untold memories.",
              "You will travel to many exotic places in your lifetime.",
              "Your ability for accomplishment will follow with success.",
              "Its amazing how much good you can do if you dont care who gets the credit.",
              "Nothing astonishes men so much as common sense and plain dealing.",
              "Everyone agrees. You are the best.",
              "It's better to be alone sometimes.",
              "Jealousy doesn't open doors, it closes them!",
              "Fortune favors the brave.",
              "Happiness is an activity.",
              "Accept your past without regrets. Handle your present with confidence. Face your future without fear.",
              "Stop wishing. Start doing.",
              "If you have something worth fighting for, then fight for it.",
              "Never give up. Always find a reason to keep trying.",
              "Sometimes you just need to lay on the floor.",
              "Help is always needed but not always appreciated. Stay true to your heart and help those in need weather they appreciate it or not.",
              "Ask yourself if what you are doing today is getting you closer to where you want to be tomorrow.",
              "Believing that you are beautiful will make you appear beautiful to others around you.",
              "You will always be surrounded by true friends",
              "If you're happy, you're successful.",
              "Before trying to please others think of what makes you happy.",
              "For hate is never conquered by hate. Hate is conquered by love .",
              "When hungry, order more Chinese food.",
              "Be tactful; overlook your own opportunity.",
              "It is very possible that you will achieve greatness in your lifetime.",
              "Go and watch anime.",
              "You are the controller of your destiny.",
              "How can you have a beutiful ending without making beautiful mistakes.",
              "You can open doors with your charm and patience.",
              "Welcome the change coming into your life.",
              "You try hard, never to fail. You don't, never to win.",
              "Never give up on someone that you don't go a day without thinking about.",
              "Next full moon brings an enchanting evening.",
              "Impossible is a word only to be found in the dictionary of fools.",
              "If you are never patient, you will never get anything done. If you believe you can do it, you will be rewarded with success.",
              "You are extremely loved. Don't worry :)",
              "You are a person of culture.",
              "You believe in the goodness of man kind.",
              "Life is like a dogsled team. If you ain't the lead dog, the scenery never changes.",
              "Intelligence is the door to freedom and alert attention is the mother of intelligence.",
              "Back away from individuals who are impulsive."]

    embedfortune.add_field(name='Fortune cookie :cookie: ', value=f'{random.choice(quotes)} {random.choice(msgend)}')
    await ctx.send(embed=embedfortune)


@client.command(name='ship', help=' ship 1st person with 2nd person')
async def ship(ctx, member1: discord.Member, member2: discord.Member):
    role = discord.utils.get(member1.guild.roles, name="💍")
    empedship = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    empedship.add_field(name=':heart_eyes:  Ship :heart: ',
                        value=f' Shipping {member1.mention} and {member2.mention} :smirk: ', inline=False)
    LovePossibility = random.randint(0, 100)
    LoveSymbolic = ["There are no love between this 2 persons. Only ",
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
        empedship.add_field(name=f'I think... There is some problems', value=f"You can't ship 2 same persons")
    if member1 != member2:
        if member2 or member1 != discord.User.bot:
            if role not in member1.roles or role not in member2.roles:
                if LovePossibility <= 5:
                    empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                        value=f'{LoveSymbolic[0]} {LovePossibility} % :broken_heart: ',
                                        inline=False)
                    empedship.set_image(
                        url='https://media1.tenor.com/images/2d432485a60674319ef423b643877ee4/tenor.gif?itemid=11302966')
                if LovePossibility >= 6:
                    if LovePossibility <= 10:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[1]} __**{LovePossibility}%**__ :broken_heart: ',
                                            inline=False)
                        empedship.set_image(url='https://cdn42.picsart.com/171043668003202.gif?c256x256')
                if LovePossibility >= 11:
                    if LovePossibility <= 19:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[2]} __**{LovePossibility}%**__ :black_heart: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/e375857e0f78c321b83040514b21a420/tenor.gif?itemid=13802170')
                if LovePossibility >= 20:
                    if LovePossibility <= 29:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[3]} __**{LovePossibility}%**__ :black_heart: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/93f5876e82ae575a6c4b4613d57f6e29/tenor.gif?itemid=13665536')
                if LovePossibility >= 30:
                    if LovePossibility <= 39:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[4]} __**{LovePossibility}%**__ :brown_heart: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/f0479ee873f30213a7a5579cc18da5d0/tenor.gif?itemid=12165912')
                if LovePossibility >= 40:
                    if LovePossibility <= 49:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[5]} __**{LovePossibility}%**__ :hearts: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/93f5876e82ae575a6c4b4613d57f6e29/tenor.gif?itemid=13665536')
                if LovePossibility >= 50:
                    if LovePossibility <= 59:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[6]} __**{LovePossibility}%**__ :heart_decoration: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/f0479ee873f30213a7a5579cc18da5d0/tenor.gif?itemid=12165912')
                if LovePossibility >= 60:
                    if LovePossibility <= 69:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[7]} __**{LovePossibility}%**__ :blue_heart: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/4490d35d5950b90df2b7bccaf4f79922/tenor.gif?itemid=3478319')
                if LovePossibility >= 70:
                    if LovePossibility <= 79:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[8]} __**{LovePossibility}%**__ :heartbeat: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/fb1aa76944c156acc494fff37ebdbcfa/tenor.gif?itemid=14521920')
                if LovePossibility >= 80:
                    if LovePossibility <= 89:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[9]} __**{LovePossibility}%**__ :heart_exclamation: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/62a43e567137edec0d5231d5ec4b814b/tenor.gif?itemid=8955295')
                if LovePossibility >= 90:
                    if LovePossibility <= 100:
                        empedship.add_field(name=f'I think possibility of love between {member1} and {member2} is :',
                                            value=f'{LoveSymbolic[10]} _**{LovePossibility}%**_ :heartpulse: ',
                                            inline=False)
                        empedship.set_image(
                            url='https://media1.tenor.com/images/8cab4f4c73547d077c56066461c40a5e/tenor.gif?itemid=12873196')
            if role in member1.roles and role in member2.roles:
                empedship.add_field(name=f' {member1} and {member2} is in love:',
                                    value=f"▄ █ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▆ ▅ ▃ ▂ _ **100%** :heartpulse: _\nThis 2 persons are married! They "
                                          f"are in love without any doubt!")
                empedship.set_image(
                    url='https://media1.tenor.com/images/8cbe0edadc12ca1056d5eb685a4c27f6/tenor.gif?itemid=14518537')
    await ctx.send(embed=empedship)


@ship.error
async def shiperror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedmarryerror = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedmarryerror.add_field(name='Ship command error',
                                  value=f' Please indicate a first member for shipping and second member. $ship @id @id\n Example:')
        await ctx.send(embed=embedmarryerror)
        await ctx.send('```$ship @Clonexy#3767 @Shiro ♣#9014```')


client.marriage_active = False


@client.command(pass_context=True)
async def divorce(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="💍")
    author = ctx.message.author
    embeddivorce = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embeddivorce.add_field(name='Divorce :broken_heart:  :broccoli: ',
                           value=f'{author.mention} now is divorced with {member.mention}')
    embeddivorce.set_image(url="https://rabujoi.files.wordpress.com/2017/02/fuu62.jpg")
    embeddivorcefail = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embeddivorcefail.add_field(name='Divorce :broccoli:',
                               value=f'{author.mention} divorce fail! Seems you are or {member.mention} already not married! ')
    embeddivorcefail.set_image(url='https://i.gifer.com/BtGB.gif')
    if role in author.roles and role in member.roles:
        await discord.Member.remove_roles(author, role)
        await discord.Member.remove_roles(member, role)
        await ctx.send(embed=embeddivorce)
    else:
        await ctx.send(embed=embeddivorcefail)


@client.command(name='ping', help=' - shows my ping')
async def ping(ctx):
    embedping = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedping.add_field(name='My ping', value=f'Pong!{round(client.latency * 1000)}ms {random.choice(msgend)}')
    await ctx.send(embed=embedping)


@client.command(help=' - test command')
async def test(ctx):
    await ctx.send(
        "1234567890ё-=йцукенгшщзхъфывапролдэячсмитьбю.`123456790-=qwertyuiop[]asdfghjkl;'zxcvbnm,./?.!@№#$;%^:&?*()_-+=\/|")


@client.command(name='avatar', help='sends avatar image')
async def avatar(ctx, member: discord.Member):
    author = ctx.message.author
    embedavatar = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedavatar.set_image(url='{}'.format(member.avatar_url))
    embedavatar.add_field(name=f'Profile image of @{member.display_name}', value=f'requested by {author.mention}')
    await ctx.send(embed=embedavatar)


@client.command(pass_context=True)
async def changenick(ctx, member: discord.Member, nick):
    if ctx.message.author.guild_permissions.change_nickname:
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')


@client.command(name='8ball', help='your question - you getting magic answer from magic ball')
async def ball8(ctx, question):
    embedball8 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    embedball8.add_field(name='ball8', value=' :8ball: ', inline=False)
    embedball8.add_field(name='Prediction', value=f'{random.choice(responses)} {random.choice(msgend)}')
    embedball8.set_image(url='https://static.zerochan.net/Wizard.Cookie.full.2415740.jpg')
    await ctx.send(embed=embedball8)


@client.command(name='8шар', help='ваш вопрос - вы получаете магический ответ от шара')
async def ball8ru(ctx, question):
    embedball8 = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    responses = ["Это точно.",
                 "Да, это так.",
                 "Без сомнений.",
                 "Да - точно.",
                 "Можешь быть уверен в этом.",
                 "Как мне кажется...Да.",
                 "Вообщем-то.... Угу.",
                 "НЕ, НЕ, НЕ, НЕ.",
                 "Ага.",
                 "Звёзды говорят - да.",
                 "Точно - нет.",
                 "Не знаю.",
                 "Тебе лучше не знать это.",
                 "Не могу сказать сейчас точно.",
                 "Спросите попозже.",
                 "Даже не рассчитывай на ответ на этот вопрос.",
                 "Мне надо подумать над ответом.",
                 "Мой ответ - нет.",
                 "Мои тайные источники говорят - нет.",
                 "Врятли.",
                 "Сомневаюсь."]
    embedball8.add_field(name='Шар Предсказаний', value=' :8ball:  ', inline=False)
    embedball8.add_field(name='Предсказание', value=f'{random.choice(responses)} {random.choice(msgend)}')
    embedball8.set_image(url='https://static.zerochan.net/Wizard.Cookie.full.2415740.jpg')
    await ctx.send(embed=embedball8)


@client.command(name='coin', help=' - You flip a coin with 2 sides')
async def coin(ctx):
    author = ctx.message.author
    embedtails = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedhead = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    sides = ["tails", "heads"]
    embedtails.add_field(name='Coin', value=f'{author.mention} flipped **tails** {random.choice(msgend)}')
    embedtails.set_image(
        url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
    embedhead.add_field(name='Coin', value=f'{author.mention} flipped **heads** {random.choice(msgend)}')
    embedhead.set_image(
        url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
    if random.choice(sides) == 'tails':
        await ctx.send(embed=embedtails)
    else:
        await ctx.send(embed=embedhead)


@client.command(name='github')
async def github(ctx):
    embed = discord.Embed(color=discord.Colour.dark_purple(), timestamp=ctx.message.created_at)

    embed.set_author(name=f'Shiro ♣', icon_url=client.user.avatar_url)

    embed.add_field(name='Link', value=f"https://github.com/Clonexy700/DiscordShiro")

    await ctx.send(embed=embed)


@client.command(name='монетка', help=' - You flip a coin with 2 sides')
async def coin(ctx):
    author = ctx.message.author
    embedtails = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedhead = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    sides = ["орёл", "решка"]
    embedtails.add_field(name='Coin', value=f'{author.mention}**Орёл** {random.choice(msgend)}')
    embedtails.set_image(
        url='https://66.media.tumblr.com/c187f27ce64bfaed2202ba83af242454/tumblr_pvmq8qaWL81xuqm6qo1_500.gif')
    embedhead.add_field(name='Coin', value=f'{author.mention}  **Решка** {random.choice(msgend)}')
    embedhead.set_image(
        url='https://68.media.tumblr.com/4c0e4d4f186433f84ad11109f0b619b2/tumblr_np6oolnI2c1td4t64o1_500.gif')
    if random.choice(sides) == 'орёл':
        await ctx.send(embed=embedtails)
    else:
        await ctx.send(embed=embedhead)


@client.command(name='thimble', help='thimbles with the baaaall')
async def thimble(ctx, couple_of_thimbles: int):
    embedsmall = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embedsmall.add_field(name='Error', value="You can't play with 1 thimble! Choose more than 1")
    if couple_of_thimbles != 1:
        embedthimble = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedthimblerightguess = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedthimblewrongguess = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        number_of_thimble = random.randint(1, couple_of_thimbles)
        embedthimble.set_image(url='https://i.gifer.com/T0lP.gif')
        embedthimble.add_field(name='Thimbles ',
                               value=f'Which one you will choose? Choose from 1 to {couple_of_thimbles}! and write it under the message!')
        embedthimblerightguess.set_image(
            url='https://i.pinimg.com/originals/08/26/31/082631de583b33f19b18ec0949128014.gif')
        embedthimblerightguess.add_field(name='You are right!',
                                         value=f'Yes! You are right! Your answer is right! Its really {number_of_thimble}')
        embedthimblewrongguess.set_image(
            url='https://thumbs.gfycat.com/ImpassionedMildHowlermonkey-size_restricted.gif')
        embedthimblewrongguess.add_field(name='Nope ;)', value=f'No, right answer was {number_of_thimble}')
        await ctx.send(embed=embedthimble)
        reply = await client.wait_for('message', timeout=20)
        if not reply or reply.content == f'{number_of_thimble}':
            await ctx.send(embed=embedthimblerightguess)
        else:
            await ctx.send(embed=embedthimblewrongguess)
    else:
        await ctx.send(embed=embedsmall)


@thimble.error
async def thimble_timeout(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedtimeout = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                               value="Please write the number of thimbles! Example: **$thimble 5**", inline=False)
        embedtimeout.set_image(url='https://i.pinimg.com/originals/3e/26/4d/3e264def78c771be662b97e51cbb1768.gif')
        await ctx.send(embed=embedtimeout)
    if isinstance(error, commands.CommandInvokeError):
        embedtimeout = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedtimeout.add_field(name='Whooopsyy! :interrobang: ',
                               value="Seems time is over. Don't worry and try to ask again!")
        embedtimeout.set_image(url='https://media3.giphy.com/media/uHJTtpE9WqfYc/source.gif')
        await ctx.send(embed=embedtimeout)


@client.command(name='dice', help='number of dice  number of sides - Simulates rolling dice.')
async def roll(ctx, number_of_sides: int = None, number_of_dice: int = None):
    number_of_dice = 1 if not number_of_dice else number_of_dice
    number_of_sides = 6 if not number_of_sides else number_of_sides
    embeddice = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    embeddice.add_field(name=':game_die: Dice', value=', '.join(dice) + f' <-- Results {random.choice(msgend)}')
    embeddice.set_image(url='https://media1.giphy.com/media/3ohjUS2N88LGAjLypO/giphy.gif')
    await ctx.send(embed=embeddice)


@client.command(name='google')
async def google(ctx, *, search: str):
    embed = discord.Embed(
        color=discord.Colour.dark_purple()
    )
    embed.add_field(name='Google',
                    value=f"[Google search for \"{search}\"](https://www.google.com/search?q={search.replace(' ', '+')})")
    await ctx.send(embed=embed)


client.run(token)