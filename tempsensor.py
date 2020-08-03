import time
import board
import adafruit_dht

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Beer_1"
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = False
dhtDevice = adafruit_dht.DHT22(board.D4)
# ---------------------------------

while True:
    try:
        temp_c = dhtDevice.temperature
        temp_f = temp_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        if METRIC_UNITS:
            print(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
        else:
            temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
            print(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
        humidity = format(humidity,".2f")
        print(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(60*MINUTES_BETWEEN_READS)