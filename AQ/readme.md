
# AQ set up

**1. set varaibles**

```
nano SDS-011-Python-master/AQ/Scripts/varaibles.py
```

Update varailes for RPINAME, LOC (Locations), intergration (Record interval), MODE (Recorind mode : LOG, GPS, TEST), RUNSEN (Sensors names), RUNPORTS (Senors connected usb ports)
![Variables](https://github.com/JarvisSan22/SDS-011-Python/blob/master/varaibleExample.png)


- **MODES**
  - **LOG**   static site recording to csv, creates a new csv ever day 
  - **GPS**   added the lat, lon and altitude to csv allowing for mobile usage, create a new csv ever run
  - **TEST**  create a new csv for a test run,  then start logging
  
  
Addional varaibles for DHT22 if connected
Set DHTON to "ON" and add the connected pin number if 

```
DHTON="ON"
DHTNAMES=["DHT22_1"]
DHTPINS=[14] #check the pin
```
Addional varaibles for BLINKT if connected 

Set BLINKT="ON" and check the PMVALUE to set light color limits
```
BLINKT="ON"  #BLINkt hat option (Cant fit DHT22 with the BLINKET Hat)
PMVALUE=[10,20,30]  #Set intevals for light colors defult colors (Green,blue,organe red) +
```

**2. Time to run**


```
sudo python SDS-011-Python-master/AQ/Scripts/start.py

```
![Run](https://github.com/JarvisSan22/SDS-011-Python/blob/master/Runexample.png)

**3. Run on start up**

In terminal
```
sudo nano crontab -e
```
Add to the bottom
```
@reboot python /home/pi/SDS-011-Python-master/AQ/Scripts/start.py &
```
Save
Then in terminal, reboot to check it works
```
sudo reboot
```

Running from start up works well with the BLINKT as you can see its working from the colors 


**Multiple SDS011 set up example**

To set up Multiple SDS011 on one RPI3, multipe sensors names and ports need to be added to RUNSEN and RUNPORT arrays in varaibles.py

```
nano SDS-011-Python-master/AQ/Scripts/varaibles.py
```

![MulsenVariables](https://github.com/JarvisSan22/SDS-011-Python/blob/master/2SDS011Varibles.png)

Add the new SDS011 name, and the SDS011 port name (/dev/tttyUSB#N #N=0,1,2,3...)


![MulSDS011](https://github.com/JarvisSan22/SDS-011-Python/blob/master/2SDS011Example.jpg)
