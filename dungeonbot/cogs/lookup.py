import discord
import textwrap
from discord.ext import commands
from DnD4py.lookup_5e import Roll20

class Lookup(commands.Cog):

    def __init__(self, client):
        self.client = client

    brief = 'Look up a spell, item, or monster'
    description = '''.lookup will return a spell, item, or monster description. Examples:

.lookup owlbear
.lookup fireball
'''

    @commands.command(brief=brief, description=description)
    async def lookup(self, ctx, *, params):
        try:
            desc = str(Roll20(params))
        except OSError:
            desc = f'{params} not found.'
        finally:
            await ctx.send('`' + desc[:1990] + '`')

    @commands.command(brief=brief, description=description)
    async def embedtest(self, ctx, *, params):
        embed = discord.Embed(
            title = "Users",
            description = "description test",
            color = 0x07999b
        )
        embed.set_author(name = "Stats")
        embed.add_field(name = "Servers", value = "hola")
        embed.add_field(name = "Lines of code", value = "codes")
        embed.add_field(name = "Amount of commands", value = "13")
        await ctx.send(embed = embed)
