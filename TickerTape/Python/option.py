import yfinance as yf
import pandas as pd
from pandasql import sqldf, load_meat, load_births
pysqldf = lambda q: sqldf(q, globals())

expiration = '2020-06-18'
symbols = ['tsla','spy']
chains = pd.DataFrame()

for symbol in symbols:
    chain =  pd.DataFrame.from_records(yf.Ticker(symbol).option_chain(expiration)[0],columns=['contractSymbol','lastTradeDate','strike','lastPrice','bid','ask','change','percentChange','volume','openInterest','impliedVolatility','inTheMoney','contractSize','currency'])
    
    previous_close = yf.Ticker(symbol).info['previousClose']
    ask = yf.Ticker(symbol).info['ask']
    stock_percent_change = (((ask - previous_close) / ask) * 100)
    chain['stockask'] = ask
    chain['ticker'] = symbol
    chain['stockpercentchange'] = stock_percent_change

    chains = chains.append(chain)

chains['type'] = 'calls'
chains['expiration'] = expiration

print(chains)

#print (pysqldf("SELECT a.ticker, a.strike, a.ask, a.percentchange, a.stockask, a.stockpercentchange FROM chains a ORDER BY a.percentchange DESC;").head())





#print (pysqldf("SELECT a.ticker, a.strike, a.ask, a.percentchange, a.stockask, a.stockpercentchange FROM chain a ORDER BY a.percentchange DESC;").head())