import time
import board
import adafruit_dht
from flask import Flask, jsonify

app = Flask(__name__)

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Potter_Closet"
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = False
dhtDevice = adafruit_dht.DHT22(board.D4)
temperature_data = 0
humidity_data = 0
metric = "Temperature(C)"

BEER_DATA = {
        'beer_location': SENSOR_LOCATION_NAME,
        'tempurature': temperature_data,
        'unit': metric,
        'humidity': humidity_data
    }
# ---------------------------------

@app.route('/beer_data/api/v1.0/data', methods=['GET'])

def get_data():
    print(jsonify(BEER_DATA))
    return jsonify(BEER_DATA)

if __name__ == '__main__':
    while True:
        try:
            temp_data = dhtDevice.temperature
            hum_data = dhtDevice.humidity
            if METRIC_UNITS:
                metric = "Temperature(C)"
            else:
                temperature_data = format(temp_data * 9.0 / 5.0 + 32.0, ".2f")
            humidity_data = format(hum_data,".2f")
        except RuntimeError as error:
            print(error.args[0])
    app.run()    