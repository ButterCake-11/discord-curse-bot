import discord
from discord.ext import commands
from discord import app_commands
import random

class RandomCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="coinflip", description="Flip a coin.")
    async def coinflip(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(["🪙 Heads!", "🪙 Tails!"]))
    
    @app_commands.command(name="dice", description="Roll a die.")
    async def dice(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🎲 You rolled **{random.randint(1, 6)}**!")
    
    @app_commands.command(name="8ball", description="Ask the magic 8-ball.")
    async def eightball(self, interaction: discord.Interaction, question: str):
        answers = [
            "Yes.", "No.", "Maybe.", "Probably.", "Definitely.",
            "Ask again later.", "The cat has no idea.", "Absolutely not."
        ]
        await interaction.response.send_message(f"🔮 **{random.choice(answers)}**")
    
    @app_commands.command(name="choose", description="Choose between options.")
    async def choose(self, interaction: discord.Interaction, options: str):
        choices = [x.strip() for x in options.split(",") if x.strip()]
        
        if len(choices) < 2:
            await interaction.response.send_message("❌ Give me at least two choices separated by commas.")
            return
        
        await interaction.response.send_message(f"🎯 I choose **{random.choice(choices)}**!")
    
    @app_commands.command(name="random", description="Generate a random number.")
    async def random_number(self, interaction: discord.Interaction, minimum: int, maximum: int):
        if minimum > maximum:
            minimum, maximum = maximum, minimum
        
        await interaction.response.send_message(f"🎲 **{random.randint(minimum, maximum)}**")
    
    @app_commands.command(name="iq", description="Generate a silly IQ number.")
    async def iq(self, interaction: discord.Interaction):
        score = random.randint(1, 200)
        await interaction.response.send_message(f"🧠 Your totally scientific IQ is **{score}**!")
    
    @app_commands.command(name="braincell", description="Check your braincells.")
    async def braincell(self, interaction: discord.Interaction):
        cells = random.randint(0, 3)
        await interaction.response.send_message(f"🧠 You currently have **{cells} braincells**.")

async def setup(bot):
    await bot.add_cog(RandomCog(bot))