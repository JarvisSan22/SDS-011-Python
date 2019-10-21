from flask import Flask, render_template
import datetime
import os
import pandas as pd
import glob
import codecs
# run SDS011 scripts


def runsen():
	os.system("sudo python /home/pi/SDS-011-Python-master/AQ/Scripts/start.py &")
	return "yes"


def dateparse(timestamp):  # read the data time properly
    time = pd.to_datetime(timestamp, yearfirst=True, dayfirst=False)
 #   print(time)
  #  time.strftime(time, '%Y-%m-%d %H:%M:%S')
    return time


def readrpi3data():
	DataFolder = "/home/pi/SDS-011-Python-master/AQ/Data/"
	today = datetime.datetime.now().strftime("%Y%m%d")
	todayfiles = []
	for file in glob.glob(DataFolder+'****.csv'):
		if today in file:
			todayfiles.append(file)

	data = pd.DataFrame()
	for file in todayfiles:
		print(file)

		dataloop = pd.read_csv(
		    file, header=4, error_bad_lines=False, engine='python')
		dataloop=dataloop.loc[:,"time":"sds-pm10"]
		data = pd.concat([data, dataloop], ignore_index=False, axis=0, sort=True)
        print(data.iloc[0]["sds-pm2.5"])
  	# pd.to_datetime(data.time,yearfirst=True, dayfirst=False)

        #data["time"] = dateparse(data["time"])
 	#data.set_index('time', inplace=True)
        print(data.head(2))
	print(data.iloc[0]["sds-pm2.5"])
	sensors = ["test"]

	return data, sensors


# flask get serverworking
app = Flask(__name__)
@app.route("/")
def start():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   on = runsen()
   data, sens = readrpi3data()
   templateData = {
      'title': 'SDS011 Data',
      'time': timeString,
      'pm2': data.iloc[~0]["sds-pm2.5"]
      }
   return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")  # get latest value
def newdata(deviceName, action):
	now = datetime.datetime.now()
 	timeString = now.strftime("%Y-%m-%d %H:%M")

	templateData = {
	'title': 'Sensors are running:?',
      'time': timeString,
      'pm2': "NAN"

	}

	if deviceName == "newdata":
		data, sens = readrpi3data()
		templateData = {
     		 'title': 'SDS011 Data',
      		'time': timeString,
   		   'pm2': data.iloc[~0]["sds-pm2.5"]
      		}
	elif deviceName == "kill":
	   	os.system("sudo pkill -f /home/pi/SDS-011-Python-master/AQ/Scripts/start.py ")
    		data,sens=readrpi3data()
      		templateData = {
      'title' : 'Sensors off',
      'time': timeString,
      'pm2':data.iloc[~0]["sds-pm2.5"]
                }
	elif deviceName== "reset":
		on=runsen()
                data,sens=readrpi3data()
                templateData = {
      'title' : 'Sensors running',
      'time': timeString,
      'pm2':data.iloc[~0]["sds-pm2.5"]
                }
        if action =="yes":
                return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
