import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

#a)
plt.figure()
data['CO2 Emissions (g/km)'].plot(kind="hist", bins=20)
plt.show()

#b)
data['Fuel Type'] = data['Fuel Type'].astype('category')
colors = {'Z': 'brown', 'X': 'red', 'E': 'blue', 'D': 'black'}

data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c=data["Fuel Type"].map(colors), s=50)
plt.show()

#c)
data.boxplot(column='CO2 Emissions (g/km)', by='Fuel Type')
plt.show()

#d)
groupedFuel = data.groupby('Fuel Type').size()
groupedFuel.plot(kind ='bar', xlabel='Fuel Type', ylabel='Number of vehicles', title='Amount of vehicles by fuel type')
plt.show()

#e)
grouperCylinders = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
grouperCylinders.plot(kind='bar', x=grouperCylinders.index, y=grouperCylinders.values, xlabel='Cylinders', ylabel='CO2 emissions (g/km)', title='CO2 emissions by number of cylinders')
plt.show()