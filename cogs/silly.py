import discord
from discord.ext import commands
from discord import app_commands

class SillyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="banana", description="BANANA.")
    async def banana(self, interaction: discord.Interaction):
        await interaction.response.send_message("🍌 BANANAAAAAAAA")
    
    @app_commands.command(name="potato", description="Potato.")
    async def potato(self, interaction: discord.Interaction):
        await interaction.response.send_message("🥔 potato.")
    
    @app_commands.command(name="spaghetti", description="Spaghetti.")
    async def spaghetti(self, interaction: discord.Interaction):
        await interaction.response.send_message("🍝 SPAGHETTI EVERYWHERE")
    
    @app_commands.command(name="loading", description="Loading...")
    async def loading(self, interaction: discord.Interaction):
        await interaction.response.send_message("⏳ Loading...\n▰▰▰▰▰▰▰▰▰▰ 100%\n✨ Done!")
    
    @app_commands.command(name="error", description="Generate an error.")
    async def error(self, interaction: discord.Interaction):
        await interaction.response.send_message("⚠️ ERROR: silliness detected.")
    
    @app_commands.command(name="404", description="404.")
    async def error404(self, interaction: discord.Interaction):
        await interaction.response.send_message("❌ 404: brain not found.")
    
    @app_commands.command(name="what", description="What?")
    async def what(self, interaction: discord.Interaction):
        await interaction.response.send_message("what 😭")
    
    @app_commands.command(name="huh", description="Huh?")
    async def huh(self, interaction: discord.Interaction):
        await interaction.response.send_message("huh 😭")

async def setup(bot):
    await bot.add_cog(SillyCog(bot))