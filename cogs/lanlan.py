import discord
import random
from discord.ext import commands
from discord.utils import get
import os

class Lanlan(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        guild = message.guild
        if(guild.name=='修課'):
            if "先睡" in message.content or "晚安" in message.content:
                await message.reply(f"睡三小 起來嗨", delete_after=10)
                
        if(guild.name=='🚥紅綠燈事務所'):
            CC = get(guild.emojis, name="CC")
            CC1= get(guild.emojis, name="CC1")
            p007 = get(guild.emojis, name="007")
            p008 = get(guild.emojis, name="008")
            p009 = get(guild.emojis, name="009")
            p001 = get(guild.emojis, name="001")
            p002 = get(guild.emojis, name="002")
            p003 = get(guild.emojis, name="003")
            p004 = get(guild.emojis, name="004")
            p005 = get(guild.emojis, name="005")
            p006 = get(guild.emojis, name="006")
            p023 = get(guild.emojis, name="023")
            p073 = get(guild.emojis, name="073")
            smile_gun_point = get(guild.emojis, name="smile_gun_point")
            spiderman_fourk = get(guild.emojis, name="spiderman_fourk")
            Zooted = get(guild.emojis, name="Zooted")
            sleep = get(guild.emojis, name="sleep")
            monkeysmile = get(guild.emojis, name="monkeysmile")
            firelemon= get(guild.emojis, name="firelemon")
            mdfirelemon= get(guild.emojis, name="mdfirelemon")
            
            if ":sleep:" in message.content or "先睡" in message.content or "晚安" in message.content:
                await message.add_reaction(sleep)

            if ":Zooted:" in message.content:
                await message.reply(f"您很無聊484，我一律推薦 五子棋", delete_after=10)
            
            if ":001:" in message.content or ":004:" in message.content:
                await message.reply(f"您呼喚了 {p001}帥氣的懶懶 {p004}!!!", delete_after=10)
                await message.add_reaction(p001)
                await message.add_reaction(p004)
            if ":002:" in message.content or ":005:" in message.content:
                await message.reply(f"您呼喚了 {p002}與開台無任何關聯的琉璃 {p005}!!!", delete_after=10)
                await message.add_reaction(p002)
                await message.add_reaction(p005)
            if ":003:" in message.content or ":006:" in message.content:
                await message.reply(f"您呼喚了 {p003}可愛吉的mod 憨吉 {p006}!!!", delete_after=10)
                await message.add_reaction(p003)
                await message.add_reaction(p006)
            if ":nhdm:" in message.content:
                await message.reply(f"您召喚了一隻聖龍萌!!!\n獎勵：聖龍唱小蠻腰一首", delete_after=10)
            if ':firelemon:' in message.content or ':mdfirelemon:' in message.content or message.content=='火檸檬' or "lemon" in message.content.lower() or "檸檬" in message.content:
                await message.reply(f"您翻開了一張陷阱卡 檸檬教主[華火玲教主]，卡片效果：[賣萌一次]", delete_after=15)
            if "🔥" in message.content:
                await message.reply(f"{message.author.nick}被燒起來了", delete_after=10)
            if ":huh:" in message.content or ":009:" in message.content:
                await message.reply(f"蛤吉米", delete_after=10)
            if ":notlikethis:" in message.content:
                await message.reply(f"您翻開了一張陷阱卡 {message.author.nick}，卡片效果：[賣萌一次]", delete_after=15)
            
            if message.content=="ban一詳":
                await message.reply(f"{smile_gun_point} ban! ban! 永ban最快!! 諧音梗+斗M怪人{Zooted}", delete_after=10)
            if message.content.lower()=="dk":
                await message.reply(f"DK真的好帥", delete_after=10)
            if message.content=="宣淋":
                await message.reply(f"宣檸檬超級萌!!!", delete_after=600)
            if message.content=="阿平":
                await message.reply(f"阿平超級萌又超帥!!!", delete_after=600)
            if message.content=="水帥哥":
                await message.reply(f"喔 水哥\n最帥氣的水哥\n打工超會水哥\n真的好帥真的好帥", delete_after=30)
            
            if "蛤" in message.content:
                await message.reply(f"{p009} 蛤蜊好吃，蛤什麼", delete_after=10)
            if "ㄩㄩ" in message.content:
                await message.reply(f"[╞那個水哥╡]\n我感覺我被臭了，馬的{message.author.nick}", delete_after=10)
            if "???" in message.content or ":073:" in message.content or ":023:" in message.content:
                await message.reply(f"有啥毛病", delete_after=10)
                await message.add_reaction("❓")
                await message.add_reaction(p023)
                await message.add_reaction(p073)
            if "cc" in message.content.lower() or "嘻嘻" in message.content:
                await message.add_reaction(CC)
                await message.add_reaction(CC1)
                await message.add_reaction(p007)
                await message.reply(f"別C了，{message.author.nick}的運氣要被C乾了{p008}", delete_after=10)

            if message.content=="喔懶懶":
                await message.reply(f"最美麗的懶懶 畫圖超會懶懶 真的好帥真的好帥", delete_after=20)
            
            if message.content=="聖龍五答":
                await message.reply(f"靠腰 三小 神經病啊 講什麼勾八 乾", delete_after=10)

            if "天籟" in message.content or "好聽" in message.content:
                await message.reply(f"我也這麼覺得!!\n更多好聽的可聽\"懶懶好帥\"或是阿璃YT的\"5MA\"", delete_after=10)
            
            if "馬的翱翔" in message.content or "ㄇㄚˇㄉㄜ˙ㄠˊㄒㄧㄤˊ" in message.content or "ㄇㄉ翱翔" in message.content:
                await message.add_reaction("❓")
                await message.add_reaction(p009)
                await message.add_reaction(p023)
                await message.reply(f"您收到一份天譴，馬的{message.author.nick}!!!", delete_after=10)
                await message.delete(delay=3)

            if "翱翔萌" in message.content:
                await message.reply(f"您收到一份天譴，{message.author.nick}萌!!!", delete_after=10)
                await message.delete(delay=3)
            
            if "火玲萌" in message.content:
                await message.add_reaction("🔥")
                await message.add_reaction("🍋")
            elif "聖龍萌" in message.content:
                await message.reply(f"聖龍可愛聖龍萌\n聖龍啥時開台", delete_after=10)
                await message.add_reaction("🇳")
                await message.add_reaction("🇭")
                await message.add_reaction("🇩")
                await message.add_reaction("🇲")

            if "甲賽" in message.content or "大便" in message.content:
                if message.author.name=="liuliliuuuu.9487" or message.author.name=='lililili4694':
                    await message.reply(f"真好吃\n最喜歡 {message.author.nick}的賽了")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Lanlan(bot))
