# Demo since AlphaAdvantage only offers 5 calls every 5 min, so I can't track more than 5 stocks
import requests
import pandas as pd

def run(stock):
    symbol = str(stock)
    response = requests.get(
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=TMVF4QR3NINC0TYF")
    response.raise_for_status()
    data = response.json()
    #print(data)
    symbol = data['Meta Data']['2. Symbol']
    value = data['Time Series (5min)']
    #print(value)
    new_value = list(value)[0]
    price = value[new_value]['1. open']

    print(symbol, round(float(price), 2))


df = pd.read_csv("stocks.csv")
for row in df.itertuples():
    run(row[1])
