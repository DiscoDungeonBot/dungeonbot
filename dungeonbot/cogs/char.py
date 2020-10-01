import discord
from discord.ext import commands
import rolldice

class Char(commands.Cog):

    def __init__(self, client):
        self.client = client

    brief = 'Create a D&D character'
    description = '''.char creates a classic D&D character by rolling four
six-sided dice and dropping the lowest six times.
'''

    @commands.command(brief=brief, description=description)
    async def char(self, ctx):
        # create a character

        attrib1, roll1 = rolldice.roll_dice('4d6K3')
        attrib2, roll2 = rolldice.roll_dice('4d6K3')
        attrib3, roll3 = rolldice.roll_dice('4d6K3')
        attrib4, roll4 = rolldice.roll_dice('4d6K3')
        attrib5, roll5 = rolldice.roll_dice('4d6K3')
        attrib6, roll6 = rolldice.roll_dice('4d6K3')

        await ctx.send(f'A character has been generated for {ctx.author.name} by rolling four '
                    'six-sided dice and dropping the lowest six times: '
                    f'**{attrib1}**, **{attrib2}**, **{attrib3}**, **{attrib4}**, **{attrib5}**, and **{attrib6}**')
