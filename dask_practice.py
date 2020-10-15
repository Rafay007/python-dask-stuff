

import warnings
warnings.filterwarnings('ignore')

from dask import datasets
import dask.dataframe as dd
df = datasets.timeseries()
print(df.shape)
print(df.columns)
for i,j in df.iterrows():
    print(j)