import discord
import os
import youtube_dl
import requests as rq
from discord import opus
import asyncio
import functools
import json
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
from discord.ext import commands
import random

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send('Cog loaded')

    @commands.command()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog unloaded')

    @commands.command()
    async def reload(self, ctx, extension):
        self.client.reload_extension(f'cogs.{extension}')
        await ctx.send('Cog reloaded')

    @commands.group(name='help', aliases=['помощь', 'хелп', 'гайд'], pass_context=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed_categories = discord.Embed(
                color=discord.Colour.dark_purple()
            )

            embed_categories.set_author(name='Помощь')
            embed_categories.add_field(name='Эмоции', value='``Отправляет меню эмоций``:laughing:', inline=False)
            embed_categories.add_field(name='Игры', value='``Отправляет меню, связанное с играми``:game_die:',
                                       inline=False)
            embed_categories.add_field(name='Информация',
                                       value='``Отправляет меню о командах с целью получения информации``:information_source:',
                                       inline=False)
            embed_categories.add_field(name='Соц/Веселое',
                                       value='``Отправляет меню социальных и веселых команд``:people_holding_hands:',
                                       inline=False)
            embed_categories.add_field(name='Экономика',
                                       value='``Отправляет меню команд связанных с экономикой и валютой '
                                             'сервера``:moneybag:', inline=False)
            embed_categories.add_field(name='Репутация', value='``Отправляет меню связанное с репутацией на '
                                                               'сервере``:heavy_plus_sign:',
                                       inline=False)
            embed_categories.add_field(name='Кликер',
                                       value='``Отправляет меню связанное с Широ кликером!``:fleur_de_lis:  ',
                                       inline=False)
            embed_categories.add_field(name='Клан',
                                       value='``Отправляет меню связанное с клановой системой``:shield:  ',
                                       inline=False)
            embed_categories.add_field(name='Музыка', value='``Отправляет меню связанное с музыкальными командами!`` '
                                                            ':musical_note:',
                                       inline=False)
            embed_categories.set_image(
                url='https://cdn.discordapp.com/attachments/621005423335702528/675953029245304832/6ebb695705e70bd2.gif')
            await ctx.send(embed=embed_categories)

    @help.command(name='emotions', aliases=['эмоции', 'Эмоции', 'эмоцыи', 'емоции', 'Емоции'], pass_context=True)
    async def _emotions(self, ctx):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.set_author(name='Help Emotions')
        embed.add_field(name='```.kiss @ .цем @ .тьмок @ .цом @ .поцеловать @```', value='``Поцеловать кого-то``',
                        inline=True)
        embed.add_field(name='```.lewd .разврат```', value='``Развратная эмоция``')
        embed.add_field(name='```.tickle @ .щекотать @```', value='``Щекотать кого-то``', inline=True)
        embed.add_field(name='```.hug @ .обнять @```', value='``Обнимашки с @``', inline=True)
        embed.add_field(name='```.wink .подмигнуть```', value='``Подмигнуть ;)``', inline=True)
        embed.add_field(name='```.pat @ .погладить @```', value='``Погладить кого-либо``', inline=True)
        embed.add_field(name='```.nyan .ня```', value='``Кошачья эмоция``', inline=True)
        embed.add_field(name='```.lick @ .лизь @ .облизать @ .лизнуть @```', value='``Облизать кого-то``', inline=True)
        embed.add_field(name='```.handhold @ .бр @```', value='``Подержать кого-то за ручки``', inline=True)
        embed.add_field(name='```.blush .смущение```', value='``Смущение``', inline=True)
        embed.add_field(name='```.punch @ .ударить @```', value='``Ударить кого-либо``', inline=True)
        embed.add_field(name='```.pout .дщ .щечки```', value='``Надуть щёчки``', inline=True)
        embed.add_field(name='```.cry .плакать .плак```', value='``Начать плакать``', inline=True)
        embed.add_field(name='```.bite @ .кусь @ .укусить @```', value='``Sends bite emotion``', inline=True)
        embed.add_field(name='```.offend .обида```', value='``Sends offend emotion``', inline=True)
        embed.add_field(name='```.spank @ .шлепнуть @ .шлеп @```', value='``Шлепнуть кого-то по попе``', inline=True)
        embed.add_field(name='```.laugh .лол .смех```', value='``Посмеяться``', inline=True)
        embed.add_field(name='```.yandere .яндере```', value='``Яндере``', inline=True)
        embed.add_field(name='```.facepalm .рукалицо```', value='``О боже какой тупой поступок. Рукалицо.``',
                        inline=True)
        embed.add_field(name='```.wtf .шо .ват .втф .удивление```', value='``Sends surprised emotion``', inline=True)
        embed.add_field(name='```.dance .танец .танцевать```', value='``Станцевать``', inline=True)
        embed.add_field(name='```.poke @ .тык @```', value='``Тыкнуть``', inline=True)
        embed.add_field(name='```.F .эф .ф```', value='``Отдать кому-то честь!F !``', inline=True)
        embed.add_field(name='```.scared .испуг```', value='``Испугаться, напугаться чего-то``', inline=True)

        embedemotions = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedemotions.add_field(name='```.idk .хз .нинаю .незнаю```', value="``Не знаю``", inline=True)
        embedemotions.add_field(name='```.run .бежим .побег```',
                                value="``Позволяет вам сбежать из неудобной ситуации``",
                                inline=True)
        embedemotions.add_field(name='```.shy .застенчивость .стесняюсь .стесняшка```',
                                value="``Оу...Ну...Я стесняюсь``",
                                inline=True)
        embedemotions.add_field(name='```.thinking .думаю```', value="``Задумчивое состояние``", inline=True)
        embedemotions.add_field(name='```.spy @ .шпионить @ .следить @```', value="``Следить за кем-либо``",
                                inline=True)
        embedemotions.add_field(name='```.disgust .отвращение .отврат .фуу```', value="``Sends disgust emotion``",
                                inline=True)
        embedemotions.add_field(name='```.yawn .зевнуть```', value="``Sends yawn emotion``", inline=True)
        embedemotions.add_field(name='```.awoo```', value="``Awoooooooooo!``", inline=True)
        embedemotions.add_field(name='```.uwu```', value="``UwU``", inline=True)
        embedemotions.add_field(name='```.jojo```', value="``JoJo!``", inline=True)
        embedemotions.set_image(
            url='https://cdn.discordapp.com/attachments/621005423335702528/675956909609844736/373b00b003619f74.gif')

        await ctx.send(embed=embed)
        await ctx.send(embed=embedemotions)

    @help.command(name='Games', aliases=['games', 'игры', 'Игры', 'игори', 'игр', 'game', 'Game'], pass_context=True)
    async def _Games(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Игры')
        embed1.add_field(name='.coin n s\n.монетка n s\n.cf n s',
                         value='``Подбросить монетку и угадать выпадающую сторону \n n - '
                               'ставка в валюте, s - сторона со значениями: **орёл** '
                               '**решка**, **о**, **р**``', inline=False)
        embed1.add_field(name='.rcp n .rps n .кнб n', value='``Камень ножницы бумага \n n - ставка в валюте``',
                         inline=False)
        embed1.add_field(name='.bkeyt n .кнкят n',
                         value='``Кирпич нож компромат яндере тентакли! \n n - ставка в валюте, bkeytinfo - меню с '
                               'дополнительной информацией о '
                               'игре``')
        embed1.add_field(name='.8шар q .8ball q',
                         value='``Где q - вопрос, задаваемый шару. В ответ вы получаете магический ответ от шара в формате да, не знаю, нет и прочие их вариации.``',
                         inline=False)
        embed1.add_field(name='.dice s n', value='``Подбрасывает кубик с s - сторон и n кубиков. ``', inline=False)
        embed1.add_field(name='.thimble n stavka \n.наперстки n stavka', value='``Напёрстки!, где n - количество '
                                                                               'напёрстков, а stavka - ваша ставка, '
                                                                               'которая при правильном угадывании '
                                                                               'умножается на количество наперстков и '
                                                                               'идет вам в карман ``', inline=False)
        embed1.add_field(name='.fortune', value='``меню фортуны(позже)``', inline=False)
        embed1.add_field(name='.slot n', value='``Игра в слоты, где n - ваша ставка``', inline=False)
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681367329753268225/gamess.gif')
        await ctx.send(embed=embed1)

    @help.command(name='info', aliases=['инфо', 'информация', 'Информация', 'информ', 'Информ', 'Info'],
                  pass_context=True)
    async def info(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Инфо')
        embed1.add_field(name='.me', value='``Профиль пользователя``', inline=False)
        embed1.add_field(name='.bgshop\n.обои', value='``Магазин обоев для вашего профиля пользователя``', inline=False)
        embed1.add_field(name='.bg\n.bgset\n.bgs\n.mybg\n.моиобои', value='``Позволяет установить, купленные пользователем обои ему в профиль. '
                                           'Присылает меню с доступными обоями по их цифровым обозначениям и от '
                                           'автора команды ожидает цифру, как ответ на установку обоев в профиль. '
                                           'Указанные цифрой в следующем сообщении обои будут установлены``', inline=False)
        embed1.add_field(name='.ping', value='``Узнать значение пинга у Тет``', inline=False)
        embed1.add_field(name='.help', value='``Отправляет меню гайда по боту``', inline=False)
        embed1.add_field(name='.avatar @', value='``Получить аватар указанного пользователя``', inline=False)
        embed1.add_field(name='.level .lvl', value='``Узнать уровень и опыт пользователя``', inline=False)
        embed1.add_field(name='.toplevel .toplvl', value='``Топ пользователей по уровню и опыту``', inline=False)
        embed1.add_field(name='.google search', value='``Результат гугл поиска по указанному запросу, где search - ваш '
                                                      'запрос``', inline=False)
        embed1.add_field(name='.reverse text\n.переверни text\n.реверс text', value='``Переворачивает введённый вами '
                                                                                    'text, где text - то, что получает '
                                                                                    'бот на вход.``', inline=False)
        embed1.add_field(name='.пароль n\n.password n', value='``Создает и отправляет вам в личные сообщения пароль '
                                                              'состоящий из n указанных символов``', inline=False)
        embed1.add_field(name='.decode кодировка',
                         value='``Декодирует  текст в заданной кодировке, чтобы получить список '
                               'доступных кодировок для декодирования - пропишите .decode``',
                         inline=False)
        embed1.add_field(name='.encode кодировка',
                         value='``Кодирует  текст в заданной кодировке, чтобы получить список '
                               'доступных кодировок для кодирования - пропишите .encode``',
                         inline=False)
        embed1.add_field(name='.жб @ содержание\n.warn @ содержание \n.жалоба @ содержание ', value='``Создает и '
                                                                                                    'отправляет в '
                                                                                                    'администраторский чат жалобу на указанного пользователя с указанным содержанием.``')
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681367023561080922/info.gif')
        await ctx.send(embed=embed1)

    @help.command(pass_context=True,
                  aliases=['fun', 'social', 'Fun', 'Social', 'funny', 'Funny', 'соц', 'социальное', 'веселое', 'весел',
                           'фан', 'Соц'])
    async def funnySocial(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Соц/Веселое')
        embed1.add_field(name='.marry @\n.свадьба @', value='``Начинает свадебный процесс с указанным пользователем``',
                         inline=False)
        embed1.add_field(name='.divorce\n.развод', value='``Развестись с тем, на ком вы женаты``', inline=False)
        embed1.add_field(name='.ship @ @\n.шип @ @\n.ебитес @ @', value='``Зашипперить первую указанную персону со второй``',
                         inline=False)
        embed1.add_field(name='.waifu\n.вайфу', value='``Ваш вайфу профиль или другого пользователя при его указании``',
                         inline=False)
        embed1.add_field(name='.gifts\n.подарки', value='``Список подарков для пользователей``',
                         inline=False)
        embed1.add_field(name='.gift @ подарок к-во\n.п @ подарок к-во', value='``Подарить указанному пользователю '
                                                                               'подарок, где атрибуты: подарок - '
                                                                               'название подарка из .gifts, а к-во, '
                                                                               'указанное количество подарка, '
                                                                               'по умолчанию значение количества = '
                                                                               '1``',
                         inline=False)
        embed1.add_field(name='.topwaifu\n.waifutop', value='``Топ вайфу по их исчисляемой подарками стоимости``',
                         inline=False)
        embed1.add_field(name='.urban word', value='``Ищет значение слова на urbandictionary (работает для '
                                                   'английский слов)``',
                         inline=False)
        embed1.add_field(name='.supreme text',
                         value='``Создает ваш логотип, основанный на логотипе компании Supreme. На '
                               'отправленной картинке будет указанный вами атрибут text.``',
                         inline=False)
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681363587264020483/gif_soc.gif')
        await ctx.send(embed=embed1)

    @help.command(pass_context=True,
                  aliases=['Economy', 'economy', 'экономика', 'деньги', 'эконом', 'Экономика', 'эко'])
    async def economycs(self, ctx):
        emoji = self.client.get_emoji(676803534758477845)
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Экономика')
        embed1.add_field(name='.balance $money', value='``sends value of your money``')
        embed1.add_field(name='.daily .дневное',
                         value=f'``Использование только один раз в два часа. Вы получаете 1000``{emoji}', inline=False)
        embed1.add_field(name='.market\n.магазин',
                         value='``Место, где вы можете приобрести роли и не только за валюту``',
                         inline=False)
        embed1.add_field(name='.give @ n\n.send @ n\n.отправить @ n', value='``Снимает и отправляет с вашего счета '
                                                                            'указанному пользователю деньги, где n - их '
                                                                            'количество ``', inline=False)
        embed1.add_field(name='.topmoney', value='``sends users with biggest value of money ``', inline=False)
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681364474086686754/money.gif')
        await ctx.send(embed=embed1)

    @help.command(pass_context=True, aliases=['Reputation', 'репутация', 'Репутация'])
    async def reputation(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Репутация')
        embed1.add_field(name='.rep\n.репутация', value='``Отправляет меню с вашей репутацией``')
        embed1.add_field(name='.addrep @\n+реп @', value='``Добавляет 1 очко репутации``', inline=False)
        embed1.add_field(name='.removerep @\n.-реп @', value='``Убирает 1 очко репутации``', inline=False)
        embed1.add_field(name='.toprep', value='``Топ пользователей по репутации ``', inline=False)
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681365735590985754/repgif.gif')
        await ctx.send(embed=embed1)

    @help.command(pass_context=True,
                  aliases=['Music', 'musik', 'Musik', 'musicc', 'musi', 'Музыка', 'музыка', 'муз', 'музяка', 'Муз'])
    async def music(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Музыка')
        embed1.add_field(name='.join .connect',
                         value='``Тет присоединяется к вам в голосовой канал``',
                         inline=False)
        embed1.add_field(name='.play song_name/url',
                         value='``Запрашивает Тет сыграть указанную вами песню``',
                         inline=False)
        embed1.add_field(name='.skip .s ',
                         value='``Запрашивает Тет пропустить играющую песню в данный момент``',
                         inline=False)
        embed1.add_field(name='.pause .stop',
                         value='``Запрашивает Тет поставить на паузу играющую песню в данный момент``',
                         inline=False)
        embed1.add_field(name='.resume .continue',
                         value='``Запрашивает Тет продолжить играющую песню в данный момент``',
                         inline=False)
        embed1.add_field(name='.np .nowplaying',
                         value='``Запрашивает Тет показать играющую сейчас песню и меню с эмодзи играющую песню в данный момент``',
                         inline=False)
        embed1.add_field(name='.leave .disconnect',
                         value='``Запрашивает Тет выйти из голосового канала``',
                         inline=False)
        embed1.set_image(url='https://cdn.discordapp.com/attachments/420952665124503553/681366857529557173/music.gif')
        await ctx.send(embed=embed1)

    @help.command(pass_context=True,
                  aliases=['Clan', 'clan', 'guild', 'Guild', 'клан', 'Клан'])
    async def _clan(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Помощь Музыка')
        embed1.add_field(name='.guildcreation',
                         value='``Меню создания гильдии, создание гильдии стоит 1000000``',
                         inline=False)
        embed1.add_field(name='.myclan .guildinfo',
                         value='``Информация о гильдии``',
                         inline=False)
        embed1.add_field(name='.setclanimg .setguildimg .clanimg',
                         value='``Устанавливает эмблему гильдии``',
                         inline=False)
        embed1.add_field(name='.clandeposit',
                         value='``Добавляет деньги в казну гильдии``',
                         inline=False)
        embed1.add_field(name='.claninvite @',
                         value='``Приглашает указанного человека в вашу гильдию``',
                         inline=False)
        embed1.add_field(name='.clanskills',
                         value='``Умения гильдии``',
                         inline=False)
        embed1.add_field(name='.clandelete',
                         value='``Удаляет гильдию и всех ее участников из нее``',
                         inline=False)
        await ctx.send(embed=embed1)

    @commands.command(pass_context=True, aliases=['mathematics', 'Math', 'mat', 'matan', 'mathe', 'maths', 'Maths'])
    async def math(self, ctx):
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.set_author(name='Help Math')
        embed1.add_field(name='Trigonometric',
                         value='``$sin # $cos # $tan #\n$sinh # $cosh # $tanh #\n$asin # $acos # $atan #\n$asinh # $acosh # $atanh``')
        embed1.add_field(name='Standart',
                         value='``$sqrt # $factorial #``')
        await ctx.send(embed=embed1)

def setup(client):
    client.add_cog(Help(client))