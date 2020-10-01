import logging

from prometheus_client import start_http_server
from discord.ext import commands

from .cogs.char import Char
from .cogs.lookup import Lookup
from .cogs.roll import Roll
from .cogs.splash import Splash

logger = logging.getLogger(__name__)

class DungeonBot:

  def __init__(self, prefix:str = '.'):

    description = "Familiar acts as a magical companion to aide \
    your Dungeons and Dragons game. Below are a list of commands the bot supports. \
    Familiar is a collaboration between Dungeon Master, Bill Silvey, Jeremy Rule, and friends."

    bot = commands.Bot(prefix, description=description)
    self.bot = bot

    bot.add_cog(Char(bot))
    bot.add_cog(Lookup(bot))
    bot.add_cog(Roll(bot))
    bot.add_cog(Splash(bot))
    bot.add_listener(self.on_ready)

  async def on_ready(self):
      logger.info(f"We have logged in as {self.bot.user}")

  def run(self, token:str):
    start_http_server(8000)
    self.bot.run(token)