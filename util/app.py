import os
from flask import Flask, jsonify,request
import mysql.connector
from math import radians, sin, cos, sqrt, atan2
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

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

@app.route('/')
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


if __name__ == '__main__':
    # app.debug = True
    app.run(host="0.0.0.0", port=3000, debug=True)
