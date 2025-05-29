import pandas as pd
a=[1,2,3,4,5,6]
s=pd.Series(a)
print(s)

from pandas import*
from numpy import *
data=array(['a','b','c'])
s=Series(data)
print(s)

data={'a':1, 'b':2, 'c':3}
s=Series(data, index=['b','c','d'])
print(s)

from pandas import *

print(s['c'])
S=Series(5, index=[1,2,3,4])
print(S)

data={"calories":[21,312,23,241],
      "duration":[1,20,1.5,15]
      }
df=pd.DataFrame(data)
print(df)

print(df.loc [[0,1]])
