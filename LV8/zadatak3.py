import numpy as np
from tensorflow import keras
from PIL import Image

model = keras.models.load_model('zadatak_1_model.keras')
#model = load_model('zadatak_1_model.keras')

def do_prediction(path):
    image = Image.open(path).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image)

    image_array = image_array.astype("float32") / 255
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)

    predicted_label = np.argmax(model.predict(image_array))
    print(f"Predicted: {predicted_label}")

    print()
    print(f"Testing...")
    print("===================================")
    do_prediction("tests/test.png")
