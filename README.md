# Crypto Tracker CLI

A lightweight, terminal-based real-time cryptocurrency price tracker built with Python. It communicates with the free CoinCap API to fetch livestock data for primary digital assets without requiring API authentication tokens.

## Features
- **Real-Time Data:** Updates asset metrics automatically every 30 seconds.
- **Clean Interface:** Formats numbers dynamically into clean, human-readable currency blocks and positive/negative percentages.
- **Zero Configuration:** No external account setups or secret keys required—works right out of the box.

## Preview
```text
=======================================================
               REAL-TIME CRYPTO TRACKER                
=======================================================
Asset Name      | Price (USD)     | 24h Change     
-------------------------------------------------------
Bitcoin         | $64,321.12      | +1.45%         
Ethereum        | $3,450.50       | -0.82%         
Monero          | $172.35         | +3.12%         
=======================================================
 Press Ctrl+C to exit. Auto-refreshing every 30s...
