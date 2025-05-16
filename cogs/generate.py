from discord.ext import commands
import discord
import torch
import random
import tempfile
import os
import gc
from diffusers import StableDiffusionPipeline
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
model = "meta-llama/llama-4-scout-17b-16e-instruct"

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

system = "Translate the user's prompt into concise, fluent English suitable for text-to-image generation. Do not add explanations or suggestions. Output only the translated prompt."
def translate_2_English(user_prompt):
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user_prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

class ImageGen(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🖼️ 啟用生圖功能，使用設備：{self.device}")

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "nitrosocke/Ghibli-Diffusion",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

    def generate_images(self, prompt, enhance_text, negative_text):
        seed = random.randint(0, 2**32 - 1)
        generator = torch.Generator(self.device).manual_seed(seed)

        translated_prompt = translate_2_English(prompt)
        final_prompt = f"{translated_prompt}, {enhance_text}"

        gc.collect()
        if self.device == "cuda":
            torch.cuda.empty_cache()

        with torch.no_grad():
            image = self.pipe(
                prompt=final_prompt,
                negative_prompt=negative_text,
                height=512,
                width=512,
                num_inference_steps=20,
                guidance_scale=7.5,
                generator=generator
            ).images[0]

        return image, seed, translated_prompt

    @commands.command(name="生圖")
    async def generate_command(self, ctx: commands.Context, *, prompt: str):
        await ctx.send("🧪 收到生成請求，請稍等5分鐘左右...")

        try:
            # 預設增強與負面提示
            enhance_text = "Masterpiece, Ultra High Quality, Cinematic Light, Ghibli Style"
            negative_text = "bad anatomy, deformed, extra fingers, blurry, worst quality"

            image, seed, translated = self.generate_images(prompt, enhance_text, negative_text)

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                image.save(f.name)
                file = discord.File(f.name, filename=f"generated_{seed}.png")

            await ctx.send(
                content=f"✅ **圖片生成完成！**\n使用的prompt: `{translated}`",
                file=file
            )

            os.unlink(f.name)

        except Exception as e:
            await ctx.send(f"❌ 發生錯誤：{e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ImageGen(bot))
