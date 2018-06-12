import pandas as pd
import matplotlib.pyplot as plt

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

complaints = pd.read_csv('./data/311-service-requests.csv')

# show 3 first rows
print(complaints[:3])

# select column
print(complaints['Complaint Type'])

# we can combine to get the first 3 rows of a column
print(complaints['Complaint Type'][:5])


# and it doesn't matter which direction we do it in:
print(complaints[:5]['Complaint Type'])

# select only 2 columns
print(complaints[['Complaint Type', 'Borough']])

# select only 2 columsn and show the first 10 rows
print(complaints[['Complaint Type', 'Borough']][:10])

#What's the most common complaint type?
#This is a really easy question to answer! There's a .value_counts() method that we can use:

print(complaints['Complaint Type'].value_counts())

# If we just wanted the top 10 most common complaints, we can do this:
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])

complaint_counts[:10].plot(kind='bar')
plt.show()


