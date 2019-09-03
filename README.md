# SDS-011-Python-
Python repository for the SDS011 on a RPI3, with function to use a GPS and DHT temp/Humid sensors. 






# RPI3 set up 

sudo apt-get update
sudo apt-get upgrade



""WIfi set up"" 

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

add network





# GPS Set up 
GPS Dongle G-mouse, set up video for setting up the dolge GPS as the RPI3 clock !!!
https://www.youtube.com/watch?v=Oag9qYuhMGg
Buy link:

1st get gps module
sudo apt-get install gpsd gpsd-clients python-gps chrony
2nd  in ""sudo nano /etc/default/gpsd"" set the following
 
START_DAEMON=”true”
USBAUTO=”true”
DEVICES=”/dev/ttyACM0″
GPSD_OPTIONS=”-n”

3rd ""sudo nano /etc/chrony/chrony.conf"" Add the following line to the end of the file:
refclock SHM 0 offset 0.5 delay 0.2 refid NMEA

3rd Reboot the RPI3 ""sudo reboot""

4th  check that both are active

systemctl is-active gpsd
systemctl is-active chronyd
su

5th see the data

gpsmon -n




# Team viewer from Terminal 
https://pimylifeup.com/raspberry-pi-teamviewer/
1st  ""sudo dpkg -i teamviewer-host_armhf.deb""

if that gives errors ""sudo apt --fix-broken install""

2nd set password ""sudo teamviewer passwd  {Your password}""


3rd "teamviewer info", if  TeamViewer ID is blank ""



# Blinkt set up install
Buy link: https://shop.pimoroni.com/products/blinkt
1st get the blinkt packages  
curl https://get.pimoroni.com/blinkt | bash

2nd fit the blinket o

