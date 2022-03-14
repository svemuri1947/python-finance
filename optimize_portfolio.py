import yfinance as yf
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pickle

plt.style.use("dark_background")

stocks = ['AAPL', 'FB']
amounts = [20, 15]
stock_values = [si.get_live_price(stocks[i])  * amounts[i] for i in range(len(stocks))]
sectors = [yf.Ticker(x).get_info()['industry'] for x in stocks]
countries = [yf.Ticker(x).get_info()['country'] for x in stocks]
market_caps = [yf.Ticker(x).get_info()['marketCap'] for x in stocks]

# print(yf.Ticker('AAPL'.get_info))

cash = 50000
etfs = ['QQQ', 'SPY']
etf_amounts = [30, 20]
etf_values = [si.get_live_price(etfs[i]) * etf_amounts[i] for i in range(len(etfs))]

cryptos = ['ETH-USD', 'BTC-USD']
crypto_amounts = [0.89, 0.34]
crypto_values = [si.get_live_price(cryptos[i]) * crypto_amounts[i] for i in range(len(etfs))]

general_dist = {
    'Stocks': sum(stock_values),
    'ETFs': sum(etf_values),
    'Cryptos': sum(crypto_values),
    'Cash': cash
}

sector_dist = {}
for i in range(len(sectors)):
    if sectors[i] not in sector_dist.keys():
        sector_dist[sectors[i]] = 0
    sector_dist[sectors[i]] += stock_values[i]

country_dist = {}
for i in range(len(countries)):
    if countries[i] not in country_dist.keys():
        country_dist[countries[i]] = 0
    country_dist[countries[i]] += stock_values[i]
    
market_cap_dist = {'small': 0.0, 'mid': 0.0, 'large': 0.0, 'huge': 0.0}

for i in range(len(stocks)):
    if market_caps[i] < 10000000000:
        market_cap_dist['small'] += stock_values[i]
    elif market_caps[i] < 50000000000:
        market_cap_dist['mid'] += stock_values[i]
    elif market_caps[i] < 100000000000:
        market_cap_dist['large'] += stock_values[i]
    else:
        market_cap_dist['huge'] += stock_values[i]


with open('general.pickle', 'wb') as f:
    pickle.dump(general_dist, f)

with open('industry.pickle', 'wb') as f:
    pickle.dump(general_dist, f)

with open('country.pickle', 'wb') as f:
    pickle.dump(general_dist, f)

with open('market_cap.pickle', 'wb') as f:
    pickle.dump(general_dist, f)
    
    
fig, axs = plt.subplots(2, 2)

fig.suptitle("Portfolio Diversification Analysis", fontsize=18)

axs[0,0].pie(general_dist.values(), labels=general_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[0,0].set_title("General Distribution")
axs[0,1].pie(sector_dist.values(), labels=sector_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[0,1].set_title("Stocks by Industry")
axs[1,0].pie(country_dist.values(), labels=country_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[1,0].set_title("Stocks by Country")
axs[1,1].pie(market_cap_dist.values(), labels=market_cap_dist.keys(), autopct="%1.1f%%", pctdistance=0.8, colors=mcolors.TABLEAU_COLORS)
axs[1,1].set_title("Stocks by Market Cap")

plt.show()
