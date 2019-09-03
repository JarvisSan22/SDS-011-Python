#!/usr/bin/env python
#imports 
from __future__ import print_function
import threading as th
import multiprocessing as mp
import serial
import time
import struct
import datetime
import sys
import os.path
import variables as V

if V.DHTON=="ON":
    from DHT import DHT
MODE=V.MODE
if MODE=="GPS":
    from GPS2 import Work #IF GPS is on import module
    
if V.BLINKT=="ON":
    from blinkt import set_pixel, set_brightness, show, clear
    
    
    
from sds_rec import SDS011 as sds


  
#Gloabl varaibles
FOLDER=V.FOLDER #Folder location for data save
LOCATION=V.LOC[0] #RPI3 operation location
lat=V.LOC[1]#location latatuide
lon=V.LOC[2]#location longatuide
RPI=V.RPINAME
def initFile(date,RPI,FOLDER,LOCATION,SENSORS):
    #create columes depending on sensors and OPRATION
    columns="time"
    NAMES=""
    if MODE =="GPS":
        LOCATION=LOCATION+"_GPS"
        columns=columns+",lat,lon,alt"
    if V.DHTON=="ON":
        for sen in V.DHTNAMES:
            columns=columns+",DHT-RH,DHT-T"
    if V.OPCON=="ON":
        for sen in SENSORS:
            #check which sensors are running to add to the csv filre name (If multiple add the togher in order data is made)
            if NAMES=="":
                NAMES=NAMES+sen
            else:
                NAMES=NAMES+","+str(sen)#solution to odd error, when python does not think str are str
            #loop through sensors to create columns 
            if "SDS" in sen or "sds" in sen:
                columns=columns+",sds-pm2.5,sds-pm10,sds-TSP"
     #create the csv
    csvnames=NAMES.replace(",","-") #replace the commers from the Sensors names to add tio file name
    ofile= FOLDER + LOCATION +"_"+ RPI+'_' +csvnames+"_"+ str(date).replace('-','') + ".csv"
#    print("Opening Output File:")
    if(not os.path.isfile(ofile)):
        print("creat new file ",ofile)
        f=open(ofile,'w+')#open file 
        #First add time period
        ts = time.time()
        tnow = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') 
        print("Time Period,start:,"+tnow+",end:,",file=f)
        #Add sensors information
        print("Sensors:,"+NAMES,file=f)
        #Add locations
        print("Location:,"+LOCATION+",Lat-Lon,"+lat+","+lon,file=f)
        #Add interval time
        print("Interval time,"+str(V.integration),file=f)
        #Add data columns 
        print(columns,file=f)
        
    else:
        f=open(ofile,'a')
        #if already created append to file     
    return f


if __name__ == "__main__":
    #run sensors
    runsen=V.RUNSEN
    if V.DHTON=="ON":
        for DHTN in V.DHTNAMES:
            runsen.append(DHTN)
    print(V.RPINAME, " Starting in Mode: ",V.MODE, "Sensors:", V.RUNSEN," Time: ", datetime.datetime.now(),"Location:",V.LOC[0])
    inter=V.integration#Interval time between readings 
   
    P=V.RUNPORT
    R=V.RUNSEN
    #Array for operational sensors class calls
    opsen=[]
    for r in R:
        if "SDS" in r:
            opsen.append(sds)
    
    #get the processes to run
    print("Starting AQ RPI, Mode:", V.MODE)
    print("**************************************************")
    if V.BLINKT=="ON":
	print("********************************")
	print("BLINKT ON")
    print("integration time (seconds)",inter)
    print("**************************************************")
    #processes=[mp.Process(target=c,args=(p,r)) for c,p ,r in zip(opsen,P,R)]
    
    #run all the processes
    if V.OPCON=="ON":
        Sen=[]
        for sen, p, r in zip(opsen,P,R):
            Start=sen(p,r) #initiate the sensors
            Sen.append(Start)
            print(r," Ready")
        print(len(Sen))
    time.sleep(4)
    points=0 #data point longer 
  
    starttime = datetime.datetime.now()
    while time.time() % inter != 0:
        pass
    
        print("Looping")
        while True:
            #set stars
            datestart = datetime.date.today()
            
            #Create file if not alrady created
            if MODE=="GPS" or MODE=="TEST": #if GPS  or a TEST add the time in mins to the file name
                f=initFile(starttime.strftime('%Y%m%d-%H%M%S'),RPI,FOLDER,LOCATION,R)
            else:  #file name just with date
                f = initFile(datestart,RPI,FOLDER,LOCATION,R)
            ts = time.time()
            tnow = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')   
            data=tnow  

            if MODE=="GPS":  #IF GPS is attahced and turned on, get GPS data
              lat,lon,alt= Work()
              print("Lat:",lat,"Lon",lon)
              data=data+","+str(lat)+","+str(lon)+","+str(alt)
            if V.DHTON=="ON": #Get DHT data, for all DHT attached
                for DH, PIN in zip(V.DHTNAMES,V.DHTPINS):
                    HT=DHT()
                    RH, T= HT.getData(DH,PIN)
                    data=data+","+str(RH)+","+str(T)
            #run through each sensors reading there data
            if V.OPCON=="ON":
                for pro, r,p in zip(Sen,R,P): #loop through OPC
                    newdata=pro.getData(p,r)
                    data=data+","+newdata
                    if V.BLINKT=="ON":
			clear()
			show()
			set_pixel(0,10,10,10)
			set_pixel(1,10,10,10)
			time.sleep(1)
			show()
                        PM=float(newdata.split(",")[0])
                        COLOR=0
                        COLRVAL={0:[0,100,0],1:[0,100,50],2:[100,50,0],3:[100]}
                        for Limit in V.PMVALUE:
                            if PM>Limit:
                                COLOR=COLOR+1
                        clear()
                        set_pixel(0,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
                        set_pixel(1,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(2,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(3,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(4,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(5,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(6,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			set_pixel(7,COLRVAL[COLOR][0],COLRVAL[COLOR][1],COLRVAL[COLOR][2])
			show()     
			
		                     
                            
                       
                        
                    
                    #printe all data  and write it to the file
                    
            print(data,file=f)
            points=points+1#add a point to point arraw
            #prase to csv
            f.flush()
            if (datetime.date.today() - datestart).days > 0:
                #add end info 
                #too do add write point and end time to top data
                
                f.close()
                datestart = datetime.date.today()
                f = initFile(datestart,RPI,FOLDER,LOCATION,R)

            secondsToRun = (datetime.datetime.now()-starttime).total_seconds() % inter
            time.sleep(inter-secondsToRun)

        
        
        
