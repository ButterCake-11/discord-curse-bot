# 🔮 Discord Curse Bot

A feature-rich, fun Discord bot with curse commands, cat features, meme commands, rating meters, and more!

## ✨ Features

### 🔮 Curse Commands
- `/curse` - Curse someone with a random curse
- `/cursecreate` - Create custom curses (owner only)
- `/curserename` - Rename custom curses (owner only)
- `/cursedelete` - Delete custom curses (owner only)
- `/curses` - List all available curses
- `/newcurses` - Show custom curses
- `/oldcurses` - Show built-in curses
- `/randomcurse` - Get a random curse

### 🐱 Cat Commands
- `/meow` - MEOW!
- `/mrrp` - Mrrp.
- `/hiss` - Hiss!
- `/zoomies` - Activate cat zoomies
- `/loaf` - Become a loaf
- `/feed` - Feed a cat
- `/catify` - Catify someone
- `/catfact` - Get a cat fact

### 😂 Meme Commands
- `/bonk` - BONK someone
- `/yap` - YAP
- `/npc` - NPC mode
- `/skillissue` - Skill issue
- `/ratio` - RATIO'D
- `/cope` - Cope
- `/sus` - VERY SUS
- `/caught` - Caught in 4K
- `/touchgrass` - Touch grass
- `/getreal` - Get real
- `/emotionaldamage` - Emotional damage
- `/whoasked` - Who asked?

### 🎲 Random/Fun Commands
- `/coinflip` - Flip a coin
- `/dice` - Roll a die
- `/8ball <question>` - Ask the magic 8-ball
- `/choose <options>` - Choose between comma-separated options
- `/random <min> <max>` - Generate a random number
- `/iq` - Silly IQ generator
- `/braincell` - Check your braincells

### 🍌 Silly Commands
- `/banana` - BANANA!
- `/potato` - Potato
- `/spaghetti` - SPAGHETTI EVERYWHERE
- `/loading` - Loading animation
- `/error` - Generate an error
- `/404` - 404 error
- `/what` - What?
- `/huh` - Huh?

### 💖 Friendly Commands
- `/hug <user>` - Give a friendly hug
- `/highfive <user>` - High five someone
- `/compliment <user>` - Give a compliment
- `/roast <user>` - Harmless silly roast
- `/say <text>` - Make the bot say something
- `/reverse <text>` - Reverse text
- `/mock <text>` - Alternate capitalization
- `/countdown <number>` - Start a countdown
- `/search <query>` - Create a Google search link
- `/imagesearch <query>` - Create a Google image search link

### 📊 Rating Commands
- `/susrate <user>` - Sus rating meter
- `/gayrate <user>` - Rainbow meter
- `/furry_rate <user>` - Furry meter
- `/femboyrate <user>` - Style meter
- `/chaosrate <user>` - Chaos level meter
- `/goofyrate <user>` - Goofiness meter
- `/iqtest <user>` - Fictional IQ test

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ButterCake-11/discord-curse-bot.git
cd discord-curse-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Create Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Name your bot
4. Go to "Bot" tab → Click "Add Bot"
5. Under "TOKEN" click "Copy" (save this!)
6. Enable these **Intents**:
   - Message Content Intent
   - Server Members Intent
7. Go to "OAuth2" → "URL Generator"
8. Select scopes: `bot`
9. Select permissions:
   - Send Messages
   - Read Messages/View Channels
   - Embed Links
   - Mention @everyone, @here, and @[Role]
10. Copy the generated URL and open it to invite the bot to your server

### Step 4: Setup Environment
1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` and add your values:
```
DISCORD_TOKEN=your_bot_token_here
OWNER_ID=your_discord_user_id_here
```

**How to get your Discord User ID:**
- Enable Developer Mode in Discord (User Settings → App Settings → Advanced → Developer Mode)
- Right-click your username and select "Copy User ID"

### Step 5: Run the Bot
```bash
python main.py
```

You should see:
```
✅ Logged in as YourBotName
🤖 Bot ID: 123456789
📊 Servers: 1
✅ Synced X slash commands
```

## 🌍 Hosting Options

### Option 1: Local Machine
Just run `python main.py` whenever you want the bot online.

### Option 2: Railway.app (Recommended - Free tier available)
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub account
3. Create new project → Deploy from GitHub
4. Select this repository
5. Add environment variables (DISCORD_TOKEN, OWNER_ID)
6. Deploy!

### Option 3: Render.com
1. Go to [render.com](https://render.com)
2. Create new "Web Service"
3. Connect GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python main.py`
6. Add environment variables
7. Deploy!

### Option 4: Heroku (Requires Payment Now)
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Run: `heroku login`
3. Create: `heroku create your-bot-name`
4. Set variables: `heroku config:set DISCORD_TOKEN=your_token`
5. Deploy: `git push heroku main`

## 📁 Project Structure

```
discord-curse-bot/
├── main.py                 # Bot entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
├── custom_curses.json     # Custom curses storage (auto-created)
└── cogs/
    ├── __init__.py
    ├── curses.py          # Curse commands
    ├── cats.py            # Cat commands
    ├── memes.py           # Meme commands
    ├── random_commands.py # Random/fun commands
    ├── silly.py           # Silly commands
    ├── friendly.py        # Friendly commands
    └── rates.py           # Rating commands
```

## 🔧 Troubleshooting

### Commands Not Showing Up
- Make sure bot is running: `python main.py`
- Check if bot has permissions in your server
- Try using `/` in chat to see if commands appear
- Wait a few minutes for slash commands to sync

### Bot Not Responding
1. Check if bot is online (green status)
2. Verify `DISCORD_TOKEN` is correct in `.env`
3. Check bot logs for errors
4. Make sure bot has "Send Messages" permission

### "Intents" Issues
- Make sure Message Content Intent is enabled in Developer Portal
- Verify bot token is copied correctly

### Custom Curses Not Saving
- Check if `custom_curses.json` exists
- Verify bot has write permissions in the directory
- Make sure owner ID is set correctly

## 🤝 Contributing

Feel free to fork, modify, and improve this bot!

## 📝 License

Free to use and modify!

## 💬 Support

If you have questions or issues:
1. Check the Troubleshooting section
2. Review your `.env` file setup
3. Make sure all dependencies are installed
4. Check bot permissions in your Discord server

---

**Enjoy your curse bot!** 🔮✨
