
# tradingbot test

import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST('PKX5NF14H5F3MK32CV8G', 'phsts9CZc6BvDMpW5osKpqh93ZXFXmAyzzBiKOxS', alpaca_endpoint)

account = api.get_account()
print(account.status)
