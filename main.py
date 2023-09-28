import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

import pronouncation_accuracy
from classify_sound import classify_class

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")
def main():
    return "home"

@app.route("/v1/pronouncationaccuracy",methods=["POST"])
@cross_origin()
def pronouncation():
    return pronouncation_accuracy.get_pronouncation_accuracy(audio_file=request.json['audio'] , pronounce_word=request.json['element'])

@app.route("/v1/sounddetect",methods=["POST"])
@cross_origin()
def soundclasification():
    return classify_class(filename=request.json['audio'])

@app.route("/form_data", methods=["POST"])
@cross_origin()
def formdata():
    uploaded_file = request.files['image']
    body = request.form['name']
    print(body)
    print(json.loads(body))
    if uploaded_file:
        # Save the uploaded file to a directory or process it as needed
        # For example, to save it to a directory:
        uploaded_file.save('uploaded.png')

        return 'File uploaded successfully!', 200

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
