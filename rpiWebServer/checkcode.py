#/usr/bin/env python
import requests
import sys
import psutil # to check the sensors are running 


def checkrun():
    #fuction checks the run varaible from the varaible.py and sees if these code are running or not
    #it returns there stats with code name with Running or NotRunning in an array 
    run=["start.py"]
    check=""
    for R in run: #for loop for each code
        print(R) #check the code
        #Create a large array with all the prosses currenlty running
        Process=[]
        for process in psutil.process_iter():
            Process=Process+process.cmdline()
            # print(Process)                        

        # check if the code is in the processes,
        if any(R in s for s in Process):
                sys.exit(':Process found.')
                status="_Running"
        else:
                print('Process not found: starting.')
                status=":NotRunning"
        sp=R.split(".") #cut out the .py in the run code 
        sencheck=sp[0]+status
        print(sencheck)
        check=check+sencheck+"_"
        
    return check
checkrun()