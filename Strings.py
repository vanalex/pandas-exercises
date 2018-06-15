import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('./data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
print(weather_2012[:5])

weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

# Not super useful
print(is_snowing[:5])

temperature = weather_2012['Temp (C)'].resample('M', how=np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M', how=np.mean)

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"

stats = pd.concat([temperature, snowiness], axis=1)
stats.plot(kind='bar')
plt.show()





