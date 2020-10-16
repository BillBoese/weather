import pandas as pd
import matplotlib.pyplot as plt
import numpy as py
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)


# Read data from the filename concord_data.csv in data dictionary
# Control delimeters, rows, column names with read_csv
data = pd.read_csv("data/conc_1891_may_2020.csv", usecols=['DATE', 'TMAX', 'TMIN'], parse_dates =['DATE'])

# Preview first 5 lines of the file loaded
print(data.head())
print(data.tail())
print(len(data.index))
print(data.describe())
#print(data.head(1000).isnull().sum())
print(f"Max Temp Null Count: {data.TMAX.isnull().sum()}")
print(f"Min Temp Null Count: {data.TMIN.isnull().sum()}")
print(f"Date Null Count: {data.DATE.isnull().sum()}")
#print(data.head(50))

#Loop through every row, delete when either tmax or tmin is null
for w_tup in data.itertuples():
    if (py.isnan(w_tup.TMAX) or py.isnan(w_tup.TMIN)):
         data = data.drop([w_tup.Index], axis=0)


tminn_ = data['TMIN'].min()
tminx_ = data['TMIN'].max()
tmaxn_ = data['TMAX'].min()
tmaxx_ = data['TMAX'].max()

print(f"Coldest low temperature day: \n{data[data['TMIN'] == tminn_]}")
print(f"Coldest high temperature day: \n{data[data['TMAX'] == tmaxn_]}")
print(f"Warmest low temperature day: \n{data[data['TMIN'] == tminx_]}")
print(f"Warmest high temperature day: \n{data[data['TMAX'] == tmaxx_]}")
# slice
#print(data.iloc[2000 : 2010])
# All rows with a null are gone now
# create date and year and dateyear colums
data['MONTH'] = pd.DatetimeIndex(data['DATE']).month
data['YEAR'] = pd.DatetimeIndex(data['DATE']).year
data['PERIOD'] = data['MONTH'].astype(str) + '-' + data['YEAR'].astype(str)
#check for new columns
print(data.head())
print(data.tail())
print(len(data.index))
print(data.describe())

#get average May high temperature by year, get all the Mays then group by year and average
print(f"May 2020 Average High Temp:  {data['TMAX'][data['PERIOD'] == '5-2020'].mean()}")  # May 2020 average high
print(f"May 2020 Average Low Temp: {data['TMIN'][data['PERIOD'] == '5-2020'].mean()}")  # May 2020 average low
# for Mays month == 5
print(data[data['MONTH'] == 5].groupby('YEAR')[['TMAX']].mean())
x = data[data['MONTH'] == 5].groupby('YEAR')[['TMAX']].mean()
print(x.describe())
x.plot.bar(y = 'TMAX')
plt.ylim([70,90])
#plt.show()
y = data.groupby(['PERIOD', 'MONTH'], as_index = False)[['TMAX']].mean()  #average monthly high temperature
z = data.groupby('PERIOD')[['TMIN']].mean()  #average monthly low temperature
print(y['MONTH'])
print(y.columns)