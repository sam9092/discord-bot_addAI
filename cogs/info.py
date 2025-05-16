import discord
import random
from discord.ext import commands
from discord.utils import get
import os

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 機器人加入伺服器
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print(f"Bot 加入「{guild.name}」伺服器")

    # 機器人離開伺服器
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        print(f"Bot 離開「{guild.name}」伺服器")
async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
