import discord
import random
import asyncio
import json
from discord.ext import commands

msgend = [":spades:", ":clubs:", ":diamonds:", ":hearts:", ":fleur_de_lis:", ":black_heart:"]


class Emotions(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True, aliases=['цем', 'тьмок', 'поцеловать', 'цом'])
    async def kiss(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedkiss = discord.Embed(
            colour=discord.Colour.dark_purple()
        )
        kissphrases = [f"{author.mention} нежно поцеловал {member.mention} ",
                       f"Губки {author.mention} соприкасаются с губками {member.mention}",
                       f"{author.mention} целует {member.mention}",
                       ]
        kissgifs = ["https://media1.tenor.com/images/896519dafbd82b9b924b575e3076708d/tenor.gif?itemid=8811697",
                    "https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722",
                    "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865",
                    "https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/tenor.gif?itemid=12837192",
                    "https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409",
                    "https://media1.tenor.com/images/e858678426357728038c277598871d6d/tenor.gif?itemid=9903014",
                    "https://media1.tenor.com/images/a1f7d43752168b3c1dbdfb925bda8a33/tenor.gif?itemid=10356314",
                    "https://media1.tenor.com/images/8e0e0c3970262b0b4b30ee6d9eb04756/tenor.gif?itemid=12542720",
                    "https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544",
                    "https://media1.tenor.com/images/c4ecd9b75be67ea56d5916c47ee3ad53/tenor.gif?itemid=14375353",
                    "https://media1.tenor.com/images/d1a11805180742c70339a6bfd7745f8d/tenor.gif?itemid=4883557",
                    "https://media1.tenor.com/images/6bd9c3ba3c06556935a452f0a3679ccf/tenor.gif?itemid=13387677",
                    "https://media1.tenor.com/images/04433eb0c31b175ab020cc9c6b94e1c4/tenor.gif?itemid=14686933",
                    "https://media1.tenor.com/images/d017f04c0383c3c6864d2a2ec414ea3d/tenor.gif?itemid=11293903",
                    "https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515",
                    "https://media1.tenor.com/images/e76e640bbbd4161345f551bb42e6eb13/tenor.gif?itemid=4829336",
                    "https://cdn.discordapp.com/attachments/624296774747553808/637901601209712640/kiss_3.gif",
                    "https://cdn.discordapp.com/attachments/624296774747553808/639093189017600000/21.gif",
                    "https://cdn.discordapp.com/attachments/624296774747553808/639093469121347595/29.gif",
                    "https://cdn.discordapp.com/attachments/621005423335702528/652822580310310924/JPEG_20190513_121707.jpg",
                    "https://cdn.discordapp.com/attachments/621005423335702528/652822932627652619/76_pLn7qnwk.jpg"
                    "https://cdn.discordapp.com/attachments/627524428447612949/655354838716121088/IwStTn6.gif"]
        embedkiss.add_field(name='Поцелуй :kissing_heart:',
                            value=f'{random.choice(kissphrases)} {random.choice(msgend)}')
        embedkiss.set_image(url=random.choice(kissgifs))
        await ctx.send(embed=embedkiss)

    @commands.command(name='idk', aliases=['хз', 'Хз', 'незнаю', 'не знаю'], help=' emotion i donno')
    async def idk(self, ctx):
        author = ctx.message.author
        embedidk = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        idkgifs = ["https://media1.tenor.com/images/7b04c9cdaf8954bb4d304df8f289ab69/tenor.gif?itemid=5252189",
                   "https://media1.tenor.com/images/dbe1ca7fdb532cf96a9bea40fa1f406e/tenor.gif?itemid=9724581",
                   "https://media1.tenor.com/images/229489f89e58f703cc3fddcf01bc9872/tenor.gif?itemid=5481020",
                   "https://media1.tenor.com/images/c8db0c0213c835832785ed2755b283c9/tenor.gif?itemid=5420884",
                   "https://media1.tenor.com/images/0c4a1a27ab665a8e23b69cc40da6c58e/tenor.gif?itemid=15487155",
                   "https://media1.tenor.com/images/aea2b3b7a199c1d5de88f71e7f5a3a95/tenor.gif?itemid=15453847",
                   "https://2static1.fjcdn.com/thumbnails/comments/Idk+lol+i+was+just+posting+smug+anime+faces+_5afa7b8aa9d5b256369566074fb8b8b1.jpg",
                   "https://media1.tenor.com/images/ce441e4f0e6f115e9eb1b321955c1b80/tenor.gif?itemid=5094560"]
        embedidk.add_field(name=" :grey_question: Не знаю :grey_question: ",
                           value=f"{author.mention} даже не знает, как поступить в данной ситуации {random.choice(msgend)}")
        embedidk.set_image(url=random.choice(idkgifs))
        await ctx.send(embed=embedidk)

    @commands.command(name='shy', aliases=['застенчивость', 'стесняюсь', 'стесняшка'], help=' emotion shyness')
    async def shy(self, ctx):
        author = ctx.message.author
        embedshy = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        shygifs = ["https://media1.tenor.com/images/097f46e1db35653902b10b0a322c908f/tenor.gif?itemid=12003933",
                   "https://media.tenor.com/images/a86f09dcfa83c009ff8e4d616224e6d7/tenor.gif",
                   "https://media.tenor.com/images/f942d8d70848555f5914cc3474f7a63f/tenor.gif",
                   "https://media1.tenor.com/images/29b04bfb2aa34a3e896463d1793d5df5/tenor.gif?itemid=5587208",
                   "https://media1.tenor.com/images/71de7826ad02a908a1c3e572f50e6901/tenor.gif?itemid=5755233",
                   "https://media0.giphy.com/media/fARFPMuspJRx6/giphy.gif",
                   "https://66.media.tumblr.com/e54be4de9ce32d5559d6e8339947ba41/tumblr_om3tvg3ZF51v8tshbo1_400.gifv",
                   "https://media1.tenor.com/images/fbcbdbff72bde829a29347bf162e870c/tenor.gif?itemid=3478341",
                   "https://data.whicdn.com/images/272630927/original.gif",
                   "https://media1.tenor.com/images/29b04bfb2aa34a3e896463d1793d5df5/tenor.gif?itemid=5587208",
                   "https://i.pinimg.com/originals/26/26/58/262658b05b19f7fac41ed8f4a39c79bc.gif",
                   "https://thumbs.gfycat.com/SatisfiedYearlyGonolek-size_restricted.gif",
                   "https://data.whicdn.com/images/121443835/original.gif"]
        embedshy.add_field(name=" :grey_question: Застенчивый :grey_question: ",
                           value=f"{author.mention} стесняется {random.choice(msgend)}")
        embedshy.set_image(url=random.choice(shygifs))
        await ctx.send(embed=embedshy)

    @commands.command(name='thinking', aliases=['думаю'], help=' emotion think')
    async def thinking(self, ctx):
        author = ctx.message.author
        embedthink = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        thinkgifs = ["https://media1.tenor.com/images/1ac375ffe6f2e99ac36eb1b42a7b9707/tenor.gif?itemid=13593873",
                     "https://i.pinimg.com/originals/a8/bd/50/a8bd501a4a8994943eba503bdbef68bf.jpg",
                     "https://animemotivation.com/wp-content/uploads/2018/10/anime-girl-curious-thinking.jpg.webp",
                     "https://cdn140.picsart.com/294766366044211.png?r1024x1024",
                     "https://www.pngkey.com/png/detail/315-3152007_png-animuthinku-thinking-meme-face-anime.png",
                     "https://i.pinimg.com/736x/f7/99/02/f7990250a60043abd57e29efd23f7844.jpg",
                     "https://www.vippng.com/png/detail/27-278214_nanothink-discord-emoji-anime-thinking-emoji.png",
                     "https://animemotivation.com/wp-content/uploads/2018/07/Kirino-chiba-thinking.jpg.webp",
                     "https://i.gifer.com/RNCb.gif",
                     "https://media.tenor.com/images/83ab21f684ec5b2325e8f86f6b7d1a85/tenor.gif",
                     "https://i.gifer.com/WaSO.gif",
                     "http://pa1.narvii.com/6763/bc4e8757b14fb6334e5038ee402167ebc0b27173_00.gif",
                     "https://data.whicdn.com/images/324658620/original.gif",
                     "https://i1.wp.com/www.animefeminist.com/wp-content/uploads/2019/06/thinking-hmm-pencil-sailor-moon.gif?fit=500%2C378&ssl=1"]
        embedthink.add_field(name="Thinking :thinking:",
                             value=f"{author.mention} is thinking right now{random.choice(msgend)}")
        embedthink.set_image(url=random.choice(thinkgifs))
        await ctx.send(embed=embedthink)

    @commands.command(name='awoo', help=' emotion awoo')
    async def awoo(self, ctx):
        author = ctx.message.author
        embedawoo = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        gifs = ["https://i.kym-cdn.com/entries/icons/original/000/017/280/e29.jpg",
                "https://thumbs.gfycat.com/QuarterlyThornyArcticwolf-size_restricted.gif",
                "https://pbs.twimg.com/profile_images/1142733438648295424/9qp0laEq_400x400.jpg",
                "https://media1.tenor.com/images/af69b9b021202ab0d736212d982e87d1/tenor.gif?itemid=11713493",
                "https://media1.tenor.com/images/c8716af31ed52ea58729b7c477b56579/tenor.gif?itemid=15386637",
                "https://media1.tenor.com/images/cd755c8bf3f27d3e4a01c3ddbb8dab63/tenor.gif?itemid=13599827"]
        embedawoo.add_field(name="Awoo ",
                            value=f"{author.mention} AWOOOOOO! {random.choice(msgend)}")
        embedawoo.set_image(url=random.choice(gifs))
        await ctx.send(embed=embedawoo)

    @commands.command(name='uwu', help=' emotion uwu')
    async def uwu(self, ctx):
        author = ctx.message.author
        embedUWU = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        gifs = [
            "https://images.discordapp.net/avatars/408785106942164992/7f7a07bfad0ad6a2faaaccd9421e5392.png?size=512",
            "https://qph.fs.quoracdn.net/main-qimg-5fa76a4166d4805b0367ae855d4ed66a",
            "https://www.netclipart.com/pp/m/274-2744132_uwu-anime-girl.png",
            "https://i.ytimg.com/vi/TM6vL7A3wWU/maxresdefault.jpg",
            "https://instagram.fdtm2-1.fna.fbcdn.net/v/t51.2885-15/e35/60961401_118801332690037_6876302812738518969_n.jpg?_nc_ht=instagram.fdtm2-1.fna.fbcdn.net&_nc_cat=101&oh=a8a6051ff3c9dcf9a36150733fbf5cae&oe=5E710DFF&ig_cache_key=MjA2MzEzMDAyNDMyODU4OTk2Mg%3D%3D.2",
            "https://media.tenor.com/images/96c10d9434f330ef10159ede5b1ded33/tenor.png",
            "https://media.tenor.com/images/b25080860e64b852cb697e81fdeb2be3/tenor.gif",
            "https://media1.tenor.com/images/bee9b19480b6fb3ab9429b130e925f3a/tenor.gif?itemid=14822364 "]
        embedUWU.add_field(name=" Uwu ",
                           value=f"{author.mention} UwU ! {random.choice(msgend)}")
        embedUWU.set_image(url=random.choice(gifs))
        await ctx.send(embed=embedUWU)

    @commands.command(name='spy', aliases=['шпионить', 'следить', 'сталкер', 'сталкерить'], help=' emotion spying')
    async def spy(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedspy = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        spygifs = ["https://media.tenor.com/images/8b487fefc640e6b19fbc42e8c82a3d77/tenor.gif",
                   "https://www.pngkey.com/png/detail/128-1283430_154-kb-png-transparent-anime-girl-peeking.png",
                   "https://i.kym-cdn.com/photos/images/newsfeed/001/081/966/694.gif",
                   "https://media1.tenor.com/images/2b7dbc632d8123acaabb462217760929/tenor.gif?itemid=13839451",
                   "https://goboiano.com/wp-content/uploads/2017/01/CF468CC8-29E3-4348-9D93-09F63D2DF358-1-1024x669.jpeg",
                   "https://data.whicdn.com/images/323150143/original.jpg",
                   "https://media2.giphy.com/media/BK8hW6YBpnvSU/giphy.gif?cid=790b761117238377d8b62781b4b863a0a52ae796d14ac785&rid=giphy.gif"]
        embedspy.add_field(name=" Слежка :eyes: ",
                           value=f":detective: {author.mention} очень внимательно наблюдает за {member.mention}{random.choice(msgend)}")
        embedspy.set_image(url=random.choice(spygifs))
        await ctx.send(embed=embedspy)

    @commands.command(name='yawn', aliases=['зевнуть'], help=' yawn emotion ')
    async def yawn(self, ctx):
        author = ctx.message.author
        embedyawn = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        yawngifs = ["https://media1.tenor.com/images/88c38db3ef0da954daa028dfbe1f01e8/tenor.gif?itemid=8722510",
                    "https://media1.tenor.com/images/9cef52ce27ab97e0fa9cfac1cdc1007f/tenor.gif?itemid=9525859",
                    "https://media1.tenor.com/images/259a11c7639b5fb5e77886c8f91c9137/tenor.gif?itemid=14818724",
                    "https://media1.tenor.com/images/35b7e7989f0bb9ec8cdb25ee2b06d973/tenor.gif?itemid=11115658",
                    "https://media1.tenor.com/images/0981aae731d5bd80bdcb40b7982e391e/tenor.gif?itemid=5604306",
                    "https://media1.tenor.com/images/6230c6a994f25608ebc28e769ed95c58/tenor.gif?itemid=12003902",
                    "https://media1.tenor.com/images/9492c8b81b122ba074808a266fdd140a/tenor.gif?itemid=8003684",
                    "https://media1.tenor.com/images/1d1e7db15d733eb56ff0f9c2ee8debbf/tenor.gif?itemid=14495428",
                    "https://media1.tenor.com/images/be2b2293d05a9c93e29b8ec3bdb06b80/tenor.gif?itemid=14325508",
                    "https://media1.tenor.com/images/e668cbabcb96426e83da852cf2f02459/tenor.gif?itemid=14108895",
                    "https://media1.tenor.com/images/cd79f17901eb72d1b410c7205c6d9a9b/tenor.gif?itemid=15006033",
                    "https://media1.tenor.com/images/0057a860ca346c44cbf0efdfd8b15eb0/tenor.gif?itemid=14086687",
                    "https://media1.tenor.com/images/2e91565f921a15960332c4c23a9b4cda/tenor.gif?itemid=7922566",
                    "https://media1.tenor.com/images/46cff5a47ebcb25816ea41bb0b6f497f/tenor.gif?itemid=13451600",
                    "https://media1.tenor.com/images/36e7cd0c53c1909d0ab2195541529243/tenor.gif?itemid=15643415"]
        embedyawn.add_field(name=" Зевание :crescent_moon:  ",
                            value=f"{author.mention} Зевает. Кажется самое время идти спатеньки {random.choice(msgend)}")
        embedyawn.set_image(url=random.choice(yawngifs))
        await ctx.send(embed=embedyawn)

    @commands.command(name='jojo', aliases=['жожо', 'JOJO', 'jj', 'JoJo'], help=' jojo emotion ')
    async def jojo(self, ctx):
        embedyawn = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        yawngifs = ["https://i.gifer.com/DXk1.gif",
                    "https://media.giphy.com/media/f9jxYYRVPHtKsCf9sy/giphy.gif",
                    "https://media1.tenor.com/images/392da4650dfa83b3055069e39ad74b45/tenor.gif?itemid=7319727",
                    "https://i.kym-cdn.com/photos/images/newsfeed/000/977/275/581.gif",
                    "https://thumbs.gfycat.com/ShabbyUnequaledFoal-size_restricted.gif",
                    "https://thumbs.gfycat.com/BrownThoughtfulGnatcatcher-size_restricted.gif",
                    "https://media1.giphy.com/media/11TN3gkseh4Vos/giphy.gif"]
        embedyawn.add_field(name=" JoJo ",
                            value=f"Время JoJo! {random.choice(msgend)}")
        embedyawn.set_image(url=random.choice(yawngifs))
        await ctx.send(embed=embedyawn)

    @commands.command(name='run', aliases=['бежать', 'побег', 'бежим'])
    async def run(self, ctx):
        author = ctx.message.author
        embedrun = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        rungifs = ["https://media.tenor.com/images/2642d327aad2a3289b824162dc5214d8/tenor.gif",
                   "https://media1.tenor.com/images/7ee1a25161f7b4fd7895635405b15711/tenor.gif?itemid=5934110",
                   "https://media1.tenor.com/images/b0669d1a326931d4e81508082de58654/tenor.gif?itemid=11896919",
                   "https://media1.tenor.com/images/b68a3eca610725b8eba6def973229955/tenor.gif?itemid=12374475",
                   "https://media1.tenor.com/images/0a1aaa016c56cd398a28ba745b541ba8/tenor.gif?itemid=11734758",
                   "https://media1.tenor.com/images/c62a8b9e0d0643874d68d09bb2c1f859/tenor.gif?itemid=12546891",
                   "https://media1.tenor.com/images/3df5b4ead18a6b5ecc0d4a7ae1476a74/tenor.gif?itemid=4718145",
                   "https://media1.tenor.com/images/db41d2a91102a4e24df9aa98fe7f97b6/tenor.gif?itemid=15082392",
                   "https://media1.tenor.com/images/e46ccc66b786ecd8cc54189031b56285/tenor.gif?itemid=9715624",
                   "https://media1.tenor.com/images/f108acb2af325bea12b8102a81aa8cc2/tenor.gif?itemid=11506742",
                   "https://media1.tenor.com/images/dffcb724cd274e666c8589a7e57e2915/tenor.gif?itemid=15355808",
                   "https://media1.tenor.com/images/dffcb724cd274e666c8589a7e57e2915/tenor.gif?itemid=15355808",
                   "https://media1.tenor.com/images/b9584605fa97c4d6455ec80a0477eb13/tenor.gif?itemid=14780939",
                   "https://media1.tenor.com/images/17edfb50ba26e75ffa27ba851034d627/tenor.gif?itemid=8737177",
                   "https://media1.tenor.com/images/17edfb50ba26e75ffa27ba851034d627/tenor.gif?itemid=8737177",
                   "https://media1.tenor.com/images/490959e02dd7de0b46a0019f872368a1/tenor.gif?itemid=9523293",
                   "https://media1.tenor.com/images/a688aa7040841b2344a49f521e1b4338/tenor.gif?itemid=15407085"
                   "https://cdn.discordapp.com/attachments/627524428447612949/655360125649027072/tumblr_plj2ilQV3L1u675fso7_400.gif"]
        embedrun.add_field(name='Run', value=f'{author.mention} is running away! {random.choice(msgend)}')
        embedrun.set_image(url=random.choice(rungifs))
        await ctx.send(embed=embedrun)

    @commands.command(name='scared', aliases=['испуг'], help=' emotion when u scare')
    async def scared(self, ctx):
        author = ctx.message.author
        embedscared = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        scaredgifs = ["https://media1.tenor.com/images/5d83670f205d9c84099e7706c19a776a/tenor.gif?itemid=14126066",
                      "https://media1.tenor.com/images/3565384f7d317d10863b140159426d86/tenor.gif?itemid=12136289",
                      "https://media1.tenor.com/images/71f23ded26b2a69caff32fc5b76c7d82/tenor.gif?itemid=6062512",
                      "https://media1.tenor.com/images/33a05b29ac2b6d9be9c8f23ceab06f46/tenor.gif?itemid=9955707",
                      "https://media1.tenor.com/images/ee5951b2fd095750b7fcf37c8ae386be/tenor.gif?itemid=10282001",
                      "https://media1.tenor.com/images/3448e18cdf3171752c60543d252611d3/tenor.gif?itemid=14701398",
                      "https://media1.tenor.com/images/8dcd340eab8e2229229f73234af9eaf2/tenor.gif?itemid=12003900",
                      "https://media1.tenor.com/images/9f3f00c9476ac5f7e96d2361a5ac7a71/tenor.gif?itemid=6102056",
                      "https://media1.tenor.com/images/57e2892ff518e077b3b9f634d72a1c11/tenor.gif?itemid=14086665",
                      "https://media1.tenor.com/images/0528814a721baaf35c6e420d76f36190/tenor.gif?itemid=14086770",
                      "https://media1.tenor.com/images/abb122c5c563d526f10050175249aafa/tenor.gif?itemid=10885923",
                      "https://media1.tenor.com/images/35b9cfb177c5c9c9699083e05ac21568/tenor.gif?itemid=14126061",
                      "https://media1.tenor.com/images/93bf6903a04939b0fbf3afbb2214b551/tenor.gif?itemid=11468244",
                      "https://media1.tenor.com/images/eca53bab25127bdda6179fd32d986d57/tenor.gif?itemid=13451251",
                      "https://media1.tenor.com/images/767f80b3fba5705776926629da6c457e/tenor.gif?itemid=9095356",
                      "https://media1.tenor.com/images/5a333f9e95956c27475c05fd4f92249b/tenor.gif?itemid=14126063",
                      "https://media1.tenor.com/images/cd415a3aab4155a1b1d1046ab51ef397/tenor.gif?itemid=14108960",
                      "https://media1.tenor.com/images/54c057c3792561cce2576c34edcc875d/tenor.gif?itemid=14319979",
                      "https://media1.tenor.com/images/625596b657bfac84e90e0da53f982f8e/tenor.gif?itemid=15171161",
                      "https://media1.tenor.com/images/5f20591b4ce8fafc80bed87df34187b9/tenor.gif?itemid=15411739",
                      "https://media1.tenor.com/images/3f1e2e008b0cf3a0ffd77164fbd9bd9b/tenor.gif?itemid=5945193",
                      "https://media1.tenor.com/images/987466f3cdc9df617fee75e7077f59e7/tenor.gif?itemid=12942769"]
        embedscared.add_field(name='Испуг :cold_sweat: ',
                              value=f'{author.mention} очень сейчас напуган {random.choice(msgend)}')
        embedscared.set_image(url=random.choice(scaredgifs))
        await ctx.send(embed=embedscared)

    @commands.command(name='yandere', aliases=['яндере'], help=' - ')
    async def yandere(self, ctx):
        author = ctx.message.author
        embedyandere = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        yanderegifs = ["https://media1.tenor.com/images/7132e6f39a0e4ada4e33d71056bcde67/tenor.gif?itemid=12858455",
                       "https://media1.tenor.com/images/6d74b0a14b509395c24dd8a43bdfefcf/tenor.gif?itemid=12476875",
                       "https://media1.tenor.com/images/ebd72fadecf1ee92620134820f7041c2/tenor.gif?itemid=5455607",
                       "https://media1.tenor.com/images/f29cb39e3afc48508f377ce59ee65978/tenor.gif?itemid=10167774",
                       "https://media1.tenor.com/images/e07e8466c814c2d872729fe4023541f4/tenor.gif?itemid=12858464",
                       "https://media1.tenor.com/images/9935a3c918b54a487759e12f0691b2a6/tenor.gif?itemid=12858466",
                       "https://media1.tenor.com/images/1ce4f3195a34951af451412f385ec30a/tenor.gif?itemid=12858461",
                       "https://media1.tenor.com/images/b844b8b2d1a4424f1308d13ee24487a5/tenor.gif?itemid=5344617",
                       "https://media1.tenor.com/images/a3e3ce17096ace560058c8c254ab7c86/tenor.gif?itemid=12507777",
                       "https://media1.tenor.com/images/9d64a1ce08da487d468ae7a055729b66/tenor.gif?itemid=14593966",
                       "https://media1.tenor.com/images/9ed18e229bde8a4cd47f1587c887c5ac/tenor.gif?itemid=5428628",
                       "https://media1.tenor.com/images/f3bf85ec59620ba85cf2a6a5e0245571/tenor.gif?itemid=13173092",
                       "https://media1.tenor.com/images/e0ecc5586420e2bff3ef46bcad940745/tenor.gif?itemid=15158440",
                       "https://media1.tenor.com/images/d10f561068060b7175ba14b9ebef409e/tenor.gif?itemid=12174461",
                       "https://media1.tenor.com/images/52c4d55c27725df1b0a35178ad7cbc08/tenor.gif?itemid=10166732"
                       "https://media.tenor.com/images/82b74068ad8e9be8c3a6678b11259c6a/tenor.gif"]

        embedyandere.add_field(name='Режим яндере :smiling_imp: ',
                               value=f'{author.mention} уже в режиме яндере и готовится кого-то кромсать. Бежим!? {random.choice(msgend)}')
        embedyandere.set_image(url=random.choice(yanderegifs))
        await ctx.send(embed=embedyandere)

    @commands.command(name='disgust', aliases=['отврат', 'отвращение', 'отвратительно', 'ужасно', 'фуу'], help=' u did something disgusting ')
    async def disgust(self, ctx):
        author = ctx.message.author
        embeddisg = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        disgustgifs = ["https://images-cdn.9gag.com/photo/aN1GWp6_460s.jpg",
                       "https://img1.ak.crunchyroll.com/i/spire4/fa43415cd93527c994992db17790514a1472151735_full.jpg",
                       "https://media1.tenor.com/images/bab858e36ca9203b7575a0656a925874/tenor.gif?itemid=15052547",
                       "https://media1.tenor.com/images/0b42fed5a4b7ff4e5f9c7680059cf0da/tenor.gif?itemid=11102640",
                       "https://media1.tenor.com/images/cca274cddfbf0890d58838bab680f30b/tenor.gif?itemid=11743477",
                       "https://media1.tenor.com/images/65de4f32280f2fb18577621fc9b7686c/tenor.gif?itemid=10880410"]

        embeddisg.add_field(name='Фу :unamused:  ',
                            value=f'{author.mention} отвратительно !  {random.choice(msgend)}')
        embeddisg.set_image(url=random.choice(disgustgifs))
        await ctx.send(embed=embeddisg)

    @commands.command(name='f', aliases=['F', 'эф', 'ф'], help=' sends random pay respects')
    async def f(self, ctx):
        author = ctx.message.author
        emberf = discord.Embed(
            colour=discord.Colour.dark_purple()
        )
        respectgifs = ["https://media1.tenor.com/images/cd1eaf67e3bf36068a3a9192908b2124/tenor.gif?itemid=14913775",
                       "http://pm1.narvii.com/7179/86f0f16d82c36dc08b824484eb2994a20fbc817br1-640-640v2_uhq.jpg",
                       "https://cs7.pikabu.ru/post_img/2018/08/13/9/1534169483128115826.jpg",
                       "https://cs10.pikabu.ru/post_img/big/2018/08/13/9/1534169515189744448.jpg",
                       "https://cs11.pikabu.ru/images/big_size_comm/2018-04_6/1524725925213024969.jpg",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/8.png",
                       "https://cs10.pikabu.ru/post_img/big/2018/08/13/9/1534169473188366396.jpg",
                       "http://pm1.narvii.com/6924/4f7715a9a0c40ba9dea2db4b0a122c38bbf757b8r1-720-471v2_uhq.jpg",
                       "https://cs9.pikabu.ru/images/big_size_comm/2018-03_3/1520875066153972517.png",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/7.png",
                       "https://i.pinimg.com/originals/38/d2/14/38d214c232f7cc550d15bb915a3af406.gif",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/5.png",
                       "https://nyaa.shikimori.one/system/user_images/original/396559/670495.jpg",
                       "https://desu.shikimori.one/system/user_images/original/59190/563098.jpg",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/12.png",
                       "https://www.meme-arsenal.com/memes/1081ae939a5ca6565cb42b1f83203e02.jpg",
                       "http://chpic.su/_data/stickers/f/FforRespect/FforRespect_013.webp",
                       "https://avatars.mds.yandex.net/get-zen_doc/230865/pub_5c392d68df53e700aa302e8b_5c392e1404bcd000ab92cf35/scale_1200"]
        emberf.add_field(name='F', value=f'{author.mention}  Отдаёт уважение! F ! {random.choice(msgend)}')
        emberf.set_image(url=random.choice(respectgifs))
        await ctx.send(embed=emberf)

    @commands.command(name='F', help=' sends random pay respects')
    async def f(self, ctx):
        author = ctx.message.author
        emberf = discord.Embed(
            colour=discord.Colour.dark_purple()
        )
        respectgifs = ["https://media1.tenor.com/images/cd1eaf67e3bf36068a3a9192908b2124/tenor.gif?itemid=14913775",
                       "http://pm1.narvii.com/7179/86f0f16d82c36dc08b824484eb2994a20fbc817br1-640-640v2_uhq.jpg",
                       "https://cs7.pikabu.ru/post_img/2018/08/13/9/1534169483128115826.jpg",
                       "https://cs10.pikabu.ru/post_img/big/2018/08/13/9/1534169515189744448.jpg",
                       "https://cs11.pikabu.ru/images/big_size_comm/2018-04_6/1524725925213024969.jpg",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/8.png",
                       "https://cs10.pikabu.ru/post_img/big/2018/08/13/9/1534169473188366396.jpg",
                       "http://pm1.narvii.com/6924/4f7715a9a0c40ba9dea2db4b0a122c38bbf757b8r1-720-471v2_uhq.jpg",
                       "https://cs9.pikabu.ru/images/big_size_comm/2018-03_3/1520875066153972517.png",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/7.png",
                       "https://i.pinimg.com/originals/38/d2/14/38d214c232f7cc550d15bb915a3af406.gif",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/5.png",
                       "https://nyaa.shikimori.one/system/user_images/original/396559/670495.jpg",
                       "https://desu.shikimori.one/system/user_images/original/59190/563098.jpg",
                       "https://s.tcdn.co/6d1/469/6d146963-fb36-33f4-b750-61b93b0b799a/12.png",
                       "https://www.meme-arsenal.com/memes/1081ae939a5ca6565cb42b1f83203e02.jpg",
                       "http://chpic.su/_data/stickers/f/FforRespect/FforRespect_013.webp",
                       "https://avatars.mds.yandex.net/get-zen_doc/230865/pub_5c392d68df53e700aa302e8b_5c392e1404bcd000ab92cf35/scale_1200"]
        emberf.add_field(name='F', value=f'{author.mention}  is paying respects! F ! {random.choice(msgend)}')
        emberf.set_image(url=random.choice(respectgifs))
        await ctx.send(embed=emberf)

    @commands.command(name='lewd', aliases=['разврат'], help=' sends random lewd emotion gif')
    async def lewd(self, ctx):
        author = ctx.message.author
        emberlewd = discord.Embed(
            colour=discord.Colour.dark_purple()
        )
        lewdgifs = ["https://media1.tenor.com/images/56053d18fa7261c540c3e84efa62c725/tenor.gif?itemid=13417533",
                    "https://media1.tenor.com/images/1624f26d722662044f50628122aaf8c8/tenor.gif?itemid=9317976",
                    "https://media1.tenor.com/images/4a1a862b67878e74f1492218c1993c53/tenor.gif?itemid=10614031",
                    "https://media1.tenor.com/images/3657bb26403858e3a2051e9aeeb540dd/tenor.gif?itemid=8979689",
                    "https://media1.tenor.com/images/d5c67ed294451a85c88f2d7cc8765059/tenor.gif?itemid=14699108",
                    "https://media1.tenor.com/images/8674cfb928b1055dd6b8227e7e61060b/tenor.gif?itemid=7979947",
                    "https://media1.tenor.com/images/023c6e776cb2191f82afdaa7c012bfc5/tenor.gif?itemid=12370247",
                    "https://media1.tenor.com/images/6b0930740a4780d989f943682f702d67/tenor.gif?itemid=4850240",
                    "https://media1.tenor.com/images/a77cccf7e2c64b6d5e056a505c070afc/tenor.gif?itemid=5453532",
                    "https://media1.tenor.com/images/74601bf35c3f39a0ff11d152c2302387/tenor.gif?itemid=14714624",
                    "https://media1.tenor.com/images/bc2810fc980244dfe6b3f0993eb70486/tenor.gif?itemid=13984951",
                    "https://media1.tenor.com/images/bc2810fc980244dfe6b3f0993eb70486/tenor.gif?itemid=13984951",
                    "https://media1.tenor.com/images/35c810aec65711edad2db9d31d785bb3/tenor.gif?itemid=3777822",
                    "https://media1.tenor.com/images/e533b686983c8a8cad7b8da869337edf/tenor.gif?itemid=13706039",
                    "https://cdn.discordapp.com/attachments/636850117995003906/637900295548174347/AL38.gif",
                    "https://media1.tenor.com/images/c011cbfcd53151ea1ef4d5a2cd03314e/tenor.gif?itemid=7556269"]
        emberlewd.add_field(name='Разврат :heart:', value=f'{author.mention} хочет сделать что-то развратное прямо '
                                                          f'сейчас {random.choice(msgend)}')
        emberlewd.set_image(url=random.choice(lewdgifs))
        await ctx.send(embed=emberlewd)

    @commands.command(name='tickle', aliases=['щекотать'], help='sends random tickle emotion gif')
    async def tickle(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embertickle = discord.Embed(
            colour=discord.Colour.dark_purple()
        )
        ticklegifs = ["https://media1.tenor.com/images/16662667791fc3275c25db595fdf89f8/tenor.gif?itemid=12374065",
                      "https://media1.tenor.com/images/d38554c6e23b86c81f8d4a3764b38912/tenor.gif?itemid=11379131",
                      "https://media1.tenor.com/images/fea79fed0168efcaf1ddfb14d8af1a6d/tenor.gif?itemid=7283507",
                      "https://media1.tenor.com/images/fcbded4ce66ab01317ee009a1aa44404/tenor.gif?itemid=11920137",
                      "https://media1.tenor.com/images/f43da23b4ed0938ce362b0374b88e42c/tenor.gif?itemid=8054679"]
        embertickle.add_field(name='Щекотка',
                              value=f'{author.mention} щекочет {member.mention} {random.choice(msgend)}')
        embertickle.set_image(url=random.choice(ticklegifs))
        await ctx.send(embed=embertickle)

    @commands.command(name='dance', aliases=['танцевать', 'танец'], help='sends random dancing emotion gif')
    async def dance(self, ctx):
        author = ctx.message.author
        embeddance = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        dancegifs = ["https://media1.tenor.com/images/0b39752a9e328237ce09af5f3c379b20/tenor.gif?itemid=12042399",
                     "https://media1.tenor.com/images/9841990160f71767843af6cf08b5502d/tenor.gif?itemid=9251559",
                     "https://media1.tenor.com/images/8fdcda26512797826631511017a11f93/tenor.gif?itemid=9765182",
                     "https://media1.tenor.com/images/e19a05faf32c511572acd08a38bebdd6/tenor.gif?itemid=13973731",
                     "https://media1.tenor.com/images/87cb78672b1f27cabd5b6997bf1e5895/tenor.gif?itemid=5539811",
                     "https://media1.tenor.com/images/35fa4dae9560065a0f647d15df0c7510/tenor.gif?itemid=5205815",
                     "https://media1.tenor.com/images/9ee571803fdbea520d723280a6c2c573/tenor.gif?itemid=15054962",
                     "https://media1.tenor.com/images/788f9d274e39299eb93698ee802ed56b/tenor.gif?itemid=14040294",
                     "https://media1.tenor.com/images/0c54f035a49503c796998003b986a07c/tenor.gif?itemid=14832460",
                     "https://media1.tenor.com/images/96d27057942c34ad7998be45ca930a31/tenor.gif?itemid=13407487",
                     "https://media1.tenor.com/images/766599022416cc0b7b7b1bd2040eb2db/tenor.gif?itemid=12039886",
                     "https://media1.tenor.com/images/078d0df8e8fc0d28533b647326bf8f3d/tenor.gif?itemid=13706721",
                     "https://media1.tenor.com/images/d250c06c34f6961087a83c6fd79d0711/tenor.gif?itemid=4718235",
                     "https://media1.tenor.com/images/366c9d8296b3ee833ba9ce7e440260f8/tenor.gif?itemid=9302339"]
        embeddance.add_field(name='Танец', value=f'{author.mention} Танцует прямо! {random.choice(msgend)}')
        embeddance.set_image(url=random.choice(dancegifs))
        await ctx.send(embed=embeddance)

    @commands.command(name='facepalm', aliases=['рукалицо'], help='sends random facepalm emotion gif')
    async def facepalm(self, ctx):
        author = ctx.message.author
        emberfacepalm = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        facepalmgifs = ["https://media1.tenor.com/images/9d30a11e7978ea3b404d5e48c5966c6b/tenor.gif?itemid=5015289",
                        "https://media1.tenor.com/images/76d2ec47ec76fa36b2fce913331ba7e3/tenor.gif?itemid=5533025",
                        "https://media1.tenor.com/images/43f438c58296dabd4bd71f282987f44c/tenor.gif?itemid=10157360",
                        "https://media1.tenor.com/images/5e29a1db9149211728b22bfd01f88771/tenor.gif?itemid=10336271",
                        "https://media1.tenor.com/images/8d224fe698e128391249e3f31814b38d/tenor.gif?itemid=5948162",
                        "https://media1.tenor.com/images/fa28ce1841f99cc2a2ce470cc642cede/tenor.gif?itemid=5519674",
                        "https://media1.tenor.com/images/b8e234ac4aa6aa64b582895911de2046/tenor.gif?itemid=12411488",
                        "https://media1.tenor.com/images/015b8063c7018c2880e88c6014a0ffaf/tenor.gif?itemid=12168336",
                        "https://media1.tenor.com/images/be96db9b9acfd04fd2f5d890e2c51781/tenor.gif?itemid=14355381",
                        "https://media1.tenor.com/images/375754f9ccdf8ac94146381c06755c09/tenor.gif?itemid=5015299",
                        "https://media1.tenor.com/images/a8d8b605d44eb2441d118f2d0bb976bd/tenor.gif?itemid=14865623",
                        "https://media1.tenor.com/images/5e7f44432181df2ba18f27b9f078545f/tenor.gif?itemid=5897489"]
        emberfacepalm.add_field(name='Рукалицо',
                                value=f'{author.mention} без комментариев...... {random.choice(msgend)}')
        emberfacepalm.set_image(url=random.choice(facepalmgifs))
        await ctx.send(embed=emberfacepalm)

    @commands.command(name='poke', aliases=['тык'], help=' give you chance to poke some1')
    async def poke(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedpoke = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        pokegifs = ["https://media1.tenor.com/images/e8b25e7d069c203ea7f01989f2a0af59/tenor.gif?itemid=12011027",
                    "https://media1.tenor.com/images/3b9cffb5b30236f678fdccf442006a43/tenor.gif?itemid=7739077",
                    "https://media1.tenor.com/images/1236e0d70c6ee3ea91d414bcaf9f3aa4/tenor.gif?itemid=5015314",
                    "https://media1.tenor.com/images/175cc4686c4c67809f48eef44965c845/tenor.gif?itemid=10217135",
                    "https://media1.tenor.com/images/175cc4686c4c67809f48eef44965c845/tenor.gif?itemid=10217135",
                    "https://media1.tenor.com/images/8fe23ec8e2c5e44964e5c11983ff6f41/tenor.gif?itemid=5600215",
                    "https://media1.tenor.com/images/90f68d48795c51222c60afc7239c930c/tenor.gif?itemid=8701034",
                    "https://media1.tenor.com/images/ab936c887562756472f83850426bf6ef/tenor.gif?itemid=11956062",
                    "https://media1.tenor.com/images/1ae62716935f12e0cf26ada43fcb1916/tenor.gif?itemid=13190374",
                    "https://media1.tenor.com/images/1e0ea8b241a7db2b9c03775133138733/tenor.gif?itemid=10064326",
                    "https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763",
                    "https://media1.tenor.com/images/76e377271bf00ba61d954b2752713596/tenor.gif?itemid=5075308",
                    "https://media1.tenor.com/images/702fd09287bbf8a907de7d1961d950e3/tenor.gif?itemid=11710639",
                    "https://media1.tenor.com/images/1a64ac660387543c5b779ba1d7da2c9e/tenor.gif?itemid=12396068",
                    "https://media1.tenor.com/images/514efe749cb611eb382713596e3427d8/tenor.gif?itemid=13054528",
                    "https://media1.tenor.com/images/d9b55173939b863da320ddba91e13b91/tenor.gif?itemid=15148498",
                    "https://media1.tenor.com/images/2b55eb1befce3e843dec7e8feebf274b/tenor.gif?itemid=10168199"]
        embedpoke.add_field(name='Тык :point_up_2: ',
                            value=f'{author.mention} тыкает в {member.mention} {random.choice(msgend)}')
        embedpoke.set_image(url=random.choice(pokegifs))
        await ctx.send(embed=embedpoke)

    @commands.command(name='hug', aliases=['Обнять', 'обнять', 'обнимашки'], help=' sends random hugs emotion gif')
    async def hug(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        emberhug = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        huggifs = ["https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978",
                   "https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
                   "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093",
                   "https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705",
                   "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
                   "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
                   "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
                   "https://media1.tenor.com/images/074d69c5afcc89f3f879ca473e003af2/tenor.gif?itemid=4898650",
                   "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
                   "https://media1.tenor.com/images/18474dc6afa97cef50ad53cf84e37d08/tenor.gif?itemid=12375072",
                   "https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
                   "https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
                   "https://media1.tenor.com/images/44b4b9d5e6b4d806b6bcde2fd28a75ff/tenor.gif?itemid=9383138",
                   "https://media1.tenor.com/images/45b1dd9eaace572a65a305807cfaec9f/tenor.gif?itemid=6238016",
                   "https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif?itemid=9882931",
                   "https://media1.tenor.com/images/79c461726e53ee8f9a5a36521f69d737/tenor.gif?itemid=13221416",
                   "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif?itemid=3532079",
                   "https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif?itemid=14721541",
                   "https://media1.tenor.com/images/f2805f274471676c96aff2bc9fbedd70/tenor.gif?itemid=7552077",
                   "https://media1.tenor.com/images/aeb42019b0409b98aed663f35b613828/tenor.gif?itemid=14108949",
                   "https://media1.tenor.com/images/09005550fb8642d13e544d2045a409c5/tenor.gif?itemid=7883854",
                   "https://media1.tenor.com/images/4ebdcd44de0042eb416345a50c3f80c7/tenor.gif?itemid=6155660",
                   "https://media1.tenor.com/images/1a73e11ad8afd9b13c7f9f9bb5c9a834/tenor.gif?itemid=13366388",
                   "https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774",
                   "https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif?itemid=9375012",
                   "https://cdn.discordapp.com/attachments/636850117995003906/637911833205932032/KHdSnNKk7.gif",
                   "https://cdn.discordapp.com/attachments/636850117995003906/637927282077466645/AL119.gif",
                   "https://cdn.discordapp.com/attachments/624296774747553808/639093222844399632/22.gif",
                   "https://cdn.discordapp.com/attachments/626362221957742602/639754461044015104/rkIK_u7Pb.gif",
                   "https://cdn.discordapp.com/attachments/621005423335702528/652823412518944791/3ZRdtZ3Ykjg.jpg"]
        emberhug.add_field(name='Объятия',
                           value=f'{author.mention}, обнимает {member.mention} {random.choice(msgend)}')
        emberhug.set_image(url=random.choice(huggifs))
        await ctx.send(embed=emberhug)

    @commands.command(name='smug', help=' sends random smug emotion gif')
    async def smug(self, ctx):
        author = ctx.message.author
        embedsmug = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        smuggifs = ["https://media1.tenor.com/images/1fe93596a8a0f84078b936305b319c55/tenor.gif?itemid=6194051",
                    "https://media1.tenor.com/images/76f7160c04d244a5f34d77d25122344e/tenor.gif?itemid=13598613",
                    "https://media1.tenor.com/images/ea2e6ec351e238d8e8bd624b3738a9b3/tenor.gif?itemid=14210719",
                    "https://media1.tenor.com/images/e8ba11ae8c4cb5ac28b0408404d02e1f/tenor.gif?itemid=11737574",
                    "https://media1.tenor.com/images/ad4804e880c2edcecbb79217b479610a/tenor.gif?itemid=10903422",
                    "https://media1.tenor.com/images/8bf3267e5f0a00eef84f9fbb6ac4ac1b/tenor.gif?itemid=13119038",
                    "https://media1.tenor.com/images/203773e8dd695b64b9cb5caf90653f30/tenor.gif?itemid=13909640",
                    "https://media1.tenor.com/images/daa1824574947530e1a86fd4f0b74761/tenor.gif?itemid=13940350",
                    "https://media1.tenor.com/images/7ad6d97772f86111611ff91532dbbd31/tenor.gif?itemid=15168575",
                    "https://media1.tenor.com/images/906bbc85a7820f68a7fc658aeeceb069/tenor.gif?itemid=10195728",
                    "https://media1.tenor.com/images/f9b7309b23cb2071f5ed70e1e33c73b5/tenor.gif?itemid=10059356",
                    "https://media1.tenor.com/images/58899ca7e0ffa4a785ad23ccda01e082/tenor.gif?itemid=13979455",
                    "https://media1.tenor.com/images/7db79599821506dc65fee1285f8263a6/tenor.gif?itemid=15157923",
                    "https://media1.tenor.com/images/0c3c1c1394c9ab4f455873a4336aa3e6/tenor.gif?itemid=11146587",
                    "https://media1.tenor.com/images/ca9adeb8e53c5fa7e3c705ea60df2f14/tenor.gif?itemid=15157933",
                    "https://media1.tenor.com/images/30df9ebfc55b7b65aff9c7df41ed5f32/tenor.gif?itemid=10199270",
                    "https://media1.tenor.com/images/9a9fdf3ff9da386e85e722654ccc6f8c/tenor.gif?itemid=13451416",
                    "https://cdn.discordapp.com/attachments/636850117995003906/637907272466432011/AL48.gif",
                    "https://cdn.discordapp.com/attachments/621005423335702528/652823857631068160/1qrD_1slC4E.jpg"]
        embedsmug.add_field(name='Smug', value=f'{author.mention} is smugging now. {random.choice(msgend)} ')
        embedsmug.set_image(url=random.choice(smuggifs))
        await ctx.send(embed=embedsmug)

    @commands.command(name='wink', aliases=['подмигнуть', 'мигнуть', 'подмигивать'],
                      help=' sends random wink emotion gif')
    async def wink(self, ctx):
        author = ctx.message.author
        embedwink = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        winkgifs = ["https://media1.tenor.com/images/b944f6101ecc78ac4164e51439d1f686/tenor.gif?itemid=6181830",
                    "https://media1.tenor.com/images/61efdb0459289dda96a3871f4f575987/tenor.gif?itemid=12188360",
                    "https://media1.tenor.com/images/5f6611a1a9248581e99bbd4698b5d872/tenor.gif?itemid=14379355",
                    "https://media1.tenor.com/images/d910e620d5956cc60eb8db21fb2beca8/tenor.gif?itemid=14683647",
                    "https://media1.tenor.com/images/922399d5cae85e03fccefcdd0f7bef59/tenor.gif?itemid=5316207",
                    "https://media1.tenor.com/images/513cc772fb1557212495c47b104bbf78/tenor.gif?itemid=12010861",
                    "https://media1.tenor.com/images/68d9ab65ee90c04f7e7a26f8ff80c371/tenor.gif?itemid=4434924",
                    "https://media1.tenor.com/images/c554aac83978470c0680543107af4b6d/tenor.gif?itemid=12244993",
                    "https://media1.tenor.com/images/eef68c65a33d9aa0bc694feb25fde028/tenor.gif?itemid=14721865",
                    "https://media1.tenor.com/images/00064e9fb65a5db0217f05b4c67bd96a/tenor.gif?itemid=15157914",
                    "https://media1.tenor.com/images/3fe61527e247ce69d64e66c2dc618a37/tenor.gif?itemid=13901666",
                    "https://media1.tenor.com/images/0c61003325f1c206fa9c34078d64176b/tenor.gif?itemid=14859809",
                    "https://media1.tenor.com/images/9c1dc7af4390583e2ca0969df07378f8/tenor.gif?itemid=14117807",
                    "https://media1.tenor.com/images/179c544bcd673597deadbe7b5d1c513c/tenor.gif?itemid=9404055",
                    "https://media1.tenor.com/images/8080153a2e36460f481e379a8e0c49b2/tenor.gif?itemid=5213500",
                    "https://media1.tenor.com/images/e200e9b483fe3c4354d322858b5d4f43/tenor.gif?itemid=11001067",
                    "https://media1.tenor.com/images/513cc772fb1557212495c47b104bbf78/tenor.gif?itemid=12010861",
                    "https://media1.tenor.com/images/aa90b55c867c2e5f13f9d413aba5b6d9/tenor.gif?itemid=5205821",
                    "https://media1.tenor.com/images/56a280ec436c043110ef936d54e25464/tenor.gif?itemid=5115897",
                    "https://media1.tenor.com/images/970cc51d80dddd48f8ab95def08d07a1/tenor.gif?itemid=11824933",
                    "https://media1.tenor.com/images/2748bbc004420e452756658376c24898/tenor.gif?itemid=13911445",
                    "https://media1.tenor.com/images/c684461fdac1c40a4d5d2175ba2d47b3/tenor.gif?itemid=14065050",
                    "https://media1.tenor.com/images/6215f430abae2c62cb197ef9fd154699/tenor.gif?itemid=9441397",
                    "https://media1.tenor.com/images/26268ba4d1f70e63c8252ef1c944fd1c/tenor.gif?itemid=14483849"]
        embedwink.add_field(name='Подмигивание :wink:', value=f'{author.mention} подмигнул {random.choice(msgend)}')
        embedwink.set_image(url=random.choice(winkgifs))
        await ctx.send(embed=embedwink)

    @commands.command(name='pat', aliases=['гладить', 'погладить'], help=' sends random pat emotion gif. PAT THE LOLI!')
    async def pat(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedpat = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        patgifs = ["https://media1.tenor.com/images/f330c520a8dfa461130a799faca13c7e/tenor.gif?itemid=13911345",
                   "https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819",
                   "https://media1.tenor.com/images/daa885ec8a9cfa4107eb966df05ba260/tenor.gif?itemid=13792462",
                   "https://media1.tenor.com/images/c0bcaeaa785a6bdf1fae82ecac65d0cc/tenor.gif?itemid=7453915",
                   "https://media1.tenor.com/images/d9b480bcd392d05426ae6150e986bbf0/tenor.gif?itemid=9332926",
                   "https://media1.tenor.com/images/857aef7553857b812808a355f31bbd1f/tenor.gif?itemid=13576017",
                   "https://media1.tenor.com/images/c61cc63503c21c8e69452639f068ad7f/tenor.gif?itemid=15402635",
                   "https://media1.tenor.com/images/f5176d4c5cbb776e85af5dcc5eea59be/tenor.gif?itemid=5081286",
                   "https://media1.tenor.com/images/13f385a3442ac5b513a0fa8e8d805567/tenor.gif?itemid=13857199",
                   "https://media1.tenor.com/images/61187dd8c7985c443bf9cd39bc310c02/tenor.gif?itemid=12018805",
                   "https://media1.tenor.com/images/291ea37382e1d6cd33349c50a398b6b9/tenor.gif?itemid=10204936",
                   "https://media1.tenor.com/images/71e74263a48a6e9a2c53f3bc1439c3ac/tenor.gif?itemid=12434286",
                   "https://media1.tenor.com/images/266e5f9bcb3f3aa87ba39526ee202476/tenor.gif?itemid=5518317",
                   "https://media1.tenor.com/images/54722063c802bac30d928db3bf3cc3b4/tenor.gif?itemid=8841561",
                   "https://media1.tenor.com/images/bf646b7164b76efe82502993ee530c78/tenor.gif?itemid=7394758",
                   "https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057",
                   "https://media1.tenor.com/images/005e8df693c0f59e442b0bf95c22d0f5/tenor.gif?itemid=10947495",
                   "https://media1.tenor.com/images/28f4f29de42f03f66fb17c5621e7bedf/tenor.gif?itemid=8659513",
                   "https://media1.tenor.com/images/64d45ee51ea8d55760c81a93353ffdb3/tenor.gif?itemid=11179299",
                   "https://media1.tenor.com/images/70960e87fb9454df6a1d15c96c9ad955/tenor.gif?itemid=10092582",
                   "https://media1.tenor.com/images/098a45951c569edc25ea744135f97ccf/tenor.gif?itemid=10895868",
                   "https://media1.tenor.com/images/ebd15359a3ae53d50a35055d79d325c9/tenor.gif?itemid=12018845",
                   "https://media1.tenor.com/images/2cf1704769d0227c69ebc4b6c85e274b/tenor.gif?itemid=10468802",
                   "https://media1.tenor.com/images/220babfd5f8b629cc16399497ed9dd96/tenor.gif?itemid=6130861"]
        embedpat.add_field(name='Поглаживание',
                           value=f'{author.mention} нежно поглаживает {member.mention} {random.choice(msgend)}')
        embedpat.set_image(url=random.choice(patgifs))
        await ctx.send(embed=embedpat)

    @commands.command(name='nyan', aliases=['ня'], help=' sends random nyan emotion gif')
    async def nyan(self, ctx):
        author = ctx.message.author
        embednyan = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        nyangifs = ["https://media1.tenor.com/images/a23b46af1e8c0235d074075c37563f5d/tenor.gif?itemid=8123170",
                    "https://media1.tenor.com/images/87578d840386d60a5b98e28a0cd44b71/tenor.gif?itemid=8774326",
                    "https://media1.tenor.com/images/ab609ea6656d39eb940432c3f9337e33/tenor.gif?itemid=11283817",
                    "https://media1.tenor.com/images/b1b11854eb22c004db882440b26aec5f/tenor.gif?itemid=5015269",
                    "https://media1.tenor.com/images/2e028a001a10bae55cd1cb90c9034734/tenor.gif?itemid=10083618",
                    "https://media1.tenor.com/images/9a17de9ae7f4432e7ff614056f7b567e/tenor.gif?itemid=14002194",
                    "https://media1.tenor.com/images/b5397d5803883e7d4a4b355d068a7375/tenor.gif?itemid=14223397",
                    "https://media1.tenor.com/images/1fc08d836800698d3e936308ce0c08f7/tenor.gif?itemid=5076489",
                    "https://media1.tenor.com/images/6372eb4432bb604cdcf4cd228206d0d7/tenor.gif?itemid=14770476"]
        embednyan.add_field(name='Ня :cat:',
                            value=f' Мяу! {author.mention} теперь очень похож(а) на кошку! {random.choice(msgend)}')
        embednyan.set_image(url=random.choice(nyangifs))
        await ctx.send(embed=embednyan)

    @commands.command(name='handhold', aliases=['Бр', 'бр'], help=' sends random handhold emotion gif')
    async def handhold(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        author = ctx.message.author
        embedhandhold = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        handholdgifs = ["https://media1.tenor.com/images/fe71f12b1afc83e5d351d6b6aefeeb45/tenor.gif?itemid=5695919",
                        "https://media1.tenor.com/images/a341e4d663412d93ec242ec5e555b382/tenor.gif?itemid=14833997",
                        "https://media1.tenor.com/images/d3c5561f3850d35ec5535dac4de2aa59/tenor.gif?itemid=5372737",
                        "https://media1.tenor.com/images/890c34d3b8a85bf1972c0a73dbd56ea8/tenor.gif?itemid=7384775",
                        "https://media1.tenor.com/images/9e375f33e538a944072598ecca5c2ec3/tenor.gif?itemid=14709525",
                        "https://media1.tenor.com/images/f5f58ab712a3b1015c7d034adcdd1ca1/tenor.gif?itemid=4828319"]
        embedhandhold.add_field(name='Держимся за ручки',
                                value=f'{author.mention}  держит за руки {member.mention} {random.choice(msgend)}')
        embedhandhold.set_image(url=random.choice(handholdgifs))
        await ctx.send(embed=embedhandhold)

    @commands.command(name='blush', aliases=['смущение'], help=' sends random blush emotion gif')
    async def blush(self, ctx):
        author = ctx.message.author
        embedblush = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        blushgifs = ["https://media1.tenor.com/images/3ce5d6af434f62cc185590e8f84f4d53/tenor.gif?itemid=8668069",
                     "https://media1.tenor.com/images/84307582253a96e4552d20e3ecef3a33/tenor.gif?itemid=5531498"
                     "https://media1.tenor.com/images/a7e87466022015e036c06c3927c251f9/tenor.gif?itemid=8971744",
                     "https://media1.tenor.com/images/09d75740089598b54342df3641dbbffc/tenor.gif?itemid=5615361",
                     "https://media1.tenor.com/images/b00fe041997afa8fff0734a1fb8dd2a4/tenor.gif?itemid=13768377",
                     "https://media1.tenor.com/images/1bb57bb553ea96c150ab167e145f9a66/tenor.gif?itemid=4964136",
                     "https://media1.tenor.com/images/82b0f0a24e1621510b1216317edd4ba0/tenor.gif?itemid=14119517",
                     "https://media1.tenor.com/images/b4ebe6c9c4786dd32b51dd346135b625/tenor.gif?itemid=5881549",
                     "https://media1.tenor.com/images/95d627e71466ebfb2a168a041c96f122/tenor.gif?itemid=13720542",
                     "https://media1.tenor.com/images/4f270d2727e514056ae63f155ba0cef2/tenor.gif?itemid=13045709",
                     "https://media1.tenor.com/images/d9b08d9984e694111ba7107c198f85b7/tenor.gif?itemid=5634600",
                     "https://media1.tenor.com/images/9af8d8afab3b509a97f2440562845682/tenor.gif?itemid=13978385",
                     "https://media1.tenor.com/images/dc917566da214fa3c4e7ddcc58228db9/tenor.gif?itemid=3554995",
                     "https://media1.tenor.com/images/fc6b82c2c8c045a0b1e6fc91294292c5/tenor.gif?itemid=6215889",
                     "https://media1.tenor.com/images/721f47c4e76756bf2f43a3877aa8da2d/tenor.gif?itemid=13159553",
                     "https://media1.tenor.com/images/620727ea2684887e9ce44e507ac6ce20/tenor.gif?itemid=7511484",
                     "https://media1.tenor.com/images/5ea40ca0d6544dbf9c0074542810e149/tenor.gif?itemid=14841901",
                     "https://media1.tenor.com/images/9237c406b776020e897c58123b1ba001/tenor.gif?itemid=12869776",
                     "https://media1.tenor.com/images/ac2f1f727d4d96a6a7c4fb5ae5a41cf0/tenor.gif?itemid=12297830",
                     "https://media1.tenor.com/images/cc187b06f246e71b07613e3957d87e00/tenor.gif?itemid=5102126",
                     "https://media1.tenor.com/images/917f92a579076c08057a0a8cb69bf62d/tenor.gif?itemid=4436427",
                     "https://media1.tenor.com/images/dd96da2dd884e3d3c684633914d99a14/tenor.gif?itemid=5674419",
                     "https://media1.tenor.com/images/a3376886916bada6736bcc6435d6d279/tenor.gif?itemid=14047158",
                     "https://media1.tenor.com/images/8f76f034ccc458bd09675c0380f59cb7/tenor.gif?itemid=5634589"]
        embedblush.add_field(name='Смущение :blush:', value=f'{author.mention} очень смущен(а) {random.choice(msgend)}')
        embedblush.set_image(url=random.choice(blushgifs))
        await ctx.send(embed=embedblush)

    @commands.command(name='punch', aliases=['ударить', 'пиздануть', 'удар'], help=' sends random punch emotion gif')
    async def punch(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        punchphrases = [" совсей силы ударяет ",
                        " хорошенько ударил ",
                        " зарядил по лицу "]

        embedpunch = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        punchgifs = ["https://media1.tenor.com/images/1c986c555ed0b645670596d978c88f6e/tenor.gif?itemid=13142581",
                     "https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446",
                     "https://media1.tenor.com/images/d7c30e46a937aaade4d7bc20eb09339b/tenor.gif?itemid=12003970",
                     "https://media1.tenor.com/images/c621075def6ca41785ef4aaea20cc3a2/tenor.gif?itemid=7679409",
                     "https://media1.tenor.com/images/6d77cf1fdaa2e7c6a32c370240a7b77c/tenor.gif?itemid=9523306",
                     "https://media1.tenor.com/images/965fabbfcdc09ee0eb4d697e25509f34/tenor.gif?itemid=7380310 ",
                     "https://media1.tenor.com/images/745d16a823805edbfe83aa9363c48a87/tenor.gif?itemid=12003981",
                     "https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif?itemid=13785833",
                     "https://media1.tenor.com/images/7d43687195b86c8ce2411484eb1951fc/tenor.gif?itemid=7922533",
                     "https://media1.tenor.com/images/6afcfbc435b698fa5ceb2ff019718e6d/tenor.gif?itemid=10480971",
                     "https://media1.tenor.com/images/b82427b0507d43afb17a6c9ddddfa0a9/tenor.gif?itemid=4903584",
                     "https://media1.tenor.com/images/995c766275e66c3aa5efd55ab7d8f86a/tenor.gif?itemid=7885164",
                     "https://media1.tenor.com/images/cf467247b8755bcb943dc535ccfd1830/tenor.gif?itemid=9753290",
                     "https://media1.tenor.com/images/29ecede6bfa61d6a2fbfb4b63620cdb4/tenor.gif?itemid=14613404",
                     "https://media1.tenor.com/images/d37431cbc9bd68eca0d700c787bf33d0/tenor.gif?itemid=5521090",
                     "https://media1.tenor.com/images/d7d52d0592bbc77bd5c629c2132c1b33/tenor.gif?itemid=9409159",
                     "https://media1.tenor.com/images/313bb02914ddb9262511b790ef4d4c7b/tenor.gif?itemid=7922535",
                     "https://cdn.discordapp.com/attachments/624296774747553808/639094165732589580/30.gif",
                     "https://cdn.discordapp.com/attachments/624296774747553808/639094187903680522/31.gif",
                     "https://pa1.narvii.com/6329/041aa0724fb6e5dbf71681a80b86d5d1add8f8c8_hq.gif"]
        embedpunch.add_field(name='Punch :punch:',
                             value=f'{author.mention} {random.choice(punchphrases)} {member.mention} {random.choice(msgend)}')
        embedpunch.set_image(url=random.choice(punchgifs))
        await ctx.send(embed=embedpunch)

    @commands.command(name='cry', aliases=['плак', 'плакать'], help=' sends random crying emotion gif')
    async def cry(self, ctx):
        author = ctx.message.author
        embedcry = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        crygifs = ["https://media1.tenor.com/images/26b0be070060011fb69dcb6df838e15e/tenor.gif?itemid=10207002",
                   "https://media1.tenor.com/images/4f22255d60f3f19edf9296992b4e3483/tenor.gif?itemid=4772697",
                   "https://media1.tenor.com/images/4b5e9867209d7b1712607958e01a80f1/tenor.gif?itemid=5298257",
                   "https://media1.tenor.com/images/f7fde4b118501c8fa5cb1a5dd171beab/tenor.gif?itemid=5652242",
                   "https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif?itemid=5648908",
                   "https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296",
                   "https://media1.tenor.com/images/8f6da405119d24f7f86ff036d02c2fd4/tenor.gif?itemid=5378935",
                   "https://media1.tenor.com/images/de730b51400ed4dfb66d04141ea79a2d/tenor.gif?itemid=7353410",
                   "https://media1.tenor.com/images/7ef999b077acd6ebef92afc34690097e/tenor.gif?itemid=10893043",
                   "https://media1.tenor.com/images/f5ec64b40d2adf7deb84e3c0e192ff32/tenor.gif?itemid=6194053",
                   "https://media1.tenor.com/images/2fb2965acbf3ed573e8b63080b947fe5/tenor.gif?itemid=5091716",
                   "https://media1.tenor.com/images/213ec50caaf02d27d358363016204d1d/tenor.gif?itemid=4553386",
                   "https://media1.tenor.com/images/031c7c348d3b86296976e2407723d4a8/tenor.gif?itemid=5014031",
                   "https://media1.tenor.com/images/8f6da405119d24f7f86ff036d02c2fd4/tenor.gif?itemid=5378935",
                   "https://media1.tenor.com/images/8f6da405119d24f7f86ff036d02c2fd4/tenor.gif?itemid=5378935",
                   "https://media1.tenor.com/images/d5668af606ca4d0332a6507418cabbce/tenor.gif?itemid=4952249",
                   "https://media1.tenor.com/images/26e7564bfb4408f9f7ff9518d4f87308/tenor.gif?itemid=8199739",
                   "https://media1.tenor.com/images/a53f4017a15753ff10e42770e89ce1d0/tenor.gif?itemid=4555995",
                   "https://media1.tenor.com/images/75edc9882e5175f86c2af777ffbb14a6/tenor.gif?itemid=5755232   ",
                   "https://media1.tenor.com/images/b88fa314f0f172832a5f41fce111f359/tenor.gif?itemid=13356071",
                   "https://media1.tenor.com/images/b0f4b5f158e8a964adbabd048fb9e556/tenor.gif?itemid=13949015",
                   "https://media1.tenor.com/images/180ece0e4a1656131513bcc60afeec81/tenor.gif?itemid=5081292",
                   "https://cdn.discordapp.com/attachments/621005423335702528/640101063839580178/0caba0318aa667572c0ae30f34ecf8b62896aee5_hq.gif",
                   "https://media1.tenor.com/images/b0a1fe4f451dd918f3961e23f5abad30/tenor.gif?itemid=15391370",
                   "https://media1.tenor.com/images/59ce331b098f5ff48a6a628530cea549/tenor.gif?itemid=13241912"]
        embedcry.add_field(name='Слёзы :sob:',
                           value=f'{author.mention} сейчас плачет. Обнимашек, пожалуйста!{random.choice(msgend)}')
        embedcry.set_image(url=random.choice(crygifs))
        await ctx.send(embed=embedcry)

    @commands.command(name='offend', aliases=['обидеться', 'обижен', 'обида'], help=' sends random offend emotion gif')
    async def offend(self, ctx):
        author = ctx.message.author
        embedoffend = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        offendgifs = ["https://cdn.discordapp.com/attachments/624296774747553808/637928724662321152/offended.gif",
                      "https://cdn.discordapp.com/attachments/624296774747553808/637929414348374026/offend2.gif",
                      "https://cdn.discordapp.com/attachments/624296774747553808/637929458103484416/offend4.gif",
                      "https://cdn.discordapp.com/attachments/624296774747553808/637929435055652874/offend3.gif",
                      "https://cdn.discordapp.com/attachments/621005423335702528/652823784616624148/p83C3Xsw_AA.jpg"]
        embedoffend.add_field(name='Обидка', value=f'{author.mention} сейчас обижен(а) {random.choice(msgend)}')
        embedoffend.set_image(url=random.choice(offendgifs))
        await ctx.send(embed=embedoffend)

    @commands.command(name='spank', aliases=['шлеп', 'шлепнуть'], help=' sends random spank emotion gif')
    async def spank(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedspank = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        spankgifs = ["https://media1.tenor.com/images/7945b3b2ecf0e7c38bc0fb554e998e35/tenor.gif?itemid=12388311",
                     "https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
                     "https://media1.tenor.com/images/d0f32f61c2964999b344c6846b30e1d6/tenor.gif?itemid=13665166",
                     "https://media1.tenor.com/images/27d084ea80cf3f678bb35e0819455d72/tenor.gif?itemid=9772233",
                     "https://media1.tenor.com/images/39985ebdf8087545cc84359b0e3fa0e7/tenor.gif?itemid=13838799",
                     "https://media1.tenor.com/images/5529ad77a3627b0b9e27de8753219690/tenor.gif?itemid=7885617",
                     "https://media1.tenor.com/images/693afd5812160c00a1fa8582de15a83e/tenor.gif?itemid=5458569",
                     "https://media1.tenor.com/images/6b3dda2e995a02ad50ae788a16bfbd64/tenor.gif?itemid=12325914",
                     "https://media1.tenor.com/images/31d58e53313dc9bbd6435d824d2a5933/tenor.gif?itemid=11756736"
                     "https://cdn.discordapp.com/attachments/627524428447612949/655356337005527041/MsR2.gif"]
        embedspank.add_field(name='Шлёп',
                               value=f'{author.mention} шлепает {member.mention} {random.choice(msgend)}')
        embedspank.set_image(url=random.choice(spankgifs))
        await ctx.send(embed=embedspank)

    @commands.command(name='laugh', aliases=['лол', 'смех'], help=' sends random laugh emotion gif')
    async def laugh(self, ctx):
        author = ctx.message.author
        embedlaugh = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        laughgifs = ["https://media1.tenor.com/images/65d8ed7d9f6121c3747f91f4d16ddc20/tenor.gif?itemid=14080522",
                     "https://media1.tenor.com/images/ad4804e880c2edcecbb79217b479610a/tenor.gif?itemid=10903422",
                     "https://media1.tenor.com/images/60752436c762fd710643cffec01f6cbd/tenor.gif?itemid=9051310",
                     "https://media1.tenor.com/images/ccf51fb7683192a9b909d7c8116cc6da/tenor.gif?itemid=11115623",
                     "https://media1.tenor.com/images/cec591b860ddf5447dba64008127309b/tenor.gif?itemid=12048187",
                     "https://media1.tenor.com/images/2775948586d6a24811726ce4dc681d47/tenor.gif?itemid=13786657",
                     "https://media1.tenor.com/images/c4f2a0b13086d0c4a3b66845c85f9020/tenor.gif?itemid=11987904",
                     "https://media1.tenor.com/images/6d7008706bd15d1ed1dc47387f02f853/tenor.gif?itemid=10665609",
                     "https://media1.tenor.com/images/182f3e1d1fc398d0ea99c9433a4f0c65/tenor.gif?itemid=12130183",
                     "https://media1.tenor.com/images/26df2182fc943676dc6cc51371efc04b/tenor.gif?itemid=8932912",
                     "https://media1.tenor.com/images/3be8aa0228169cf5748e21eb972ffa1d/tenor.gif?itemid=12252557",
                     "https://media1.tenor.com/images/2dcfc6694bb1a931c60bb67a6323e40d/tenor.gif?itemid=10067925",
                     "https://media1.tenor.com/images/f7d0b534e95c24a53b9767b480e76df3/tenor.gif?itemid=11203476",
                     "https://media1.tenor.com/images/de9deca0d39e158c3d13d42f511d8013/tenor.gif?itemid=14088527",
                     "https://media1.tenor.com/images/76a775a3b063f589af8c05c26316a1cb/tenor.gif?itemid=10191158",
                     "https://media1.tenor.com/images/faebec11a5be81a95f69d7b38f4b8171/tenor.gif?itemid=14132796",
                     "https://media1.tenor.com/images/b63941fc92c0c4f741596b709883c0bf/tenor.gif?itemid=15150337",
                     "https://media1.tenor.com/images/d47b270c91ee8d97b8499c9c5a864e38/tenor.gif?itemid=14064857"]
        embedlaugh.add_field(name='Смех :laughing:', value=f'{author.mention} сейчас смеется.  Смешно кстати XD {random.choice(msgend)}')
        embedlaugh.set_image(url=random.choice(laughgifs))
        await ctx.send(embed=embedlaugh)

    @commands.command(name='bite', aliases=['кусь', 'укусить'], help=' sends random bite emotion gif')
    async def biteru(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedbite = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        bitegifs = ["https://media1.tenor.com/images/d97e4bc853ed48bf83386664956d75ec/tenor.gif?itemid=10364764",
                    "https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585",
                    "https://media1.tenor.com/images/418a2765b0bf54eb57bab3fde5d83a05/tenor.gif?itemid=12151511",
                    "https://media1.tenor.com/images/3baeaa0c5ae3a1a4ae9ac2780b2d965d/tenor.gif?itemid=13342683",
                    "https://media1.tenor.com/images/f3f456723f2f8735d118b43823c837f5/tenor.gif?itemid=14659250",
                    "https://media1.tenor.com/images/0d192209c8e9bcd9826af63ba72fc584/tenor.gif?itemid=15164408",
                    "https://media1.tenor.com/images/2adef5d4fba623aeb4c5b74879107b56/tenor.gif?itemid=5160295",
                    "https://media1.tenor.com/images/69546e40c361a59ce442c4d08e47bb05/tenor.gif?itemid=15157862",
                    "https://media1.tenor.com/images/f78e68053fcaf23a6ba7fbe6b0b6cff2/tenor.gif?itemid=10614631"]
        embedbite.add_field(name='Кусь', value=f'{author.mention} нежно покусывает {member.mention} {random.choice(msgend)}')
        embedbite.set_image(url=random.choice(bitegifs))
        await ctx.send(embed=embedbite)

    @commands.command(name='pout', aliases=['щечки', 'надутьщечки', 'дщ'], help=' sends random pouting emotion gif')
    async def pout(self, ctx):
        author = ctx.message.author
        embedpout = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        poutgifs = ["https://media1.tenor.com/images/271668b1037633d7f7ae63dc1a1c29f2/tenor.gif?itemid=14739721",
                    "https://media.tenor.com/images/46c9b8da42a62778fb37f89513c8af0e/tenor.gif",
                    "https://media.tenor.com/images/0f5d12aa3dfa6d8fd9e8a41bc51ec421/tenor.gif",
                    "https://media.tenor.com/images/abe8bc8b0b76b8ffe6694fa8b8f48853/tenor.gif",
                    "https://media1.tenor.com/images/e15433a7af99094cc98df27802b8948c/tenor.gif?itemid=5688400",
                    "https://media.tenor.com/images/a9a1ee151d114920f6914bd507f8b3c5/tenor.gif"]
        embedpout.add_field(name='Щечки', value=f'{author.mention} прямо сейчас надул(а) щечки {random.choice(msgend)}')
        embedpout.set_image(url=random.choice(poutgifs))
        await ctx.send(embed=embedpout)

    @commands.command(name='lick', aliases=['лизь', 'облизать', 'лизнуть'])
    async def lick(self, ctx, member: discord.Member):
        author = ctx.message.author
        member = ctx.author if not member else member
        embedlick = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        lickgifs = ["https://media1.tenor.com/images/f0a7f04a7bc32029cc1273d06b93237f/tenor.gif?itemid=13451464",
                    "https://media1.tenor.com/images/5f73f2a7b302a3800b3613095f8a5c40/tenor.gif?itemid=10005495",
                    "https://media1.tenor.com/images/359d9a5038eb688e9d5b25eead83ad3e/tenor.gif?itemid=4854805",
                    "https://media1.tenor.com/images/5c5828e51733c8ffe1c368f1395a03d0/tenor.gif?itemid=14231351",
                    "https://media1.tenor.com/images/5c5828e51733c8ffe1c368f1395a03d0/tenor.gif?itemid=14231351",
                    "https://media1.tenor.com/images/f46762ad38fbfed9e4e46bf7b89497c2/tenor.gif?itemid=12141724",
                    "https://media1.tenor.com/images/7132e6f39a0e4ada4e33d71056bcde67/tenor.gif?itemid=12858455",
                    "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727",
                    "https://media1.tenor.com/images/c4f68fbbec3c96193386e5fcc5429b89/tenor.gif?itemid=13451325",
                    "https://media1.tenor.com/images/1a2d051f28155db0e4cf175d987cdac2/tenor.gif?itemid=12141721",
                    "https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773",
                    "https://media1.tenor.com/images/fc0ef2ba03d82af0cbd6c5815c3c83d5/tenor.gif?itemid=12141725",
                    "https://media1.tenor.com/images/ec2ca0bf12d7b1a30fea702b59e5a7fa/tenor.gif?itemid=13417195",
                    "https://media1.tenor.com/images/81769ee6622b5396d1489fb4667fd20a/tenor.gif?itemid=14376074",
                    "https://media1.tenor.com/images/1925e468ff1ac9efc2100a3d092c54ff/tenor.gif?itemid=4718221",
                    "https://media1.tenor.com/images/d702fa41028207c6523b831ec2db9467/tenor.gif?itemid=5990650",
                    "https://media1.tenor.com/images/5ca31fd724f6baca41e366db4258a1e6/tenor.gif?itemid=12141726",
                    "https://cdn.idunetwork.eu.org/images/lick/7.gif"]
        embedlick.add_field(name='Лизание :stuck_out_tongue: ', value=f'{author.mention} облизывает {member.mention}')
        embedlick.set_image(url=random.choice(lickgifs))
        await ctx.send(embed=embedlick)

    @commands.command(name='втф', help=' sends random surprised emotion gif')
    async def wtfru(self, ctx):
        author = ctx.message.author
        embedwtf = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        wtfgifs = ["https://media.tenor.com/images/9ef9320a887d7ed45bf0b4dd00c91965/tenor.gif",
                   "https://media1.tenor.com/images/895fc6fe1dd915ded9cb85dd45a8ab0a/tenor.gif?itemid=14126080",
                   "https://media1.tenor.com/images/8728d889525dbf62c8c8c683b79077ff/tenor.gif?itemid=5109314",
                   "https://media1.tenor.com/images/2b3588720ac648c63349d727427dca48/tenor.gif?itemid=13058275",
                   "https://media1.tenor.com/images/85bc5b32ce4bee0ec93fa40c6a73db52/tenor.gif?itemid=10137967",
                   "https://media1.tenor.com/images/d21c1e645a4a754d9306ff72e8ccf735/tenor.gif?itemid=5563707",
                   "https://media1.tenor.com/images/435820fd4dc44c90ba5da15526ef913c/tenor.gif?itemid=8346464",
                   "https://media1.tenor.com/images/c47064848655a87b40ecf836b662daa6/tenor.gif?itemid=12342170",
                   "https://media1.tenor.com/images/9c391db760d747be14742be2cb6ab64f/tenor.gif?itemid=15198304",
                   "https://media1.tenor.com/images/bab858e36ca9203b7575a0656a925874/tenor.gif?itemid=15052547"]
        embedwtf.add_field(name='Что!? :scream:', value=f'{author.mention} очень удивлён {random.choice(msgend)}')
        embedwtf.set_image(url=random.choice(wtfgifs))
        await ctx.send(embed=embedwtf)

    @commands.command(name='хмм', help=' emotion think')
    async def thinkingru(self, ctx):
        author = ctx.message.author
        embedthink = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        thinkgifs = ["https://media1.tenor.com/images/1ac375ffe6f2e99ac36eb1b42a7b9707/tenor.gif?itemid=13593873",
                     "https://i.pinimg.com/originals/a8/bd/50/a8bd501a4a8994943eba503bdbef68bf.jpg",
                     "https://animemotivation.com/wp-content/uploads/2018/10/anime-girl-curious-thinking.jpg.webp",
                     "https://cdn140.picsart.com/294766366044211.png?r1024x1024",
                     "https://www.pngkey.com/png/detail/315-3152007_png-animuthinku-thinking-meme-face-anime.png",
                     "https://i.pinimg.com/736x/f7/99/02/f7990250a60043abd57e29efd23f7844.jpg",
                     "https://www.vippng.com/png/detail/27-278214_nanothink-discord-emoji-anime-thinking-emoji.png",
                     "https://animemotivation.com/wp-content/uploads/2018/07/Kirino-chiba-thinking.jpg.webp",
                     "https://i.gifer.com/RNCb.gif",
                     "https://media.tenor.com/images/83ab21 f684ec5b2325e8f86f6b7d1a85/tenor.gif",
                     "https://i.gifer.com/WaSO.gif",
                     "http://pa1.narvii.com/6763/bc4e8757b14fb6334e5038ee402167ebc0b27173_00.gif",
                     "https://data.whicdn.com/images/324658620/original.gif",
                     "https://i1.wp.com/www.animefeminist.com/wp-content/uploads/2019/06/thinking-hmm-pencil-sailor-moon.gif?fit=500%2C378&ssl=1"]
        embedthink.add_field(name=" Чертоги разума :thinking: ",
                             value=f"{author.mention} думает прямо сейчас {random.choice(msgend)}")
        embedthink.set_image(url=random.choice(thinkgifs))
        await ctx.send(embed=embedthink)


def setup(bot):
    bot.add_cog(Emotions(bot))