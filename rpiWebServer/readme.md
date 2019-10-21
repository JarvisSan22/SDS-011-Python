# rpiwebserver 
rpiwebserver for live viewing of reading, and ploy of todays data. Currently work for SDS011 with DHT22, and take the mean of multible sensors if opration.


## set up
1st install flask and the other needed package psutil (used to check the SDS011 log script is running) 

```
 pip install flask
 pip install psutil 
```

2nd RUN interface.py 

```
sudo python SDS-011-Python-master/AQ/rpiWebServer/interface.py
```
If you have not changed any folder names it should all work fine and come up wtih the following
```
* Serving Flask app "interface" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 254-904-053
```

3rd Check the server

Put your RPI3 ip address in a webbrowser



![RpiWeb](https://github.com/JarvisSan22/SDS-011-Python/blob/master/Screenshot_20191020-170102_Chrome.jpg)

If you dont now your RPI3 ip address, use an ip scanner or type the following in the terminal
```
ifconfig
```
It should in next to inet in the wlan0 settings.


