import discord
from discord.ext import commands
import math
import asyncio

class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["squareroot", "square_root"])
    async def sqrt(self, ctx, value: float):
        embed = discord.Embed(
        color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f'√‎{value} = {math.sqrt(value)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def factorial(self, ctx, value: int):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f'{value}! = {math.factorial(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["acosine", "arccos", "arccosine", "a_cosine", "arc_cos", "arc_cosine"])
    async def acos(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc cos {value} = {math.acos(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["acosineh", "arccosh", "arccosineh", "a_cosineh", "arc_cosh", "arc_cosineh"])
    async def acosh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc cos hyperbolic {value} = {math.acosh(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["asine", "arcsin", "arcsine", "a_sine", "arc_sin", "arc_sine"])
    async def asin(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc sin {value} = {math.asin(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["asineh", "arcsinh", "arcsineh", "a_sineh", "arc_sinh", "arc_sineh"])
    async def asinh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc sin hyperbolic {value} = {math.asinh(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["atangent", "arctan", "arctangent", "a_tangent", "arc_tan", "arc_tangent"])
    async def atan(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc tan {value} = {math.atan(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["atangenth", "arctanh", "arctangenth", "a_tangenth", "arc_tanh", "arc_tangenth"])
    async def atanh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' arc tan hyperbolic {value} = {math.atanh(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["cosine"])
    async def cos(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' cos {value} = {math.cos(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["cosineh"])
    async def cosh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' cos hyperbolic {value} = {math.cosh(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["sine"])
    async def sin(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' sin {value} = {math.sin(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["sineh"])
    async def sinh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' sin hyperbolic {value} = {math.sinh(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["tangent"])
    async def tan(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' tan {value} = {math.tan(value)}')
        await ctx.send(embed=embed)

    @commands.command(alises=["tangenth"])
    async def tanh(self, ctx, value: float):
        embed = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embed.add_field(name='Math', value=f' tan hyperbolic {value} = {math.tanh(value)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['calc', 'calculate'])
    async def calculator(self, ctx, *, equation: str):
        member = ctx.author
        replacements = {"pi": "math.pi", 'e': "math.e", "sin": "math.sin",
                        "cos": "math.cos", "tan": "math.tan", "sqrt":"math.sqrt", "^":"**", "√":"math.sqrt"}
        allowed = set("0123456789.+-*/^%()")
        try:
            for key, value in replacements.items():
                equation = equation.replace(key, value)
            equation_final = eval(equation)
            equation_final = str(equation_final)
            replacements = {"math.pi": "π", "math.e": "e", "math.sin": "sin", "math.cos": "cos", "math.tan": "tan",
                            "math.sqrt": "√‎"}
            for key, value in replacements.items():
                equation = equation.replace(key, value)
            calculator = discord.Embed(
                color=discord.Colour.dark_purple(),
                timestamp=ctx.message.created_at)
            calculator.set_author(name=f'Calculator', icon_url=member.avatar_url)
            calculator.add_field(name='Equation', value=f'{equation} = {equation_final}')
            await ctx.send(embed=calculator)
        except SyntaxError:
            embed_error = discord.Embed(
                color=discord.Colour.dark_purple(),
                timestamp=ctx.message.created_at)
            embed_error.add_field(name='Error', value='Syntax error')
            await ctx.send(embed=embed_error)
        except AttributeError as e:
            embed_error = discord.Embed(
                color=discord.Colour.dark_purple(),
                timestamp=ctx.message.created_at)
            embed_error.add_field(name='Error', value=f"AttributeError {e} \n Try to add your value in (), like sqrt(4)")
            await ctx.send(embed=embed_error)

    @calculator.error
    async def calculator_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed_error = discord.Embed(
                color=discord.Colour.dark_purple(),
                timestamp=ctx.message.created_at)
            embed_error.add_field(name='Error', value='Equation is a required argument that is missing.')
            await ctx.send(embed=embed_error)





def setup(client):
    client.add_cog(Math(client))