#from keras.models import load_model
import os
import numpy as np
import matplotlib.pyplot as plt
import keras

os.environ['TF_USE_LEGACY_KERAS'] = '1'

# model = keras.models.load_model('zadatak_1_model.keras')
model = load_model('zadatak_1_model.keras')

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

predictions = model.predict(x_test_s)
prediction_labels = np.argmax(predictions, axis=1)
wrong_labels = np.where(prediction_labels != y_test)[0]

for i in range(16):
    index = wrong_labels[i]
    plt.subplot(4, 4, i + 1)
    plt.imshow(x_test[index].reshape(28, 28))
    plt.title(f'Actual: {y_test[index]}, Predicted: {prediction_labels[index]}')
    plt.axis("off")

plt.show()
