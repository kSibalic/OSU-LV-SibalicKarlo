import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

model = keras.models.load_model('FCN/zad_model.h5')
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

y_pred = model.predict(x_test_s)
pred_labels = np.argmax(y_pred, axis=1)
wrong_labels = np.where(pred_labels != y_test)[0]

for i in range(3):
    plt.figure()
    index = wrong_labels[i]
    plt.imshow(x_test[index].reshape(28, 28), cmap='gray')
    plt.title(f'Real Label: {y_test[index]}, Predicted Label: {pred_labels[index]}')
plt.show()
