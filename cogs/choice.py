import discord
import asyncio
import random
from discord.ext import commands

class Choice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="選擇")
    async def 選擇(self, ctx, title: str, option_yes: str, option_no: str):
        result = random.choice([option_yes, option_no,option_yes, option_no])

        msg = await ctx.reply(f'**{title}**\n{result}')
        
        if result.strip() == option_yes.strip():
            await ctx.message.add_reaction("✅")
        else:
            await ctx.message.add_reaction("❌")
        
        await asyncio.sleep(15)
        await msg.delete()

async def setup(bot: commands.Bot):
    await bot.add_cog(Choice(bot))
