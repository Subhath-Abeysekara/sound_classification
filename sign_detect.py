import glob
import cv2 as cv
import numpy as np
import pandas as pd
import tensorflow as tf

model = tf.keras.models.load_model('sign_detector.h5')
model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=[
                tf.keras.metrics.CategoricalAccuracy(name='accuracy'),
                tf.keras.metrics.Precision(name='precision'),
                tf.keras.metrics.Recall(name='recall')
            ])

class_dict = {
            '1': 0,
            '3': 1,
            '4': 2,
            '5': 3,
            '7': 4,
            '8': 5,
            '9': 6,
            'A': 7,
            'B': 8,
            'Baby': 9,
            'Brother': 10,
            'C': 11,
            'D': 12,
            'Dont_like': 13,
            'E': 14,
            'F': 15,
            'Friend': 16,
            'G': 17,
            'H': 18,
            'Help': 19,
            'House': 20,
            'I': 21,
            'J': 22,
            'K': 23,
            'L': 24,
            'Like': 25,
            'Love': 26,
            'M': 27,
            'Make': 28,
            'More': 29,
            'N': 30,
            'Name': 31,
            'No': 32,
            'O_OR_0': 33,
            'P': 34,
            'Pay': 35,
            'Play': 36,
            'Q': 37,
            'R': 38,
            'S': 39,
            'Stop': 40,
            'T': 41,
            'U': 42,
            'V_OR_2': 43,
            'W_OR_6': 44,
            'With': 45,
            'X': 46,
            'Y': 47,
            'Yes': 48,
            'Z': 49,
            'nothing': 50
            }
class_dict_rev = {v: k for k, v in class_dict.items()}

def inference(
            image_path,
            target_size=(224, 224)
            ):
    image_path = image_path.replace('\\', '/')
    img = cv.imread(image_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, target_size)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.xception.preprocess_input(img)
    prediction = model.predict(img).squeeze()
    p = prediction.argmax()
    proba = prediction[p]
    proba = round(proba, 3)
    return class_dict_rev[int(p)], proba