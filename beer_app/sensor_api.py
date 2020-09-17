import board
import adafruit_dht
from flask import Flask, jsonify

dht = adafruit_dht.DHT22(board.D4)

app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def hello():
    return "Hello Brewer!"

@app.route('/sensor_data/api/v1.0/current_data', methods=['GET'])
def current_data():
    import sys
    import time
    SENSOR_LOCATION_NAME = "Potter_Closet"
    DEVICE = "DHT22"
    while True:
        try: 
            humidity = dht.humidity
            temperature = dht.temperature
            
            BEER_DATA = {
                'device': DEVICE,
                'sensor_location': SENSOR_LOCATION_NAME,
                'tempurature': temperature,
                'unit': "Metric",
                'humidity': humidity
            }
            # print (BEER_DATA)
            if humidity is not None and temperature is not None:
                return jsonify(BEER_DATA)
            
        except RuntimeError as error:
            print(error.args[0])
        time.sleep(2.0)