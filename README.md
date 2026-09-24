# PricePulse API ⚡
> The Fastest Real-Time E-Commerce Competitor, Price & Stock Intelligence Engine. Sub-350ms extraction for Etsy, Shopify, and Global Online Stores.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Subscribe%20Now-0052CC?style=for-the-badge&logo=rapidapi&logoColor=white)](https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)
[![Service Level](https://img.shields.io/badge/Service%20Level-100%25-brightgreen?style=for-the-badge)](https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)
[![Latency](https://img.shields.io/badge/Latency-233ms-blue?style=for-the-badge)](https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PricePulseApi/pricepulse-api-client/blob/main/PricePulse_Quickstart.ipynb)
[![Postman](https://img.shields.io/badge/Postman-Collection%20Included-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](#-postman-collection)

---

### 🚀 Get Instant API Key
PricePulse API is hosted 24/7 on high-performance cloud infrastructure and exclusively distributed via **RapidAPI Hub**:

👉 **[Start Free on RapidAPI Marketplace (10 Free Evaluation Calls)](https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)**

---

### 💡 Why Developers Choose PricePulse Over Traditional Scrapers

| Feature | Headless Scrapers (Selenium / Puppeteer) | **PricePulse API** |
| :--- | :--- | :--- |
| **Response Latency** | 8,000ms – 20,000ms (Heavy Chromium) | **⚡ 190ms – 350ms (Ultralight C-DOM Engine)** |
| **Etsy DataDome WAF** | ❌ 403 Forbidden / Captcha Blocked | **✅ 100% Unblockable Native API Access** |
| **Shopify Intelligence** | ❌ Slow full-page rendering | **✅ Sub-200ms Direct Variant Catalog JSON** |
| **Price Diff & Alerts** | ❌ Build your own historical DB engine | **✅ Built-in `/v1/monitor/diff` Instant Alerts** |
| **Server Cost** | \$300 – \$1,000+ / month (Proxies & VPS) | **Starting at \$0 (Evaluation) / \$39 (Pro)** |

---

### 📦 Python SDK Quickstart (`pricepulse_client`)
Install locally with `pip install .` or import directly:

```python
from pricepulse_client import PricePulseClient

client = PricePulseClient(api_key="YOUR_RAPIDAPI_KEY")

# 1. Single product extraction (Etsy, Shopify, WooCommerce)
data = client.extract("https://www.etsy.com/listing/1776489744/ultimate-annual-budget-spreadsheet")
print("Current Price:", data["data"]["current_price"], data["data"]["currency"])

# 2. Automated price drop check
diff = client.monitor_diff("https://allbirds.com/products/mens-tree-runners", previous_price=120.0, alert_threshold_percent=5.0)
if diff["alert_triggered"]:
    print("🚨 Price Alert Triggered:", diff["alert_type"], diff["price_change"])

# 3. Batch extract up to 25 URLs in parallel
batch = client.extract_batch([
    "https://www.etsy.com/listing/1776489744/ultimate-annual-budget-spreadsheet",
    "https://allbirds.com/products/mens-tree-runners"
])
print("Extracted items:", batch["successful"])
```

---

### 💻 Terminal CLI Utility (`cli.py`)
Run instant extractions and price comparisons straight from your command line:

```bash
# Extract single product
python cli.py extract "https://allbirds.com/products/mens-tree-runners" --key YOUR_KEY

# Compare against historical benchmark
python cli.py diff "https://allbirds.com/products/mens-tree-runners" --prev 120.0 --threshold 5.0 --key YOUR_KEY

# Batch extract multiple URLs
python cli.py batch "https://url1.com" "https://url2.com" --key YOUR_KEY
```

---

### 🤖 Turnkey Automation Bots (Ready to Deploy)
- **[Discord Price Drop Bot (discord_price_alert.py)](./discord_price_alert.py):** Posts rich embeds to your Discord channel when a competitor cuts prices or goes out of stock.
- **[Telegram Deal Alert Bot (telegram_price_bot.py)](./telegram_price_bot.py):** Automatically broadcasts discount alerts to your Telegram deal channel or group.
- **[Shopify Real-Time Tracker (shopify_tracker.js)](./shopify_tracker.js):** Lightweight Node.js tracker for Shopify stores.

---

### 📬 Postman Collection & Colab Notebook
- **Interactive Google Colab:** [Run in Google Colab](https://colab.research.google.com/github/PricePulseApi/pricepulse-api-client/blob/main/PricePulse_Quickstart.ipynb)
- **Postman Collection:** [`PricePulse_API.postman_collection.json`](./PricePulse_API.postman_collection.json)

---

### 💎 Subscription Plans on RapidAPI
| Tier | Price | Monthly Quota | Best For |
| :--- | :--- | :--- | :--- |
| **Basic (Evaluation)** | **\$0.00 / mo** | 10 requests | Quick testing & sandbox integration |
| **Pro (Recommended ⭐)** | **\$39.00 / mo** | 15,000 requests | E-commerce stores, repricers, Discord/Telegram bots |
| **Ultra** | **\$149.00 / mo** | 100,000 requests | High-volume dropshipping & SaaS platforms |

👉 **[Subscribe on RapidAPI Marketplace](https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)**
