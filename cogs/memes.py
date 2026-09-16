import discord
from discord.ext import commands
from discord import app_commands
import random

class MemesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="bonk", description="BONK someone.")
    async def bonk(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"🔨 BONK! {user.mention}")
    
    @app_commands.command(name="yap", description="YAP.")
    async def yap(self, interaction: discord.Interaction):
        await interaction.response.send_message("🗣️ YAP YAP YAP YAP YAP")
    
    @app_commands.command(name="npc", description="NPC mode.")
    async def npc(self, interaction: discord.Interaction):
        await interaction.response.send_message("🧍 NPC MODE ACTIVATED")
    
    @app_commands.command(name="skillissue", description="Skill issue.")
    async def skillissue(self, interaction: discord.Interaction):
        await interaction.response.send_message("💀 sounds like a skill issue")
    
    @app_commands.command(name="ratio", description="Ratio.")
    async def ratio(self, interaction: discord.Interaction):
        await interaction.response.send_message("📊 RATIO'D")
    
    @app_commands.command(name="cope", description="Cope.")
    async def cope(self, interaction: discord.Interaction):
        await interaction.response.send_message("🫵 cope")
    
    @app_commands.command(name="sus", description="Sus.")
    async def sus(self, interaction: discord.Interaction):
        await interaction.response.send_message("ඞ VERY SUS")
    
    @app_commands.command(name="caught", description="Caught in 4K.")
    async def caught(self, interaction: discord.Interaction):
        await interaction.response.send_message("📸 CAUGHT IN 4K")
    
    @app_commands.command(name="touchgrass", description="Touch grass.")
    async def touchgrass(self, interaction: discord.Interaction):
        await interaction.response.send_message("🌱 GO TOUCH GRASS")
    
    @app_commands.command(name="getreal", description="Get real.")
    async def getreal(self, interaction: discord.Interaction):
        await interaction.response.send_message("🗿 bro please get real")
    
    @app_commands.command(name="emotionaldamage", description="Emotional damage.")
    async def emotionaldamage(self, interaction: discord.Interaction):
        await interaction.response.send_message("💥 EMOTIONAL DAMAGE")
    
    @app_commands.command(name="whoasked", description="Who asked?")
    async def whoasked(self, interaction: discord.Interaction):
        await interaction.response.send_message("👀 who asked")

async def setup(bot):
    await bot.add_cog(MemesCog(bot))