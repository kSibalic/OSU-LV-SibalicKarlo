import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=",", dtype="str")
data = data[1::]
data = np.array(data, np.float64)
print(f"Broj izmjerenih ljudi: {len(data)}")                    #a) dio
height, weight = data[:, 1], data[:, 2]
plt.scatter(height, weight)                                     #b) dio
plt.show()

mean = height.mean()
maxHeight = height.max()
minHeight = height.min()
height, weight = data[0::50, 1], data[0::50, 2]                 #c) dio
plt.scatter(height, weight)
plt.show()
print(f"MAX: {maxHeight}, MIN: {minHeight}, SRED: {mean}")      #d) dio

men = data[data[:, 0] == 1]                                     #e) dio
women = data[data[:, 0] == 0]
print(f"ZA MUŠKARCE:\n MAX: {men[:, 1].max()}, MIN: {men[:, 1].min()}, SRED: {men[:, 1].mean()}")
print(f"ZA ŽENE:\n MAX: {women[:, 1].max()}, MIN: {women[:, 1].min()}, SRED: {women[:, 1].mean()}")
