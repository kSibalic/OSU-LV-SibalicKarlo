import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import pandas as pd
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

data = pd.read_csv('data_C02_emission.csv')

#a)
input_variables = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'Fuel Consumption Comb (mpg)']
output_variables = 'CO2 Emissions (g/km)'

X = data[input_variables]
y = data[output_variables]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#b)
plt.scatter(X_train['Engine Size (L)'], y_train, c='Blue', s=10)
plt.scatter(X_test['Engine Size (L)'], y_test, c='Red', s=10)
plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('CO2 emissions compared to engine size')
plt.show()

#c)
plt.hist(X_train['Engine Size (L)'])
plt.show()

sc = MinMaxScaler()
X_train_sc = sc.fit_transform(X_train)
plt.hist(X_train_sc[:, 0])
plt.show()

X_test_n = sc.transform(X_test)

#d)
linearModel = lm.LinearRegression()
linearModel.fit(X_train_sc, y_train)

print(linearModel.coef_)

#e)
y_test_pred = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_pred, s=10)
plt.title("Real values compared to predicted values")
plt.xlabel("Real values")
plt.ylabel("Predicted values")
plt.show()

#f)
MSE = mean_squared_error(y_test, y_test_pred)
RMSE = math.sqrt(MSE)
MAE = mean_absolute_error(y_test, y_test_pred)
MAPE = mean_absolute_percentage_error(y_test, y_test_pred)
R2_SCORE = r2_score(y_test, y_test_pred)

print(f"MSE: {round(MSE, 4)}, \nRMSE: {round(RMSE, 4)}, \nMAE: {round(MAE, 4)}, \nMAPE: {round(MAPE, 4)}, \nR2 SCORE: {round(R2_SCORE, 4)}")