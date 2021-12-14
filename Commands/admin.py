from nextcord import Embed, Member, Role, Colour
from nextcord.ext import commands

class Admin(commands.Cog):
    """
    Admin Commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def clear(self, ctx: commands.Context):
        """Purge entire Conversation in a channel"""
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.purge()
        else:
            embed = Embed(title='Clear Command', description=f'{ctx.author.mention} you have no permission to use this command!', color=Colour.random())
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
