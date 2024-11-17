from flask import Flask, Response, request, jsonify, render_template_string
from flask_cors import CORS
from bedrock import Chat
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/<id>") #count is how many images we want, starting from ID=1 to ID=count
def output(id):
    return Chat(id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
