from flask import Flask, render_template, jsonify
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)
try:
    cnx = mysql.connector.connect(user='root', password='springboot', host='localhost', database='mytraffic')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

@app.route('/')
def index():
    # connect mysql
    cnx = mysql.connector.connect(user='root',password='springboot', database='mytraffic')
    cursor = cnx.cursor()

    # sql query
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = [users for users in cursor]

    # close the connection
    cursor.close()
    cnx.cursor()
    return jsonify(users)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3000, debug=True)