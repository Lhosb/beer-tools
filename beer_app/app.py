# Reads dht22 sensor and saves to database

import sqlite3
import sys
import board
import time
import adafruit_dht

# TODO: Add front end manipulation of name, sleep time, etc
SENSOR_LOCATION_NAME = "Potter_Closet"
DEVICE = "DHT22"
SLEEP_TIME = 60 * 10
dht = adafruit_dht.DHT22(board.D4)

def log_values(device, location, temp, hum):
    conn=sqlite3.connect('./sensordata.db')  
    curs=conn.cursor()
    curs.execute("""INSERT INTO dhtreadings(currentdate, currenttime, device, location, temperature, humidity) values(date('now'), time('now'),
         (?), (?), (?), (?))""", (device, location, temp, hum))
    conn.commit()
    conn.close()

while True:
    try: 
        humidity = dht.humidity
        temperature = dht.temperature
        
        if humidity is not None and temperature is not None:
            print("Humidity: " + str(humidity) +"%")
            print("Temp (C): " + str(temperature))
            log_values(DEVICE, SENSOR_LOCATION_NAME, temperature, humidity)
        else:
            log_values(DEVICE, SENSOR_LOCATION_NAME, -999, -999)
        
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(SLEEP_TIME)
