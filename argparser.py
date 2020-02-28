<<<<<<< HEAD
import argparse
 # from serial import Serial
import serial
=======
import serial,argparse
import requests
#def check(x,y):
#    global prev_state,duration,cost,pay
    
#    for i in range(2):
#        if(x[i]==0 and y[i]==1):
#            timer[i]=time.time()
#            print(timer[i])
#        elif(x[i]==1 and y[i]==0):
#            duration[i]=timer[i]-time.time()
#            print(duration[i]+" "+i)
#        else:
#            print("x:  "+str(x))
#            print("y :  "+str(y))
#            pay[i]=duratin[i]*cost
#            print("amount"+pay[i])
#def time_start():
#    return time.time()
#def pre_state_update():
#    prev_state=parking_valid
#        
>>>>>>> 27152cca011c2e34a99aa12b903e80050960074b
parser = argparse.ArgumentParser(description="com port")
  # add expected arguments
parser.add_argument('--com', dest='com', required=True)
<<<<<<< HEAD
comp = parser.parse_args()
ser = comp.com
ser2 = serial.Serial(ser,9600)
while True:
    line = ser2.readline()
    print(line)
=======

  # parse args
comp= parser.parse_args()
    
ser = comp.com
serl = serial.Serial(ser,9600)
#pay=[0,0,0]
#cost=10
#duration=[0,0,0]
#timer=[0,0,0]
prev_state=[1,1,1]
parking_valid=[1,1,1]
st_url="http://192.168.43.250:8080/update?p="
#update=True
while True:
   

    line = str(serl.readline())
#        i=0
    print(parking_valid)
    
    parking_valid=[int(i) for i in line.split(",")]
    if prev_state != parking_valid:
        st_url=st_url+str(parking_valid[0])+"&q="+str(parking_valid[1])+"&r="+str(parking_valid[2])
        requests.get(url=st_url)
        prev_state=parking_valid
    
#    prev_state=parking_valid
#    for i in range(2):
#        if parking_valid[i] == 0 and update==False:
#            timer[i]=time.time()
#            print(timer[i])        
#            update =True
#        elif parking_valid[i]== 1 and update== True:
#            duration[i]=time.time()-timer[i]
#            
#            update= False
            
        
#    check(parking_valid,prev_state)
#    time.sleep(2)
    
    
    
>>>>>>> 27152cca011c2e34a99aa12b903e80050960074b
