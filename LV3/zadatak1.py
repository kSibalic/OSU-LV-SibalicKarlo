import pandas as pd
import numpy as np

data = pd.read_csv('data_C02_emission.csv')

#a)
length = len(data['Make'])

print(f'DataFrame ima {length} mjerenja')

for col in data.columns:
    print(f'{col} ima tip: {data[col].dtype}')

data['Vehicle Class'] = data['Vehicle Class'].astype('category')

print(f'Redovi s izostalim vrijednostima: {data.isnull().sum()}')
print(f'Duplicirane vrijednosti: {data.duplicated().sum()}')

#b)
leastConsuming = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
mostConsuming = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print('Most consuming: ')
print(mostConsuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print('Least consuming: ')
print(leastConsuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

#c)
selectedData = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
length = len(selectedData['Make'])
avgC02 = selectedData['CO2 Emissions (g/km)'].mean()

print(f'Postoji {length} vozila koji imaju zapremninu motora između 2.5 i 3.5 litara')
print(f'Prosjecna CO2 emisija odabranih vozila je: {avgC02} g/km')

#d)
selectedData = data[(data['Make'] == 'Audi')]
length = len(selectedData['Make'])

print(f'U mjerenjima ima {length} vozila marke Audi')

selectedData = selectedData[(selectedData['Cylinders'] == 4)]
avgC02 = selectedData['CO2 Emissions (g/km)'].mean()

print(f'Prosjecna C02 emisija automobila s 4 cilindra marke Audi je {avgC02} g/km')

#e)
selectedByCylinders = data['Cylinders'].value_counts().sort_index()

print(f'Cylinders count: {selectedByCylinders}')

emmisionsPerCyliders = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()

print(f'Cylinder emissions {emmisionsPerCyliders}')

#f)
selectedDiesel = data[(data['Fuel Type'] == 'D')]
selectedPetrol = data[(data['Fuel Type'] == 'Z')]

print(f'\nDizeli: \nProsječna gradska potrošnja: {selectedDiesel['Fuel Consumption City (L/100km)'].mean()} \nMedijalno: {selectedDiesel['Fuel Consumption City (L/100km)'].median()}')
print(f'Benzinci: \nProsječna gradska potrošnja: {selectedPetrol['Fuel Consumption City (L/100km)'].mean()} \nMedijalno: {selectedPetrol['Fuel Consumption City (L/100km)'].median()}')

#g)
mostConsumingDiesel = selectedDiesel[(selectedDiesel['Cylinders'] == 4)].nlargest(1, 'Fuel Consumption City (L/100km)')

print(f'Vozilo s najvećom gradskom potrošnjom i 4 cilindra koje koristi dizelski motor je: {mostConsumingDiesel}')

#h)
selectedManuals = data[(data['Transmission'].str[0] == 'M')]
length = len(selectedManuals['Make'])

print(f'Postoji {length} vozila s ručnim mjenjačem')

#i)
print(data.corr(numeric_only=True))

'''
KOMENTAR:
Veličine imaju dosta veliki koeficijent korelacije. Gdje je npr. koeficijent veličine zapremnine motora i broj cilindara cca. 0.9. Također vrijedi i za broj cilindara i potrošnju gdje automobili s većim brojem cilindara imaju veću potrošnju.
To nam govori da bismo mogli moći predvidjeti podatke te da možemo očekivati proporcionalan rast/pad (ako je koeficijent korelacije pozitivan) pri promjeni neke od vrijednosti, odnosno obrnuto proporcionalan (ako je koeficijent korelacije negativan).
'''