#!/usr//bin/python

import sys
import datetime
import Adafruit_DHT


# Parse command line parameters.
              
sensor = Adafruit_DHT.DHT11
pin = 4
currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    print('{0} {1}'.format(temperature, humidity))
    f = open('/etc/weather/log/logtest','a')
    f.write('{0}\t{1}\t{2}\n'.format(currentTime, temperature, humidity))
    f.close()
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
