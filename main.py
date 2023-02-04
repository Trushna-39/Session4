import pandas as pd
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv', usecols=["hospital_onset_covid_coverage", "critical_staffing_shortage_today_not_reported", "total_staffed_pediatric_icu_beds"])

# Get the statistics of hospital_onset_covid_coverage column
print("\nStatistics of 'hospital_onset_covid_coverage' column: ")
print("Minimum of hospital_onset_covid_coverage: ", df['hospital_onset_covid_coverage'].min())
print("Maximum of hospital_onset_covid_coverage: ", df['hospital_onset_covid_coverage'].max())
print("Mean of hospital_onset_covid_coverage: ", df['hospital_onset_covid_coverage'].mean())
print("Mode of hospital_onset_covid_coverage: ", df['hospital_onset_covid_coverage'].mode()[0])

# Get the statistics of hospital_onset_covid_coverage column
print("\nStatistics of 'critical_staffing_shortage_today_not_reported' column: ")
print("Minimum of critical_staffing_shortage_today_not_reported: ", df['critical_staffing_shortage_today_not_reported'].min())
print("Maximum of critical_staffing_shortage_today_not_reported: ", df['critical_staffing_shortage_today_not_reported'].max())
print("Mean of critical_staffing_shortage_today_not_reported: ", df['critical_staffing_shortage_today_not_reported'].mean())
print("Mode of critical_staffing_shortage_today_not_reported: ", df['critical_staffing_shortage_today_not_reported'].mode()[0])

# Get the statistics of hospital_onset_covid_coverage column
print("\nStatistics of 'total_staffed_pediatric_icu_beds' column: ")
print("Minimum of total_staffed_pediatric_icu_beds: ", df['total_staffed_pediatric_icu_beds'].min())
print("Maximum of total_staffed_pediatric_icu_beds: ", df['total_staffed_pediatric_icu_beds'].max())
print("Mean of total_staffed_pediatric_icu_beds: ", df['total_staffed_pediatric_icu_beds'].mean())
print("Mode of total_staffed_pediatric_icu_beds: ", df['total_staffed_pediatric_icu_beds'].mode()[0])

# Describe will give count, mean, min, max, std, data in (25%, 50% and 70%)
# print(df.describe())

# Get the histogram
hist = df.hist(bins = 10)

# Show the histogram
plt.show()
