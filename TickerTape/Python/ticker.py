import pandas as pd
from get_all_tickers import get_tickers as gt

DataSet = pd.DataFrame(gt.get_tickers(NASDAQ=True));


print(DataSet.sort_values(0));