import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (15, 5)

pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

df = pd.read_csv('./data/311-service-requests.csv')

# we select the first five rows to see how the file looks like
print(df[:5])

# To get the noise complaints, we need to find the rows where the Complain Type column is "Noise-Street/Sidewalk"

noise_complaints = df[df['Complaint Type'] == "Noise - Street/Sidewalk"]
print(noise_complaints)

# print only the first three rows
print(noise_complaints[:3])

print(df['Complaint Type'] == "Noise - Street/Sidewalk")

is_noise = df['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = df['Borough'] == "BROOKLYN"

# You can also combine more than one condition with the & operator like this:
print(df[is_noise & in_brooklyn][:5])

# Which borough has the most noise complaints?
noise_complaints = df[is_noise]
print(noise_complaints['Borough'].value_counts())

# But what if we wanted to divide by the total number of complaints,
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = df['Borough'].value_counts()
print(noise_complaint_counts / complaint_counts)

# plot
(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')
plt.show()




