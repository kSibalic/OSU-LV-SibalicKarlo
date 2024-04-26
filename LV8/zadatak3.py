import numpy as np
from tensorflow import keras
from PIL import Image

model = keras.models.load_model('FCN/zad_model.h5')

for i in range(10):
    image_path = f'tests/test_{i}.png'
    image = Image.open(image_path).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image)

    image_array = image_array.astype("float32") / 255
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    predicted_label = np.argmax(model.predict(image_array))

    print(f"Predicted label for {i}: {predicted_label}")