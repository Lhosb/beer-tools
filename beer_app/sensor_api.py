import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
# app.debug = False # Make this False if you are no longer debugging

# build dict for json
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
def hello():
    return "Hello Brewer!"

@app.route('/sensor_data/api/v1.0/current_data', methods=['GET'])
def current_data():
    conn=sqlite3.connect('./sensordata.db')
    conn.row_factory = dict_factory
    curs=conn.cursor()
    curs.execute("SELECT * FROM dhtreadings ORDER BY id DESC LIMIT 1")
    data = curs.fetchone()
    while data is not None:
        print(data)
        return jsonify(data)
