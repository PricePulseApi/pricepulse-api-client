/**
 * PricePulse API - Shopify & E-Commerce Real-Time Tracker (Node.js)
 * High-speed price & stock extractor for e-commerce developers.
 *
 * Install: npm install axios
 */

const axios = require('axios');

const RAPIDAPI_KEY = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY";

const client = axios.create({
  baseURL: "https://pricepulse-e-commerce-price-stock-intelligence-api.p.rapidapi.com",
  headers: {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "pricepulse-e-commerce-price-stock-intelligence-api.p.rapidapi.com",
    "Content-Type": "application/json"
  }
});

async function extractProduct(productUrl) {
  try {
    console.log(`⚡ Extracting data from: ${productUrl}`);
    const start = Date.now();
    const response = await client.post('/v1/extract', { url: productUrl });
    const elapsed = Date.now() - start;

    const { data } = response.data;
    console.log(`✅ Success in ${elapsed}ms:`);
    console.log(`   Title:         ${data.title}`);
    console.log(`   Current Price: ${data.current_price} ${data.currency}`);
    console.log(`   In Stock:      ${data.in_stock ? 'YES' : 'NO'}`);
    console.log(`   Discount:      ${data.discount_percent}%`);
    console.log(`   Platform:      ${data.platform}`);
  } catch (error) {
    console.error("❌ Extraction failed:", error.response ? error.response.data : error.message);
  }
}

// Run test
extractProduct("https://allbirds.com/products/mens-tree-runners");
