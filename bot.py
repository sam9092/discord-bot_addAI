import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數
load_dotenv()
bot_TOKEN = os.getenv("DISCORD_TOKEN")
# 設置機器人指令前綴
intents = discord.Intents.default()
# 設定 Intents
intents.message_content = True  # 若要讀取訊息文字一定要打開
intents.guilds = True
intents.members = True

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)
# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    excluded_channel_id = 1226607522341715994
    if "@everyone" in message.content and message.channel.id != excluded_channel_id:
        await message.delete()
        await message.channel.send(
            f"請誇誇本機器人，我攔截了{message.author.name}({message.author.nick})的被盜訊息"
        )
    else:
        await bot.process_commands(message)

# ✅ 載入 cogs 指令
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"✅ Loaded {extension}")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"✅ Unloaded {extension}")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"✅ Reloaded {extension}")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(bot_TOKEN)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())
