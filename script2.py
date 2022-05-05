import pandas as pd
import matplotlib.pyplot as plt 
from alpha_vantage.timeseries import TimeSeries



## initializers 

# api_key = "Enter YOUR API KEY HERE"
# *** For Example, Something Like: *** 
# api_key = "ZZZZZZZZZZZZZZZZ" 
            
ts = TimeSeries(api_key, output_format = 'pandas')

file1 = open("nasdaq_screener.csv")   ### Name of Stock Symbols you want Pulled  

lines = file1.readlines()

lines.remove(lines[0])  ## Strip Header


calls = 0 


def get_stocks(list1):

    # Skeleton taken from Mop 

    x = 0
    y = len(list1)
    repo = []
    global calls 

    while x!= y:

        try:

            q = list1[x].split(" \n")
            data, meta = ts.get_monthly('{}'.format(q[0]))
            data.iloc[::-1].to_csv("{}.csv".format(q[0]))
    

        except ValueError:
            repo.append(q[0])
            pass

        x += 1 
        calls += 1 

    return repo



def mop_stocks( list1 ):

    return get_stocks(list1)



call1 = get_stocks(lines)

call2 = mop_stocks(call1)

bugFix = 0


while(len(call2) != 0 ):
    call2 = mop_stocks(call2)
	
  
    if (bugFix == 10):
        break
    print(bugFix)
    bugFix += 1 


    ## Add bug feature to catch running loops
    ## and empty calls 

print(call2, len(call2), "bugFix {}".format(bugFix), calls) 

