import tensorflow as tf
import numpy as np
import statistics

from cash import type_list, my_classes
from sound_feature_extract import feature_extraction

def classify_class(filename):
    embeddings , model_id, inferred_class = feature_extraction(filename=filename)
    model = tf.keras.models.load_model('models/sound_classifier' + str(model_id) + '.h5')
    predictions = model.predict(embeddings)
    predicted_class = np.argmax(predictions, axis=-1)
    print(predicted_class)
    res = statistics.mode(predicted_class)
    count= 0
    for cls in predicted_class:
        if res == cls:
            count+=1
    print(count)
    class_obj = my_classes[type_list.index(inferred_class)]
    print(class_obj)
    if count>3:
        class_ = list(class_obj.keys())[list(class_obj.values()).index(res)]
    else:
        class_ = "Can not predict this sound"
    print(class_)
    print(type_list.index(inferred_class))
    print(my_classes[type_list.index(inferred_class)])
    return {
        "prediction" : class_
    }

# print(classify_class('1-115920-B-22.wav'))