#experimental only

import os
import logging
import nextcord
from nextcord import Embed, Colour, NotFound, Forbidden
from nextcord.ext import commands

log = logging.getLogger()

class Event(commands.Cog):
    """
    Bot Events
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'Logged in as: {self.bot.user.name} - {self.bot.user.id} | Version: {nextcord.__version__}\n')

        
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                log.info(f'{filename[:-3]} successfully loaded.')
            except Exception as ex:
                log.info(f'Could not load {filename[:-3]}. Reason: {ex}')

def setup(bot):
    bot.add_cog(Event(bot))
