from re import sub
import discord
from discord.ext import commands
import rolldice
import logging
from random import Random

logger = logging.getLogger(__name__)

brief = '.splash <substance>'
description = '''Calculate the splash damage of a thrown substance.
Examples:
.splash oil
  Result: Your oil lands 1 foot Long Right, and does 2 damage.
.splash holy water
  Result: Your holy water lands 1 foot Short Left, and does 2 damage.
.splash acid
  Result: Your holy water lands 4 foot Right, and does 2 damage.
'''

DIRECTIONS = [
    'long right',
    'right',
    'short right',
    'short (before)',
    'short left',
    'left',
    'long left',
    'long (over)'
]

class UnknownSubstance(Exception):
    def __inti__(self, substance):
        self.message = f'Unknown substance {substance}'
    pass

class Splash(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.randint = Random().randint

    def handle_splash(self, substance):
        substance == str(substance).lower
        direction_rand = self.randint(1, 8)  # direction
        distance_rand = self.randint(1, 6)  # distance
        damage_rand = self.randint(1, 3)  # damage

        distance = 'foot' if distance_rand == 1 else 'feet'
        direction = DIRECTIONS[direction_rand - 1]

        if substance == 'oil':
            damage = self.randint(1, 3) if distance_rand < 4 else 0
        elif substance == 'holy water':
            damage = 2 if distance_rand == 1 else 0
        elif substance == 'acid':
            damage = 1 if distance_rand == 1 else 0
        else:
            raise UnknownSubstance(substance)

        return f'Your {substance} landed {distance_rand} {distance} {direction} and did {damage} damage.'


    @commands.command(brief=brief, description=description)
    async def splash(self, ctx, *, substance):
        logger.info(f'splash {substance}')
        message = self.handle_splash(substance)
        logger.info(f'splash result: {message}')
        await ctx.send(message)

    @splash.error
    async def splash_error(self, ctx, e):
        # listen for errors on roll
        if isinstance(e, commands.MissingRequiredArgument):
            await ctx.send('A substance must be given; one of: oil, holy water, acid.')
        elif isinstance(e, UnknownSubstance):
            await ctx.send(f'Unrecognized substance "{e.message}"')
        else:
            await ctx.send(e)
