import requests
import matplotlib.pyplot as plt

api_key = open('api_key', 'r').read()

company = 'AAPL'
years = 10

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")

# for income stmt in the form of csv use the below url
#income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?datatype=csv&limit={years}&apikey={api_key}")

income_statement = income_statement.json()

# print(income_statement[0]['revenue'])
# print(income_statement[0]['grossProfit'])
# print(income_statement[0]['eps'])
# print(income_statement[0]['ebitda'])

revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

plt.plot(revenues, label='Revenue')
plt. plot(profits, label='Profit')
plt.legend(loc='Upper left')
plt.show()