import datetime
import os
import pandas as pd
import glob
import codecs
import matplotlib.pylab as plt
import matplotlib.dates as mdates





def dataplotter(data):
  var="pm2.5"
  sen="SDS011"
  fig,ax=plt.subplots(1,1,figsize=(15,10))
   
  if "pm" in var.lower() and "sds" in sen.lower():
      ax.plot(data["sds-"+var])
  else:
      ax.plot(data[var])
  ax.grid()
  ax.set_xlim(data.index[0],data.index[~0])
  myFmt = mdates.DateFormatter('%H:%M \n %d/%m')
  ax.xaxis.set_major_formatter(myFmt)
  ax.legend()
  today = datetime.datetime.now().strftime("%Y%m%d")
  title=var+"_"+today
  ax.set_title(title)
  #create plot dic if not alread exist
#  if not os.path.exists("Plots/"):
 #     os.mkdir("Plots/")
  #    print("new plots dir created")
 # else:
  #    print("plots dir already exists")
  if var.lower=="pm2.5":  #HTML does not like "." in titles 
	title="pm25_"+today
  fig.savefig("Plots/"+title+".png",dpi=300,format='png')
  print(title+" plote created")
     
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
		    file, header=4, error_bad_lines=False, engine='python',index_col=False)
		dataloop=dataloop.loc[:,"time":"sds-pm10"]
   	        
		sensors=pd.read_csv(file,header=None, skiprows=1,nrows=1)
	    	#sen=[]
		#for col in sensors:
		#	sen.append(sensors[col].astype(str))
      		sensors=sensors.values.tolist()[0]
    		print(sensors[1:])
		data = pd.concat([data, dataloop], ignore_index=False, axis=0, sort=True)
 #       print(data.index)
	#print(data["time"])
	#print(data.iloc[0]["sds-pm2.5"])
  	# pd.to_datetime(data.time,yearfirst=True, dayfirst=False)

        data["time"] = dateparse(data["time"])
 	data.set_index('time', inplace=True)
        print(data.head(2))
	print(data.iloc[0]["sds-pm2.5"])
	print(data.columns)
	DHT=0
	SDS=0
	OPC=0
	for sen in sensors:
		if "DHT" in sen.upper():
			DHT=DHT+1
		elif "SDS" in sen.upper():
			SDS=SDS+1
		elif "OPC" in sen.upper():
				OPC=OPC+1
	print(DHT)
	if DHT>1:
    		DHTMeandata=pd.DataFrame(columns=["RH","Temp"])
		print("There are "+ str(DHT)+" in Data")
		DHTColumns=["DHT-RH","DHT-T"]
		for i in range(0,DHT):
			if i>0:
				DHTColumns.append("DHT-RH."+str(i))
				DHTColumns.append("DHT-T."+str(i))
        
  	DHTMeandata["RH"]=data[DHTColumns[::2]].mean(axis=1)
  	DHTMeandata["Temp"]=data[DHTColumns[1::2]].mean(axis=1)
  	print(DHTMeandata.describe())
	print(DHTColumns[::2])
	print(data[DHTColumns[::2]].mean(axis=0))
	print(DHTColumns[1::2])
	print(data[DHTColumns[1::2]].mean(axis=0))
	print(data[DHTColumns].head(3))
  	
	return data, sensors


data,sensors=readrpi3data()
dataplotter(data)
