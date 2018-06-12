import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)

# Read data from a csv file
bikes_df = pd.read_csv('./data/bikes.csv')

# Look at the first 3 rows
print(bikes_df[:3])

# the content of the file is not well formatted. We can do a bunch of actions to do it prettier
# 1. change column separator
# 2. Set the encoding to 'latin1'
# 3. Parse the dates in the dates column
# 4. Tell it that our dates have the day first instead of the month
# 5. Set the index to  be the date column

formatted_df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
print(formatted_df[:3])

# select a column
print(formatted_df['Berri 1'])

# select a column and plot
print(formatted_df['Berri 1'].plot())
plt.show()

formatted_df.plot(figsize=(15,10))
plt.show()

# we can do all the steps as follows
df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
df['Berri 1'].plot()
plt.show()




