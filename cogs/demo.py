import discord
import random
from discord.ext import commands
from discord.utils import get
import os

class Demo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        guild = message.guild
        if(guild.id != 1226593143630331996):
            p006 = get(guild.emojis, name="006")
            p008 = get(guild.emojis, name="008")
            p042 = get(guild.emojis, name="042")
            # 偵測 文字訊息
            if "好難" in message.content:
                await message.channel.send(f"{message.author.name}加油，你一定可以的", delete_after=10)
            # 偵測 Emoji訊息(預設，自訂)
            if "🥱" in message.content:
                await message.channel.send(f"您很無聊484，我一律推薦 五子棋", delete_after=10)
            if ":042:" in message.content:
                await message.reply(f"這是可愛的我(作者朋友畫的)", delete_after=10)
                await message.add_reaction(p042)
            # 用文字 回覆訊息 
            if "安安" in message.content or "這裡是哪裡" in message.content:
                await message.reply(f"{message.author.name}您好，這裡是超酷的 機器人展示基地", delete_after=10)
            # 用Emoji 回覆訊息 
            if "翹課" in message.content:
                await message.add_reaction("❓")
            if ":006:" in message.content or ":008:" in message.content:
                await message.add_reaction(p006)
                await message.add_reaction(p008)
async def setup(bot: commands.Bot):
    await bot.add_cog(Demo(bot))