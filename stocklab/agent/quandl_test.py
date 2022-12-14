import quandl

quandl.ApiConfig.api_key = 'Vxa8Sxwc5mQoutX1ucas'
data = quandl.get('BITFINEX/LUNAF0USTF0', start_date='2022-05-22', end_date='2022-05-22')

print(data)