import logging
from nextcord import Embed, Colour, NotFound, Forbidden
from nextcord.ext import commands

log = logging.getLogger()

class Member(commands.Cog):
    """
    Member Commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.dm_only()
    async def register(self, ctx: commands.Context, user, pwd):
        """Account Registration e.g !register [username] [password]"""
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            query = "SELECT AccountName FROM dbo.Accounts WHERE AccountName = %s"
            params = (user,)
            check = self.bot.db.execute(query, params, single=True)
            if check is None:
                try:
                    embed = Embed(color=Colour.random())
                    embed.title = 'Registration'
                    embed.description = '{} user already exists! Please another Username'.format(str(user))
                    await ctx.channel.send(embed=embed)
                except NotFound:
                    pass
                except Forbidden:
                    pass
            else:
                query = 'EXEC dbo.__CreateAccount @AccountName = %s, @Password = %s'
                params = (user, pwd,)
                await self.bot.db.execute(query, params, single=True)
                embed = Embed(color=Colour.random())
                embed.title = 'Registration'
                embed.description = '{} has successfully registered! You can now login'.format(str(user))
                await ctx.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def Character(self, ctx, charname):
        """View Character Info e.g !character [character name/ign]"""
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            query = "SELECT CharacterName FROM dbo.Characters WHERE CharacterName = %s"
            params = (charname,)
            check = self.bot.db.execute(query, params, single=True)
            if check is None:
                try:
                    embed = Embed(color=Colour.random())
                    embed.title = 'Character: {}'.format(charname)
                    embed.description = 'Character Doesnt Exists!'
                    await ctx.channel.send(embed = embed)
                except NotFound:
                    pass
                except Forbidden:
                    pass
            else:
                try:
                    query = """SELECT
                        dbo.Characters.CharacterID,
                        dbo.CharacterStatus.CharacterLevel,
                        dbo.CharacterStatus.JobCode,
                        dbo.CharacterStatus.Coin,
                        dbo.CharacterStatus.Fatigue 
                    FROM dbo.Characters
                        INNER JOIN dbo.CharacterStatus ON dbo.Characters.CharacterID = dbo.CharacterStatus.CharacterID
                    WHERE dbo.Characters.CharacterName = %s
                    """
                    character_id = character_level = job_code = coin = fatigue = ""
                    params = (charname,)
                    await self.bot.db.execute(query, params, single=True)

                    if (job_code == 1):
                        job = 'Warrior'
                    elif(job_code == 2):
                        job = 'Archer'
                    elif(job_code == 3):
                        job = 'Sorceress'
                    elif(job_code == 4):
                        job = 'Cleric'
                    elif(job_code == 5):
                        job = 'Academic'
                    elif(job_code == 6):
                        job = 'kali'
                    elif(job_code == 7):
                        job = 'Assassin'
                    elif(job_code == 8):
                        job = 'Lancea'
                    elif(job_code == 9):
                        job = 'Machina'
                    elif(job_code == 11):
                        job = 'Sword Master'
                    elif(job_code == 12):
                        job = 'Mercenary'
                    elif(job_code == 14):
                        job = 'Bow Master'
                    elif(job_code == 15):
                        job = 'Acrobat'
                    elif(job_code == 17):
                        job = 'Elemental Lord'
                    elif(job_code == 18):
                        job = 'Force User'
                    elif(job_code == 19):
                        job = 'Warlock'
                    elif(job_code == 20):
                        job = 'Paladin'
                    elif(job_code == 21):
                        job = 'Monk'
                    elif(job_code == 22):
                        job = 'Priest'
                    elif(job_code == 23):
                        job = 'Gladiator'
                    elif(job_code == 24):
                        job = 'Moon Lord'
                    elif(job_code == 25):
                        job = 'Barbarian'
                    elif(job_code == 26):
                        job = 'Destroyer'
                    elif(job_code == 29):
                        job = 'Sniper'
                    elif(job_code == 30):
                        job = 'Artillery'
                    elif(job_code == 31):
                        job = 'Tempest'
                    elif(job_code == 32):
                        job = 'Wind Walker'
                    elif(job_code == 35):
                        job = 'Saleana'
                    elif(job_code == 36):
                        job = 'Elestra'
                    elif(job_code == 37):
                        job = 'Smasher'
                    elif(job_code == 38):
                        job = 'Majesty'
                    elif(job_code == 41):
                        job = 'Guardian'
                    elif(job_code == 42):
                        job = 'Crusador'
                    elif(job_code == 43):
                        job = 'Saint'
                    elif(job_code == 44):
                        job = 'Inquisitor'
                    elif(job_code == 45):
                        job = 'Exorcist'
                    elif(job_code == 46):
                        job = 'Engineer'
                    elif(job_code == 47):
                        job = 'Shooting Star'
                    elif(job_code == 48):
                        job = 'Gear Master'
                    elif(job_code == 49):
                        job = 'Alchemist'
                    elif(job_code == 50):
                        job = 'Adept'
                    elif(job_code == 51):
                        job = 'Physician'
                    elif(job_code == 54):
                        job = 'Screamer'
                    elif(job_code == 55):
                        job = 'Dark Summoner'
                    elif(job_code == 56):
                        job = 'Soul Eater'
                    elif(job_code == 57):
                        job = 'Dancer'
                    elif(job_code == 58):
                        job = 'Blade Dancer'
                    elif(job_code == 59):
                        job = 'Spirit Dancer'
                    elif(job_code == 62):
                        job = 'Chaser'
                    elif(job_code == 63):
                        job = 'Ripper'
                    elif(job_code == 64):
                        job = 'Raven'
                    elif(job_code == 67):
                        job = 'Bringer'
                    elif(job_code == 68):
                        job = 'Light Fury'
                    elif(job_code == 69):
                        job = 'Abyss Walker'
                    elif(job_code == 72):
                        job = 'Piercer'
                    elif(job_code == 73):
                        job = 'Flurry'
                    elif(job_code == 74):
                        job = 'Sting Breezer'
                    elif(job_code == 75):
                        job = 'Avenger'
                    elif(job_code == 76):
                        job = 'Dark Avenger'
                    elif(job_code == 77):
                        job = 'Patrona'
                    elif(job_code == 78):
                        job = 'Defensio'
                    elif(job_code == 79):
                        job = 'Ruina'
                    elif(job_code == 80):
                        job = 'Hunter'
                    elif(job_code == 81):
                        job = 'Silver Hunter'
                    elif(job_code == 82):
                        job = 'Heretic'
                    elif(job_code == 83):
                        job = 'Arch Heretic'
                    elif(job_code == 84):
                        job = 'Mara'
                    elif(job_code == 85):
                        job = 'Black Mara'
                    elif(job_code == 86):
                        job = 'Mechanic'
                    elif(job_code == 87):
                        job = 'Ray Mechanic'
                    elif(job_code == 88):
                        job = 'Oracle'
                    elif(job_code == 89):
                        job = 'Oracle Elder'
                    elif(job_code == 90):
                        job = 'Phantom'
                    elif(job_code == 91):
                        job = 'Bleed Phantom'
                    elif(job_code == 92):
                        job = 'Knightess'
                    elif(job_code == 93):
                        job = 'Avalanche'
                    elif(job_code == 94):
                        job = 'Randgrid'
                    elif(job_code == 95):
                        job = 'Launcher'
                    elif(job_code == 96):
                        job = 'Impactor'
                    elif(job_code == 97):
                        job = 'Buster'
                    elif(job_code == 98):
                        job = 'Plaga'
                    elif(job_code == 99):
                        job = 'Vena Plaga'

                    embed = Embed(color=Colour.random())
                    embed.title = 'Character: {}'.format(str(charname))
                    embed.description = 'Job: {}\nCharacter Level: {}\nCoin: {}\nFatigue: {}'.format(str(job), character_level, coin, fatigue)
                    await ctx.channel.send(embed = embed)
                except NotFound:
                    pass
                except Forbidden:
                    pass

def setup(bot):
    bot.add_cog(Member(bot))
