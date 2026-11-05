"""Check Telegram Stars pricing and look up a recipient using TGTools.

Run: python3 quickstart.py TELEGRAM_USERNAME
Both requests are read-only and require no API key.
API docs: https://tg-tools.shop/api-docs
Get an API key: https://t.me/ifragmentapibot?start=github
"""

import argparse
import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

BASE_URL = "https://api.tg-tools.shop"


def get(path):
    with urlopen(BASE_URL + path, timeout=15) as response:
        result = json.load(response)

    if isinstance(result, dict) and "isSuccess" in result:
        if not result["isSuccess"]:
            raise ValueError(result.get("message") or "The API rejected the request.")
        return result["data"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("username", help="Telegram username with or without @")
    args = parser.parse_args()
    username = args.username.removeprefix("@")
    if not re.fullmatch(r"[A-Za-z0-9_]{1,32}", username):
        parser.error("Enter a Telegram username, using letters, digits, or underscores.")

    try:
        prices = get("/api/purchase/prices")
        recipient = get(f"/api/purchase/user/{username}")
        print(json.dumps({
            "stars_price_ton": prices["stars_price_ton"],
            "recipient": recipient,
        }, indent=2, ensure_ascii=False))
    except HTTPError as error:
        parser.exit(1, f"TGTools returned HTTP {error.code}.\n")
    except (URLError, ValueError, KeyError, TimeoutError) as error:
        parser.exit(1, f"Could not complete the lookup: {error}\n")


if __name__ == "__main__":
    main()
