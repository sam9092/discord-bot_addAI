import discord
from discord.ext import commands
import asyncio
import random
class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="指令列表")
    async def custom_help(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        help_text = (
            "📖 **可用指令列表**\n"
            "➤ `/指令列表` - 顯示這個說明列表\n"
            "➤ `/直播處` - 生成式AI課程直播連結\n"
            "➤ `/ai <Prompt>` - 讓 AI 回復文字訊息\n"
            "➤ `/生圖 <Prompt>` - 讓 AI 透過文字生成圖片\n"
            "➤ `/選擇 <人生難題> <選項1> <選項2>` - 隨機選擇一個選項\n"
        )
        await ctx.send(help_text)

    # 指令：直播處
    @commands.command(name="直播處")
    async def portal_youtube(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        msg = await ctx.send("🌐 你的傳送門：https://www.youtube.com/@ive-iveai")
        await asyncio.sleep(10)
        await msg.delete()
# 註冊這個 cog
async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))
