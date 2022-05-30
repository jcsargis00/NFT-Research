from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time
cmc=requests.get('https://coinmarketcap.com/')
soup=BeautifulSoup(cmc.content, 'html.parser')
print(soup.prettify())
data=soup.find('script',id="__NEXT_DATA__",type="application/json")
coins ={}
# using data.contents[0] to remove script tags
coin_data=json.loads(data.content[0])
listing=coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
for i in listings:
    coins[str(i['id'])]=i['slug']
for i in coins:
    page=requests.get(f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=202001016end=20200630')
    soup=BeautifulSoup(page.conent,'html.parser')
    data=soup.find('script',id="__NEXT_DATA__",type="application/json")
    historical_data=json.loads(data.contents[0])
quotes=historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]['quotes']
info = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]
market_cap=[]
volume=[]
timestamp=[]
name=[]
symbol=[]
slug=[]
for j in quotes:
    market_cap.append(j['quote']['USD']['market_cap'])
    volume.append(j['quote']['USD']['volume'])
    timestamp.append(j['quote']['USD']['timestamp'])
    name.append(info['name'])
    symbol.append(info['symbol'])
    slug.append(coins[i])
    df = pd.DataFrame(columns=['marketcap','volume','timestamp','name','symbol','slug'])
    df['marketcap']=market_cap
    df['volume']=volume
    df['timestamp']=timestamp
    df['name']=name
    df['symbol']=symbol
    df['slug']=slug
    df.to_csv('criptoes.csv',index=False)
