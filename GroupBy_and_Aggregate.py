import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

bikes_df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
print(bikes_df['Berri 1'].plot())
plt.show()

berri_bikes = bikes_df[['Berri 1']].copy()
print(berri_bikes[:5])

berri_bikes.index

print(berri_bikes.index.day)
print(berri_bikes.index.weekday)

berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print(weekday_counts)

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)

weekday_counts.plot(kind='bar')
plt.show()