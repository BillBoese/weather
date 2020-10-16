import pandas as pd
import matplotlib.pyplot as plt
import numpy as py


# Read  data from the filename concord_data.csv in data dictionary
# Control delimeters, rows, column names with read_csv
data = pd.read_csv("data/2155275.csv", usecols=['DATE', 'TMAX', 'TMIN'], parse_dates =['DATE'])

# Preview first 5 lines of the file loaded
print(data.head())
print(data.tail())
print(len(data.index))
print(data.describe())
x_, y_ = 0, 0
#print(data.head(1000).isnull().sum())
print(f"Max Temp Null Count: {data.TMAX.isnull().sum()}")
print(f"Min Temp Null Count: {data.TMIN.isnull().sum()}")
print(f"Date Null Count: {data.DATE.isnull().sum()}")
#print(data.head(50))

d_, tmax_, tmin, = 0, 0, 0
dat = {'bk': '', 'maxcnt': '', 'mincnt': '' }
df = pd.DataFrame(data=dat, index=range(1, 34))
# get length of df including nulls
l_ = len(data.index)
bks = l_/1000
bks_ = int(bks)+1
loc_count = 0
for b in range(1, bks_ +1): # for each bucket
    d_, tmax_, tmin_, = 0, 0, 0 # initialize counters for each group of 1000
    for i in range(1, 1001): # get next 1000
        try:
            if py.isnan(data.TMAX.iloc[loc_count]):
                tmax_ += 1
            if py.isnan(data.TMIN.iloc[loc_count]):
                tmin_ += 1
        except IndexError:
            print(f"Error at {loc_count}")
        if loc_count + 1 == l_: #if we have reached the end exit
            break
        else:
            loc_count += 1

    #store bucket number and tmax_count a better solution would just add rows
    df.bk.iloc[b-1] = b
    df.maxcnt.iloc[b-1] = tmax_
    df.mincnt.iloc[b-1] = tmin_
#print(df)
print(f"Calculated total max null count: {df.maxcnt.sum()}")

fig, ax = plt.subplots()

ax.bar(list(df.bk), list(df.maxcnt), alpha=0.5)
ax.bar(list(df.bk), list(df.mincnt), alpha=0.5)
#ax.hist(df.mincnt, bins=33, alpha=0.5, label='Null Min')
#plt.ylim(0, 10)
#ax.legend(loc='upper right')
plt.show()

tminn_ = data['TMIN'].min()
tminx_ = data['TMIN'].max()
tmaxn_ = data['TMAX'].min()
tmaxx_ = data['TMAX'].max()

print(f"Coldest low temperature day: \n{data[data['TMIN'] == tminn_]}")
print(f"Coldest high temperature day: \n{data[data['TMAX'] == tmaxn_]}")
print(f"Warmest low temperature day: \n{data[data['TMIN'] == tminx_]}")
print(f"Warmest high temperature day: \n{data[data['TMAX'] == tmaxx_]}")
# slice
print(data.iloc[2000 : 2010])
