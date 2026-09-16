# Curse Bot Deployment Guide

## Quick Start - Local

1. **Clone & Setup**
```bash
git clone https://github.com/ButterCake-11/discord-curse-bot.git
cd discord-curse-bot
pip install -r requirements.txt
cp .env.example .env
```

2. **Configure .env**
```
DISCORD_TOKEN=your_token_here
OWNER_ID=your_user_id_here
```

3. **Run**
```bash
python main.py
```

---

## Docker (Recommended for Long-term Running)

### Using Docker Compose

1. **Setup**
```bash
git clone https://github.com/ButterCake-11/discord-curse-bot.git
cd discord-curse-bot
cp .env.example .env
```

2. **Edit .env with your credentials**

3. **Run**
```bash
docker-compose up -d
```

4. **View logs**
```bash
docker-compose logs -f
```

5. **Stop**
```bash
docker-compose down
```

### Using Docker Directly

```bash
# Build image
docker build -t curse-bot .

# Run container
docker run -d \
  --name curse-bot \
  -e DISCORD_TOKEN="your_token" \
  -e OWNER_ID="your_id" \
  -v $(pwd)/custom_curses.json:/app/custom_curses.json \
  curse-bot

# View logs
docker logs -f curse-bot

# Stop
docker stop curse-bot
```

---

## Railway.app Deployment

1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select this repository
4. Add variables:
   - `DISCORD_TOKEN`: Your bot token
   - `OWNER_ID`: Your Discord user ID
5. Click Deploy!
6. Bot will auto-restart if it crashes

**Cost**: Free tier gives you $5/month (enough for a hobby bot)

---

## Render.com Deployment

1. Go to [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect GitHub account and select this repo
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `python main.py`
6. Add environment variables:
   - `DISCORD_TOKEN`
   - `OWNER_ID`
7. Deploy!

**Cost**: Free tier works but will spin down after 15 mins of inactivity. Pay plan starts at $7/month for always-on.

---

## Replit (Not Recommended)

⚠️ **Replit has limitations** (can't save external apps, limited runtime). Use Railway or Render instead.

---

## Troubleshooting

### Bot won't start
```
❌ ERROR: DISCORD_TOKEN is missing!
```
→ Add `DISCORD_TOKEN=your_token` to `.env`

### Commands not syncing
→ Wait 2-5 minutes for Discord's cache to update
→ Try `/` in chat to see commands

### "Invalid token" error
→ Copy token again from [Developer Portal](https://discord.com/developers)
→ Make sure there's no extra whitespace

### Custom curses not saving
→ Check file permissions in the directory
→ Make sure `custom_curses.json` is not read-only

### Docker issues
```bash
# Rebuild image
docker-compose build --no-cache

# Check for errors
docker-compose logs curse-bot

# Remove everything and start fresh
docker-compose down -v
docker-compose up -d
```

---

## Keeping Bot 24/7

**Best Options**:
1. ⭐ **Railway.app** - Easiest, free tier, very reliable
2. ⭐ **Render.com** - Also free tier, good uptime
3. 🐳 **Docker on your own VPS** - Most control, need to manage yourself

**Avoid**:
- ❌ Replit (limited)
- ❌ Heroku (paid only now)
- ❌ Running on personal PC (electricity costs)

---

## Support

If you have issues:
1. Check the README.md
2. Review your `.env` file setup
3. Check bot permissions in Discord server
4. View bot logs for error messages
