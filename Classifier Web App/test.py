import ipytest
ipytest.autoconfig()

import numpy as np
import tensorflow as tf
from PIL import Image
import pytest

def test_preprocessing_images():
    # Load the test image
    test_image_path = "Test/lungaca1.jpeg"
    test_image = np.array(Image.open(test_image_path))
    test_image = tf.image.resize(test_image, (80, 80))
    test_image = tf.cast(test_image, tf.float32) / 255.0  # Normalize the image

    assert test_image.shape == (80, 80, 3)
    assert test_image.dtype == tf.float32

def test_model_prediction():
    # Load the pre-trained model
    model = tf.keras.models.load_model("Model/CNN_saved_model.h5")  # Load your model

    # Load the test image
    test_image_path = "Test/lungaca102.jpeg"
    test_image = np.array(Image.open(test_image_path))
    test_image = tf.image.resize(test_image, (80, 80))
    test_image = tf.cast(test_image, tf.float32) / 255.0  # Normalize the image

    # Predict the label
    prediction = model.predict(np.expand_dims(test_image, axis=0))
    class_names = ["Adenocarcinoma", "Benign_Tissue", "Squamous_Cell_Carcinoma"]

    # Check if the prediction is correct
    assert class_names[np.argmax(prediction)] == "Adenocarcinoma"

if __name__ == "__main__":
    ipytest.run('-vv')
