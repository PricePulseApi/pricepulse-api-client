"""
PricePulse API - Official Lightweight Python SDK Client
Enables sub-350ms e-commerce price and stock extraction in just 3 lines of code.
"""

from typing import Any, Dict, List, Optional
import httpx


class PricePulseClient:
    """Official SDK client for PricePulse API on RapidAPI."""

    DEFAULT_HOST = "pricepulse-e-commerce-price-stock-intelligence-api.p.rapidapi.com"
    BASE_URL = f"https://{DEFAULT_HOST}"

    def __init__(self, api_key: str, host: Optional[str] = None, timeout: float = 15.0):
        """
        Initialize PricePulse client.
        :param api_key: Your RapidAPI Key (Get free at https://rapidapi.com/pricepulse-api-pricepulse-api-default/api/pricepulse-e-commerce-price-stock-intelligence-api)
        """
        if not api_key:
            raise ValueError("RapidAPI Key is required to initialize PricePulseClient.")

        self.api_key = api_key
        self.host = host or self.DEFAULT_HOST
        self.timeout = timeout
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host,
            "Content-Type": "application/json"
        }

    def extract(self, url: str) -> Dict[str, Any]:
        """
        Extract real-time price, stock, discount, and variant data for a single product URL.
        :param url: Target e-commerce URL (Etsy, Shopify, WooCommerce, etc.)
        :return: JSON response dictionary
        """
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(
                f"{self.BASE_URL}/v1/extract",
                json={"url": url},
                headers=self.headers
            )
            resp.raise_for_status()
            return resp.json()

    def monitor_diff(self, url: str, previous_price: float, alert_threshold_percent: float = 0.0) -> Dict[str, Any]:
        """
        Compare current live price against historical baseline and check if alert triggered.
        :param url: Target product URL
        :param previous_price: Historical known price to compare against
        :param alert_threshold_percent: Minimum drop percentage to flag alert_triggered: true
        :return: Diff analysis response dictionary
        """
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(
                f"{self.BASE_URL}/v1/monitor/diff",
                json={
                    "url": url,
                    "previous_price": previous_price,
                    "alert_threshold_percent": alert_threshold_percent
                },
                headers=self.headers
            )
            resp.raise_for_status()
            return resp.json()

    def extract_batch(self, urls: List[str]) -> Dict[str, Any]:
        """
        Extract multiple e-commerce URLs concurrently (up to 25 URLs per request).
        :param urls: List of product URLs
        :return: Batch results dictionary
        """
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(
                f"{self.BASE_URL}/v1/batch",
                json={"urls": urls},
                headers=self.headers
            )
            resp.raise_for_status()
            return resp.json()
