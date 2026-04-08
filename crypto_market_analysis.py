# crypto_market_analysis.py
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Pobranie danych z API Binance (ostatnie 30 cen BTC/USDT)
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response = requests.get(url)
data = response.json()

print("Aktualna cena BTC/USDT:", data["price"])

# 2. Pobranie historycznych danych świec (kluczowe: open, high, low, close)
# limit=30 oznacza 30 ostatnich minut (można zmienić na inne interwały)
history_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=30"
history_response = requests.get(history_url)
history_data = history_response.json()

# 3. Przetworzenie danych na DataFrame
df = pd.DataFrame(history_data, columns=[
    "Open time", "Open", "High", "Low", "Close", "Volume",
    "Close time", "Quote asset volume", "Number of trades",
    "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
])

# Zamiana na float
df["Open"] = df["Open"].astype(float)
df["High"] = df["High"].astype(float)
df["Low"] = df["Low"].astype(float)
df["Close"] = df["Close"].astype(float)

# 4. Podstawowa analiza
print("\nPodstawowe statystyki BTC/USDT (ostatnie 30 minut):")
print(df[["Open", "High", "Low", "Close"]].describe())

# 5. Wykres cen zamknięcia
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Close"], marker='o', linestyle='-')
plt.title("Cena zamknięcia BTC/USDT (ostatnie 30 minut)")
plt.xlabel("Minuta")
plt.ylabel("Cena (USDT)")
plt.grid(True)
plt.show()