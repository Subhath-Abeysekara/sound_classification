import os
import subprocess

def convert_aud_ffmpeg():
    ffmpeg_path = '/usr/bin/ffmpeg'  # The path to the ffmpeg binary
    input_file = 'uploaded.amr'
    output_file = 'uploaded.wav'
    if os.path.exists(output_file):
        os.remove(output_file)
    ffmpeg_command = f'{ffmpeg_path} -i {input_file} {output_file}'

    try:
        result = subprocess.run(ffmpeg_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}")
    else:
        print("FFmpeg command executed successfully")