import logging
import os

from dungeonbot import DungeonBot

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

bot = DungeonBot()

token = os.environ.get('DISCORD_TOKEN', '')

if len(token) == 0:
  raise Exception('DISCORD_TOKEN must be passed as an environment variable')

bot.run(token)
