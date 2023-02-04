import pandas as pd
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv', usecols=['critical_staffing_shortage_today_yes'])

# Get the statistics of data
print("Minimum of critical_staffing_shortage_today_yes: ", df['critical_staffing_shortage_today_yes'].min())
print("Maximum of critical_staffing_shortage_today_yes: ", df['critical_staffing_shortage_today_yes'].max()) # You need to check whether there are 191 hospitals actually
print("Mean of critical_staffing_shortage_today_yes: ", df['critical_staffing_shortage_today_yes'].mean()) # 10.27 cannot be number of hospitals but absolute of it can be the output
print("Mode of critical_staffing_shortage_today_yes: ", df['critical_staffing_shortage_today_yes'].mode()[0]) # Most of the time the value of this column is 0

# Describe will give count, mean, min, max, std, data in (25%, 50% and 70%)
print(df.describe())

# Get the histogram
hist = df.hist(bins = 10)

# Show the histogram
plt.show()

# df = pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv', nrows=5, usecols=['date', 'state'], parse_dates=['date'])
# pd.to_date()
# print(df.columns)
# print(df['date'])
# print(df['date'].dt.year)
# print(df['date'].dt.month)