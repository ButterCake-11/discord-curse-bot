import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# =========================================================
# VALIDATION
# =========================================================

if not TOKEN:
    print("\n❌ ERROR: DISCORD_TOKEN is missing!")
    print("   Please add DISCORD_TOKEN to your .env file")
    print("   See .env.example for reference\n")
    sys.exit(1)

if not OWNER_ID:
    print("\n⚠️  WARNING: OWNER_ID is missing!")
    print("   Some commands will not work without this\n")
else:
    try:
        int(OWNER_ID)
    except ValueError:
        print("\n❌ ERROR: OWNER_ID must be a valid Discord user ID (numbers only)\n")
        sys.exit(1)

# =========================================================
# BOT SETUP
# =========================================================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.direct_messages = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None,
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="for curses... 🔮"
    )
)

# =========================================================
# EVENTS
# =========================================================

@bot.event
async def on_ready():
    """Bot ready event"""
    print("\n" + "="*50)
    print(f"✅ Logged in as {bot.user}")
    print(f"🤖 Bot ID: {bot.user.id}")
    print(f"📊 Connected to {len(bot.guilds)} server(s)")
    print("="*50)
    
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"❌ Sync error: {e}")
    
    print("\n🟢 Bot is ready!\n")

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing required argument: {error.param}")
    elif isinstance(error, commands.CommandError):
        await ctx.send(f"❌ Command error: {error}")
    else:
        print(f"Uncaught error: {error}")

@bot.event
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    """Handle slash command errors"""
    if isinstance(error, discord.app_commands.CommandInvokeError):
        await interaction.response.send_message(
            "❌ An error occurred while executing the command.",
            ephemeral=True
        )
        print(f"Command error: {error}")
    else:
        print(f"App command error: {error}")

# =========================================================
# COG LOADING
# =========================================================

async def load_cogs():
    """Load all cogs from the cogs directory"""
    cogs_dir = "./cogs"
    
    if not os.path.exists(cogs_dir):
        print(f"❌ ERROR: {cogs_dir} directory not found!")
        return False
    
    loaded = 0
    failed = 0
    
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                cog_name = filename[:-3]
                await bot.load_extension(f"cogs.{cog_name}")
                print(f"✅ Loaded cog: {cog_name}")
                loaded += 1
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")
                failed += 1
    
    print(f"\n📦 Loaded {loaded} cog(s), {failed} failed")
    return failed == 0

# =========================================================
# MAIN
# =========================================================

async def main():
    """Main bot startup function"""
    async with bot:
        print("\n🔮 Discord Curse Bot Starting...\n")
        
        success = await load_cogs()
        
        if not success:
            print("\n⚠️  Some cogs failed to load, but bot will continue...\n")
        
        try:
            await bot.start(TOKEN)
        except discord.LoginFailure:
            print("\n❌ ERROR: Invalid Discord token!")
            print("   Please check your DISCORD_TOKEN in .env file\n")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ ERROR: Failed to start bot: {e}\n")
            sys.exit(1)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        sys.exit(1)
