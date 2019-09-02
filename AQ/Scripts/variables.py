# -*- coding: utf-8 -*-
"""
Created on 31/08/2019
@author: Daniel Jarvis
Variables for the sensors operation
"""
#All the needed varaibles
#RPI3 Name
RPINAME="AQRPI8"
#Desired operation mode

#folder locations 
FOLDER = '/home/pi/SDS-011-Python/AQ/Data/' #for raw data
FOLDERCODE='/home/pi/SDS-011-Python/AQ/Scripts/' #For the scpirs locaton 
#Operation location, if using with GPS use area name, add inital lat and lon
#Makse sure there are no spaces in Location name or / or ,  for this goes into ther file name
LOC=['Location','Lat','lon'] #Add test name into this too, say aersol and calbration ...

#Data record period(in seconds)
integration=10

#Check internet connect, URL to ping
URL = 'https://github.com/JarvisSan22/SDS-011-Python'

#LoG: logs data, new file every day #GPS add lat, long, alt to data if GPS is added #TEST create a new data file ever time scrip is run (GPS does the same as well)
MODE= "LOG"   #"GPS"  

#Note if GPS is on it takes up "/dev/ttyACM0" port
##Desired sensors to run on RPI3
OPCON="ON"
RUNSEN=["SDS011_1"]  #add your SDS011 name, if you have more then 1 sds attaced, add the other name to the array  i.e RUNSEN=["SDS011_1,SDS011_2"]

#Sensor ports for deried sensors, if you dont know check the /dev folder
RUNPORT=["/dev/ttyUSB0"] #for more SDS011 add a "/dev/ttyUSB#" #=number to this array

#Temp sensors port number, if a DHT11 or 22 is running get the por  
DHTON="OFF"
DHTNAMES=["DHT22_1"]
DHTPINS=[14] #check the pin

#Light settings 
LIGHT="OFF" #LEDS option,  
BLINKET="ON"  #BLINkt hat option (Cant fit DHT22 with the BLINKET Hat)
PMVALUE=[10,20,30]  #Set intevals for light colors 



