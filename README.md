# SDS-011-Python Repoisitory (Now with data ploting server)
Author: Danien Jarvis
Contacts: ee18dj@leeds.ac.uk or Jarvissan21@gmail.com

Python repository for the SDS011 on a RPI3. Functions for use with a GPS, DHT22 and Blinkt LED lights. 
**NEW** Data plotting web server in rpiWebServer, click into rpiWebServer folder for setup

[Set up Video](https://www.youtube.com/watch?v=fvaiyqwaWeM)

![SDS-011](https://github.com/JarvisSan22/SDS-011-Python/blob/master/SDS011-setup.jpg)


# Kit Links 
- [SDS011](https://www.amazon.co.uk/gp/product/B07D7BL33R/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B07D7BL33R&linkCode=as2&tag=jarvissan-21&linkId=40bb211f585f6fb48dd5feecb261bd3f)
- [RPI3](https://www.amazon.co.uk/gp/product/B01CI5879A/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B01CI5879A&linkCode=as2&tag=jarvissan-21&linkId=d64cc755f2dcf6ff27d37a7fc09b8ac5) 
- [GPS](https://www.amazon.co.uk/gp/product/B015E2XSSO/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B015E2XSSO&linkCode=as2&tag=jarvissan-21&linkId=8563986ebd9d60f3488a35d2cb5a34f4) 
- [DHT22](https://www.amazon.co.uk/gp/product/B072391SJV?ie=UTF8) 
- [BLINKT](https://www.amazon.co.uk/gp/product/B01J7Y332Q/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B01J7Y332Q&linkCode=as2&tag=jarvissan-21&linkId=dbda11585051ff253bc34c06913a4a40) 
- [Battery Pack](https://www.amazon.co.uk/gp/product/B07QTJDGJ1?ie=UTF8)


# Repository details 
1. **AQ** {Logging scipts, go into this folder for run details}
   - **Data** {Folder to store data files }
   - **Scripts** 
     - 2 **DHT** {DHT repository}
     - 2 **DHT.py** {DHT 11 and 22 script}
     - 2 **GPS2.py** {GPS scipts}
     - 2 **sds_rec.py** {SDS011 get data sripts}
     - 2 **start.py**  {Start recording and logg data script}
     - 2 **status.py** {RPI3 status scripts, checks if running, and updates time}
     - 2 **variables.py** {RPI3 and sensors varaible script}
1. **AQ-Plot** {Plotter scripts, go into this folder for details on how to run}
   - **AQDataplot.py** {Main plotter scripts}
   - **AQMapfunctions.py** {Map plotting functions}
   - **AQfunctions.py** {Data file reading functions}
   - **Genlivehtml.py** {HTML interfacte functions}


  


# RPI3 set up 
```
sudo apt-get update
sudo apt-get upgrade
```

**WIfi set up** 
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
add  your network network
```
network={
   ssid="{your interent name}"
   psk="{your internet password}"
}
```

**Download this repository**
```
git clone https://github.com/JarvisSan22/SDS-011-Python
```


# GPS Set up 
GPS Dongle G-mouse, set up video for setting up the dolge GPS as the RPI3 clock !!!
https://www.youtube.com/watch?v=Oag9qYuhMGg


1st get gps module
```
sudo apt-get install gpsd gpsd-clients python-gps chrony
```
2nd  in terminal 
```
sudo nano /etc/default/gpsd
```
set the following
``` 
START_DAEMON=”true”
USBAUTO=”true”
DEVICES=”/dev/ttyACM0″
GPSD_OPTIONS=”-n”
```
3rd  in the terminal 
```
sudo nano /etc/chrony/chrony.conf
```
Add the following line to the end of the file:

```
refclock SHM 0 offset 0.5 delay 0.2 refid NMEA
```
3rd Reboot the RPI3 ""sudo reboot""

4th  check that both are active in the terminal
```
systemctl is-active gpsd
systemctl is-active chronyd
su
```
5th see the data
```
gpsmon -n
```



# Team viewer from Terminal 
https://pimylifeup.com/raspberry-pi-teamviewer/
1st set up  in terminal 
```
sudo dpkg -i teamviewer-host_armhf.deb
```
if that gives errors ""sudo apt --fix-broken install""

2nd set password 
```
sudo teamviewer passwd  {Your password}
```


3rd get ID
```teamviewer info```
if  TeamViewer ID is blank ""



# Blinkt set up install

1st get the blinkt packages  
```
curl https://get.pimoroni.com/blinkt | bash
```
2nd fit the blinket into the RPI3 


![SDS-0112](https://github.com/JarvisSan22/SDS-011-Python/blob/master/SDSsetup.jpg)
