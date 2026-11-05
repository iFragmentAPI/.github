# Fragment API Bot for Telegram Stars, Premium & Gifts

Get a TGTools API key from [@ifragmentapibot](https://t.me/ifragmentapibot?start=github). Open the bot and send `/start`. **API key issuance is free, with no subscription or KYC required to get a key.** Purchases are charged to your funded TGTools wallet.

[**Start the Telegram bot**](https://t.me/ifragmentapibot?start=github) · [**Read the API docs**](https://tg-tools.shop/api-docs) · [**Visit TGTools**](https://tg-tools.shop/)

## Get your API key

1. Open [@ifragmentapibot](https://t.me/ifragmentapibot?start=github) and tap **Start** or send `/start`.
2. Follow the bot prompts to get your key.
3. Store the key on your server and send it in the `X-Api-Key` header. Keep it out of client code, logs, and public repositories.
4. Check live prices and validate the recipient before creating an order. Fund your wallet before submitting a purchase.

## What you can build

| Feature | What the API does |
| --- | --- |
| Telegram Stars | Buy Stars for a Telegram username. |
| Telegram Premium | Send 3-, 6-, or 12-month subscriptions. |
| Telegram Gifts | Browse available gifts and send one with an optional message. |
| Pricing and recipient lookup | Check live quotes and look up recipients before ordering. |
| Wallet and orders | Check your balance, deposit history, and order status. |

## Try a read-only request

Run the [Python quickstart](quickstart.py) with a Telegram username to check live Stars pricing and look up the recipient. It needs Python 3.9 or newer and uses only the standard library.

```bash
python3 quickstart.py TELEGRAM_USERNAME
```

Set `TGTOOLS_API_KEY` in your shell using the key from the bot. This authenticated request checks your wallet balance.

```bash
curl --fail-with-body 'https://api.tg-tools.shop/api/wallet' \
  -H "X-Api-Key: ${TGTOOLS_API_KEY}"
```

When you're ready to integrate purchases, start with `POST /api/purchase/stars` or `POST /api/purchase/premium`. Use a distinct tracking code for each order, and check its status before treating it as delivered. The [API reference](https://tg-tools.shop/api-docs) includes request and response examples in cURL, JavaScript, Python, and PHP.

iFragmentAPI promotes the TGTools integration for developers building bots, storefronts, and reseller tools. TGTools is an independent service.
