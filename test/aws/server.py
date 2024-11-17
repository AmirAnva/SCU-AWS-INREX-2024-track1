from flask import Flask, Response, request, jsonify, render_template_string
from flask_cors import CORS
from bedrock import Chat
import os
import mysql.connector
from math import radians, sin, cos, sqrt, atan2
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

def connect_db():
    db_config = {
        'host': os.getenv("host"),
        'user': os.getenv("user"),
        'password': os.getenv("password"),
        'database': os.getenv("database")
    }
    cnx = mysql.connector.connect(**db_config)
    return cnx

def compute_radius(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def send_notification_with_gmail(recipient_email):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "SELECT subject, body FROM email_messages"
    cursor.execute(query)
    email_messages = cursor.fetchall()
    subject = email_messages[0][0]
    body = email_messages[0][1]
    load_dotenv()
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")

    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server and start TLS (Transport Layer Security)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the server
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)

        # Disconnect from the server
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

@app.route('/select_all_users', methods=['GET'])
def select_all_users():
    # connect mysql
    load_dotenv()
    cnx = connect_db()
    cursor = cnx.cursor()

    # sql query
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = [users for users in cursor]

    # close the connection
    cursor.close()
    cnx.cursor()
    return jsonify(users)

@app.route('/find_users_within_radius', methods=['GET'])
def find_users_within_radius_and_send_notification():
    try:
        # Get query parameters
        accident_lat = request.args.get('latitude', type=float)
        accident_lon = request.args.get('longitude', type=float)
        radius = request.args.get('radius', default=3, type=float)

        # Validate inputs
        if accident_lat is None or accident_lon is None:
            return jsonify({"error": "Latitude and longitude are required"}), 400

        load_dotenv()
        cnx = connect_db()
        cursor = cnx.cursor(dictionary=True)

        # Fetch all users from the database
        query = "SELECT username, email, latitude, longitude FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        # Find users within the radius
        nearby_users = []
        for user in users:
            user_lat = float(user['latitude'])
            user_lon = float(user['longitude'])
            distance = compute_radius(float(accident_lat), float(accident_lon), user_lat, user_lon)
            if distance <= radius:
                nearby_users.append(user)
                send_notification_with_gmail(user['email'])

        cursor.close()
        cnx.close()

        return nearby_users
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
