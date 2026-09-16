import discord
from discord.ext import commands
from discord import app_commands
import random

class RatesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="susrate", description="Get a random sus rating.")
    async def susrate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"ඞ **Sus-o-meter:** {user.mention} is **{rating}% sus!**"
        )
    
    @app_commands.command(name="gayrate", description="Get a random rainbow meter.")
    async def gayrate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"🌈 **Rainbow meter:** {user.mention} = **{rating}%**!"
        )
    
    @app_commands.command(name="furry_rate", description="Get a random furry meter.")
    async def furry_rate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"🐾 **Furry meter:** {user.mention} = **{rating}%**!"
        )
    
    @app_commands.command(name="femboyrate", description="Get a random style meter.")
    async def femboyrate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"🎀 **Style meter:** {user.mention} = **{rating}%**!"
        )
    
    @app_commands.command(name="chaosrate", description="Measure someone's chaos level.")
    async def chaosrate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"🌪️ **Chaos meter:** {user.mention} = **{rating}% chaos!**"
        )
    
    @app_commands.command(name="goofyrate", description="Measure someone's goofiness.")
    async def goofyrate(self, interaction: discord.Interaction, user: discord.User):
        rating = random.randint(0, 100)
        await interaction.response.send_message(
            f"🤪 **Goofy meter:** {user.mention} = **{rating}% goofy!**"
        )
    
    @app_commands.command(name="iqtest", description="Take a completely fictional IQ test.")
    async def iqtest(self, interaction: discord.Interaction, user: discord.User):
        score = random.randint(70, 150)
        await interaction.response.send_message(
            f"🧠 **Totally Scientific IQ Test™**\n"
            f"{user.mention}: **{score} IQ**\n"
            f"*This is just a random joke number!*"
        )

async def setup(bot):
    await bot.add_cog(RatesCog(bot))