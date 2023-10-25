import os
from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'soundclassification-403103-e747d85c7c85.json'

def transcribe_audio(audio_file , sample_rate):
    client = speech.SpeechClient()

    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="en-US",
        audio_channel_count=1
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript

def get_text_google_api(audio_path):
  stereo_audio = AudioSegment.from_wav(audio_path)
  sample_rate = stereo_audio.frame_rate
  print(f"Sample rate of the audio file: {sample_rate} Hz")
  mono_audio = stereo_audio.set_channels(1)
  mono_audio.export('mono-audio.wav', format='wav')
  return transcribe_audio('mono-audio.wav',sample_rate)