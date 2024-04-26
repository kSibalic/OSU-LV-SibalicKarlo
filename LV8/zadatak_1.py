import numpy as np
from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

num_classes = 10
input_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.figure()
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_train[i])
    plt.xlabel(y_train[i])
plt.show()

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")

y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

# TODO: kreiraj model pomoću keras.Sequential(); prikaži njegovu strukturu
model = keras.Sequential()
model.add(layers.Input(shape=input_shape))
model.add(layers.Flatten())
model.add(layers.Dense(100, activation="relu"))
model.add(layers.Dense(50, activation="relu"))
model.add(layers.Dense(num_classes, activation="softmax"))

model.summary()

# TODO: definiraj karakteristike procesa učenja pomoću .compile()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# TODO: provedi učenje mreže
batch_size = 32
epochs = 10
history = model.fit(x_train_s, y_train_s, batch_size=batch_size, epochs=epochs, validation_split=0.1)

predictions = model.predict(x_test_s)

# TODO: Prikaži test accuracy i matricu zabune
score = model.evaluate(x_test_s, y_test_s, verbose=0)

disp = ConfusionMatrixDisplay(confusion_matrix(np.argmax(y_test_s, axis=1), np.argmax(predictions, axis=1)))
disp.plot()
plt.show()

# TODO: spremi model
model.save('FCN/zad_model.h5')
