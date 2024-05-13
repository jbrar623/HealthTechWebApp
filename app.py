# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_scd4x
from flask import Flask, jsonify

app = Flask(__name__)

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
scd4x = adafruit_scd4x.SCD4X(i2c)
print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")

@app.route('/api/sensor-data')
def sensor_data():
    while True:
        if scd4x.data_ready:
            co2 = scd4x.CO2
            temperature = scd4x.temperature
            humidity = scd4x.relative_humidity
            return jsonify({
                'co2': co2,
                'temperature': temperature,
                'humidity': humidity
            })
        time.sleep(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
