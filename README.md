# LoL Player Analyzer

A small local desktop app for checking League of Legends player history and live-game status using Riot's public API.

## Features

- Search a summoner by region and name
- Fetch recent match IDs and summarize recent results
- Check whether a live game is active
- Show the status of Riot ban checks transparently

## Important note

Riot does not provide an official public ban-status endpoint for a summoner. This app clearly shows that limitation instead of pretending it can fetch private account enforcement data directly.

## Local setup

1. Install Python 3.10+
2. Create a virtual environment
3. Install dependencies
4. Create a `.env` file with your Riot API key

Example `.env`:

```dotenv
RIOT_API_KEY=your_key_here
```

Install:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

## Build to Windows EXE

```bash
pip install pyinstaller
pyinstaller --onefile --windowed app.py --name LolPlayerAnalyzer
```

## Compliance

Use Riot's API according to their terms and rate limits. This project is intended for local development and personal analysis use.
