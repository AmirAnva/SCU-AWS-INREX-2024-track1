import os
from flask import Flask, jsonify,request
import mysql.connector
from mysql.connector import errorcode
from math import radians, sin, cos, sqrt, atan2
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    # connect mysql
    load_dotenv()
    db_config = {
        'host': os.getenv("host"),
        'user': os.getenv("user"),
        'password': os.getenv("password"),
        'database': os.getenv("database")
    }
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # sql query
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = [users for users in cursor]

    # close the connection
    cursor.close()
    cnx.cursor()
    return jsonify(users)

def compute_radius(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


@app.route('/find_users_within_radius', methods=['GET'])
def find_users_within_radius():
    try:
        # Get query parameters
        accident_lat = request.args.get('latitude', type=float)
        accident_lon = request.args.get('longitude', type=float)
        radius = request.args.get('radius', default=3, type=float)

        # Validate inputs
        if accident_lat is None or accident_lon is None:
            return jsonify({"error": "Latitude and longitude are required"}), 400

        load_dotenv()
        db_config = {
            'host': os.getenv("host"),
            'user': os.getenv("user"),
            'password': os.getenv("password"),
            'database': os.getenv("database")
        }

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

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

        cursor.close()
        connection.close()

        return nearby_users
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # app.debug = True
    app.run(host="0.0.0.0", port=3000, debug=True)

    # accident_latitude = -33.968100
    # accident_longitude = 18.582020
    # users_in_radius = find_users_within_radius(accident_latitude, accident_longitude, radius=3)
    # print("Users within 3 km radius:")
    # for user in users_in_radius:
    #     print(f"Username: {user['username']}, Email: {user['email']}")