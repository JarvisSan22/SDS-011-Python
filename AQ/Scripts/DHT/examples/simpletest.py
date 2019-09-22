#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
sys.path.insert(0, '/home/pi/AQ/OPCscripts/DHT')
import Adafruit_DHT






class DHT:
    def sen(self,sen)
        if "DHT22" in sen:      
            sensor = Adafruit_DHT.DHT22
            return sensor
        elif "DHT11" in sen:
            sensor = Adafruit_DHT.DHT11
            return sensor
    
    def initFile(date,FOLDER,LOCATION,NAME):
        ofile=   FOLDER + LOCATION + '_'+NAME+'_' + str(date).replace('-','') + ".csv"
        print("Opening Output File:")
        if(not os.path.isfile(ofile)):
                f=open(ofile,'w+')
                print("time,RH,temp",file=f)
        else:
                f=open(ofile,'a')
        return f
        
def __init__(self,inter,PIN,NAME):
    sensor=self.sen(NAME)
     # Example using a Raspberry Pi with DHT sensor
     # connected to GPIO23.
        #pin = 14
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        humidity="NaN"
        temperature="NaN"
    return humidity, temperature
