#!/usr/bin/env python3
"""
PricePulse CLI - Lightning-Fast E-Commerce Intelligence Terminal Utility
Usage:
    python cli.py extract "https://www.etsy.com/listing/..." --key YOUR_KEY
    python cli.py diff "https://allbirds.com/products/..." --prev 120.0 --key YOUR_KEY
"""

import argparse
import json
import os
import sys
from pricepulse_client import PricePulseClient


def main():
    parser = argparse.ArgumentParser(description="PricePulse API CLI - E-Commerce Price & Stock Intelligence")
    parser.add_argument("--key", default=os.getenv("RAPIDAPI_KEY"), help="Your RapidAPI Key (or set RAPIDAPI_KEY env var)")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: extract
    p_extract = subparsers.add_parser("extract", help="Extract real-time product data from URL")
    p_extract.add_argument("url", help="Product page URL (Etsy, Shopify, WooCommerce, etc.)")

    # Command: diff
    p_diff = subparsers.add_parser("diff", help="Compare current price against historical baseline")
    p_diff.add_argument("url", help="Product page URL")
    p_diff.add_argument("--prev", type=float, required=True, help="Previous known price")
    p_diff.add_argument("--threshold", type=float, default=0.0, help="Alert threshold drop percentage (e.g. 5.0 for 5%)")

    # Command: batch
    p_batch = subparsers.add_parser("batch", help="Extract multiple URLs in parallel")
    p_batch.add_argument("urls", nargs="+", help="Space-separated product URLs (up to 25)")

    args = parser.parse_args()

    api_key = args.key
    if not api_key:
        print("❌ Error: RapidAPI Key is required! Provide via --key or set export RAPIDAPI_KEY='your_key'")
        print("👉 Get your key at: https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api")
        sys.exit(1)

    client = PricePulseClient(api_key=api_key)

    try:
        if args.command == "extract":
            print(f"⚡ Extracting: {args.url} ...")
            res = client.extract(args.url)
            print(json.dumps(res, indent=2))
        elif args.command == "diff":
            print(f"📊 Analyzing price diff for: {args.url} (Baseline: ${args.prev}) ...")
            res = client.monitor_diff(args.url, previous_price=args.prev, alert_threshold_percent=args.threshold)
            print(json.dumps(res, indent=2))
        elif args.command == "batch":
            print(f"🚀 Batch extracting {len(args.urls)} URLs in parallel ...")
            res = client.extract_batch(args.urls)
            print(json.dumps(res, indent=2))
    except Exception as exc:
        print(f"❌ API Request Failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
