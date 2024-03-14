import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('road.jpg')
image = image.copy()

plt.figure()
plt.imshow(image, alpha=0.5)  # a) dio
plt.show()

width = len(image[0])
quarter = int(width / 4)  # b) dio
plt.imshow(image[:, 1 * quarter: 2 * quarter])
plt.show()

rotated = np.rot90(image, 3)  # c) dio
plt.imshow(rotated)
plt.show()

flippedV = np.flip(image, 0)  # d) dio
flippedH = np.flip(image, 1)
plt.imshow(flippedV)
plt.show()
plt.imshow(flippedH)
plt.show()
