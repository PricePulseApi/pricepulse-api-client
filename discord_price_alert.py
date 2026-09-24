"""
PricePulse API - Automated Discord Price Drop & Stock Alert Bot
Tracks e-commerce prices (Etsy, Shopify, etc.) and posts instant alerts to Discord via Webhook.

Requirements:
    pip install requests
"""

import time
import requests

# 1. Configuration
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # Get free at https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

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


def send_discord_notification(title: str, message: str, color: int, product_url: str):
    """Dispatches a rich embed to Discord webhook."""
    payload = {
        "embeds": [
            {
                "title": f"⚡ PricePulse Alert: {title}",
                "description": message,
                "url": product_url,
                "color": color,
                "footer": {"text": "Powered by PricePulse API • RapidAPI"}
            }
        ]
    }
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


def check_prices():
    print("🔍 Checking tracked products via PricePulse API...")
    for item in MONITORED_PRODUCTS:
        body = {
            "url": item["url"],
            "previous_price": item["baseline_price"],
            "alert_threshold_percent": 1.0  # Alert if price drops by >= 1%
        }

        try:
            resp = requests.post(DIFF_ENDPOINT, json=body, headers=HEADERS, timeout=10)
            if resp.status_code == 200:
                result = resp.json()
                if result.get("alert_triggered"):
                    alert_type = result.get("alert_type")
                    curr_price = result.get("current_price")
                    diff_pct = result.get("price_change_percent")
                    
                    if alert_type == "price_drop":
                        msg = f"📉 **Price Dropped!** Now **${curr_price}** (Saved {abs(diff_pct):.1f}% from ${item['baseline_price']})"
                        print(f"🚨 ALERT: {item['name']} - {msg}")
                        send_discord_notification(item["name"], msg, 0x00FF88, item["url"])
                    elif alert_type == "out_of_stock":
                        msg = "⚠️ **Item went OUT OF STOCK!**"
                        print(f"🚨 ALERT: {item['name']} - {msg}")
                        send_discord_notification(item["name"], msg, 0xFF3366, item["url"])
                else:
                    print(f"✅ {item['name']}: No significant price change (Current: ${result.get('current_price')})")
            else:
                print(f"❌ Error {resp.status_code}: {resp.text}")
        except Exception as e:
            print(f"❌ Failed to check {item['name']}: {e}")


if __name__ == "__main__":
    check_prices()
