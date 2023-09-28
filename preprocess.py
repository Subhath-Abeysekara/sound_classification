import tensorflow as tf
from PIL import Image
import numpy as np

# Load and preprocess an image for prediction
img_path = 'Adult_IMG_02.jpg'

# Load the image using PIL
img = Image.open(img_path)

# Resize the image to the desired target size (299x299 for Xception)
img = img.resize((299, 299))

# Convert the PIL image to a NumPy array
img_array = np.array(img)

# Expand dimensions to create a batch of size 1 (1 image)
img_array = np.expand_dims(img_array, axis=0)

# Preprocess the image for Xception model
img_array = img_array.astype('float32')  # Convert to float32
img_array = tf.keras.applications.xception.preprocess_input(img_array)
