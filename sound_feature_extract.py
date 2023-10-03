import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd

from cash import type_list

yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1'
yamnet_model = hub.load(yamnet_model_handle)

def load_wav_16k_mono(filename):
    """ Load a WAV file, convert it to a float tensor, resample to 16 kHz single-channel audio. """
    file_contents = tf.io.read_file(filename)
    print(file_contents)
    wav, sample_rate = tf.audio.decode_wav(
          file_contents,
          desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    print(sample_rate)
    # wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    print(wav)
    return wav

def feature_extraction(filename):
    class_map_path = yamnet_model.class_map_path().numpy().decode('utf-8')
    class_names = list(pd.read_csv(class_map_path)['display_name'])
    testing_wav_data = load_wav_16k_mono(filename)
    print(testing_wav_data)
    scores, embeddings, spectrogram = yamnet_model(testing_wav_data)
    class_scores = tf.reduce_mean(scores, axis=0)
    top_class = tf.math.argmax(class_scores)
    inferred_class = class_names[top_class]
    types = type_list
    model_id = 0
    i = 0
    for type in types:
        if inferred_class in type:
            print(type)
            model_id = i
        i += 1
    print(model_id)
    print(inferred_class)
    return embeddings , model_id , inferred_class