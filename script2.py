import pandas as pd
from alpha_vantage.timeseries import TimeSeries



## initializers 

# api_key = "ZZZZZZZZZZZZZZZZ" 

api_key = "GH5RZKE5CLNDYG61"
          
ts = TimeSeries(api_key, output_format = 'pandas')

file1 = open("constituents_csv.csv")   ### Name of Stock Symbols you want Pulled  

lines = file1.readlines()

lines.remove(lines[0])  ## Takes away the first row of of the first column, in case there is a column title


calls = 0 


def get_stocks(list1):

    # Skeleton taken from Mop 

    x = 0
    y = len(list1)
    repo = []
    global calls 

    while x!= y:

        try:
            ## This may have to be changed depending on how the string needs to be split.
            ## A good way to check is to print(lines) and see how the string is arranged
            ## You might have to try list1[x].split("\n") or list1[x].split(" \n") 
            q = list1[x].split("\n")  
            data, meta = ts.get_monthly('{}'.format(q[0]))
            data.iloc[::-1].to_csv("{}.csv".format(q[0]))
    
            ''' Other Data Calls:

             data, meta = ts.get_intraday(i, interval='1min', outputsize = 'full')
             data, meta = ts.get_intraday(i, interval ='15min', outputsize = 'full') 
             data, meta = ts.get_intraday(i, interval ='30min', outputsize = 'full') 
             data, meta = ts.get_intraday(i, interval = '60min', outputsize = 'full') 
             data.iloc[::-1].to_csv("{}_{}.csv".format(i,"Daily"))
             data.iloc[::-1].to_csv("{}_{}.csv".format(i,"Monthly")) ''' 

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

