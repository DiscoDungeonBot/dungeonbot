from discord.ext import commands
import rolldice
import logging

from prometheus_client import Counter

brief = 'dice. Example: .roll 1d6 or .roll 2d20+1'
description = '''Roll dice with .roll or .r and dice notation. Examples:

.r 1D6: Roll 1 6-sided die
.r 4d10 + 17: Roll a 10-sided die 4 times and add 17 to the result
.r 2d20 - 3: Roll a 20 sided die 2 times and subtract 3
.r 4d10K: Roll 4d10 and keep only the highest roll
.r 7d12K3: Roll 7d12 and keep the highest three rolls
.r 3d3k: Roll 3d3 and keep the lowest roll
.r 100d6k99: Roll 100d6 and keep all but the highest.
'''

dice_roll_counter = Counter('dice_rolls', 'Counts the dice rolls')

class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['r'], brief=brief, description=description)
    async def roll(self, ctx, *, rollvalue):
    # Parse the roll into number of dice and sides on the dice
        dice_roll_counter.inc()

        logging.info(f'Rolling {rollvalue}')
        result, explanation = rolldice.roll_dice(rollvalue)
        logging.info(f'Result: {result}')

        if rollvalue[0] > '1':
            await ctx.send(f':game_die: {ctx.author.name} rolls... **{result}**! ... with these dice: {explanation} :game_die:')
        else:
            await ctx.send(f':game_die: {ctx.author.name} rolls... **{result}**! :game_die:')

    @roll.error
    async def roll_error(self, ctx, error):
    # listen for errors on roll
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Give a type of die to roll (e.g. .roll 1d6)')
