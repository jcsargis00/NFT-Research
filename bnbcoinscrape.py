import requests
import json
import pandas as pd
import plotly.express as px
api_url= 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5&convertId=2781&timeStart=1643514218&timeEnd=1653878618'
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
df.to_csv('bnb.csv',index = False)
fig=px.line(df, x='date',y="close")
fig.show()

