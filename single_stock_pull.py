import pandas as pd
import matplotlib.pyplot as plt 
from alpha_vantage.timeseries import TimeSeries



## initializers 

#api_key = "ZZZZZZZZZZZZZZZZ"

ts = TimeSeries(api_key, output_format = 'pandas')

stock_symbol = 'AAPL'   ## Change to Desired Symbol 


def get_intra():

        data, meta = ts.get_intraday(stock_symbol, interval = '1min', outputsize= 'full')    ## Change for Intra, Weekly, etc. 
        data.iloc[::-1].to_csv("{}_intra.csv".format(stock_symbol))

def get_daily():

        data, meta = ts.get_daily(stock_symbol)  ## Change for Intra, Weekly, etc. 
        data.iloc[::-1].to_csv("{}_daily.csv".format(stock_symbol))

def get_monthly():
        data, meta = ts.get_monthly(stock_symbol)  ## Change for Intra, Weekly, etc. 
        data.iloc[::-1].to_csv("{}_monthly.csv".format(stock_symbol))


## Select Which Functions you want ## 

get_intra()
get_daily()
get_monthly()
print("done")

