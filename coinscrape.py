import requests
import json
import pandas as pd
api_url= 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1496112218&timeEnd=1653878618'
r = requests.get(api_url)
data = []
for item in r.json()['data']['quotes']:
    close = item['quote']['close']
    volume =item['quote']['volume']
    date=item['quote']['timestamp']
    high=item['quote']['high']
    low=item['quote']['low']
    data.append([close,volume,date,high,low])


cols = ["close", "volume","date","high","low"]

df = pd.DataFrame(data, columns= cols)
print(df)
df.to_csv('info.csv',index = False)

