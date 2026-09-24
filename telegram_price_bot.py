"""
PricePulse API - Turnkey Telegram Deal Alert & Price Drop Bot
Monitors competitor e-commerce prices and automatically broadcasts alerts to a Telegram Channel or Group.

Requirements:
    pip install requests
"""

import time
import requests

# 1. Configuration
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # Get free at https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # From @BotFather
TELEGRAM_CHAT_ID = "@your_channel_or_chat_id"   # Channel @username or numeric ID

MONITORED_PRODUCTS = [
    {
        "url": "https://www.etsy.com/listing/1776489744/ultimate-annual-budget-spreadsheet",
        "baseline_price": 30.00,
        "name": "Etsy Annual Budget Template"
    },
    {
        "url": "https://allbirds.com/products/mens-tree-runners",
        "baseline_price": 110.00,
        "name": "Allbirds Men's Tree Runners"
    }
]

DIFF_ENDPOINT = "https://pricepulse-e-commerce-price-stock-intelligence-api.p.rapidapi.com/v1/monitor/diff"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "pricepulse-e-commerce-price-stock-intelligence-api.p.rapidapi.com",
    "Content-Type": "application/json"
}


def send_telegram_alert(text: str):
    """Sends message to Telegram via Bot API."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    requests.post(url, json=payload)


def monitor_loop():
    print("🚀 PricePulse Telegram Monitor Bot Started...")
    for item in MONITORED_PRODUCTS:
        body = {
            "url": item["url"],
            "previous_price": item["baseline_price"],
            "alert_threshold_percent": 1.0
        }

        try:
            resp = requests.post(DIFF_ENDPOINT, json=body, headers=HEADERS, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("alert_triggered"):
                    alert_type = data.get("alert_type")
                    curr_price = data.get("current_price")
                    diff_pct = abs(data.get("price_change_percent", 0.0))

                    if alert_type == "price_drop":
                        msg = (
                            f"⚡ *PRICE DROP ALERT!* ⚡\n\n"
                            f"📦 *Product:* {item['name']}\n"
                            f"💰 *New Price:* `${curr_price}` (Saved {diff_pct:.1f}%)\n"
                            f"🔗 [Direct Product Link]({item['url']})\n\n"
                            f"_Powered by PricePulse API on RapidAPI_"
                        )
                        print(f"🚨 Sending Telegram alert for: {item['name']}")
                        send_telegram_alert(msg)
                    elif alert_type == "out_of_stock":
                        msg = f"⚠️ *OUT OF STOCK:* {item['name']} is currently unavailable.\n🔗 {item['url']}"
                        send_telegram_alert(msg)
                else:
                    print(f"✅ {item['name']} checked: Price is stable at ${data.get('current_price')}")
            else:
                print(f"❌ API Error {resp.status_code}: {resp.text}")
        except Exception as e:
            print(f"❌ Error checking {item['name']}: {e}")


if __name__ == "__main__":
    monitor_loop()
