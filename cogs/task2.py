import time, discord, datetime
# 導入discord.ext模組中的tasks工具
from discord.ext import tasks, commands

class Task2(commands.Cog):
    # 臺灣時區 UTC+8
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 8, minute = 0, tzinfo = tz)
    liveday = datetime.time(hour = 16, minute = 0, tzinfo = tz)
    opps = datetime.time(hour = 0, minute = 0, tzinfo = tz)
    birthday_time = datetime.time(hour = 0, minute = 0, tzinfo = tz)
    # 生日名單
    birthdays = {
        "翱翔機器人一代": "0516",
        "政治大學": "0520",
        "翱翔(作者)": "0902"
    }

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()
        self.opps.start()
        self.birthday_time.start()
        self.liveday.start()
    
    @tasks.loop(time = everyday_time)
    async def everyday(self):
        # 設定頻道：任務簽到
        channel_id = 1371821191148601420
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = "📅 每日提醒",
            description = (
                "🌟 今天是新的一天，今天的你也是全新的你🌟\n\n"
            ),
            color = discord.Color.blue()
        )

        await channel.send(embed = embed)

    @tasks.loop(time = liveday)
    async def liveday(self):
        # 設定頻道：任務簽到
        channel_id = 1371821191148601420
        channel = self.bot.get_channel(channel_id)
        today = datetime.datetime.now(self.tz).weekday()
        if today != 4:  # 1 表示星期二
            return
        embed = discord.Embed(
            title = "📅 任務提醒",
            description = (
                "🌟 現在有超好玩的生成式 AI課程🌟\n\n"
                "\"/直播處 \"會有連結，記得出席\n"
            ),
            color = discord.Color.blue()
        )

        await channel.send(embed = embed)

    @tasks.loop(time = opps)
    async def opps(self):
        # 設定頻道：任務簽到
        channel_id = 1371821191148601420
        channel = self.bot.get_channel(channel_id)
        today = datetime.datetime.now(self.tz).weekday()
        if today != 4:  # 0 表示星期一
            return
        embed = discord.Embed(
            title = "🔔**任務名稱**：交作業",
            description = (
                "🕒 **任務截止**：今天！\n\n"
                "⏳ **任務狀態**：還沒交的快點去上傳📤！"
            ),
            color = discord.Color.red()
        )
        await channel.send(embed = embed)
    
    @tasks.loop(time=birthday_time)
    async def birthday_time(self):
        # 設定頻道：注意，這邊有壽星
        channel_id = 1371846577785933917
        channel = self.bot.get_channel(channel_id)
        if channel is None:
            print("頻道未找到，請確認 channel_id 是否正確")
            return
        
        today = datetime.datetime.now(self.tz).strftime("%m%d")
        birthday_messages = [f"🎉 {name} 生日快樂🎂" for name, bday in self.birthdays.items() if bday == today]

        if birthday_messages:
            embed = discord.Embed(
                title="注意!!本日有壽星出沒",
                description="\n".join(birthday_messages),
                color=discord.Color.gold()
            )
            await channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Task2(bot))