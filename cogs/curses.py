import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import random

CURSES_FILE = "custom_curses.json"

class CurseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.custom_curses = self.load_curses()
        
        self.builtin_curses = {
            "kitty": "🐱 You have been cursed with uncontrollable cat noises.",
            "silly": "🤪 You are now legally silly.",
            "npc": "🧍 NPC mode activated.",
            "goose": "🪿 A goose has noticed you.",
            "fish": "🐟 You have been fishified.",
            "loading": "⏳ Your brain is still loading...",
            "tax": "💸 The silly tax collector has arrived.",
            "brainrot": "🧠 Your brain has been replaced with soup.",
            "cat": "🐈 You have been turned into a cat.",
            "bonk": "🔨 BONK! Go to the silly corner.",
            "confusion": "❓ Confusion has entered the chat.",
            "goofy": "🤡 Goofy mode activated.",
            "spaghetti": "🍝 Your thoughts are now spaghetti.",
        }
    
    # =========================================================
    # CURSE STORAGE
    # =========================================================
    
    def load_curses(self):
        """Load custom curses from JSON file"""
        if not os.path.exists(CURSES_FILE):
            return {}
        try:
            with open(CURSES_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Error loading curses: {e}")
            return {}
    
    def save_curses(self):
        """Save custom curses to JSON file"""
        try:
            with open(CURSES_FILE, "w", encoding="utf-8") as file:
                json.dump(self.custom_curses, file, indent=4, ensure_ascii=False)
        except OSError as e:
            print(f"Error saving curses: {e}")
    
    async def owner_check(self, interaction: discord.Interaction) -> bool:
        """Check if user is the bot owner"""
        owner_id = int(os.getenv("OWNER_ID", "0"))
        if interaction.user.id != owner_id:
            await interaction.response.send_message(
                "🚫 This command is only for my owner.",
                ephemeral=True
            )
            return False
        return True
    
    # =========================================================
    # CURSE COMMANDS
    # =========================================================
    
    @app_commands.command(
        name="curse",
        description="Curse someone with a random curse."
    )
    async def curse(self, interaction: discord.Interaction, user: discord.User):
        """Curse a user with a random curse"""
        all_curses = {**self.builtin_curses, **self.custom_curses}
        
        if not all_curses:
            await interaction.response.send_message("🔮 There aren't any curses yet!")
            return
        
        curse_name, curse_text = random.choice(list(all_curses.items()))
        
        await interaction.response.send_message(
            f"🔮 **Cursed {user.mention}!**\n**{curse_name}:** {curse_text}"
        )
        
        try:
            await user.send(f"🔮 **You have been cursed!**\n{curse_text}")
        except discord.Forbidden:
            print(f"Couldn't DM {user}.")
    
    @app_commands.command(
        name="cursecreate",
        description="Create a custom curse."
    )
    async def cursecreate(self, interaction: discord.Interaction, name: str, text: str):
        """Create a new custom curse (owner only)"""
        if not await self.owner_check(interaction):
            return
        
        self.custom_curses[name.lower()] = text
        self.save_curses()
        
        await interaction.response.send_message(f"🔮 Added custom curse **{name}**!")
    
    @app_commands.command(
        name="curserename",
        description="Rename a custom curse."
    )
    async def curserename(self, interaction: discord.Interaction, old_name: str, new_name: str):
        """Rename a custom curse (owner only)"""
        if not await self.owner_check(interaction):
            return
        
        old_name = old_name.lower()
        new_name = new_name.lower()
        
        if old_name not in self.custom_curses:
            await interaction.response.send_message("❌ That custom curse doesn't exist.")
            return
        
        self.custom_curses[new_name] = self.custom_curses.pop(old_name)
        self.save_curses()
        
        await interaction.response.send_message(f"✏️ Renamed **{old_name}** → **{new_name}**!")
    
    @app_commands.command(
        name="cursedelete",
        description="Delete a custom curse."
    )
    async def cursedelete(self, interaction: discord.Interaction, name: str):
        """Delete a custom curse (owner only)"""
        if not await self.owner_check(interaction):
            return
        
        name = name.lower()
        
        if name not in self.custom_curses:
            await interaction.response.send_message("❌ That custom curse doesn't exist.")
            return
        
        del self.custom_curses[name]
        self.save_curses()
        
        await interaction.response.send_message(f"🗑️ Deleted **{name}**!")
    
    @app_commands.command(
        name="curses",
        description="List all available curses."
    )
    async def curses(self, interaction: discord.Interaction):
        """List all available curses"""
        names = list(self.builtin_curses.keys()) + list(self.custom_curses.keys())
        
        if not names:
            await interaction.response.send_message("🔮 No curses exist.")
            return
        
        text = "\n".join(f"• `{name}`" for name in names)
        await interaction.response.send_message(f"🔮 **Curses ({len(names)})**\n{text}")
    
    @app_commands.command(
        name="newcurses",
        description="Show custom curses."
    )
    async def newcurses(self, interaction: discord.Interaction):
        """Show all custom curses"""
        if not self.custom_curses:
            await interaction.response.send_message("🆕 No custom curses yet!")
            return
        
        text = "\n".join(f"• `{name}` — {curse}" for name, curse in self.custom_curses.items())
        await interaction.response.send_message(f"🆕 **Custom Curses**\n{text}")
    
    @app_commands.command(
        name="oldcurses",
        description="Show built-in curses."
    )
    async def oldcurses(self, interaction: discord.Interaction):
        """Show all built-in curses"""
        text = "\n".join(f"• `{name}`" for name in self.builtin_curses)
        await interaction.response.send_message(f"📜 **Built-in Curses**\n{text}")
    
    @app_commands.command(
        name="randomcurse",
        description="Get a random curse."
    )
    async def randomcurse(self, interaction: discord.Interaction):
        """Get a random curse without cursing anyone"""
        all_curses = {**self.builtin_curses, **self.custom_curses}
        curse_name, curse_text = random.choice(list(all_curses.items()))
        
        await interaction.response.send_message(f"🔮 **{curse_name}**\n{curse_text}")

async def setup(bot):
    await bot.add_cog(CurseCog(bot))
