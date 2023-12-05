from flask import Flask, request, jsonify, render_template
import whisper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files['audio']
    audio_path = './' + audio_file.filename
    audio_file.save(audio_path)

    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return jsonify({"transcription": result['text']})

if __name__ == '__main__':
    app.run(debug=True)