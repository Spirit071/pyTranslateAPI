from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    content = data['content']
    language = data['language']

    try:
        translated = translator.translate(content, dest=language, autocorrect=True)
        return jsonify({'data': translated.text}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/')
def home():
    return 'Hi'

if __name__ == '__main__':
    app.run(port=8000)
