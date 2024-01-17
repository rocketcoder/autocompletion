from flask import Flask, request, jsonify
from flask_cors import CORS;
from auto_complete import (complete)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5173"}})
@app.route('/', methods=['POST', 'OPTIONS'])
def hello_world():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        response = jsonify()
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    r = request.get_json()
    autocompletion = complete(r['msg'])
    return autocompletion

if __name__ == '__main__':
    app.run()
