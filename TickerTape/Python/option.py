import yfinance as yf
import pandas as pd
from pandasql import sqldf, load_meat, load_births
from get_all_tickers import get_tickers as gt
pysqldf = lambda q: sqldf(q, globals())

symbols = pd.DataFrame(gt.get_tickers_filtered(mktcap_min=500000))
expiration = '2020-06-18'
chains = pd.DataFrame()

symbols = symbols.append(['tsla','spy'])

for symbol in symbols[0]:

    chain =  pd.DataFrame.from_records(yf.Ticker(symbol).option_chain(expiration)[0],columns=['contractSymbol','lastTradeDate','strike','lastPrice','bid','ask','change','percentChange','volume','openInterest','impliedVolatility','inTheMoney','contractSize','currency'])
    
    previous_close = yf.Ticker(symbol).info['previousClose']
    ask = yf.Ticker(symbol).info['ask']
    stock_percent_change = (((ask - previous_close) / ask))
    chain['stockask'] = ask
    chain['ticker'] = symbol
    chain['stockpercentchange'] = stock_percent_change
    chain['breakevenprice'] = chain['strike'] + chain['ask']
    chain['breakevenpercent'] = (((chain['breakevenprice'] - chain['stockask'])/chain['breakevenprice']))

    chains = chains.append(chain)

chains['type'] = 'calls'
chains['expiration'] = expiration


print(chains)