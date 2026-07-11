import os
import time
import requests

# The public CoinCap API doesn't require any API keys
API_URL = "https://api.coincap.io/v2/assets?ids=bitcoin,monero,ethereum"

def fetch_crypto_data():
    """Fetches real-time crypto assets from the CoinCap API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"\n[Error] Unable to connect to API: {e}")
        return []

def clear_screen():
    """Clears the terminal window depending on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_dashboard(crypto_list):
    """Formats and prints the asset data in a clean dashboard grid."""
    clear_screen()
    print("=" * 55)
    print(f"{'REAL-TIME CRYPTO TRACKER':^55}")
    print("=" * 55)
    print(f"{'Asset Name':<15} | {'Price (USD)':<15} | {'24h Change':<15}")
    print("-" * 55)
    
    for coin in crypto_list:
        name = coin.get("name", "Unknown")
        price = float(coin.get("priceUsd", 0))
        change = float(coin.get("changePercent24Hr", 0))
        
        # Clean formatting for numbers
        price_str = f"${price:,.2f}"
        change_str = f"{change:+.2f}%"
        
        print(f"{name:<15} | {price_str:<15} | {change_str:<15}")
    
    print("=" * 55)
    print(" Press Ctrl+C to exit. Auto-refreshing every 30s...")

def main():
    try:
        while True:
            data = fetch_crypto_data()
            if data:
                display_dashboard(data)
            else:
                print("Retrying connection in 30 seconds...")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nTracker stopped. Have a great day!")

if __name__ == "__main__":
    main()
