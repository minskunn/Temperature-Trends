import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("city_temperature.csv")  

print(data.head())

#Overwrite original temperature to Celsius 

data['AvgTemperature'] = (data['AvgTemperature'] - 32) * 5/9

paris_data = data[data['City'] == 'Paris']

average_temperature_per_year = paris_data.groupby('Year')['AvgTemperature'].mean()

print(average_temperature_per_year)

# Plot the average temperature trend for Paris over the years
average_temperature_per_year.plot(kind='line')

plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')

plt.title('Temperature Trends in Paris Over Time')

plt.show()

