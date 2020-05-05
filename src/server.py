from khaiii import KhaiiiApi
from flask import Flask, request, jsonify

api = KhaiiiApi()
app = Flask(__name__)


@app.route('/analyze/<text>', methods=['GET'])
def analyze(text):
    results = []
    for word in api.analyze(text):
        for morph in word.morphs:
            results.append([morph.lex, morph.tag])
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

