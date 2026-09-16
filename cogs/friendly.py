import discord
from discord.ext import commands
from discord import app_commands
import random
import urllib.parse

class FriendlyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="hug", description="Give a friendly virtual hug.")
    async def hug(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(
            f"🫂 {interaction.user.mention} gives {user.mention} a friendly hug!"
        )
    
    @app_commands.command(name="highfive", description="High five someone.")
    async def highfive(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"✋ HIGH FIVE! {user.mention}")
    
    @app_commands.command(name="compliment", description="Give someone a compliment.")
    async def compliment(self, interaction: discord.Interaction, user: discord.User):
        compliments = [
            "✨ You're awesome!",
            "🌟 You're doing great!",
            "🐱 The cats approve of you.",
            "💖 You're cool!",
            "🎨 Your creativity is awesome!"
        ]
        await interaction.response.send_message(f"{user.mention} — {random.choice(compliments)}")
    
    @app_commands.command(name="roast", description="Give a harmless silly roast.")
    async def roast(self, interaction: discord.Interaction, user: discord.User):
        roasts = [
            "Your Wi-Fi needs emotional support.",
            "Your brain is currently on airplane mode.",
            "You have the energy of a loading screen.",
            "Even the NPCs are confused by you.",
            "Your last braincell is on vacation."
        ]
        await interaction.response.send_message(f"🔥 {user.mention}: {random.choice(roasts)}")
    
    @app_commands.command(name="say", description="Make the bot say something.")
    async def say(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(text)
    
    @app_commands.command(name="reverse", description="Reverse some text.")
    async def reverse(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(text[::-1])
    
    @app_commands.command(name="mock", description="Make text alternate capitalization.")
    async def mock(self, interaction: discord.Interaction, text: str):
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                result += char.upper() if i % 2 else char.lower()
            else:
                result += char
        await interaction.response.send_message(result)
    
    @app_commands.command(name="countdown", description="Start a tiny countdown.")
    async def countdown(self, interaction: discord.Interaction, number: int):
        if number < 1 or number > 10:
            await interaction.response.send_message("❌ Pick a number from 1 to 10.")
            return
        
        numbers = " ".join(str(x) for x in range(number, 0, -1))
        await interaction.response.send_message(f"⏳ {numbers} → 🚀")
    
    @app_commands.command(name="search", description="Create a Google search link.")
    async def search(self, interaction: discord.Interaction, query: str):
        encoded = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded}"
        await interaction.response.send_message(f"🔎 **Search:** {url}")
    
    @app_commands.command(name="imagesearch", description="Create a Google image search link.")
    async def imagesearch(self, interaction: discord.Interaction, query: str):
        encoded = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?tbm=isch&q={encoded}"
        await interaction.response.send_message(f"🖼️ **Image search:** {url}")

async def setup(bot):
    await bot.add_cog(FriendlyCog(bot))