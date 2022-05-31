from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

test = 'BTC'

cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol= test, market='USD')
data
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()