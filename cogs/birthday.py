import discord
import datetime
from discord.ext import tasks, commands

class TaskBitrh(commands.Cog):
    # 設定台灣時區 UTC+8
    tz = datetime.timezone(datetime.timedelta(hours=8))
    everyday_time = datetime.time(hour=0, minute=0, tzinfo=tz)  # 設定生日提醒時間

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()

    # 生日名單
    birthdays = {
        "月狐": "0111",
        "肥志": "0115",
        "準槍": "0124",
        "雷神": "0128",
        "柯姬": "0128",
        "秋雪": "0203",
        "琉璃": "0218",
        "星依": "0225",
        "秋雪": "0308",
        "卡諾": "0312",
        "牛仔": "0312",
        "樂天": "0319",
        "冒險啾": "0320",
        "阿雪": "0322",
        "不叮喵": "0327",
        "瘋楓": "0409",
        "笨啦啦": "0417",
        "神崎佑哉": "0418",
        "良女易悲": "0428",
        "薯條": "0429",
        "梅傑": "0501",
        "醬比": "0501",
        "淩洢": "0503",
        "猴子": "0504",
        "宣淋": "0516",
        "紫瑤": "0529",
        "泰瑞": "0530",
        "葉止": "0531",
        "魯菇": "0615",
        "亞羅": "0616",
        "甜甜圈": "0620",
        "賴皮桑": "0703",
        "餅乾": "0705",
        "九歌": "0719",
        "玉米": "0726",
        "盧卡": "0801",
        "水帥哥": "0802",
        "懶懶": "0806",
        "蕾夢": "0806",
        "蘿蔔": "0808",
        "小淋": "0812",
        "凌喵": "0814",
        "阿熊": "0831",
        "夜夜": "0907",
        "小芯": "0913",
        "亞蘭": "0927",
        "句子": "1006",
        "聖龍": "1012",
        "魔路斯": "1012",
        "白靈": "1021",
        "憨吉": "1024",
        "花花": "1031",
        "鐳鍶": "1102",
        "可達鴨": "1106",
        "書書": "1111",
        "火檸檬": "1112",
        "妦苓": "1113",
        "梅爾": "1114",
        "日系": "1129",
        "DK(珂珂)": "1202",
        "173": "1202",
        "一詳": "1224",
        "宗賢": "1229"
    }

    @tasks.loop(time=everyday_time)
    async def everyday(self):
        # 設定發送訊息的頻道ID
        # channel_id = 1339151836543979541
        channel_id = 1226598112605376572
        channel = self.bot.get_channel(channel_id)
        if channel is None:
            print("頻道未找到，請確認 channel_id 是否正確")
            return
        
        today = datetime.datetime.now(self.tz).strftime("%m%d")  # 取得今天日期 (MMDD)
        birthday_messages = [f"🎉 {name} 生日快樂🎂" for name, bday in self.birthdays.items() if bday == today]

        if birthday_messages:
            embed = discord.Embed(
                # title="注意!!本人要求他要生日快樂",
                title="注意!!本日有壽星出沒",
                description="\n".join(birthday_messages),
                color=discord.Color.gold()
            )
            await channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(TaskBitrh(bot))
