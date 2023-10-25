from pydub import AudioSegment
import soundfile as sf
import re
# Load the AMR audio file
def is_wav_file(file_path):
    print(file_path)
    return file_path.lower().endswith('.amr')

# def convert_audio_type(audio_file):
#     pattern = r"'(.*?)'"
#     match = re.search(pattern, audio_file)
#     filename = match.group(1)
#     print(filename)
#     if is_wav_file(filename):
#         amr_audio = AudioSegment.from_file(audio_file, format='amr')
#         amr_audio.export('uploaded.wav', format='wav')

def convert_audio_type():
    amr_audio = AudioSegment.from_file('C:/Users/DFT/Downloads/20231010_011200.amr', format='amr')
    amr_audio.export('uploaded2.wav', format='wav')
# Specify the input 32-bit WAV file paths
def convert_wav_bit_type():
    try:
        input_file_path = "uploaded.wav"  # Change this to the actual path

        # Specify the output 16-bit WAV file path
        output_file_path = "uploaded.wav"  # Change this to the desired output path

        # Read the 32-bit WAV file
        audio_data, sample_rate = sf.read(input_file_path)

        # Convert the audio data to 16-bit
        audio_data_16bit = (audio_data * 32767).astype('int16')

        # Write the 16-bit audio data to a new WAV file
        sf.write(output_file_path, audio_data_16bit, sample_rate)
    except:
        print("error converting")