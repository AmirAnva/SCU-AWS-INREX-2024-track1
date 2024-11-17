from flask import Flask, Response, request, jsonify, render_template_string
from flask_cors import CORS
from bedrock import Chat
from PIL import Image
from io import BytesIO
import base64
from Token import get_token
from CamerasBox import get_cameras_in_a_box
from CameraImage import get_camera_image

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/<id>") #count is how many images we want, starting from ID=1 to ID=count
def output(id):
    return Chat(id)

# Example URL: localhost:3000/token
@app.route("/token")
def get_token_route():
    token = get_token()
    return jsonify({"token": token})


# Example URL: localhost:3000/cameras?token=TOKEN&corner1=LAT|LONG&corner2=LAT|LONG
@app.route("/cameras")
def get_cameras_route():
    token = request.args.get("token")
    corner1 = request.args.get("corner1")
    corner2 = request.args.get("corner2")
    if not token or not corner1 or not corner2:
        return jsonify({"error": "Token or geobox corners not found. Please provide."})
    cameras = get_cameras_in_a_box(token, corner1, corner2)
    return jsonify({"cameras": cameras})


# Example URL: localhost:3000/camera-image?camera_id=CAMERA_ID&token=TOKEN
@app.route("/camera-image")
def get_camera_image_route():
    camera_id = request.args.get("camera_id")
    token = request.args.get("token")
    if not camera_id or not token:
        return jsonify({"error": "Camera ID or token not found. Please provide."})
    image = get_camera_image(camera_id, token)
    return image

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)