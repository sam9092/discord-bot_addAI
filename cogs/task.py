import time, discord, datetime
# 導入discord.ext模組中的tasks工具
from discord.ext import tasks, commands

class TaskTime(commands.Cog):
    # 臺灣時區 UTC+8
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 8, minute = 0, tzinfo = tz)
    opps = datetime.time(hour = 12, minute = 0, tzinfo = tz)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()
        self.opps.start()

    @tasks.loop(time = everyday_time)
    async def everyday(self):
        # 設定發送訊息的頻道ID
        channel_id = 1226598112605376572
        channel = self.bot.get_channel(channel_id)

        embed = discord.Embed(
            title = "📅 任務提醒",
            description = f"🌟 今日還沒去!簽到的 記得去簽到 🌟\n"
                        f"\"/簽到處 \"會有連結",
            color = discord.Color.blue()
        )

        await channel.send(embed = embed)

    @tasks.loop(time = opps)
    async def opps(self):
        # 設定發送訊息的頻道ID
        channel_id = 1226598112605376572
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = "每日提醒",
            description = f"阿璃 餐廳\n懶懶 記得吃飯\n憨吉 可愛吉了\n",
            color = discord.Color.red()
        )
        await channel.send(embed = embed)
    
async def setup(bot: commands.Bot):
    await bot.add_cog(TaskTime(bot))