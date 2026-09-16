import discord
from discord.ext import commands
from discord import app_commands
import random

class CatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="meow", description="MEOW!")
    async def meow(self, interaction: discord.Interaction):
        await interaction.response.send_message("🐱 MEOW!")
    
    @app_commands.command(name="mrrp", description="Mrrp.")
    async def mrrp(self, interaction: discord.Interaction):
        await interaction.response.send_message("🐈 mrrrp...")
    
    @app_commands.command(name="hiss", description="Hiss!")
    async def hiss(self, interaction: discord.Interaction):
        await interaction.response.send_message("😾 HSSSSSS!")
    
    @app_commands.command(name="zoomies", description="Activate cat zoomies.")
    async def zoomies(self, interaction: discord.Interaction):
        await interaction.response.send_message("🐈💨 ZOOMIES ACTIVATED!!!")
    
    @app_commands.command(name="loaf", description="Become a loaf.")
    async def loaf(self, interaction: discord.Interaction):
        await interaction.response.send_message("🍞🐱 You are now loaf.")
    
    @app_commands.command(name="feed", description="Feed a cat.")
    async def feed(self, interaction: discord.Interaction):
        foods = ["🐟 fish", "🍗 chicken", "🥩 meat", "🐟 tuna"]
        await interaction.response.send_message(f"🍽️ You fed the cat some **{random.choice(foods)}**!")
    
    @app_commands.command(name="catify", description="Catify someone.")
    async def catify(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"🐱 {user.mention} has been catified!")
    
    @app_commands.command(name="catfact", description="Get a cat fact.")
    async def catfact(self, interaction: discord.Interaction):
        facts = [
            "🐱 Cats can use slow blinking as a friendly signal.",
            "🐱 A group of cats can be called a clowder.",
            "🐱 Cats can move their ears independently.",
            "🐱 Many cats enjoy high places.",
            "🐱 Cat whiskers help them sense nearby objects."
        ]
        await interaction.response.send_message(random.choice(facts))

async def setup(bot):
    await bot.add_cog(CatsCog(bot))