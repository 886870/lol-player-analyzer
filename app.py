from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

from riot_client import RiotClient
from gui import main

API_KEY = os.getenv("RIOT_API_KEY", "")

if __name__ == "__main__":
    if not API_KEY:
        print("Missing RIOT_API_KEY. Create a .env file with RIOT_API_KEY=your_key")
        input("Press Enter to exit...")
        raise SystemExit(1)

    client = RiotClient(API_KEY)
    main(client)
