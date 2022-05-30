import json
import requests
from bs4 import BeautifulSoup


def fetch_coingecko_html():
    # make a request to the target website
    r = requests.get("https://www.coingecko.com")
    if r.status_code == 200:
        # if the request is successful return the HTML content
        return r.text
    else:
        # throw an exception if an error occurred
        raise Exception("an error occurred while fetching coingecko html")


def extract_crypto_info(html):
    # parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # find all the cryptocurrency elements
    coin_table = soup.find("div", {"class": "coin-table"})
    crypto_elements = coin_table.find_all("tr")[1:]

    # iterate through our cryptocurrency elements
    cryptos = []
    for crypto in crypto_elements:
        # extract the information needed using our observations
        cryptos.append({
            "name": crypto.find("td", {"class": "coin-name"})["data-sort"],
            "price": crypto.find("td", {"class": "td-price"}).text.strip(),
            "change_1h": crypto.find("td", {"class": "td-change1h"}).text.strip(),
            "change_24h": crypto.find("td", {"class": "td-change24h"}).text.strip(),
            "change_7d": crypto.find("td", {"class": "td-change7d"}).text.strip(),
            "volume": crypto.find("td", {"class": "td-liquidity_score"}).text.strip(),
            "market_cap": crypto.find("td", {"class": "td-market_cap"}).text.strip()
        })

    return cryptos


# fetch CoinGecko's HTML content
html = fetch_coingecko_html()

# extract our data from the HTML document
cryptos = extract_crypto_info(html)

# display the scraper results
for crypto in cryptos:
    print(crypto, "\n")

# save the results locally in JSON
with open("coingecko.json", "w") as f:
    f.write(json.dumps(cryptos, indent=2))