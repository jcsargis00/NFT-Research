def load_data(symbol, NLHR04LATEYL0K16):
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+symbol+'&market=USD&interval=1min&outputsize=compact&apikey='+API_KEY
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame.from_dict(data['Time Series Crypto (1min)']).T
    df = df.rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    df.index = pd.to_datetime(df.index)
    df =df.astype(float)
    df['date'] = df.index.date.astype(str)
    return df