import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((50, 50))
white = np.ones((50, 50))

upper = np.hstack((black, white))
lower = np.hstack((white, black))
image = np.vstack((upper, lower))

plt.imshow(image, cmap='gray')
plt.show()
