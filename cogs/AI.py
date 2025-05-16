import os
import discord
from discord.ext import commands
from openai import OpenAI
from dotenv import load_dotenv

MAX_TURNS = 10

# 載入 .env 檔案中的環境變數
load_dotenv()
api_key = os.getenv("api_key")
model = "meta-llama/llama-4-scout-17b-16e-instruct"

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

system = "你是一位博學多聞的好朋友，善用EMOJI和台灣常用的中文(繁體中文)來跟使用者閒談製造話題。"
messages = [{"role":"system","content":system}]

class AIreply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="AI")
    async def AI(self, ctx, prompt: str):
        """輸入一句話，讓AI幫你回應話題。"""
        try:
            messages.append({"role": "user", "content": prompt})

            dialogue = messages[1:]  # 排除 system prompt
            if len(dialogue) > MAX_TURNS * 2:
                messages[:] = [messages[0]] + dialogue[-MAX_TURNS * 2:]

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=False
            )
            if not response.choices:
                await ctx.reply(f"⚠️ AI 沒有回應（收到的問題為：{prompt}）", mention_author=False)
                return
            reply = response.choices[0].message.content.strip()
           
            if not reply or not reply.strip():
                await ctx.send("⚠️ 回傳內容為空")
            else:
                await ctx.reply(reply.strip(), mention_author=False)
        except Exception as e:
            await ctx.send(f"❌ 發生錯誤：{e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(AIreply(bot))