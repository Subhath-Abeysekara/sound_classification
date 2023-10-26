import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from convert_using_ffmpeg import convert_aud_ffmpeg
from sound_convert_wav import convert_audio_type , convert_wav_bit_type
import pronouncation_accuracy
from classify_sound import classify_class
# from sign_detect import inference
from sign_detect import inference
from summerization import get_summerized_paragraph

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")
def main():
    return "home"

@app.route("/v1/pronouncationaccuracy",methods=["POST"])
@cross_origin()
def pronouncation():
    uploaded_file = request.files['audio']
    if uploaded_file:
        uploaded_file.save('uploaded.wav')
    return pronouncation_accuracy.get_pronouncation_accuracy(audio_file='uploaded.wav' , pronounce_word=request.form['element'])

@app.route("/v1/sounddetect",methods=["POST"])
@cross_origin()
def soundclasification():
    uploaded_file = request.files['audio']
    if uploaded_file:
        uploaded_file.save('uploaded.amr')
        convert_aud_ffmpeg()
        # convert_audio_type()
        convert_wav_bit_type()
    return classify_class(filename='uploaded.wav')

@app.route('/v1/sign', methods=['POST'])
def sign():
    image_obj = request.files['image_path']
    sign_obj = request.form['sign']
    filename = image_obj.filename
    image_path = f'uploads/{filename}'
    image_obj.save(image_path)
    prediction, proba = inference(image_path)
    if prediction == sign_obj:
        matched = True
    else:
        matched = False
    return jsonify({
                    "PredSignType": f"{prediction}",
                    "TrueSignType": f"{sign_obj}",
                    "probability" : f"{proba}",
                    "matched": f"{matched}"
                    })

@app.route('/v1/summerize', methods=['POST'])
def summerize():
    paragraph = request.form['paragraph']
    return get_summerized_paragraph(paragraph)
@app.route("/form_data", methods=["POST"])
@cross_origin()
def formdata():
    uploaded_file = request.files['image']
    body = request.form['name']
    print(body)
    print(json.loads(body))
    if uploaded_file:
        uploaded_file.save('uploaded.png')
        return 'File uploaded successfully!', 200

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
