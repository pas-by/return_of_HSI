#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  returnOfHsi.py
#  to compute the return rate of HSI of past 10 years

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf;

def first_day_of_year(offset=0, d=np.datetime64('today')):
    dt = '{}-01-01'.format(str(d.astype(object).year + offset))
    dt = np.datetime64(dt)

    #  turn it into string
    dt = np.datetime_as_string(dt, unit='D')
    return dt

# timestamp right now 
today = np.datetime64('now')

yearList = []
retList = []

thisYear = today.astype(object).year
for index in range(-10, 0):
    yearList.append(thisYear + index)

#  程罪員的測試碼
#  print(yearList)

yearArr = np.array(yearList)

#  程罪員的測試碼
#  print(yearArr)
#  print(yearArr.dtype)

retList = []

stock = yf.Ticker("%5EHSI")

for index in range(-10, 0):
    #  程罪員的測試碼
    #  print(first_day_of_year(index))
    #  print(first_day_of_year(index+1))

    hist = stock.history(start=first_day_of_year(index), end=first_day_of_year(index+1), interval="1d")

    #  程罪員的測試碼
    #  print(hist.columns)
    #  print(hist.index.max())
    #  x = hist.index.array
    #  print(x.size)

    print(hist.iloc[0]['Open'], end=', ')
    print(hist.iloc[hist.index.array.size-1]['Close'])
    
    #  open value at the begin of year
    x = hist.iloc[0]['Open']
    #  closing value at the end of year
    y = hist.iloc[hist.index.array.size-1]['Close']

    retList.append(y/x)

    #  程罪員的測試碼
    print(hist)

retArr = np.array(retList)

#  to create a new dataframe
d = {'year':yearArr, 'return(%)':np.log(retArr) * 100}
df = pd.DataFrame(data=d)

#  程罪員的測試碼
print(df)

plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['return(%)'], '-k', label='return of HSI')
plt.legend()
plt.xlabel('Year')
plt.ylabel('%')
plt.grid(True)
plt.show()
