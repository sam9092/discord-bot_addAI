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
    # 指令：簽到處
    @commands.command(name="簽到處")
    async def portal_twitch(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        allowed_guild_id = 1226593143630331996
        if ctx.guild is None or ctx.guild.id != allowed_guild_id:
            await ctx.send("這個指令只能在指定的伺服器中使用！")
            return
        msg = await ctx.send("🌐 你的傳送門：https://www.twitch.tv/lanlan0806")
        await asyncio.sleep(10)
        await msg.delete()

    # 指令：直播處
    @commands.command(name="直播處")
    async def portal_youtube(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        msg = await ctx.send("🌐 你的傳送門：https://www.youtube.com/@ive-iveai")
        await asyncio.sleep(10)
        await msg.delete()
    # 指令：直播處
    def generate_praise(self, who: str) -> str:
        templates = [
            "{who}女神，請您狠狠地蹂躪我吧！\n您的威嚴，您的強大，都讓我無法自拔地沉淪！\n我渴望成為您最忠誠的奴僕，任您差遣，任您懲罰！ᐠ(///▽///)ᐟ",
            "{who}貼心舉世無雙！ᐠ( ᑒ )ᐟ\n{who}可愛聰明絕頂！ᐠ( ᑒ )ᐟ\n{who}天使沉魚落雁！ᐠ( ᑒ )ᐟ",
            "世間萬物皆黯淡，唯有{who}閃耀不滅 ✨",
            "{who}降臨人世，萬神退位！",
        ]
        return random.choice(templates).format(who=who)
    @commands.command(name="legna")
    async def legna(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        allowed_guild_id = 1226593143630331996
        if ctx.guild is None or ctx.guild.id != allowed_guild_id:
            await ctx.send("這個指令只能在指定的伺服器中使用！")
            return
        responses = [
            "憨吉可愛吉了",  # 專屬語錄
            self.generate_praise("憨吉")  # 通用誇獎模板
        ]
        await ctx.send(random.choice(responses))

    @commands.command(name="lanlan")
    async def lan(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        allowed_guild_id = 1226593143630331996
        if ctx.guild is None or ctx.guild.id != allowed_guild_id:
            await ctx.send("這個指令只能在指定的伺服器中使用！")
            return
        await ctx.send(self.generate_praise("懶懶"))
    @commands.command(name="xingyi")
    async def xingyi(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        allowed_guild_id = 1226593143630331996
        if ctx.guild is None or ctx.guild.id != allowed_guild_id:
            await ctx.send("這個指令只能在指定的伺服器中使用！")
            return
        await ctx.send(self.generate_praise("星依"))
    @commands.command(name="4T")
    async def siti4T(self, ctx: commands.Context):
        if ctx.author.bot:
            return
        allowed_guild_id = 1226593143630331996
        if ctx.guild is None or ctx.guild.id != allowed_guild_id:
            await ctx.send("這個指令只能在指定的伺服器中使用！")
            return
        await ctx.send(self.generate_praise("琉璃"))
# 註冊這個 cog
async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))
