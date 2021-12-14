#version 2.5 (12/14/21)
#migrated to nextcord
import logging

import os
import nextcord
from nextcord.ext import commands
from datetime import datetime

from nextcord.ext.commands.flags import F
from utils import default

logging.basicConfig(format='%(asctime)s [%(filename)14s:%(lineno)4d][%(funcName)30s][%(levelname)8s] %(message)s',
                    level=logging.INFO)

fileHandler = logging.FileHandler(filename='logs/' + '{:%Y-%m-%d}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s [%(filename)14s:%(lineno)4d][%(levelname)8s] %(message)s')
fileHandler.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(fileHandler)

config = default.get_config()

initial_extensions = ['commands.member',
                    'commands.admin',
                    'utils.db']

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config['SETTINGS']['prefix'],
                   intents=intents,
                   activity=nextcord.Game(name='Dragon Nest', type=1))
bot.remove_command('help')


@bot.event
async def on_ready():
    log.info(f'Logged in as: {bot.user.name} - {bot.user.id} | Version: {nextcord.__version__}\n')


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                log.info(f'{filename[:-3]} successfully loaded.')
            except Exception as ex:
                log.info(f'Could not load {filename[:-3]}. Reason: {ex}')

    if config.getboolean('TOKEN', 'is-developing'):
        log.info("Running with Development token")
        TOKEN = config['TOKEN']['dev-token']
    else:
        log.info("Running with Production token")
        TOKEN = config['TOKEN']['prod-token']

    bot.run(TOKEN)
