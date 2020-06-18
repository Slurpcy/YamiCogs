import discord
import random
from redbot.core import commands, Config, checks


class MinecraftCasino(commands.Cog):
    """
    Play Casino games with random Minecraft stuff
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=582650109, force_registration=True)

        default_guild = {
            "conversion": 100,
            "poker_cost": 45
        }

        self.config.register_guild(**default_guild)
    
    @commands.group()
    @checks.guildowner_or_permissions(manage_guild=True)
    async def mccasino(self, ctx):
        """Configure the Casino"""
        pass

    @mccasino.command(name="info")
    async def mcc_info(self, ctx):
        """View configured settings"""
        pass
    
    @commands.group()
    async def mcpoker(self, ctx):
        """Participate in a betting game using randomly generated Minecraft Statistics"""
        pass
    
    @mcpoker.command(name="start")
    async def mcp_start(self, ctx):
        """Start a game"""
        pass

    @mcpoker.command(name="join")
    async def mcp_join(self, ctx):
        """Join a game"""
        pass