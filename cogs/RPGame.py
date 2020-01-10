import discord
import json
import asyncio
import random
from discord.ext import commands


class RPGgame(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open(r'rpg.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open(r'rpg.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.command()
    async def charactercreate(self, ctx):
        await ctx.send('Character creating process started!')
        member = ctx.author
        member_id = str(member.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5')

            return inner_check

        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Race choose menu',
                        value='Choose your race! Write in chat for example ```1``` and other numbers for choosing a race of your character! \n 1) Human \n 2) Elf \n 3) Succubus \n 4) Draconis \n 5) Neko')
        await ctx.send(embed=embed)
        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.add_field(name='Human',
                         value="Balanced start race. Most balanced race. Start params: \n  strength 15 \n  agility 3\n  intelligence 0\n can't learn magic! \n AngelicLevel 0 \n  DemonicLevel 0 \n Karma 3 \n Have advantage in shop prices and increased loot chance from treasures! ")
        embed1.set_image(url='https://i.ytimg.com/vi/31vXOQjiz-Y/maxresdefault.jpg')
        await ctx.send(embed=embed1)
        embed2 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed2.add_field(name='Elf',
                         value="Wise and elder race. Start params: \n  strength 5 \n  agility 5\n  intelligence 20\n Know magic from start! \n AngelicLevel 1 \n  DemonicLevel 0 \n Karma 5 \n Powerful magic spells and angelic level, but low hp!")
        embed2.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/657179193595133963/af781f579d19ab28.png')
        await ctx.send(embed=embed2)
        embed3 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed3.add_field(name='Succubus',
                         value="Demonic powered and forged race. Start params: \n  strength 8 \n  agility 3\n  intelligence 15\n Know magic from start! \n AngelicLevel 0 \n  DemonicLevel 4 \n Karma -30 \n Demonic magic, demonic conversions, demonic level, summons and other!")
        embed3.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/657180558828503051/38b34098ee41054c.png')
        await ctx.send(embed=embed3)
        embed4 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed4.add_field(name='Draconis',
                         value='Very heavy and armored race! Try to punch! Start params: \n  strength 30 \n  agility 2\n  intelligence 10\n Can learn fire magic with level \n AngelicLevel 1 \n  DemonicLevel 1 \n Karma 2 \n Big HP amount and can learn magic')
        embed4.set_image(url='https://i.imgur.com/zF1KUm5.jpg')
        await ctx.send(embed=embed4)
        embed5 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed5.add_field(name='Neko',
                         value="Very fast and agiled race!Start params: \n  strength 4 \n  agility 12\n  intelligence 0\n Can't learn magic \n AngelicLevel 0 \n DemonicLevel 0 \n Karma 0 \n More money from enemy after the fight! Big damage!")
        embed5.set_image(url='https://i.pinimg.com/564x/6e/07/f2/6e07f238683ce2d8137d8202f06ef98a.jpg')
        await ctx.send(embed=embed5)
        reply = await self.client.wait_for('message', check=check, timeout=120)
        if reply.content == '1':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 3
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 15
            self.users[member_id]['strength'] = 15
            self.users[member_id]['agility'] = 3
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'common'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '2':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 5
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 5
            self.users[member_id]['strength'] = 5
            self.users[member_id]['agility'] = 5
            self.users[member_id]['intelligence'] = 20
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = 'с'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'magic'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '3':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = -30
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 8
            self.users[member_id]['strength'] = 8
            self.users[member_id]['agility'] = 3
            self.users[member_id]['intelligence'] = 15
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 5
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Succub_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = 'с'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'magic'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '4':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 2
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 30
            self.users[member_id]['strength'] = 30
            self.users[member_id]['agility'] = 2
            self.users[member_id]['intelligence'] = 10
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 1
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Dragon_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'heavy'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '5':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 0
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 4
            self.users[member_id]['strength'] = 4
            self.users[member_id]['agility'] = 12
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'cat'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')

    @commands.command()
    async def testcreate(self, ctx):
        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5')

            return inner_check

        member = ctx.author
        member_id = str(member.id)
        await ctx.send('commands for testers')
        await ctx.send('1) human 2) elf 3) succubus 4) dragon 5) neko')
        reply = await self.client.wait_for('message', check=check, timeout=120)
        if reply.content == '1':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 3
            self.users[member_id]['gold'] = 1000
            self.users[member_id]['level'] = 12
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 40
            self.users[member_id]['strength'] = 40
            self.users[member_id]['agility'] = 13
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 1
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'Learned'
            self.users[member_id]['Succub_Skill_1'] = 'Learned'
            self.users[member_id]['Dragon_Skill_1'] = 'Learned'
            await ctx.send('Your character was created!')
        if reply.content == '2':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 5
            self.users[member_id]['gold'] = 1000
            self.users[member_id]['level'] = 12
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 25
            self.users[member_id]['strength'] = 25
            self.users[member_id]['agility'] = 5
            self.users[member_id]['intelligence'] = 20
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 1
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'Learned'
            self.users[member_id]['Succub_Skill_1'] = 'Learned'
            self.users[member_id]['Dragon_Skill_1'] = 'Learned'
            await ctx.send('Your character was created!')
        if reply.content == '3':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = -30
            self.users[member_id]['gold'] = 1000
            self.users[member_id]['level'] = 12
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 18
            self.users[member_id]['strength'] = 18
            self.users[member_id]['agility'] = 3
            self.users[member_id]['intelligence'] = 15
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 5
            self.users[member_id]['storyfantasy'] = 1
            self.users[member_id]['Elf_Skill_1'] = 'Learned'
            self.users[member_id]['Succub_Skill_1'] = 'Learned'
            self.users[member_id]['Dragon_Skill_1'] = 'Learned'
            await ctx.send('Your character was created!')
        if reply.content == '4':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 2
            self.users[member_id]['gold'] = 1000
            self.users[member_id]['level'] = 12
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 60
            self.users[member_id]['strength'] = 60
            self.users[member_id]['agility'] = 8
            self.users[member_id]['intelligence'] = 10
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 1
            self.users[member_id]['storyfantasy'] = 1
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'Learned'
            self.users[member_id]['Succub_Skill_1'] = 'Learned'
            self.users[member_id]['Dragon_Skill_1'] = 'Learned'
            await ctx.send('Your character was created!')
        if reply.content == '5':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 0
            self.users[member_id]['gold'] = 1000
            self.users[member_id]['level'] = 12
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 14
            self.users[member_id]['strength'] = 14
            self.users[member_id]['agility'] = 32
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 1
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'Learned'
            self.users[member_id]['Succub_Skill_1'] = 'Learned'
            self.users[member_id]['Dragon_Skill_1'] = 'Learned'
            await ctx.send('Your character was created!')

    @commands.command()
    async def createcharacter(self, ctx):
        await ctx.send('Character creating process started!')
        member = ctx.author
        member_id = str(member.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5')

            return inner_check

        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Race choose menu',
                        value='Choose your race! Write in chat for example```1``` and other numbers for choosing a race of your character! \n 1) Human \n 2) Elf \n 3) Succubus 4) Draconis \n 5) Neko')
        await ctx.send(embed=embed)

        embed1 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed1.add_field(name='Human',
                         value="Balanced start race. Most balanced race. Start params: \n  strength 15 \n  agility 3\n  intelligence 0\n can't learn magic! \n AngelicLevel 0 \n  DemonicLevel 0 \n Karma 3 \n Have advantage in shop prices and increased loot chance from treasures! ")
        embed1.set_image(url='https://i.ytimg.com/vi/31vXOQjiz-Y/maxresdefault.jpg')
        await ctx.send(embed=embed1)
        embed2 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed2.add_field(name='Elf',
                         value="Wise and elder race. Start params: \n  strength 5 \n  agility 5\n  intelligence 20\n Know magic from start! \n AngelicLevel 1 \n  DemonicLevel 0 \n Karma 5 \n Powerful magic spells and angelic level, but low hp!")
        embed2.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/657179193595133963/af781f579d19ab28.png')
        await ctx.send(embed=embed2)
        embed3 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed3.add_field(name='Succubus',
                         value="Demonic powered and forged race. Start params: \n  strength 8 \n  agility 3\n  intelligence 15\n Know magic from start! \n AngelicLevel 0 \n  DemonicLevel 4 \n Karma -30 \n Demonic magic, demonic conversions, demonic level, summons and other!")
        embed3.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/657180558828503051/38b34098ee41054c.png')
        await ctx.send(embed=embed3)
        embed4 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed4.add_field(name='Draconis',
                         value='Very heavy and armored race! Try to punch! Start params: \n  strength 30 \n  agility 2\n  intelligence 10\n Can learn fire magic with level \n AngelicLevel 1 \n  DemonicLevel 1 \n Karma 2 \n Big HP amount and can learn magic')
        embed4.set_image(url='https://i.imgur.com/zF1KUm5.jpg')
        await ctx.send(embed=embed4)
        embed5 = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed5.add_field(name='Neko',
                         value="Very fast and agiled race!Start params: \n  strength 4 \n  agility 12\n  intelligence 0\n Can't learn magic \n AngelicLevel 0 \n DemonicLevel 0 \n Karma 0 \n More money from enemy after the fight! Big damage!")
        embed5.set_image(url='https://i.pinimg.com/564x/6e/07/f2/6e07f238683ce2d8137d8202f06ef98a.jpg')
        await ctx.send(embed=embed5)
        reply = await self.client.wait_for('message', check=check, timeout=120)
        if reply.content == '1':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 3
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 15
            self.users[member_id]['strength'] = 15
            self.users[member_id]['agility'] = 3
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'common'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '2':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 5
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 5
            self.users[member_id]['strength'] = 5
            self.users[member_id]['agility'] = 5
            self.users[member_id]['intelligence'] = 20
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Elf_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = 'с'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'magic'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '3':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = -30
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 8
            self.users[member_id]['strength'] = 8
            self.users[member_id]['agility'] = 3
            self.users[member_id]['intelligence'] = 15
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 5
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Succub_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = 'с'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'magic'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '4':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 2
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 30
            self.users[member_id]['strength'] = 30
            self.users[member_id]['agility'] = 2
            self.users[member_id]['intelligence'] = 10
            self.users[member_id]['angel'] = 1
            self.users[member_id]['demon'] = 1
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['Dragon_Skill_1'] = 'unLearned'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'heavy'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')
        if reply.content == '5':
            self.users[member_id] = {}
            self.users[member_id]['karma'] = 0
            self.users[member_id]['gold'] = 30
            self.users[member_id]['level'] = 1
            self.users[member_id]['exp'] = 0
            self.users[member_id]['health'] = 4
            self.users[member_id]['strength'] = 4
            self.users[member_id]['agility'] = 12
            self.users[member_id]['intelligence'] = 0
            self.users[member_id]['angel'] = 0
            self.users[member_id]['demon'] = 0
            self.users[member_id]['storyfantasy'] = 0
            self.users[member_id]['ach1'] = '❌'
            self.users[member_id]['ach2'] = '❌'
            self.users[member_id]['ach3'] = '❌'
            self.users[member_id]['ach4'] = '❌'
            self.users[member_id]['ach5'] = '❌'
            self.users[member_id]['weapon'] = '❌'
            self.users[member_id]['weaponstat'] = 0
            self.users[member_id]['armor'] = '❌'
            self.users[member_id]['armorstat'] = 0
            self.users[member_id]['type'] = 'cat'
            self.users[member_id]['item1'] = 0
            self.users[member_id]['item2'] = 0
            self.users[member_id]['item3'] = 0
            self.users[member_id]['treasure'] = 0
            await ctx.send('Your character was created!')

    @commands.command()
    async def rpgstorystart(self, ctx):
        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2')

            return inner_check

        member = ctx.author
        member_id = str(member.id)
        magic_damage = 1 * self.users[member_id]['intelligence']
        physical_damage = random.randint(self.users[member_id]['agility'],
                                         self.users[member_id]['agility'] + 40)
        embedstart = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedstart.add_field(name='Your eyes open!', value="Your eyes is opened and you are waking up in cave? You "
                                                           "don't...Smell is awful, near to you is dead body of the "
                                                           "common girl. She not even in armor or something like that. "
                                                           "Looks like she is a innocent resident of village or town. "
                                                           "You checked body and found a strange scroll with symbols "
                                                           "which you can't read because language is strange and "
                                                           "obscure. Near to her hand was unused torch, so now you use it and go forward in mysteries of dungeon! ")
        embedstart.set_image(url='https://sun9-65.userapi.com/c858436/v858436328/11cb94/HZvsLi4ul2c.jpg')
        await ctx.send(embed=embedstart)
        clearmind = 'шо нада? Я ОЛД'
        if self.users[member_id]['karma'] == 3 or self.users[member_id]['karma'] == 2 or self.users[member_id][
            'karma'] == 0:
            clearmind = 'Your mind now is so clear!You remembered skills of how to fight in close combat!You taking up your sword and ready for battle!'
        if self.users[member_id]['karma'] == 5 or self.users[member_id]['karma'] == -30:
            clearmind = 'Your mind now is so clear!You remembered skills of how to use magic skills!Now your soul is ready!'
        embedmind = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedmind.add_field(name='Your mind is clear!', value=clearmind)
        await ctx.send(embed=embedmind)
        embedfight1 = discord.Embed(
            color=discord.Colour.dark_purple())
        embedfight1.add_field(name='Fight!',
                              value="You going deep in cave and see a dead body and goblin! He looks very aggresive!")
        embedfight1.set_image(
            url='https://cdn.discordapp.com/attachments/657178465174552616/657194216002289677/-LKpTPfq6Cc.png')
        await ctx.send(embed=embedfight1)
        goblinhp = 6
        while goblinhp > 0:
            embedslime = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedslime.add_field(name='Goblin', value=f'{goblinhp} HP \n 1) Attack 2) Dodge')
            embedslime.set_image(
                url='https://sun9-58.userapi.com/c204816/v204816185/12cee/3ZDGnub-Qhw.jpg')

            await ctx.send(embed=embedslime)

            reply3 = await self.client.wait_for('message', check=check, timeout=180)
            dop_damage = 0
            if reply3.content == '1':
                if self.users[member_id]['intelligence'] >= 15:
                    magic_damage += dop_damage
                    goblinhp -= magic_damage
                    await ctx.send(f'You did {magic_damage} magic damage to goblin! Now his HP is {goblinhp}')
                    magic_damage -= dop_damage
                    dop_damage = 0
                if self.users[member_id]['intelligence'] < 15:
                    physical_damage += dop_damage
                    goblinhp -= physical_damage
                    await ctx.send(f'You did {physical_damage} damage to goblin!Good punch. Now his HP is {goblinhp}')
                    physical_damage -= dop_damage
                    dop_damage = 0
                if goblinhp > 0:
                    mob_damage = random.randint(1, 3)
                    self.users[member_id]['health'] -= mob_damage
                    await ctx.send(
                        f"Goblin gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
            if reply3.content == '2':
                dodgechance = random.randint(1, 2)
                mob_damage = random.randint(1, 3)
                if dodgechance == 1:
                    mob_damage = 0
                    await ctx.send('Succesful dodge!You gain +3 damage in next attack!')
                    dop_damage = 3
                if dodgechance == 2:
                    self.users[member_id]['health'] -= mob_damage
                    await ctx.send(
                        f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")

        if goblinhp <= 0:
            embedslimewin = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            exp_slime = random.randint(7, 15)
            gold_slime = random.randint(1, 3)
            if self.users[member_id]['karma'] == 0:
                gold_slime += 6
            embedslimewin.add_field(name='Win',
                                    value=f"You won the fight against goblin with remaining {self.users[member_id]['health']} That's good!You got {exp_slime} and found {gold_slime}")
            self.users[member_id]['exp'] += exp_slime
            self.users[member_id]['gold'] += gold_slime
            if self.lvl_up(member_id):
                self.users[member_id]['strength'] += 1
                self.users[member_id]['agility'] += 1
                if self.users[member_id]['intelligence'] > 0:
                    self.users[member_id]['intelligence'] += 1
                await ctx.send(
                    f"{member.mention} Your character is now level {self.users[member_id]['level']}")
            embedAttention = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedAttention.add_field(name='Event',
                                     value='A two sneaky goblins noticed your battle with other already dead goblin!They ran out and seems will call for help! Prepare for a good fight')
            embedAttention.set_image(url='https://sun9-56.userapi.com/c200424/v200424002/16891/QGmePf0OvJ0.jpg')
            await ctx.send(embed=embedAttention)
            embedprefight2 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embedprefight2.add_field(name='Fight',
                                     value="You see a medium sized group of goblins and they are really ready to fight with you. Some of them have even an armor. Are you ready? You can't give up.")
            embedprefight2.set_image(url='https://media.kg-portal.ru/anime/g/goblinslayer/images/goblinslayer_5.jpg')
            await ctx.send(embed=embedprefight2)
            goblinhp = 26
            while goblinhp > 0:
                embedslime = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedslime.add_field(name='Goblin', value=f'{goblinhp} HP \n 1) Attack 2) Dodge')
                embedslime.set_image(
                    url='https://www.anime-planet.com/images/characters/goblin-phantom-in-the-twilight-148811.jpg?t=1535389542')

                await ctx.send(embed=embedslime)

                reply3 = await self.client.wait_for('message', check=check, timeout=180)
                dop_damage = 0
                if reply3.content == '1':
                    if self.users[member_id]['intelligence'] >= 15:
                        magic_damage += dop_damage
                        goblinhp -= magic_damage
                        await ctx.send(f'You did {magic_damage} magic damage to goblin! Now his HP is {goblinhp}')
                        magic_damage -= dop_damage
                        dop_damage = 0
                    if self.users[member_id]['intelligence'] < 15:
                        physical_damage += dop_damage
                        goblinhp -= physical_damage
                        await ctx.send(
                            f'You did {physical_damage} damage to goblin!Good punch. Now his HP is {goblinhp}')
                        physical_damage -= dop_damage
                        dop_damage = 0
                    if goblinhp > 0:
                        mob_damage = random.randint(1, 3)
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Goblin gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                if reply3.content == '2':
                    dodgechance = random.randint(1, 3)
                    mob_damage = random.randint(1, 3)
                    if dodgechance == 1:
                        mob_damage = 0
                        await ctx.send('Succesful dodge!You gain +3 damage in next attack!')
                        dop_damage = 3
                    if dodgechance == 2:
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                    if dodgechance == 3:
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")

            if goblinhp <= 0:
                embedslimewin = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                exp_slime = random.randint(9, 24)
                gold_slime = random.randint(3, 5)
                if self.users[member_id]['karma'] == 0:
                    gold_slime += 6
                embedslimewin.add_field(name='Win',
                                        value=f"You won the fight against goblin with remaining {self.users[member_id]['health']} That's good!You got {exp_slime} and found {gold_slime}")
                self.users[member_id]['exp'] += exp_slime
                self.users[member_id]['gold'] += gold_slime
                if self.lvl_up(member_id):
                    self.users[member_id]['strength'] += 1
                    self.users[member_id]['agility'] += 1
                    if self.users[member_id]['intelligence'] > 0:
                        self.users[member_id]['intelligence'] += 1
                    await ctx.send(
                        f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                embedfight3 = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedfight3.add_field(name='Fight', value='Goblin captain and his allies is attacking you together')
                embedfight3.set_image(url='https://vdp.mycdn.me/getImage?id=546955987567&idx=32&thumbType=32')
                await ctx.send(embed=embedfight3)
                goblinhp = 45
                while goblinhp > 0:
                    if self.users[member_id]['health'] <= 0:
                        self.users[member_id]['health'] += 3
                        await ctx.send('Something giving you powers to continue a fight!')
                    embedslime = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedslime.add_field(name='Goblin', value=f'{goblinhp} HP \n 1) Attack 2) Dodge')
                    embedslime.set_image(
                        url='https://sun9-55.userapi.com/c854016/v854016814/1aedb9/wVb9NfFsJdw.jpg')

                    await ctx.send(embed=embedslime)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['intelligence'] >= 15:
                            magic_damage += dop_damage
                            goblinhp -= magic_damage
                            await ctx.send(f'You did {magic_damage} magic damage to goblin! Now his HP is {goblinhp}')
                            magic_damage -= dop_damage
                            dop_damage = 0
                        if self.users[member_id]['intelligence'] < 15:
                            physical_damage += dop_damage
                            goblinhp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to goblin!Good punch. Now his HP is {goblinhp}')
                            physical_damage -= dop_damage
                            dop_damage = 0
                        if goblinhp > 0:
                            mob_damage = random.randint(1, 3)
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(1, 3)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!You gain +3 damage in next attack!')
                            dop_damage = 3
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                        if dodgechance == 3:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")

                if goblinhp <= 0:
                    embedslimewin = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    exp_slime = random.randint(11, 39)
                    gold_slime = random.randint(5, 6)
                    if self.users[member_id]['karma'] == 0:
                        gold_slime += 6
                    embedslimewin.add_field(name='Win',
                                            value=f"You won the fight against goblin with remaining {self.users[member_id]['health']} That's good!You got {exp_slime} and found {gold_slime}")
                    self.users[member_id]['exp'] += exp_slime
                    self.users[member_id]['gold'] += gold_slime
                    if self.lvl_up(member_id):
                        self.users[member_id]['strength'] += 1
                        self.users[member_id]['agility'] += 1
                        if self.users[member_id]['intelligence'] > 0:
                            self.users[member_id]['intelligence'] += 1
                        await ctx.send(
                            f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                embedprefight4 = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embedprefight4.add_field(name='Fight',
                                         value='A really big goblin is pushed out all the little goblins and made his way to you. YOU HAVE NO WAY TO RUN. Just face your fate.')
                embedprefight4.set_image(
                    url='http://www.animefanshub.com/wp-content/uploads/2018/11/Goblin-Champion-1024x583.jpeg')
                await ctx.send(embed=embedprefight4)
                goblinhp = 1000
                while goblinhp > 0:
                    await ctx.send('**you pray**')
                    await ctx.send('Your pray is heard')
                    if self.users[member_id]['health'] <= 0:
                        self.users[member_id]['health'] += 900
                        await ctx.send('Something giving you powers to continue a fight!')
                    embedslime = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedslime.add_field(name='Champion Goblin [???]', value=f'{goblinhp} HP \n 1) Attack 2) Dodge')
                    embedslime.set_image(
                        url='https://cdn.anidb.net/images/main/226850.jpg')

                    await ctx.send(embed=embedslime)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['intelligence'] >= 15:
                            magic_damage += dop_damage + 265
                            goblinhp -= magic_damage
                            await ctx.send(f'You did {magic_damage} magic damage to goblin! Now his HP is {goblinhp}')
                            magic_damage -= dop_damage
                            dop_damage = 0
                        if self.users[member_id]['intelligence'] < 15:
                            physical_damage += dop_damage + 265
                            goblinhp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to goblin!Good punch. Now his HP is {goblinhp}')
                            physical_damage -= dop_damage
                            dop_damage = 0
                        if goblinhp > 0:
                            mob_damage = random.randint(700, 900)
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(300, 900)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!You gain +3 damage in next attack!')
                            dop_damage = 3
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                        if dodgechance == 3:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Goblin gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")

                if goblinhp <= 0:
                    embedslimewin = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    exp_slime = random.randint(87, 307)
                    gold_slime = random.randint(52, 109)
                    if self.users[member_id]['karma'] == 0:
                        gold_slime += 100
                    embedslimewin.add_field(name='Win',
                                            value=f"You won the fight against goblin with remaining {self.users[member_id]['health']} That's good!You got {exp_slime} and found {gold_slime}")
                    self.users[member_id]['exp'] += exp_slime
                    self.users[member_id]['gold'] += gold_slime
                    if self.lvl_up(member_id):
                        self.users[member_id]['strength'] += 1
                        self.users[member_id]['agility'] += 1
                        if self.users[member_id]['intelligence'] > 0:
                            self.users[member_id]['intelligence'] += 1
                        await ctx.send(
                            f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                    embedscrool = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedscrool.add_field(name='Event',
                                          value='After killing a big goblin some strange and scary events '
                                                'have happened. Someone used a strong spell and chaotic '
                                                'explosion happened! All goblins are dead! And you must be too, '
                                                'but scrool saved u and disappeared. Cave now is shaking '
                                                'and you feeling evil powers.')
                    embedscrool.set_image(
                        url='https://i.pinimg.com/originals/68/34/84/68348466b7c0cdcd1c5ac628314a4020.gif')
                    await ctx.send(embed=embedscrool)
                    embedpredragon = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedpredragon.add_field(name='Fight', value='Bone dragon is materialising. Someone summoned it')
                    embedpredragon.set_image(
                        url='http://vignette2.wikia.nocookie.net/overlordmaruyama/images/1/14/Overlord_EP09_021.png/revision/latest?cb=20150902102606')
                    await ctx.send(embed=embedpredragon)
                    dragonhp = 10000
                    while dragonhp > 0:
                        await ctx.send('**you pray**')
                        await ctx.send('Your pray is heard')
                        if self.users[member_id]['health'] <= 0:
                            self.users[member_id]['health'] = 0
                            self.users[member_id]['health'] += 2000
                        a = random.randint(1, 4)
                        special_damage = 0
                        if a == 2:
                            special_damage = 999999999999
                            await ctx.send('DRAGON IS PREPARING FOR STRONG ATTACK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                            await ctx.send('Something giving you powers to continue a fight!')
                        embedslime = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        embedslime.add_field(name='Bone Dragon [???]', value=f'{dragonhp} HP \n 1) Attack 2) Dodge')
                        embedslime.set_image(
                            url='https://em.wattpad.com/9ec8e9122c4902f8f2ea54f9a59401e37cd93c17/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f35634454626e50686e634e5466413d3d2d3531373037373831332e313530363630626266306634313265653832323838383032333438302e706e67?s=fit&w=720&h=720')

                        await ctx.send(embed=embedslime)

                        reply3 = await self.client.wait_for('message', check=check, timeout=180)
                        dop_damage = 0
                        if reply3.content == '1':
                            if self.users[member_id]['intelligence'] >= 15:
                                magic_damage = dop_damage + 1500
                                dragonhp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} magic damage to bone dragon! Now his HP is {dragonhp}')
                                magic_damage -= dop_damage
                                dop_damage = 0
                            if self.users[member_id]['intelligence'] < 15:
                                physical_damage = dop_damage + 1500
                                dragonhp -= physical_damage
                                await ctx.send(
                                    f'You did {physical_damage} damage to bone dragon!Good punch. Now his HP is {dragonhp}')
                                physical_damage -= dop_damage
                                dop_damage = 0
                            if dragonhp > 0:
                                mob_damage = random.randint(1500, 5000)
                                mob_damage += special_damage
                                self.users[member_id]['health'] -= mob_damage
                                mob_damage -= special_damage
                                await ctx.send(
                                    f"Bone dragon gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if reply3.content == '2':
                            dodgechance = random.randint(1, 2)
                            mob_damage = random.randint(1500, 5000)
                            if dodgechance == 1:
                                mob_damage = 0
                                await ctx.send('Succesful dodge!You gain +300 damage in next attack!')
                                dop_damage = 300
                            if dodgechance == 2:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bone dragon gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                    if dragonhp <= 0:
                        embedslimewin = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        exp_slime = random.randint(11, 39)
                        gold_slime = random.randint(5, 6)
                        if self.users[member_id]['karma'] == 0:
                            gold_slime += 6
                        embedslimewin.add_field(name='Win',
                                                value=f"You won the fight against bone dragon with remaining {self.users[member_id]['health']} That's good!You got {exp_slime} and found {gold_slime}")
                        self.users[member_id]['exp'] += exp_slime
                        self.users[member_id]['gold'] += gold_slime
                        if self.lvl_up(member_id):
                            self.users[member_id]['strength'] += 1
                            self.users[member_id]['agility'] += 1
                            if self.users[member_id]['intelligence'] > 0:
                                self.users[member_id]['intelligence'] += 1
                            await ctx.send(
                                f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                    embedlast_fight = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedlast_fight.add_field(name='Last Fight',
                                              value=f'A mysterious evil person appeared.\n - Oh. You are still alive. Okay, i will help you to die :smiling_imp: .',
                                              inline=False)
                    embedlast_fight.add_field(name='pray',
                                              value=f"**you pray** \n - HAHAHAHHAH :rofl:  stop praying. It can't help you against me. **your prays are hopeless now** \n Your current health: 150000, Your current damage: 17500",
                                              inline=False)
                    embedlast_fight.set_image(
                        url='https://i.pinimg.com/originals/d2/e6/01/d2e601d66a27990469b38e32e023cb3e.jpg')
                    await ctx.send(embed=embedlast_fight)
                    evil_hp = 100000
                    self.users[member_id]['health'] = 150000
                    while evil_hp > 0:
                        evil_avatars = ["https://pbs.twimg.com/profile_images/567222370000056320/zi1g4tR9_400x400.png",
                                        "https://pbs.twimg.com/profile_images/808233876044673024/TJ3GKhZz_400x400.jpg",
                                        "http://pm1.narvii.com/6338/a82571a6560523d05a41faf55b1326ea08b54e11_00.jpg",
                                        "https://i.ytimg.com/vi/gWxcsSj_8RU/hqdefault.jpg",
                                        "https://i.ytimg.com/vi/JqaU6Yamdrs/maxresdefault.jpg",
                                        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/de40a77c-bc96-4548-ae8e-3aeff50eae2e/d95h216-c8b4365e-39c5-4200-b801-056fbdbe6350.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2RlNDBhNzdjLWJjOTYtNDU0OC1hZThlLTNhZWZmNTBlYWUyZVwvZDk1aDIxNi1jOGI0MzY1ZS0zOWM1LTQyMDAtYjgwMS0wNTZmYmRiZTYzNTAuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.zKYJ9A0EV38ajMgvySkWVBjnmZKmtrDPNNz8dGfcnDM"]
                        if self.users[member_id]['health'] <= 0:
                            await ctx.send('**You died?** \n ```$rpgplay```')
                            self.users[member_id]['level'] = 12
                            self.users[member_id]['storyfantasy'] = 1
                            self.users[member_id]['agility'] += 6
                            self.users[member_id]['strength'] += 6
                            break
                        a = random.randint(1, 32)
                        special_damage = 0
                        if a == 2:
                            special_damage = 999999999999
                            await ctx.send('[???] IS CHARCHING POWERFUL CHAOTIC LASER')
                            await ctx.send('[100%] LASER IS READY [DODGE]')
                        if a == 3:
                            special_damage = 999999999999
                            await ctx.send('[???] IS GOIND TO HEAVY ATTACK FROM AIR')
                            await ctx.send('[100%] ATTACK IS READY [DODGE]')
                        if a == 4:
                            special_damage = 999999999999
                            await ctx.send('[???] IS SUMMONING ORBS OF WORLD DESTRUCTION')
                            await ctx.send('[100%] ORBS IS READY TO EXPLODE [DODGE]')
                        embedslime = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        embedslime.add_field(name=' [???]', value=f'{evil_hp} HP \n 1) Attack 2) Dodge')
                        embedslime.set_image(
                            url=f'{random.choice(evil_avatars)}')

                        await ctx.send(embed=embedslime)

                        reply3 = await self.client.wait_for('message', check=check, timeout=180)
                        dop_damage = 0
                        if reply3.content == '1':
                            if self.users[member_id]['intelligence'] >= 15:
                                magic_damage = 17500
                                evil_hp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} magic damage to [???]! Now his HP is {evil_hp}')
                                magic_damage -= dop_damage
                                dop_damage = 0
                            if self.users[member_id]['intelligence'] < 15:
                                physical_damage = 175000
                                evil_hp -= physical_damage
                                await ctx.send(
                                    f'You did {physical_damage} damage to [???]!Good punch. Now his HP is {evil_hp}')
                                physical_damage -= dop_damage
                                dop_damage = 0
                            if evil_hp > 0:
                                mob_damage = random.randint(6000, 15000)
                                mob_damage += special_damage
                                self.users[member_id]['health'] -= mob_damage
                                mob_damage -= special_damage
                                await ctx.send(
                                    f"[???] gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if reply3.content == '2':
                            dodgechance = random.randint(1, 2)
                            mob_damage = random.randint(1500, 5000)
                            if dodgechance == 1 or a == 2 or a == 3 or a == 4:
                                mob_damage = 0
                                await ctx.send('Succesful dodge!You gain +3000 damage for this battle!')
                                physical_damage += 3000
                                magic_damage += 3000
                            if dodgechance == 2:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"[???] gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                    if evil_hp <= 0:
                        await ctx.send(
                            ' PATHETIIIIIIIIIC!! Pathetic... Pathetic! You are so pathetic! \nHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAH **transformation** **mutation**')
                        evil_hp = 1000000
                        while evil_hp > 0:
                            if self.users[member_id]['health'] <= 0:
                                await ctx.send('**You died?** \n ```$rpgplay```')
                                self.users[member_id]['level'] = 12
                                self.users[member_id]['storyfantasy'] = 1
                                self.users[member_id]['agility'] += 6
                                self.users[member_id]['strength'] += 6
                                break
                            embedslime = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            embedslime.add_field(name=' [???]', value=f'{evil_hp} HP \n 1) Attack 2) Dodge')
                            embedslime.set_image(
                                url='https://img1.goodfon.ru/wallpaper/nbig/3/e8/bleach-aizen-sousuke-by-seigi.jpg')

                            await ctx.send(embed=embedslime)

                            reply3 = await self.client.wait_for('message', check=check, timeout=180)
                            dop_damage = 0
                            if reply3.content == '1':
                                if self.users[member_id]['intelligence'] >= 15:
                                    magic_damage = 17500
                                    evil_hp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} magic damage to [???]! Now his HP is {evil_hp}')
                                    magic_damage -= dop_damage
                                    dop_damage = 0
                                if self.users[member_id]['intelligence'] < 15:
                                    physical_damage = 17500
                                    evil_hp -= physical_damage
                                    await ctx.send(
                                        f'You did {physical_damage} damage to [???]!Good punch. Now his HP is {evil_hp}')
                                    physical_damage -= dop_damage
                                    dop_damage = 0
                                if evil_hp > 0:
                                    mob_damage = random.randint(132131231116000, 12312321311312313115000)
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"[???] gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                            if reply3.content == '2':
                                dodgechance = random.randint(1, 2)
                                mob_damage = random.randint(1500, 5000)
                                if dodgechance == 1:
                                    mob_damage = 0
                                    await ctx.send('Succesful dodge!You gain +300 damage in next attack!')
                                    dop_damage = 300
                                if dodgechance == 2:
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"[???] gave you {mob_damage} Now your hp is {self.users[member_id]['health']}")
                        if evil_hp <= 0:
                            embedCLONEXY = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            embedCLONEXY.add_field(name='Not bad LMAO',
                                                   value='Clonexy700#3767[Developer]: "LMAO not bad :D well some meme for you XD You thought about good reward or something like that? No no no XD  Just take look on this dancing Ricardo"')
                            embedCLONEXY.set_image(url='https://media3.giphy.com/media/UtcBRO8cxulRzkrVLc/giphy.gif')
                            self.users[member_id]['level'] = 12
                            self.users[member_id]['storyfantasy'] = 1
                            self.users[member_id]['agility'] += 6
                            self.users[member_id]['strength'] += 6
                            await ctx.send('Not end, your journey only is starting! \n ```$rpgstart ```')

    @commands.command()
    async def rpgshop(self, ctx):
        member = ctx.author
        member_id = str(member.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2')

            return inner_check

        def checkshop(author):
            def inner_check2(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4', '5', '6', '7', '8', '9')

            return inner_check2

        merchant = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        merchant.add_field(name='Merchant', value='Welcome to my shop! \n 1) Shop \n 2) Leave')
        merchant.set_image(url='https://i.etsystatic.com/7169212/r/il/f3a8c3/1248095931/il_570xN.1248095931_d5ty.jpg')
        await ctx.send(embed=merchant)
        replyMerch = await self.client.wait_for('message', check=check, timeout=60)
        if replyMerch.content == '1':
            embed_shop = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_shop.add_field(name='1', value='Little healing potion [100 Gold] - heal 25% HP')
            embed_shop.add_field(name='2', value='Common healing potion [250 Gold] - heal 50% HP')
            embed_shop.add_field(name='3', value='Big healing potion [500 Gold] - heal 100% HP')
            if self.users[member_id]['type'] == 'cat':
                embed_shop.add_field(name='4', value='Naginata 薙刀 [1500 Gold] - Provides 27 additional attack | weapon')
                embed_shop.add_field(name='5', value='Cat scarf [300 Gold] - 1 armor 2 agility | trinket')
                embed_shop.add_field(name='6', value='Elven Leather Armor [2000 Gold] - 6 armor 3 agility | armor')
                embed_shop.add_field(name='7',
                                     value='Demonic Katana 鬼の歯[12000 Gold] - Provides 101 additional attack + 10 agility - 10 strength | weapon')
                embed_shop.add_field(name='8', value='Agility band [1500 Gold] - 7 agility | trinket')
                embed_shop.add_field(name='9', value='Samurai armor[20000 Gold] - 30 armor | armor')
            if self.users[member_id]['type'] == 'magic':
                embed_shop.add_field(name='4',
                                     value='Inteligence book - [2500 Gold] Read it and gain + 10 intelligence| magic book')
                embed_shop.add_field(name='5',
                                     value='Witch hat - [1000 Gold] 3 intelligence 1 armor | trinket')
                embed_shop.add_field(name='6',
                                     value="Wizard's robe - [3000 Gold] 8 intelligence 3 armor | armor")
                embed_shop.add_field(name='7',
                                     value='Secret arcane tome - [12000 Gold] Read it and gain + 50 inteligence| magic book')
                embed_shop.add_field(name='8',
                                     value='??? - [50000 Gold] ??? Description: piece of the past universe | trinket')
                embed_shop.add_field(name='9',
                                     value='Grand Wizard robe - [8000 Gold] 14 intelligence 10 armor| armor')
            if self.users[member_id]['type'] == 'common':
                embed_shop.add_field(name='4', value='Wide sword [500 Gold] - Provides 10 additional attack | weapon')
                embed_shop.add_field(name='5',
                                     value='Amulet of defence [600 Gold] - 6 armor 3 strength 3 agility | trinket')
                embed_shop.add_field(name='6', value='Chain-mail [1200 Gold] - 25 armor | armor')
                embed_shop.add_field(name='7',
                                     value='Paladin sword [7000 Gold] - Provides 52 additional attack | weapon')
                embed_shop.add_field(name='8', value='Essence of attack [1500 Gold] - 8 agility | trinket')
                embed_shop.add_field(name='9',
                                     value='Paladin armor[8000 Gold] - 40 armor 10 strength 3 agility | armor')
            if self.users[member_id]['type'] == 'heavy':
                embed_shop.add_field(name='4', value='Chopper [1500 Gold] - Provides 25 additional attack | weapon')
                embed_shop.add_field(name='5',
                                     value='Dragon scale [1600 Gold] - 12 strength 3 agility | trinket')
                embed_shop.add_field(name='6', value='Heavy armor [3200 Gold] - 40 armor | armor')
                embed_shop.add_field(name='7',
                                     value='True dragon sword [9500 Gold] - Provides 60 additional attack | weapon')
                embed_shop.add_field(name='8',
                                     value='Soul awakening [11500 Gold] - + 30 ATTACK + 30 ARMOR + 30 STRENGTH + 30 AGILITY  | trinket')
                embed_shop.add_field(name='9',
                                     value='Dragon armor[20000 Gold] - 80 armor 20 strength 6 agility | armor')
            await ctx.send(embed=embed_shop)
            replyMerch = await self.client.wait_for('message', check=checkshop, timeout=60)
            if replyMerch.content == '1':
                price = 100
                self.users[member_id]['gold'] -= price
                if self.users[member_id]['gold'] < 0:
                    await ctx.send('You have not enough money to buy it')
                    self.users[member_id]['gold'] += price
                else:
                    self.users[member_id]['item1'] += 1
                    await ctx.send('Bought is successful')
            if replyMerch.content == '2':
                price = 250
                self.users[member_id]['gold'] -= price
                if self.users[member_id]['gold'] < 0:
                    await ctx.send('You have not enough money to buy it')
                    self.users[member_id]['gold'] += price
                else:
                    self.users[member_id]['item2'] += 1
                    await ctx.send('Bought is successful')
            if replyMerch.content == '3':
                price = 500
                self.users[member_id]['gold'] -= price
                if self.users[member_id]['gold'] < 0:
                    await ctx.send('You have not enough money to buy it')
                    self.users[member_id]['gold'] += price
                else:
                    self.users[member_id]['item3'] += 1
                    await ctx.send('Bought is successful')
            if replyMerch.content == '4':
                if self.users[member_id]['type'] == 'magic':
                    price = 2500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Gained 10 intelligence!')
                        self.users[member_id]['intelligence'] += 10
                if self.users[member_id]['type'] == 'cat':
                    price = 1500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 27
                if self.users[member_id]['type'] == 'heavy':
                    price = 1500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 25
                if self.users[member_id]['type'] == 'common':
                    price = 500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 10
            if replyMerch.content == '5':
                if self.users[member_id]['type'] == 'magic':
                    price = 1000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['armorstat'] += 1
                        self.users[member_id]['intelligence'] += 3

                if self.users[member_id]['type'] == 'cat':
                    price = 300
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['armorstat'] += 1
                        self.users[member_id]['agility'] += 2

                if self.users[member_id]['type'] == 'heavy':
                    price = 1600
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['strength'] += 12
                        self.users[member_id]['agility'] += 3

                if self.users[member_id]['type'] == 'common':
                    price = 600
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['armorstat'] += 6
                        self.users[member_id]['strength'] += 3
                        self.users[member_id]['agility'] += 3
            if replyMerch.content == '6':
                if self.users[member_id]['type'] == 'magic':
                    price = 3000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['intelligence'] += 8
                        self.users[member_id]['armorstat'] = 3
                if self.users[member_id]['type'] == 'cat':
                    price = 2000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['agility'] += 3
                        self.users[member_id]['armorstat'] = 6
                if self.users[member_id]['type'] == 'heavy':
                    price = 3200
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['armorstat'] = 40
                if self.users[member_id]['type'] == 'common':
                    price = 500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['armorstat'] = 25
            if replyMerch.content == '7':
                if self.users[member_id]['type'] == 'magic':
                    price = 12000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Gained 50 intelligence!')
                        self.users[member_id]['intelligence'] += 50
                if self.users[member_id]['type'] == 'cat':
                    price = 12000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 101
                if self.users[member_id]['type'] == 'heavy':
                    price = 9500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 60
                if self.users[member_id]['type'] == 'common':
                    price = 7000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Weapon equiped!')
                        self.users[member_id]['weapon'] = '✓'
                        self.users[member_id]['weaponstat'] = 52
            if replyMerch.content == '8':
                if self.users[member_id]['type'] == 'magic':
                    price = 50000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['armorstat'] += 100
                        self.users[member_id]['strength'] += 100
                        self.users[member_id]['intelligence'] += 300

                if self.users[member_id]['type'] == 'cat':
                    price = 1500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['agility'] += 7

                if self.users[member_id]['type'] == 'heavy':
                    price = 11500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['strength'] += 30
                        self.users[member_id]['agility'] += 30
                        self.users[member_id]['weaponstat'] += 30
                        self.users[member_id]['armorstat'] += 30

                if self.users[member_id]['type'] == 'common':
                    price = 1500
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('equiped!')
                        self.users[member_id]['agility'] += 8
            if replyMerch.content == '9':
                if self.users[member_id]['type'] == 'magic':
                    price = 8000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['intelligence'] += 14
                        self.users[member_id]['armorstat'] = 10
                if self.users[member_id]['type'] == 'cat':
                    price = 20000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['agility'] += 10
                        self.users[member_id]['armorstat'] = 30
                if self.users[member_id]['type'] == 'heavy':
                    price = 20000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['armorstat'] = 80
                        self.users[member_id]['strength'] += 20
                        self.users[member_id]['agility'] += 6
                if self.users[member_id]['type'] == 'common':
                    price = 8000
                    self.users[member_id]['gold'] -= price
                    if self.users[member_id]['gold'] < 0:
                        await ctx.send('You have not enough money to buy it')
                        self.users[member_id]['gold'] += price
                    else:
                        await ctx.send('Armor equiped')
                        self.users[member_id]['armor'] = '✓'
                        self.users[member_id]['armorstat'] = 40
                        self.users[member_id]['strength'] += 10
                        self.users[member_id]['agility'] += 3

        if replyMerch.content == '2':
            await ctx.send('See you!')

    @commands.command()
    async def rpgtreasure(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        embed_treasurment = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_treasurment.add_field(name='Treasure menu',
                                    value=f"Welcome to treasure menu! Right now you have {self.users[member_id]['treasure']} treasure box. Wanna open it? Print ``$treasureopen`` Wanna see more info about treasures and loot in them? Print ``$treasureinfo``")
        embed_treasurment.set_image(
            url='https://vignette.wikia.nocookie.net/overlordmaruyama/images/d/d2/Overlord_EP11_044.png/revision/latest?cb=20150916115130')
        await ctx.send(embed=embed_treasurment)

    @commands.command()
    async def treasureinfo(self, ctx):
        embed_info_t = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_info_t.add_field(name='Information',
                               value='LOOT: \n Demonic armor 0.03% \n Demonic Weapon 0.075% \n Demonic trinket 0.085% \n Titan forged armor 0.1% \n Titan forged weapon 0.2% \n Titan forged trinket 0.3% \n +85 treasures 0.5% \n +48 treasures 0.8%')
        await ctx.send(embed=embed_info_t)

    @commands.command()
    async def treasureopen(self, ctx, box_number: int = None):
        member = ctx.author
        member_id = str(member.id)
        box_number = 1 if not box_number else box_number
        embed_treasure = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_treasure.add_field(name='Treasure',
                                 value=f"Trying to open {box_number} treasure. Right now you have {self.users[member_id]['treasure']} treasure boxes.")
        self.users[member_id]['treasure'] -= box_number
        if self.users[member_id]['treasure'] < 0:
            await ctx.send('Not enough boxes to open!')
            self.users[member_id]['treasure'] += box_number
        else:
            for i in range(0, box_number):
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                c = random.randint(1, 100)
                if (a == c and a == b) or (b == c and b == a) or (c == a and c == b):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. WOOOOOW IT'S THE BEST THAT YOU CAN GET \n ドラゴンスキン [Demonic] | armor (+3650 armor, +2110 agility + 1160 strength)")
                    await ctx.send(embed=embed_prize)
                if (a + 1 == b or a - 1 == b) and (a + 1 == c or a - 1 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. WOOOOOW IT'S THE BEST THAT YOU CAN GET \n 死をもたらす者 [Demonic] (+8000 attack + 4000 agility) | weapon  or\n  [Demonic tome]| magic book (+3000 intelligence)")
                    await ctx.send(embed=embed_prize)
                if (a + 2 == b or a - 2 == b) and (a + 2 == c or a - 2 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. WOOOOOW IT'S THE BEST THAT YOU CAN GET \n すべて破壊的 [Demonic] (+ 2000 armor + 2000 agility + 1000 strength + 1500 intelligence if mage) ")
                    await ctx.send(embed=embed_prize)
                if (a + 3 == b or a - 3 == b) and (a + 3 == c or a - 3 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor Armor [Titan forged] | armor (+1800 armor, +910 agility + 660 strength)")
                    await ctx.send(embed=embed_prize)
                if (a + 4 == b or a - 4 == b) and (a + 4 == c or a - 4 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor Armor [Titan forged] | armor (+1800 armor, +910 agility + 660 strength)")
                    await ctx.send(embed=embed_prize)
                if (a + 5 == b or a - 5 == b) and (a + 5 == c or a - 5 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor weapon [Titan forged] | weapon (+2500 attack + 1000 agility + 500 strength) or \n [Titan book] +1500 intelligence")
                    await ctx.send(embed=embed_prize)
                if (a + 6 == b or a - 6 == b) and (a + 6 == c or a - 6 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor weapon [Titan forged] | weapon (+2500 attack + 1000 agility + 500 strength) or \n [Titan book] +1500 intelligence")
                    await ctx.send(embed=embed_prize)
                if (a + 7 == b or a - 7 == b) and (a + 7 == c or a - 7 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor amulet [Titan forged] | weapon (+500 armor + 500 strength + 500 agility + 500 intelligence if mage")
                    await ctx.send(embed=embed_prize)
                if (a + 8 == b or a - 8 == b) and (a + 8 == c or a - 8 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n Ancestor amulet [Titan forged] | weapon (+500 armor + 500 strength + 500 agility + 500 intelligence if mage")
                    await ctx.send(embed=embed_prize)
                if (a + 9 == b or a - 9 == b) and (a + 9 == c or a - 9 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n +85 treasures")
                    await ctx.send(embed=embed_prize)
                    self.users[member_id]['treasure'] += 85
                if (a + 10 == b or a - 10 == b) and (a + 10 == c or a - 10 == c):
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. Not bad \n +48 treasures")
                    await ctx.send(embed=embed_prize)
                    self.users[member_id]['treasure'] += 48
                else:
                    embed_prize = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embed_prize.add_field(name='Prize',
                                          value=f"Your result is {a} {b} {c}. nep nep")
                    await ctx.send(embed=embed_prize)

    @commands.command()
    async def ttest(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        self.users[member_id]['treasure'] = 999999
        await ctx.send('gg')

    @commands.command()
    async def shoptest(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        self.users[member_id]['gold'] = 999999
        await ctx.send('gg')

    @commands.command()
    async def rpgheal(self, ctx):
        member = ctx.author
        member_id = str(member.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2')

            return inner_check

        embed_nurse = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_nurse.add_field(name='Nurse',
                              value='Wanna heal? Of course want. You have no choice :smiling_imp: \n 1) Heal \n 2) Leave')
        embed_nurse.set_image(
            url='https://i.pinimg.com/originals/87/45/43/8745433c3721e80fd94c3e7210a9eb95.jpg')
        await ctx.send(embed=embed_nurse)
        replyNurse = await self.client.wait_for('message', check=check, timeout=60)
        if replyNurse.content == '1':
            await ctx.send('You was healed ;) ')
            amount_of_money = self.users[member_id]['strength'] - self.users[member_id]['health']
            self.users[member_id]['gold'] -= amount_of_money
            self.users[member_id]['health'] = self.users[member_id]['strength']
        if replyNurse.content == '2':
            await ctx.send('Ehh... See you are. Come back soon')

    @commands.command()
    async def rpgblacksmith(self, ctx):
        member = ctx.author
        member_id = str(member.id)

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3', '4')

            return inner_check

        embed_nurse = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_nurse.add_field(name='Blacksmith',
                              value='Upgrade armor and weapons! Craft armor and weapon!\n 1) Upgrade armor \n2) Upgrade weapon \n 3) Crafting menu \n4) Leave')
        embed_nurse.set_image(
            url='https://www.elsetge.cat/myimg/f/167-1675138_pixiv-art-1080p-hd-wallpaper-background-anime-blacksmith.jpg')
        await ctx.send(embed=embed_nurse)
        replySmith = await self.client.wait_for('message', check=check, timeout=60)
        if replySmith.content == '1':
            await ctx.send('Armor upgraded ')
        if replySmith.content == '2':
            await ctx.send('Weapon upgraded')
        if replySmith.content == '3':
            await ctx.send('Later')
        if replySmith.content == '4':
            await ctx.send('Goodbye. Good luck.')

    @commands.command()
    async def rpginfo(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        embed_info = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed_info.set_author(name=f'RPG - {member}', icon_url=member.avatar_url)
        embed_info.add_field(name='Character info',
                             value=f" Your level - {self.users[member_id]['level']}\n Strength - {self.users[member_id]['strength']}:shield: \n Agility - {self.users[member_id]['agility']}:crossed_swords: \n Intelligence - {self.users[member_id]['intelligence']}:mage: \n Current health - {self.users[member_id]['health']} :heart: \n Your Karma - {self.users[member_id]['karma']}:sparkles: \n Your money - {self.users[member_id]['gold']}:moneybag: gold  ",
                             inline=True)
        if self.users[member_id]['weapon'] == '✓':
            embed_info.add_field(name='Weapon', value=f"Weapon stat - {self.users[member_id]['weaponstat']}")
        if self.users[member_id]['armor'] == '✓':
            embed_info.add_field(name='Armor', value=f"Armor stat - {self.users[member_id]['armorstat']}")
        await ctx.send(embed=embed_info)

    @commands.command()
    async def rpgplayrestart(self, ctx):
        member = ctx.author
        member_id = str(member.id)
        self.users[member_id]['storyfantasy'] = 1
        await ctx.send('Story restarted! Parameters saved!')

    @commands.command()
    async def rpgmagic(self, ctx):
        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1')

            return inner_check

        member = ctx.author
        member_id = str(member.id)
        await ctx.send('Please wait...Calculating your level and race')
        if self.users[member_id]['karma'] == -30:
            Magic_Succubus = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            Magic_Succubus.add_field(name='Magic learning menu!',
                                     value='1) LVL 12 - [Demonic change]:<Choose the magic effect in fight! \n ```1) Damage yourself on 2 damage and deal 2*your intellegince damage \n2) Damage your enemy on round of 0.3 of your intelligence and heal yourself on amount of damage```> ``` if you have enough lvl to learn skill write in chat 1```')
            Magic_Succubus.set_image(url='http://cache.desktopnexus.com/thumbseg/295/295520-bigthumbnail.jpg')
            await ctx.send(embed=Magic_Succubus)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '1':
                if self.users[member_id]['level'] >= 12:
                    if not self.users[member_id]['Succub_Skill_1'] == 'Learned':
                        self.users[member_id]['Succub_Skill_1'] = 'Learned'
                        await ctx.send('You learned a new skill!')
                    else:
                        await ctx.send('You already know this skill!')
        if self.users[member_id]['karma'] == 5:
            Magic_Elfius = discord.Embed(
                color=discord.Colour.green()
            )
            Magic_Elfius.add_field(name='Magic learning menu',
                                   value='1) LVL 12 - [Mind Blow]:<Desintegration of enemy mind. round of + 0.5 damage for every your intelligence. How it works? If you have 9 intelligence your damage will be 0.5+1+1.5+2+2.5+3+3.5+4+4.5=22.5=23> ``` if you have enough lvl to learn skill write in chat 1```')
            Magic_Elfius.set_image(
                url='https://www.wallpapermaiden.com/image/2019/03/12/fire-emblem-heroes-elf-ears-hoodie-coat-magic-heterochromia-anime-games-31123.png')
            await ctx.send(embed=Magic_Elfius)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '1':
                if self.users[member_id]['level'] >= 12:
                    if not self.users[member_id]['Elf_Skill_1'] == 'Learned':
                        self.users[member_id]['Elf_Skill_1'] = 'Learned'
                        await ctx.send('You learned a new skill!')
                    else:
                        await ctx.send('You already know this skill!')
        if self.users[member_id]['karma'] == 2:
            Magic_Draconis = discord.Embed(
                color=discord.Colour.red()
            )
            Magic_Draconis.add_field(name='Magic learning menu',
                                     value='1) LVL 12 - [Fire breath]:<Breath on your enemy with your draconic nature and deal 0.5*your strength damage!>')
            Magic_Draconis.set_image(
                url='https://image.myanimelist.net/ui/t7qrb70KKlmskIhjtymKK11gNPDipVGeEOy6EW31bCXtnNW3IrQilcYF2mNRxSSsN84_72hJTsQ8-NGYxQV3TYm1ib7FSGoFQ-vpzs4-TcK0nUkiCnxb7nS23iB3MwYi')
            await ctx.send(embed=Magic_Draconis)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '1':
                if self.users[member_id]['level'] >= 12:
                    if not self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                        self.users[member_id]['Dragon_Skill_1'] = 'Learned'
                        await ctx.send('You learned a new skill!')
                    else:
                        await ctx.send('You already know this skill!')
        if self.users[member_id]['karma'] == 0 or self.users[member_id]['karma'] == 3:
            await ctx.send('No magic for your race. Sorry!')

    @commands.command()
    async def rpgplay(self, ctx):
        elf_n = 0.5
        old_int = 0
        magic_damage = 0
        physical_damage = 0

        def check(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2')

            return inner_check

        def check3(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2', '3')

            return inner_check

        def checkfight(author):
            def inner_check(message):
                return message.author == author and message.content in (
                    '1', '2')

            return inner_check

        member = ctx.author
        member_id = str(member.id)
        if self.users[member_id]['storyfantasy'] == 1:
            self.users[member_id]['health'] = self.users[member_id]['strength']
            e1 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            e1.add_field(name='You waking up', value="Seems it was a nightmare! Oh my. Someone knocking in my door... "
                                                     "I wanna sleep more, why so early? \n - I'm royal ambassador. "
                                                     "Please, open the door, it's important. \n Well. Seems i must wake up and go. Or maybe sleep 10 minutes?:thinking: \n 1)Wake up \n 2) Sleep")
            e1.set_image(url='https://i.pinimg.com/236x/c5/0c/57/c50c57ae5d6254d6dbf00062b3669934.jpg')
            await ctx.send(embed=e1)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '1':
                self.users[member_id]['storyfantasy'] = 2

            if reply.content == '2':
                if self.users[member_id]['ach1'] == "\u274c":
                    self.users[member_id]['ach1'] = "\u2713"
                    embedach1 = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedach1.add_field(name='Achievment',
                                        value=f"Achievment 'Sweet dreams' received! \n {self.users[member_id]['ach1']}")
                    await ctx.send(embed=embedach1)
                    await ctx.send('Sweet dreams! :D Your journey ends here!')
                else:
                    await ctx.send('Sweet dreams! :D Your journey ends here!')

        if self.users[member_id]['storyfantasy'] == 2:
            e2 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            e2.add_field(name='Ambassador',
                         value='- **giving you letter** so. Good luck, your path leads to the king. \n In letter said: \n "'
                               'General meeting of heroes of the past, '
                               'present and future! A terrible event is coming soon, and the kingdom and king need you all for protection! Together,'
                               'we are an indestructible force that will stop future destruction. " \n I need some time and after it moving forward. \n 1) Move forward \n 2) Save and quit')
            e2.set_image(url='https://i.pinimg.com/originals/36/e0/0b/36e00b25521727bfa20fe11e4626bc7c.jpg')
            await ctx.send(embed=e2)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '1':
                self.users[member_id]['storyfantasy'] = 3
            if reply.content == '2':
                await ctx.send('Game process saved!')

        if self.users[member_id]['storyfantasy'] == 3:
            e3 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            e3.add_field(name='Event',
                         value='You was peacefully walking your way but suddenly wagon driver asked you to stop and help him. \n 1) Help [Quest] \n 2) Reject \n 3) Save and quit')
            e3.set_image(
                url='https://image.myanimelist.net/ui/fkHpHKa8ZRvgXF3EvLfxXJwxEUD0Uw9ky_kPrNcD6QQzbbKiV4tAUqDc5IPl7QwEnkSqGtb7qVwFxDTT41o8Tk5vPSf4AvcAVxSAfTVWhz4o37j79Yzb0JdDormoj86f9OVwKE2YMCz6JB_GXdrZNGrjPZeWgvVXypeL13ZQ-I1dGvtJYTRuogEKJUHLCg26')
            await ctx.send(embed=e3)
            reply = await self.client.wait_for('message', check=check3, timeout=180)
            if reply.content == '2':
                self.users[member_id]['storyfantasy'] = 4

            if reply.content == '3':
                await ctx.send('Game process saved!')
            if reply.content == '1':
                e_quest_3_1 = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                e_quest_3_1.add_field(name='Quest',
                                      value="- I'm need help in protecting my wagon from bandits! I will reward you. So, lets go.")
                e_quest_3_1.set_image(
                    url='https://www.anime-planet.com/images/characters/wagon-driver-121621.jpg?t=1488737841')
                await ctx.send(embed=e_quest_3_1)

                e_quest_3_1_battle = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                e_quest_3_1_battle.add_field(name='Battle',
                                             value='Bandits attacking wagon! Defend it!\n 1) Fight \n 2) Save and quit\n [GAME SYSTEM MESSAGE] \n <Race players who can learn magic (Elfs, Succubus and Draconis) please save and quit and learn magic with $rpgmagic for correct fight! Or you will just die in fight!> ```$rpgmagic```')
                await ctx.send(embed=e_quest_3_1_battle)
                reply = await self.client.wait_for('message', check=check, timeout=180)
                if reply.content == '2':
                    await ctx.send('Game process saved!')
                if reply.content == '1':
                    bandithp = 22
                    while bandithp > 0:
                        if self.users[member_id]['health'] <= 0:
                            embed_death = discord.Embed(
                                color=discord.Colour.dark_red()
                            )
                            embed_death.add_field(name='Death', value='YOU DIED')
                            embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                            await ctx.send(embed=embed_death)
                            self.users[member_id]['storyfantasy'] = -1
                            break
                        e_f = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        e_f.add_field(name='Bandit', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                        e_f.set_image(
                            url='https://i.pinimg.com/474x/6b/15/b0/6b15b06ae23f690e20968bc87c370831--hot-anime-anime-manga.jpg')

                        await ctx.send(embed=e_f)

                        reply3 = await self.client.wait_for('message', check=check, timeout=180)
                        dop_damage = 0
                        if reply3.content == '1':
                            if self.users[member_id]['karma'] == -30:
                                e_f_m_s = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                    e_f_m_s.add_field(name='1) Demonic change', value='Choose one of 2 effects!')
                                await ctx.send(embed=e_f_m_s)
                                await ctx.send('choose skill!')
                                reply_succ = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_succ.content == '1':
                                    await ctx.send('choose effect of skill!')
                                    await ctx.send(
                                        '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                    reply_succ1 = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_succ1.content == '1':
                                        self.users[member_id]['health'] -= 2
                                        magic_damage = 2 * self.users[member_id]['intelligence']
                                    if reply_succ1.content == '2':
                                        magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                        self.users[member_id]['health'] += magic_damage
                                        if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                            self.users[member_id]['health'] = self.users[member_id]['strength']
                                    bandithp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandithp}')
                            if self.users[member_id]['karma'] == 5:
                                e_f_m_f = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                    e_f_m_f.add_field(name='1) Mind Blow',
                                                      value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                                await ctx.send(embed=e_f_m_f)
                                await ctx.send('choose skill!')
                                reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_elf.content == '1':
                                    a = self.users[member_id]['intelligence']
                                    for i in range(1, a + 1):
                                        magic_damage += elf_n
                                        elf_n += 0.5
                                    magic_damage = round(magic_damage)
                                    bandithp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandithp}')
                                    magic_damage = 0
                                    elf_n = 0.5
                            if self.users[member_id]['karma'] == 2:
                                await ctx.send('1) Physical attack \n 2) Magic attack')
                                dragon_await = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if dragon_await.content == '1':
                                    old_int = self.users[member_id]['intelligence']
                                    self.users[member_id]['intelligence'] = 0
                                if dragon_await.content == '2':
                                    e_f_m_d = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                        e_f_m_d.add_field(name='1) Dragon breath',
                                                          value='0.5 * your strength magic damage')
                                        await ctx.send(embed=e_f_m_d)
                                        await ctx.send('choose skill!')
                                        reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                                  timeout=180)
                                        if reply_dragon.content == '1':
                                            magic_damage = round(0.5 * self.users[member_id]['strength'])
                                            bandithp -= magic_damage
                                            await ctx.send(
                                                f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandithp}')

                            if self.users[member_id]['intelligence'] == 0:
                                physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                                 self.users[member_id]['agility'] + 3) + \
                                                  self.users[member_id]['weaponstat']
                                bandithp -= physical_damage
                                await ctx.send(
                                    f'You did {physical_damage} damage to bandit!Good punch. Now his HP is {bandithp}')
                                self.users[member_id]['intelligence'] = old_int
                            if bandithp > 0:
                                mob_damage = random.randint(3, 7) - self.users[member_id]['armorstat']
                                if mob_damage < 0:
                                    mob_damage = 0
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if reply3.content == '2':
                            dodgechance = random.randint(1, 3)
                            mob_damage = random.randint(1, 3)
                            if dodgechance == 1:
                                mob_damage = 0
                                await ctx.send('Succesful dodge!')
                            if dodgechance == 2:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                            if dodgechance == 3:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                    if bandithp <= 0:
                        embedslimewin = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        exp_slime = random.randint(49, 78)
                        gold_slime = random.randint(17, 26)
                        if self.users[member_id]['karma'] == 0:
                            gold_slime += 39
                        embedslimewin.add_field(name='Win',
                                                value=f"You won the fight against bandit with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                        self.users[member_id]['exp'] += exp_slime
                        self.users[member_id]['gold'] += gold_slime
                        await ctx.send(embed=embedslimewin)
                        if self.lvl_up(member_id):
                            self.users[member_id]['strength'] += 1
                            self.users[member_id]['agility'] += 1
                            if self.users[member_id]['intelligence'] > 0:
                                self.users[member_id]['intelligence'] += 1
                            await ctx.send(
                                f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                        e_quest_3_2_battle = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        e_quest_3_2_battle.add_field(name='Battle',
                                                     value='Last bandit attacking you! Protect yourself! Fight !')
                        await ctx.send(embed=e_quest_3_2_battle)
                        bandit2hp = 48
                        while bandit2hp > 0:
                            if self.users[member_id]['health'] <= 0:
                                embed_death = discord.Embed(
                                    color=discord.Colour.dark_red()
                                )
                                embed_death.add_field(name='Death', value='YOU DIED')
                                embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                                await ctx.send(embed=embed_death)
                                self.users[member_id]['storyfantasy'] = -1
                                break
                            e_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            e_f.add_field(name='Bandit', value=f'{bandit2hp} HP \n 1) Attack 2) Dodge')
                            e_f.set_image(
                                url='https://static.zerochan.net/Parashi.full.367728.jpg')

                            await ctx.send(embed=e_f)

                            reply3 = await self.client.wait_for('message', check=check, timeout=180)
                            dop_damage = 0
                            if reply3.content == '1':
                                if self.users[member_id]['karma'] == -30:
                                    e_f_m_s = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                        e_f_m_s.add_field(name='1) Demonic change',
                                                          value='Choose one of 2 effects!')
                                    await ctx.send(embed=e_f_m_s)
                                    await ctx.send('choose skill!')
                                    reply_succ = await self.client.wait_for('message', check=checkfight,
                                                                            timeout=180)
                                    if reply_succ.content == '1':
                                        await ctx.send('choose effect of skill!')
                                        await ctx.send(
                                            '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                        reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                                 timeout=180)
                                        if reply_succ1.content == '1':
                                            self.users[member_id]['health'] -= 2
                                            magic_damage = 2 * self.users[member_id]['intelligence']
                                        if reply_succ1.content == '2':
                                            magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                            self.users[member_id]['health'] += magic_damage
                                            if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                                self.users[member_id]['health'] = self.users[member_id]['strength']
                                        bandit2hp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandit2hp}')
                                if self.users[member_id]['karma'] == 5:
                                    e_f_m_f = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                        e_f_m_f.add_field(name='1) Mind Blow',
                                                          value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                                    await ctx.send(embed=e_f_m_f)
                                    await ctx.send('choose skill!')
                                    reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_elf.content == '1':
                                        a = self.users[member_id]['intelligence']
                                        for i in range(1, a + 1):
                                            magic_damage += elf_n
                                            elf_n += 0.5
                                        magic_damage = round(magic_damage)
                                        bandit2hp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandit2hp}')
                                        magic_damage = 0
                                        elf_n = 0.5
                                if self.users[member_id]['karma'] == 2:
                                    await ctx.send('1) Physical attack \n 2) Magic attack')
                                    dragon_await = await self.client.wait_for('message', check=checkfight,
                                                                              timeout=180)
                                    if dragon_await.content == '1':
                                        old_int = self.users[member_id]['intelligence']
                                        self.users[member_id]['intelligence'] = 0
                                    if dragon_await.content == '2':
                                        e_f_m_d = discord.Embed(
                                            color=discord.Colour.dark_purple()
                                        )
                                        if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                            e_f_m_d.add_field(name='1) Dragon breath',
                                                              value='0.5 * your strength magic damage')
                                            await ctx.send(embed=e_f_m_d)
                                            await ctx.send('choose skill!')
                                            reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                                      timeout=180)
                                            if reply_dragon.content == '1':
                                                magic_damage = round(0.5 * self.users[member_id]['strength'])
                                                bandit2hp -= magic_damage
                                                await ctx.send(
                                                    f'You did {magic_damage} damage to bandit!Good punch. Now his HP is {bandit2hp}')

                                if self.users[member_id]['intelligence'] == 0:
                                    physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                                     self.users[member_id]['agility'] + 3) + \
                                                      self.users[member_id]['weaponstat']
                                    bandit2hp -= physical_damage
                                    await ctx.send(
                                        f'You did {physical_damage} damage to bandit!Good punch. Now his HP is {bandit2hp}')
                                    self.users[member_id]['intelligence'] = old_int
                                if bandit2hp > 0:
                                    mob_damage = random.randint(4, 7) - self.users[member_id]['armorstat']
                                    if mob_damage < 0:
                                        mob_damage = 0
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                            if reply3.content == '2':
                                dodgechance = random.randint(1, 3)
                                mob_damage = random.randint(3, 6)
                                if dodgechance == 1:
                                    mob_damage = 0
                                    await ctx.send('Succesful dodge!')
                                if dodgechance == 2:
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                                if dodgechance == 3:
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bandit gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                        if bandit2hp <= 0:
                            embedslimewin = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            exp_slime = random.randint(49, 78)
                            gold_slime = random.randint(17, 26)
                            if self.users[member_id]['karma'] == 0:
                                gold_slime += 39
                            embedslimewin.add_field(name='Win',
                                                    value=f"You won the fight against bandit with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                            self.users[member_id]['exp'] += exp_slime
                            self.users[member_id]['gold'] += gold_slime
                            await ctx.send(embed=embedslimewin)
                            if self.lvl_up(member_id):
                                self.users[member_id]['strength'] += 1
                                self.users[member_id]['agility'] += 1
                                if self.users[member_id]['intelligence'] > 0:
                                    self.users[member_id]['intelligence'] += 1
                                await ctx.send(
                                    f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                            quest_complete = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            quest_complete.add_field(name='Quest completed succesfully',
                                                     value='Wow! Your skills are impressive. Without you my chance to stay alive was zero! Thanks and take a reward!',
                                                     inline=True)
                            quest_complete.add_field(name='Reward', value=f'+ 200 gold + 300 exp', inline=True)
                            self.users[member_id]['exp'] += 300
                            self.users[member_id]['gold'] += 200
                            if self.lvl_up(member_id):
                                self.users[member_id]['strength'] += 1
                                self.users[member_id]['agility'] += 1
                                if self.users[member_id]['intelligence'] > 0:
                                    self.users[member_id]['intelligence'] += 1
                            await ctx.send(embed=quest_complete)
                            self.users[member_id]['storyfantasy'] = 4

        if self.users[member_id]['storyfantasy'] == 4:
            embed_duelanto = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_duelanto.add_field(name='Duelist',
                                     value="Let's bet your life and fight. Win or die. If you win i giving you 250 gold. \n 1) Fight 2) Go away 3) Save and quit")
            embed_duelanto.set_image(
                url='https://www.bestfunforall.com/wallpaperbetter/imgs/Anime%20girl%20katana%20butterfly%20temple%20wallpaper%20%2018.jpg')
            await ctx.send(embed=embed_duelanto)
            reply = await self.client.wait_for('message', check=check3, timeout=180)
            if reply.content == '1':
                bandithp = 100
                while bandithp > 0:
                    if self.users[member_id]['health'] <= 0:
                        embed_death = discord.Embed(
                            color=discord.Colour.dark_red()
                        )
                        embed_death.add_field(name='Death', value='YOU DIED')
                        embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                        await ctx.send(embed=embed_death)
                        self.users[member_id]['storyfantasy'] = -1
                        break
                    e_f = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    e_f.add_field(name='Duelist', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                    e_f.set_image(
                        url='https://i.pinimg.com/originals/6d/e6/e3/6de6e35effe9482c7e40a7c3e7ade88f.jpg')

                    await ctx.send(embed=e_f)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['karma'] == -30:
                            e_f_m_s = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                e_f_m_s.add_field(name='1) Demonic change', value='Choose one of 2 effects!')
                            await ctx.send(embed=e_f_m_s)
                            await ctx.send('choose skill!')
                            reply_succ = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_succ.content == '1':
                                await ctx.send('choose effect of skill!')
                                await ctx.send(
                                    '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                reply_succ1 = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_succ1.content == '1':
                                    self.users[member_id]['health'] -= 2
                                    magic_damage = 2 * self.users[member_id]['intelligence']
                                if reply_succ1.content == '2':
                                    magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                    self.users[member_id]['health'] += magic_damage
                                    if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                        self.users[member_id]['health'] = self.users[member_id]['strength']
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Duelist!Good punch. Now his HP is {bandithp}')
                        if self.users[member_id]['karma'] == 5:
                            e_f_m_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                e_f_m_f.add_field(name='1) Mind Blow',
                                                  value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                            await ctx.send(embed=e_f_m_f)
                            await ctx.send('choose skill!')
                            reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_elf.content == '1':
                                a = self.users[member_id]['intelligence']
                                for i in range(1, a + 1):
                                    magic_damage += elf_n
                                    elf_n += 0.5
                                magic_damage = round(magic_damage)
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Duelist!Good punch. Now his HP is {bandithp}')
                                magic_damage = 0
                                elf_n = 0.5
                        if self.users[member_id]['karma'] == 2:
                            await ctx.send('1) Physical attack \n 2) Magic attack')
                            dragon_await = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if dragon_await.content == '1':
                                old_int = self.users[member_id]['intelligence']
                                self.users[member_id]['intelligence'] = 0
                            if dragon_await.content == '2':
                                e_f_m_d = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                    e_f_m_d.add_field(name='1) Dragon breath',
                                                      value='0.5 * your strength magic damage')
                                    await ctx.send(embed=e_f_m_d)
                                    await ctx.send('choose skill!')
                                    reply_dragon = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_dragon.content == '1':
                                        magic_damage = round(0.5 * self.users[member_id]['strength'])
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Duelist!Good punch. Now his HP is {bandithp}')

                        if self.users[member_id]['intelligence'] == 0:
                            physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                             self.users[member_id]['agility'] + 3) + \
                                              self.users[member_id]['weaponstat']
                            bandithp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to Duelist!Good punch. Now his HP is {bandithp}')
                            self.users[member_id]['intelligence'] = old_int
                        if bandithp > 0:
                            mob_damage = random.randint(0, 13) - self.users[member_id]['armorstat']
                            if mob_damage < 0:
                                mob_damage = 0
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Duelist gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(1, 3)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!')
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Duelist gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if dodgechance == 3:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Duelist gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                if bandithp <= 0:
                    embedslimewin = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    exp_slime = random.randint(200, 300)
                    gold_slime = random.randint(0, 0)
                    if self.users[member_id]['karma'] == 0:
                        gold_slime += 100
                    embedslimewin.add_field(name='Win',
                                            value=f"You won the fight against bandit with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                    self.users[member_id]['exp'] += exp_slime
                    self.users[member_id]['gold'] += gold_slime
                    await ctx.send(embed=embedslimewin)
                    self.users[member_id]['storyfantasy'] = 5
                    if self.lvl_up(member_id):
                        self.users[member_id]['strength'] += 1
                        self.users[member_id]['agility'] += 1
                        if self.users[member_id]['intelligence'] > 0:
                            self.users[member_id]['intelligence'] += 1
                        await ctx.send(
                            f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                    await ctx.send('Nice fight!Take your gold!')
                    await ctx.send('+250 gold')
                    self.users[member_id]['gold'] += 250
            if reply.content == '2':
                self.users[member_id]['storyfantasy'] = 5
            if reply.content == '3':
                await ctx.send('Game process saved')
        if self.users[member_id]['storyfantasy'] == 5:
            pre_event = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            pre_event.add_field(name='Nothing interesting',
                                value='You just continue to go, nothing interesting \n 1) Go 2) Save and quit')
            pre_event.set_image(
                url='https://c4.wallpaperflare.com/wallpaper/67/775/785/artwork-road-drawing-anime-wallpaper-preview.jpg')
            await ctx.send(embed=pre_event)
            reply = await self.client.wait_for('message', check=checkfight, timeout=180)
            if reply.content == '1':
                self.users[member_id]['storyfantasy'] = 6
            if reply.content == '2':
                await ctx.send('Game process saved')
        if self.users[member_id]['storyfantasy'] == 6:
            event_blood_moon = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            event_blood_moon.add_field(name='Event', value='Darkness is hiding sun. Eclipse?')
            event_blood_moon.set_image(url='http://pm1.narvii.com/6563/3d6f72d2dc32b0e4211ee9427c952580bbd479a0_hq.jpg')
            await ctx.send(embed=event_blood_moon)
            event_blood_moon1 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            event_blood_moon1.add_field(name='Event', value='Sky color now is red')
            event_blood_moon1.set_image(
                url='https://66.media.tumblr.com/bd91060d4af2b1de882835f0b2552a4a/tumblr_pvwkal4foE1sqn0mto1_500.gifv')
            await ctx.send(embed=event_blood_moon1)
            event_blood_moon2 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            event_blood_moon2.add_field(name='Event', value='You saw a strange shadow. Or is it was not a shadow?')
            event_blood_moon2.set_image(
                url='https://data.whicdn.com/images/199235849/original.png')
            await ctx.send(embed=event_blood_moon2)
            event_blood_moon3 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            event_blood_moon3.add_field(name='Town', value='You came in town and see it in fire. Oh my goodness!')
            event_blood_moon3.set_image(
                url='https://steamuserimages-a.akamaihd.net/ugc/101724518970937891/AF85D181E33984FFEABDCE574F6EC281E49D3F33/')
            await ctx.send(embed=event_blood_moon3)
            event_blood_moon4 = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            event_blood_moon4.add_field(name='Town',
                                        value='Almost all town in fire and now you see some monsters. Prepare for battle! \n 1) Battle 2) Save and quit')
            event_blood_moon4.set_image(
                url='https://celestialkitsune.files.wordpress.com/2010/03/howl-moving-castle_00056.jpg?w=640')
            await ctx.send(embed=event_blood_moon4)
            reply = await self.client.wait_for('message', check=check3, timeout=180)
            if reply.content == '2':
                await ctx.send('game process saved!')
            if reply.content == '1':
                pre_battle4 = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                pre_battle4.add_field(name='Battle', value='This big creatures eating people...')
                pre_battle4.set_image(url='https://pm1.narvii.com/6437/23c0fa9cb94d5d20394692c681bac6d76f54fbfc_hq.jpg')
                await ctx.send(embed=pre_battle4)
                bandithp = 1
                while bandithp > 0:
                    if self.users[member_id]['health'] <= 0:
                        embed_death = discord.Embed(
                            color=discord.Colour.dark_red()
                        )
                        embed_death.add_field(name='Death', value='YOU DIED')
                        embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                        await ctx.send(embed=embed_death)
                        self.users[member_id]['storyfantasy'] = -1
                        break
                    e_f = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    e_f.add_field(name='Bunny', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                    e_f.set_image(
                        url='https://vignette.wikia.nocookie.net/bloodc/images/8/83/Vlcsnap-2011-10-04-16h57m48s124.png/revision/latest?cb=20111004215819')

                    await ctx.send(embed=e_f)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['karma'] == -30:
                            e_f_m_s = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                e_f_m_s.add_field(name='1) Demonic change', value='Choose one of 2 effects!')
                            await ctx.send(embed=e_f_m_s)
                            await ctx.send('choose skill!')
                            reply_succ = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_succ.content == '1':
                                await ctx.send('choose effect of skill!')
                                await ctx.send(
                                    '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                reply_succ1 = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_succ1.content == '1':
                                    self.users[member_id]['health'] -= 2
                                    magic_damage = 2 * self.users[member_id]['intelligence']
                                if reply_succ1.content == '2':
                                    magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                    self.users[member_id]['health'] += magic_damage
                                    if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                        self.users[member_id]['health'] = self.users[member_id]['strength']
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                        if self.users[member_id]['karma'] == 5:
                            e_f_m_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                e_f_m_f.add_field(name='1) Mind Blow',
                                                  value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                            await ctx.send(embed=e_f_m_f)
                            await ctx.send('choose skill!')
                            reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_elf.content == '1':
                                a = self.users[member_id]['intelligence']
                                for i in range(1, a + 1):
                                    magic_damage += elf_n
                                    elf_n += 0.5
                                magic_damage = round(magic_damage)
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                magic_damage = 0
                                elf_n = 0.5
                        if self.users[member_id]['karma'] == 2:
                            await ctx.send('1) Physical attack \n 2) Magic attack')
                            dragon_await = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if dragon_await.content == '1':
                                old_int = self.users[member_id]['intelligence']
                                self.users[member_id]['intelligence'] = 0
                            if dragon_await.content == '2':
                                e_f_m_d = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                    e_f_m_d.add_field(name='1) Dragon breath',
                                                      value='0.5 * your strength magic damage')
                                    await ctx.send(embed=e_f_m_d)
                                    await ctx.send('choose skill!')
                                    reply_dragon = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_dragon.content == '1':
                                        magic_damage = round(0.5 * self.users[member_id]['strength'])
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')

                        if self.users[member_id]['intelligence'] == 0:
                            physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                             self.users[member_id]['agility'] + 3) + \
                                              self.users[member_id]['weaponstat']
                            bandithp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                            self.users[member_id]['intelligence'] = old_int
                        if bandithp > 0:
                            mob_damage = random.randint(113, 117) - self.users[member_id]['armorstat']
                            if mob_damage < 0:
                                mob_damage = 0
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(1, 3)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!')
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if dodgechance == 3:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                if bandithp <= 0:
                    embedslimewin = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    exp_slime = random.randint(349, 478)
                    gold_slime = random.randint(117, 126)
                    if self.users[member_id]['karma'] == 0:
                        gold_slime += 139
                    embedslimewin.add_field(name='Win',
                                            value=f"You won the fight against Bunny with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                    self.users[member_id]['exp'] += exp_slime
                    self.users[member_id]['gold'] += gold_slime
                    await ctx.send(embed=embedslimewin)
                    if self.lvl_up(member_id):
                        self.users[member_id]['strength'] += 1
                        self.users[member_id]['agility'] += 1
                        if self.users[member_id]['intelligence'] > 0:
                            self.users[member_id]['intelligence'] += 1
                        await ctx.send(
                            f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                    # вторая битва
                    bandithp = 1
                    while bandithp > 0:
                        if self.users[member_id]['health'] <= 0:
                            embed_death = discord.Embed(
                                color=discord.Colour.dark_red()
                            )
                            embed_death.add_field(name='Death', value='YOU DIED')
                            embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                            await ctx.send(embed=embed_death)
                            self.users[member_id]['storyfantasy'] = -1
                            break
                        e_f = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        e_f.add_field(name='Bunny', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                        e_f.set_image(
                            url='https://vignette.wikia.nocookie.net/bloodc/images/8/83/Vlcsnap-2011-10-04-16h57m48s124.png/revision/latest?cb=20111004215819')

                        await ctx.send(embed=e_f)

                        reply3 = await self.client.wait_for('message', check=check, timeout=180)
                        dop_damage = 0
                        if reply3.content == '1':
                            if self.users[member_id]['karma'] == -30:
                                e_f_m_s = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                    e_f_m_s.add_field(name='1) Demonic change', value='Choose one of 2 effects!')
                                await ctx.send(embed=e_f_m_s)
                                await ctx.send('choose skill!')
                                reply_succ = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_succ.content == '1':
                                    await ctx.send('choose effect of skill!')
                                    await ctx.send(
                                        '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                    reply_succ1 = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_succ1.content == '1':
                                        self.users[member_id]['health'] -= 2
                                        magic_damage = 2 * self.users[member_id]['intelligence']
                                    if reply_succ1.content == '2':
                                        magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                        self.users[member_id]['health'] += magic_damage
                                        if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                            self.users[member_id]['health'] = self.users[member_id]['strength']
                                    bandithp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                            if self.users[member_id]['karma'] == 5:
                                e_f_m_f = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                    e_f_m_f.add_field(name='1) Mind Blow',
                                                      value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                                await ctx.send(embed=e_f_m_f)
                                await ctx.send('choose skill!')
                                reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if reply_elf.content == '1':
                                    a = self.users[member_id]['intelligence']
                                    for i in range(1, a + 1):
                                        magic_damage += elf_n
                                        elf_n += 0.5
                                    magic_damage = round(magic_damage)
                                    bandithp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                    magic_damage = 0
                                    elf_n = 0.5
                            if self.users[member_id]['karma'] == 2:
                                await ctx.send('1) Physical attack \n 2) Magic attack')
                                dragon_await = await self.client.wait_for('message', check=checkfight, timeout=180)
                                if dragon_await.content == '1':
                                    old_int = self.users[member_id]['intelligence']
                                    self.users[member_id]['intelligence'] = 0
                                if dragon_await.content == '2':
                                    e_f_m_d = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                        e_f_m_d.add_field(name='1) Dragon breath',
                                                          value='0.5 * your strength magic damage')
                                        await ctx.send(embed=e_f_m_d)
                                        await ctx.send('choose skill!')
                                        reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                                  timeout=180)
                                        if reply_dragon.content == '1':
                                            magic_damage = round(0.5 * self.users[member_id]['strength'])
                                            bandithp -= magic_damage
                                            await ctx.send(
                                                f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')

                            if self.users[member_id]['intelligence'] == 0:
                                physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                                 self.users[member_id]['agility'] + 3) + \
                                                  self.users[member_id]['weaponstat']
                                bandithp -= physical_damage
                                await ctx.send(
                                    f'You did {physical_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                self.users[member_id]['intelligence'] = old_int
                            if bandithp > 0:
                                mob_damage = random.randint(113, 117) - self.users[member_id]['armorstat']
                                if mob_damage < 0:
                                    mob_damage = 0
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if reply3.content == '2':
                            dodgechance = random.randint(1, 3)
                            mob_damage = random.randint(1, 3)
                            if dodgechance == 1:
                                mob_damage = 0
                                await ctx.send('Succesful dodge!')
                            if dodgechance == 2:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                            if dodgechance == 3:
                                self.users[member_id]['health'] -= mob_damage
                                await ctx.send(
                                    f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                    if bandithp <= 0:
                        embedslimewin = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        exp_slime = random.randint(349, 478)
                        gold_slime = random.randint(117, 126)
                        if self.users[member_id]['karma'] == 0:
                            gold_slime += 139
                        embedslimewin.add_field(name='Win',
                                                value=f"You won the fight against Bunny with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                        self.users[member_id]['exp'] += exp_slime
                        self.users[member_id]['gold'] += gold_slime
                        await ctx.send(embed=embedslimewin)
                        if self.lvl_up(member_id):
                            self.users[member_id]['strength'] += 1
                            self.users[member_id]['agility'] += 1
                            if self.users[member_id]['intelligence'] > 0:
                                self.users[member_id]['intelligence'] += 1
                            await ctx.send(
                                f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                        # третья битва
                        await ctx.send("Why he not dying??")
                        bandithp = 1
                        while bandithp > 0:
                            if self.users[member_id]['health'] <= 0:
                                embed_death = discord.Embed(
                                    color=discord.Colour.dark_red()
                                )
                                embed_death.add_field(name='Death', value='YOU DIED')
                                embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                                await ctx.send(embed=embed_death)
                                self.users[member_id]['storyfantasy'] = -1
                                break
                            e_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            e_f.add_field(name='Bunny', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                            e_f.set_image(
                                url='https://vignette.wikia.nocookie.net/bloodc/images/8/83/Vlcsnap-2011-10-04-16h57m48s124.png/revision/latest?cb=20111004215819')

                            await ctx.send(embed=e_f)

                            reply3 = await self.client.wait_for('message', check=check, timeout=180)
                            dop_damage = 0
                            if reply3.content == '1':
                                if self.users[member_id]['karma'] == -30:
                                    e_f_m_s = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                        e_f_m_s.add_field(name='1) Demonic change', value='Choose one of 2 effects!')
                                    await ctx.send(embed=e_f_m_s)
                                    await ctx.send('choose skill!')
                                    reply_succ = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_succ.content == '1':
                                        await ctx.send('choose effect of skill!')
                                        await ctx.send(
                                            '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                        reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                                 timeout=180)
                                        if reply_succ1.content == '1':
                                            self.users[member_id]['health'] -= 2
                                            magic_damage = 2 * self.users[member_id]['intelligence']
                                        if reply_succ1.content == '2':
                                            magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                            self.users[member_id]['health'] += magic_damage
                                            if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                                self.users[member_id]['health'] = self.users[member_id]['strength']
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                if self.users[member_id]['karma'] == 5:
                                    e_f_m_f = discord.Embed(
                                        color=discord.Colour.dark_purple()
                                    )
                                    if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                        e_f_m_f.add_field(name='1) Mind Blow',
                                                          value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                                    await ctx.send(embed=e_f_m_f)
                                    await ctx.send('choose skill!')
                                    reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if reply_elf.content == '1':
                                        a = self.users[member_id]['intelligence']
                                        for i in range(1, a + 1):
                                            magic_damage += elf_n
                                            elf_n += 0.5
                                        magic_damage = round(magic_damage)
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                        magic_damage = 0
                                        elf_n = 0.5
                                if self.users[member_id]['karma'] == 2:
                                    await ctx.send('1) Physical attack \n 2) Magic attack')
                                    dragon_await = await self.client.wait_for('message', check=checkfight, timeout=180)
                                    if dragon_await.content == '1':
                                        old_int = self.users[member_id]['intelligence']
                                        self.users[member_id]['intelligence'] = 0
                                    if dragon_await.content == '2':
                                        e_f_m_d = discord.Embed(
                                            color=discord.Colour.dark_purple()
                                        )
                                        if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                            e_f_m_d.add_field(name='1) Dragon breath',
                                                              value='0.5 * your strength magic damage')
                                            await ctx.send(embed=e_f_m_d)
                                            await ctx.send('choose skill!')
                                            reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                                      timeout=180)
                                            if reply_dragon.content == '1':
                                                magic_damage = round(0.5 * self.users[member_id]['strength'])
                                                bandithp -= magic_damage
                                                await ctx.send(
                                                    f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')

                                if self.users[member_id]['intelligence'] == 0:
                                    physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                                     self.users[member_id]['agility'] + 3) + \
                                                      self.users[member_id]['weaponstat']
                                    bandithp -= physical_damage
                                    await ctx.send(
                                        f'You did {physical_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                    self.users[member_id]['intelligence'] = old_int
                                if bandithp > 0:
                                    mob_damage = random.randint(113, 117) - self.users[member_id]['armorstat']
                                    if mob_damage < 0:
                                        mob_damage = 0
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                            if reply3.content == '2':
                                dodgechance = random.randint(1, 3)
                                mob_damage = random.randint(1, 3)
                                if dodgechance == 1:
                                    mob_damage = 0
                                    await ctx.send('Succesful dodge!')
                                if dodgechance == 2:
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                                if dodgechance == 3:
                                    self.users[member_id]['health'] -= mob_damage
                                    await ctx.send(
                                        f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                        if bandithp <= 0:
                            embedslimewin = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            exp_slime = random.randint(349, 478)
                            gold_slime = random.randint(117, 126)
                            if self.users[member_id]['karma'] == 0:
                                gold_slime += 139
                            embedslimewin.add_field(name='Win',
                                                    value=f"You won the fight against Bunny with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                            self.users[member_id]['exp'] += exp_slime
                            self.users[member_id]['gold'] += gold_slime
                            await ctx.send(embed=embedslimewin)
                            if self.lvl_up(member_id):
                                self.users[member_id]['strength'] += 1
                                self.users[member_id]['agility'] += 1
                                if self.users[member_id]['intelligence'] > 0:
                                    self.users[member_id]['intelligence'] += 1
                                await ctx.send(
                                    f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                            # battle final
                            bandithp = 1
                            while bandithp > 0:
                                if self.users[member_id]['health'] <= 0:
                                    embed_death = discord.Embed(
                                        color=discord.Colour.dark_red()
                                    )
                                    embed_death.add_field(name='Death', value='YOU DIED')
                                    embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                                    await ctx.send(embed=embed_death)
                                    self.users[member_id]['storyfantasy'] = -1
                                    break
                                e_f = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                e_f.add_field(name='Bunny', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                                e_f.set_image(
                                    url='https://vignette.wikia.nocookie.net/bloodc/images/8/83/Vlcsnap-2011-10-04-16h57m48s124.png/revision/latest?cb=20111004215819')

                                await ctx.send(embed=e_f)

                                reply3 = await self.client.wait_for('message', check=check, timeout=180)
                                dop_damage = 0
                                if reply3.content == '1':
                                    if self.users[member_id]['karma'] == -30:
                                        e_f_m_s = discord.Embed(
                                            color=discord.Colour.dark_purple()
                                        )
                                        if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                            e_f_m_s.add_field(name='1) Demonic change',
                                                              value='Choose one of 2 effects!')
                                        await ctx.send(embed=e_f_m_s)
                                        await ctx.send('choose skill!')
                                        reply_succ = await self.client.wait_for('message', check=checkfight,
                                                                                timeout=180)
                                        if reply_succ.content == '1':
                                            await ctx.send('choose effect of skill!')
                                            await ctx.send(
                                                '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                            reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                                     timeout=180)
                                            if reply_succ1.content == '1':
                                                self.users[member_id]['health'] -= 2
                                                magic_damage = 2 * self.users[member_id]['intelligence']
                                            if reply_succ1.content == '2':
                                                magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                                self.users[member_id]['health'] += magic_damage
                                                if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                                    self.users[member_id]['health'] = self.users[member_id]['strength']
                                            bandithp -= magic_damage
                                            await ctx.send(
                                                f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                    if self.users[member_id]['karma'] == 5:
                                        e_f_m_f = discord.Embed(
                                            color=discord.Colour.dark_purple()
                                        )
                                        if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                            e_f_m_f.add_field(name='1) Mind Blow',
                                                              value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                                        await ctx.send(embed=e_f_m_f)
                                        await ctx.send('choose skill!')
                                        reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                                        if reply_elf.content == '1':
                                            a = self.users[member_id]['intelligence']
                                            for i in range(1, a + 1):
                                                magic_damage += elf_n
                                                elf_n += 0.5
                                            magic_damage = round(magic_damage)
                                            bandithp -= magic_damage
                                            await ctx.send(
                                                f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                            magic_damage = 0
                                            elf_n = 0.5
                                    if self.users[member_id]['karma'] == 2:
                                        await ctx.send('1) Physical attack \n 2) Magic attack')
                                        dragon_await = await self.client.wait_for('message', check=checkfight,
                                                                                  timeout=180)
                                        if dragon_await.content == '1':
                                            old_int = self.users[member_id]['intelligence']
                                            self.users[member_id]['intelligence'] = 0
                                        if dragon_await.content == '2':
                                            e_f_m_d = discord.Embed(
                                                color=discord.Colour.dark_purple()
                                            )
                                            if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                                e_f_m_d.add_field(name='1) Dragon breath',
                                                                  value='0.5 * your strength magic damage')
                                                await ctx.send(embed=e_f_m_d)
                                                await ctx.send('choose skill!')
                                                reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                                          timeout=180)
                                                if reply_dragon.content == '1':
                                                    magic_damage = round(0.5 * self.users[member_id]['strength'])
                                                    bandithp -= magic_damage
                                                    await ctx.send(
                                                        f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')

                                    if self.users[member_id]['intelligence'] == 0:
                                        physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                                         self.users[member_id]['agility'] + 3) + \
                                                          self.users[member_id]['weaponstat']
                                        bandithp -= physical_damage
                                        await ctx.send(
                                            f'You did {physical_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                        self.users[member_id]['intelligence'] = old_int
                                    if bandithp > 0:
                                        mob_damage = random.randint(1, 20) - self.users[member_id]['armorstat']
                                        if mob_damage < 0:
                                            mob_damage = 0
                                        self.users[member_id]['health'] -= mob_damage
                                        await ctx.send(
                                            f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                                if reply3.content == '2':
                                    dodgechance = random.randint(1, 3)
                                    mob_damage = random.randint(3, 6)
                                    if dodgechance == 1:
                                        mob_damage = 0
                                        await ctx.send('Succesful dodge!')
                                    if dodgechance == 2:
                                        self.users[member_id]['health'] -= mob_damage
                                        await ctx.send(
                                            f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                                    if dodgechance == 3:
                                        self.users[member_id]['health'] -= mob_damage
                                        await ctx.send(
                                            f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                            if bandithp <= 0:
                                embedslimewin = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                exp_slime = random.randint(549, 678)
                                gold_slime = random.randint(617, 926)
                                if self.users[member_id]['karma'] == 0:
                                    gold_slime += 139
                                embedslimewin.add_field(name='Win',
                                                        value=f"You won the fight against Bunny with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                                self.users[member_id]['exp'] += exp_slime
                                self.users[member_id]['gold'] += gold_slime
                                await ctx.send(embed=embedslimewin)
                                if self.lvl_up(member_id):
                                    self.users[member_id]['strength'] += 1
                                    self.users[member_id]['agility'] += 1
                                    if self.users[member_id]['intelligence'] > 0:
                                        self.users[member_id]['intelligence'] += 1
                                    await ctx.send(
                                        f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                                self.users[member_id]['storyfantasy'] = 7
        if self.users[member_id]['storyfantasy'] == 7:
            embendoo = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embendoo.add_field(name='Ooffh',
                               value="It was a hard battle, but not final. More bunnies is going to attack you! Prepare...")
            await ctx.send(embed=embendoo)
            bunny = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            bunny.add_field(name='Fight',
                            value='Very big and muscular bunny ready to attack you! Behind of him his horde. \n 1) Fight 2) Save and quit')
            bunny.set_image(
                url='https://vignette.wikia.nocookie.net/blood-c/images/f/f1/Wmplayer_2012-06-17_14-17-26-16.jpg/revision/latest/top-crop/width/300/height/300?cb=20120617172417&path-prefix=es')
            await ctx.send(embed=bunny)
            reply3 = await self.client.wait_for('message', check=check, timeout=180)
            if reply3.content == '2':
                await ctx.send('Game process saved!')
            if reply3.content == '1':
                bandithp = 350
                while bandithp > 0:
                    if self.users[member_id]['health'] <= 0:
                        embed_death = discord.Embed(
                            color=discord.Colour.dark_red()
                        )
                        embed_death.add_field(name='Death', value='YOU DIED')
                        embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                        await ctx.send(embed=embed_death)
                        self.users[member_id]['storyfantasy'] = -1
                        break
                    e_f = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    e_f.add_field(name='Bunny', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                    e_f.set_image(
                        url='https://vignette.wikia.nocookie.net/blood-c/images/f/f1/Wmplayer_2012-06-17_14-17-26-16.jpg/revision/latest/top-crop/width/300/height/300?cb=20120617172417&path-prefix=es')
                    await ctx.send(embed=e_f)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['karma'] == -30:
                            e_f_m_s = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                e_f_m_s.add_field(name='1) Demonic change',
                                                  value='Choose one of 2 effects!')
                            await ctx.send(embed=e_f_m_s)
                            await ctx.send('choose skill!')
                            reply_succ = await self.client.wait_for('message', check=checkfight,
                                                                    timeout=180)
                            if reply_succ.content == '1':
                                await ctx.send('choose effect of skill!')
                                await ctx.send(
                                    '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                         timeout=180)
                                if reply_succ1.content == '1':
                                    self.users[member_id]['health'] -= 2
                                    magic_damage = 2 * self.users[member_id]['intelligence']
                                if reply_succ1.content == '2':
                                    magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                    self.users[member_id]['health'] += magic_damage
                                    if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                        self.users[member_id]['health'] = self.users[member_id]['strength']
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                        if self.users[member_id]['karma'] == 5:
                            e_f_m_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                e_f_m_f.add_field(name='1) Mind Blow',
                                                  value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                            await ctx.send(embed=e_f_m_f)
                            await ctx.send('choose skill!')
                            reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_elf.content == '1':
                                a = self.users[member_id]['intelligence']
                                for i in range(1, a + 1):
                                    magic_damage += elf_n
                                    elf_n += 0.5
                                magic_damage = round(magic_damage)
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                                magic_damage = 0
                                elf_n = 0.5
                        if self.users[member_id]['karma'] == 2:
                            await ctx.send('1) Physical attack \n 2) Magic attack')
                            dragon_await = await self.client.wait_for('message', check=checkfight,
                                                                      timeout=180)
                            if dragon_await.content == '1':
                                old_int = self.users[member_id]['intelligence']
                                self.users[member_id]['intelligence'] = 0
                            if dragon_await.content == '2':
                                e_f_m_d = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                    e_f_m_d.add_field(name='1) Dragon breath',
                                                      value='0.5 * your strength magic damage')
                                    await ctx.send(embed=e_f_m_d)
                                    await ctx.send('choose skill!')
                                    reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                              timeout=180)
                                    if reply_dragon.content == '1':
                                        magic_damage = round(0.5 * self.users[member_id]['strength'])
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')

                        if self.users[member_id]['intelligence'] == 0:
                            physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                             self.users[member_id]['agility'] + 3) + \
                                              self.users[member_id]['weaponstat']
                            bandithp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to Bunny!Good punch. Now his HP is {bandithp}')
                            self.users[member_id]['intelligence'] = old_int
                        if bandithp > 0:
                            mob_damage = random.randint(1, 20) - self.users[member_id]['armorstat']
                            if mob_damage < 0:
                                mob_damage = 0
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(3, 6)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!')
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                        if dodgechance == 3:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Bunny gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                if bandithp <= 0:
                    embedslimewin = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    exp_slime = random.randint(549, 678)
                    gold_slime = random.randint(217, 226)
                    if self.users[member_id]['karma'] == 0:
                        gold_slime += 139
                    embedslimewin.add_field(name='Win',
                                            value=f"You won the fight against Bunny with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                    self.users[member_id]['exp'] += exp_slime
                    self.users[member_id]['gold'] += gold_slime
                    await ctx.send(embed=embedslimewin)
                    if self.lvl_up(member_id):
                        self.users[member_id]['strength'] += 1
                        self.users[member_id]['agility'] += 1
                        if self.users[member_id]['intelligence'] > 0:
                            self.users[member_id]['intelligence'] += 1
                        await ctx.send(
                            f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                    voice = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    voice.add_field(name='Event', value='You hear woman voice from your back: "Good job, now my turn"')
                    await ctx.send(embed=voice)
                    await ctx.send("**all bunnies are dead now** but where's a woman?")
                    self.users[member_id]['storyfantasy'] = 8
        if self.users[member_id]['storyfantasy'] == 8:
            fire_in_town = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            fire_in_town.add_field(name='Important choice',
                                   value='The city is engulfed in flames and soon nothing will remain of it. The sad beginning of the story for a man who just lay in bed and slept, and he was forced to go here. What to do now? After a little reflection there are several options, which one will you choose?\n 1) Go to palace of King 2)Go to the second largest town 3) Just go back to home')
            fire_in_town.set_image(
                url='https://steamuserimages-a.akamaihd.net/ugc/101724518970937891/AF85D181E33984FFEABDCE574F6EC281E49D3F33/')
            await ctx.send(embed=fire_in_town)
            reply = await self.client.wait_for('message', check=check3, timeout=180)
            if reply.content == '3':
                if self.users[member_id]['ach2'] == "\u274c":
                    self.users[member_id]['ach2'] = "\u2713"
                    embedach1 = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    embedach1.add_field(name='Achievment',
                                        value=f"Achievment 'Lazy hero' received! \n {self.users[member_id]['ach1']}")
                    await ctx.send(embed=embedach1)
                    await ctx.send('So lazy to do something! :D Your journey ends here!')
                    self.users[member_id]['storyfantasy'] = 1
                else:
                    await ctx.send('So lazy to do something! :D Your journey ends here!')
                    self.users[member_id]['storyfantasy'] = 1
            if reply.content == '2':
                self.users[member_id]['storyfantasy'] = 14
            if reply.content == '1':
                self.users[member_id]['storyfantasy'] = 9
        if self.users[member_id]['storyfantasy'] == 9:
            king_palace = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            king_palace.add_field(name='Palace',
                                  value='Palace in fire, but you can come in and you even know how. 1) Come in 2) Go away from palace in second largest town')
            king_palace.set_image(
                url='https://s3.bioware.ru/forum/monthly_2017_12/96.jpg.55642607ccae0f132367325b1a274d50.jpg')
            await ctx.send(embed=king_palace)
            reply = await self.client.wait_for('message', check=check, timeout=180)
            if reply.content == '2':
                self.users[member_id]['storyfantasy'] = 14
            if reply.content == '1':
                self.users[member_id]['storyfantasy'] = 10
        if self.users[member_id]['storyfantasy'] == 10:
            await ctx.send(
                'You came in palace and seems near to something interesting but suddenly you faced a big monster. Big eye.')
            bandithp = 400
            while bandithp > 0:
                if self.users[member_id]['health'] <= 0:
                    embed_death = discord.Embed(
                        color=discord.Colour.dark_red()
                    )
                    embed_death.add_field(name='Death', value='YOU DIED')
                    embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                    await ctx.send(embed=embed_death)
                    self.users[member_id]['storyfantasy'] = -1
                    break
                e_f = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                e_f.add_field(name='Giant Eye', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                e_f.set_image(
                    url='https://vignette.wikia.nocookie.net/goblin-slayer/images/4/4f/Giant_Eyeball_%28GS_Manga%29.png/revision/latest?cb=20181129080555')
                await ctx.send(embed=e_f)

                reply3 = await self.client.wait_for('message', check=check, timeout=180)
                dop_damage = 0
                if reply3.content == '1':
                    if self.users[member_id]['karma'] == -30:
                        e_f_m_s = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                            e_f_m_s.add_field(name='1) Demonic change',
                                              value='Choose one of 2 effects!')
                        await ctx.send(embed=e_f_m_s)
                        await ctx.send('choose skill!')
                        reply_succ = await self.client.wait_for('message', check=checkfight,
                                                                timeout=180)
                        if reply_succ.content == '1':
                            await ctx.send('choose effect of skill!')
                            await ctx.send(
                                '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                            reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                     timeout=180)
                            if reply_succ1.content == '1':
                                self.users[member_id]['health'] -= 2
                                magic_damage = 2 * self.users[member_id]['intelligence']
                            if reply_succ1.content == '2':
                                magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                self.users[member_id]['health'] += magic_damage
                                if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                    self.users[member_id]['health'] = self.users[member_id]['strength']
                            bandithp -= magic_damage
                            await ctx.send(
                                f'You did {magic_damage} damage to Giant Eye!Good punch. Now his HP is {bandithp}')
                    if self.users[member_id]['karma'] == 5:
                        e_f_m_f = discord.Embed(
                            color=discord.Colour.dark_purple()
                        )
                        if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                            e_f_m_f.add_field(name='1) Mind Blow',
                                              value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                        await ctx.send(embed=e_f_m_f)
                        await ctx.send('choose skill!')
                        reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                        if reply_elf.content == '1':
                            a = self.users[member_id]['intelligence']
                            for i in range(1, a + 1):
                                magic_damage += elf_n
                                elf_n += 0.5
                            magic_damage = round(magic_damage)
                            bandithp -= magic_damage
                            await ctx.send(
                                f'You did {magic_damage} damage to Giant Eye!Good punch. Now his HP is {bandithp}')
                            magic_damage = 0
                            elf_n = 0.5
                    if self.users[member_id]['karma'] == 2:
                        await ctx.send('1) Physical attack \n 2) Magic attack')
                        dragon_await = await self.client.wait_for('message', check=checkfight,
                                                                  timeout=180)
                        if dragon_await.content == '1':
                            old_int = self.users[member_id]['intelligence']
                            self.users[member_id]['intelligence'] = 0
                        if dragon_await.content == '2':
                            e_f_m_d = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                e_f_m_d.add_field(name='1) Dragon breath',
                                                  value='0.5 * your strength magic damage')
                                await ctx.send(embed=e_f_m_d)
                                await ctx.send('choose skill!')
                                reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                          timeout=180)
                                if reply_dragon.content == '1':
                                    magic_damage = round(0.5 * self.users[member_id]['strength'])
                                    bandithp -= magic_damage
                                    await ctx.send(
                                        f'You did {magic_damage} damage to Giant Eye!Good punch. Now his HP is {bandithp}')

                    if self.users[member_id]['intelligence'] == 0:
                        physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                         self.users[member_id]['agility'] + 3) + \
                                          self.users[member_id]['weaponstat']
                        bandithp -= physical_damage
                        await ctx.send(
                            f'You did {physical_damage} damage to Giant Eye!Good punch. Now his HP is {bandithp}')
                        self.users[member_id]['intelligence'] = old_int
                    if bandithp > 0:
                        mob_damage = random.randint(1, 28) - self.users[member_id]['armorstat']
                        if mob_damage < 0:
                            mob_damage = 0
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Giant Eye gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                if reply3.content == '2':
                    dodgechance = random.randint(1, 3)
                    mob_damage = random.randint(3, 6)
                    if dodgechance == 1:
                        mob_damage = 0
                        await ctx.send('Succesful dodge!')
                    if dodgechance == 2:
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Giant eye gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if dodgechance == 3:
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Giant eye gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

            if bandithp <= 0:
                embedslimewin = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                exp_slime = random.randint(549, 678)
                gold_slime = random.randint(117, 326)
                if self.users[member_id]['karma'] == 0:
                    gold_slime += 339
                embedslimewin.add_field(name='Win',
                                        value=f"You won the fight against Giant Eye with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                self.users[member_id]['exp'] += exp_slime
                self.users[member_id]['gold'] += gold_slime
                await ctx.send(embed=embedslimewin)
                if self.lvl_up(member_id):
                    self.users[member_id]['strength'] += 1
                    self.users[member_id]['agility'] += 1
                    if self.users[member_id]['intelligence'] > 0:
                        self.users[member_id]['intelligence'] += 1
                    await ctx.send(
                        f"{member.mention} Your character is now level {self.users[member_id]['level']}")
                self.users[member_id]['storyfantasy'] = 11
        if self.users[member_id]['storyfantasy'] == 11:
            embed_treasure = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_treasure.add_field(name='Event',
                                     value='After a battle you found a treasure box! \n +1 treasure \n ``$rpgtreasure``')
            embed_treasure.set_image(
                url='https://randomc.net/image/Overlord%20III/Overlord%20III%20-%2007%20-%20Large%2004.jpg')
            await ctx.send(embed=embed_treasure)
            self.users[member_id]['treasure'] += 1
            embed_king = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_king.add_field(name='Event',
                                 value="The castle is completely devastated. The only option is that the king and his wards fled to another city or died. It gets too hot due to a flaming flame, so it's time to leave. \n 1) Leave palace 2) Save and quit")
            await ctx.send(embed=embed_king)
            reply3 = await self.client.wait_for('message', check=check, timeout=180)
            if reply3.content == '1':
                self.users[member_id]['storyfantasy'] = 12
            if reply3.content == '2':
                await ctx.send('Game process saved!')

        if self.users[member_id]['storyfantasy'] == 12:
            embed_bye_bye = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_bye_bye.add_field(name='Town',
                                    value="The town is living it last minutes and you can notice how it begins to surround a mysterious ring of red energy. Are these magic circles of appeal? Who creates them? When will the sun rise? So many questions, but so far there is no answer. Now you going to other town, but there's no guarantee that it's not destroyed too.")
            self.users[member_id]['storyfantasy'] = 14
        if self.users[member_id]['storyfantasy'] == 14:
            embed_fiht_samurai = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            embed_fiht_samurai.add_field(name='Fight', value='Your path blocks the disfigured creation of darkness similar to a samurai. \n 1) Fight 2) Save and quit')
            await ctx.send(embed=embed_fiht_samurai)
            reply3 = await self.client.wait_for('message', check=check, timeout=180)
            if reply3.content == '2':
                await ctx.send('Your game process saved')
            if reply3.content == '1':
                embed_too_fast = discord.Embed(
                    color=discord.Colour.dark_purple()
                )
                embed_too_fast.add_field(name='Creature',
                                         value="This creature is so fast! Seems i can't keep up with his attacks")
                await ctx.send(embed=embed_too_fast)
                bandithp = 140
                while bandithp > 0:
                    if bandithp > 0:
                        mob_damage = random.randint(1, 3) - self.users[member_id]['armorstat']
                        if mob_damage < 0:
                            mob_damage = 0
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Samurai gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if bandithp > 0:
                        mob_damage = random.randint(2, 4) - self.users[member_id]['armorstat']
                        if mob_damage < 0:
                            mob_damage = 0
                        self.users[member_id]['health'] -= mob_damage
                        await ctx.send(
                            f"Samurai gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if self.users[member_id]['health'] <= 0:
                        embed_death = discord.Embed(
                            color=discord.Colour.dark_red()
                        )
                        embed_death.add_field(name='Death', value='YOU DIED')
                        embed_death.set_image(url='https://i.ytimg.com/vi/-ZGlaAxB7nI/maxresdefault.jpg')
                        await ctx.send(embed=embed_death)
                        self.users[member_id]['storyfantasy'] = -1
                        break
                    e_f = discord.Embed(
                        color=discord.Colour.dark_purple()
                    )
                    e_f.add_field(name='Creature', value=f'{bandithp} HP \n 1) Attack 2) Dodge')
                    e_f.set_image(
                        url='https://vignette.wikia.nocookie.net/onepunchman/images/7/72/Haragiri_profile.png/revision/latest?cb=20190902185247')
                    await ctx.send(embed=e_f)

                    reply3 = await self.client.wait_for('message', check=check, timeout=180)
                    dop_damage = 0
                    if reply3.content == '1':
                        if self.users[member_id]['karma'] == -30:
                            e_f_m_s = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Succub_Skill_1'] == 'Learned':
                                e_f_m_s.add_field(name='1) Demonic change',
                                                  value='Choose one of 2 effects!')
                            await ctx.send(embed=e_f_m_s)
                            await ctx.send('choose skill!')
                            reply_succ = await self.client.wait_for('message', check=checkfight,
                                                                    timeout=180)
                            if reply_succ.content == '1':
                                await ctx.send('choose effect of skill!')
                                await ctx.send(
                                    '1) 2 dmg yourself, 2 * your int = dmg \n 2) 0.3 * your int = dmg = heal yourself')
                                reply_succ1 = await self.client.wait_for('message', check=checkfight,
                                                                         timeout=180)
                                if reply_succ1.content == '1':
                                    self.users[member_id]['health'] -= 2
                                    magic_damage = 2 * self.users[member_id]['intelligence']
                                if reply_succ1.content == '2':
                                    magic_damage = round(self.users[member_id]['intelligence'] * 0.3)
                                    self.users[member_id]['health'] += magic_damage
                                    if self.users[member_id]['health'] > self.users[member_id]['strength']:
                                        self.users[member_id]['health'] = self.users[member_id]['strength']
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Samurai!Good punch. Now his HP is {bandithp}')
                        if self.users[member_id]['karma'] == 5:
                            e_f_m_f = discord.Embed(
                                color=discord.Colour.dark_purple()
                            )
                            if self.users[member_id]['Elf_Skill_1'] == 'Learned':
                                e_f_m_f.add_field(name='1) Mind Blow',
                                                  value=' Damage from 1st intelligence point to last point with +0.5 multiplier')
                            await ctx.send(embed=e_f_m_f)
                            await ctx.send('choose skill!')
                            reply_elf = await self.client.wait_for('message', check=checkfight, timeout=180)
                            if reply_elf.content == '1':
                                a = self.users[member_id]['intelligence']
                                for i in range(1, a + 1):
                                    magic_damage += elf_n
                                    elf_n += 0.5
                                magic_damage = round(magic_damage)
                                bandithp -= magic_damage
                                await ctx.send(
                                    f'You did {magic_damage} damage to Samurai!Good punch. Now his HP is {bandithp}')
                                magic_damage = 0
                                elf_n = 0.5
                        if self.users[member_id]['karma'] == 2:
                            await ctx.send('1) Physical attack \n 2) Magic attack')
                            dragon_await = await self.client.wait_for('message', check=checkfight,
                                                                      timeout=180)
                            if dragon_await.content == '1':
                                old_int = self.users[member_id]['intelligence']
                                self.users[member_id]['intelligence'] = 0
                            if dragon_await.content == '2':
                                e_f_m_d = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                if self.users[member_id]['Dragon_Skill_1'] == 'Learned':
                                    e_f_m_d.add_field(name='1) Dragon breath',
                                                      value='0.5 * your strength magic damage')
                                    await ctx.send(embed=e_f_m_d)
                                    await ctx.send('choose skill!')
                                    reply_dragon = await self.client.wait_for('message', check=checkfight,
                                                                              timeout=180)
                                    if reply_dragon.content == '1':
                                        magic_damage = round(0.5 * self.users[member_id]['strength'])
                                        bandithp -= magic_damage
                                        await ctx.send(
                                            f'You did {magic_damage} damage to Samurai!Good punch. Now his HP is {bandithp}')

                        if self.users[member_id]['intelligence'] == 0:
                            physical_damage = random.randint(self.users[member_id]['agility'] - 2,
                                                             self.users[member_id]['agility'] + 3) + \
                                              self.users[member_id]['weaponstat']
                            bandithp -= physical_damage
                            await ctx.send(
                                f'You did {physical_damage} damage to Samurai!Good punch. Now his HP is {bandithp}')
                            self.users[member_id]['intelligence'] = old_int
                        if bandithp > 0:
                            mob_damage = random.randint(3, 5) - self.users[member_id]['armorstat']
                            if mob_damage < 0:
                                mob_damage = 0
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Samurai gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")
                    if reply3.content == '2':
                        dodgechance = random.randint(1, 3)
                        mob_damage = random.randint(3, 6)
                        if dodgechance == 1:
                            mob_damage = 0
                            await ctx.send('Succesful dodge!')
                        if dodgechance == 2:
                            self.users[member_id]['health'] -= mob_damage
                            await ctx.send(
                                f"Samurai gave you {mob_damage} damage. Now your hp is {self.users[member_id]['health']}")

                            if bandithp <= 0:
                                embedslimewin = discord.Embed(
                                    color=discord.Colour.dark_purple()
                                )
                                exp_slime = random.randint(779, 1078)
                                gold_slime = random.randint(217, 526)
                                if self.users[member_id]['karma'] == 0:
                                    gold_slime += 339
                                embedslimewin.add_field(name='Win',
                                                        value=f"You won the fight against Samurai with remaining {self.users[member_id]['health']} HP :heart: That's good!You got {exp_slime} EXP and found {gold_slime} GOLD :moneybag:")
                                self.users[member_id]['exp'] += exp_slime
                                self.users[member_id]['gold'] += gold_slime
                                self.users[member_id]['storyfantasy'] = 15
                                await ctx.send(embed=embedslimewin)
                                if self.lvl_up(member_id):
                                    self.users[member_id]['strength'] += 1
                                    self.users[member_id]['agility'] += 1
                                    if self.users[member_id]['intelligence'] > 0:
                                        self.users[member_id]['intelligence'] += 1
                                    await ctx.send(
                                        f"{member.mention} Your character is now level {self.users[member_id]['level']}")
        if self.users[member_id]['storyfantasy'] == 15:
            dead_forest = discord.Embed(
                color=discord.Colour.dark_purple()
            )
            dead_forest.add_field(name='Location',
                                  value='You came into dead forest and this place looking very dangerous. I see 3 ways to go, which one should i choose? First way is lies through the dark forest , but who knows that the secrets and horrors it keeps? Second way is the nearby cave passage, but there are sectarians. Third way is very long and you even dont know that is there. \n 1) Go through forest 2) Go through cave 3) Go through long path')
            dead_forest.set_image(
                url='https://img1.goodfon.com/wallpaper/nbig/2/49/les-ptica-derevya-svet-dead.jpg')
            await ctx.send(embed=dead_forest)


def setup(client):
    client.add_cog(RPGgame(client))
