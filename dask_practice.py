

import warnings
import time
warnings.filterwarnings('ignore')

import dask as dd
from dask import dataframe as ddf

#============================== basic
start= time.perf_counter()

def inc(num:int)->int:
    time.sleep(1)
    return num+1

results=[]


for i in range(10):
    results.append(dd.delayed(inc)(1))

total = dd.delayed(sum)(results)

total.compute()
total.visualize()
end= time.perf_counter()

print(f'time taken is {round(end-start,5)}')



#============================== dataframes
df=ddf.read_csv('/Users/abdulrafay/PycharmProjects/cookiepedia_refined/Cookiepedia_scraped_data.csv')
print(df)
print(df.head(1))
print(df.tail(1))

result=df['Cookie Name'].unique().compute()
print(len(result))
df['Cookie Name'].unique().visualize(rankdir='LR')


