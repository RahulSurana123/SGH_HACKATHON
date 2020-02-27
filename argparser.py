import argparse
import serial
import time
def check(x):
    global prev_state,duration
    for i in range(2):
        if(x[i]==0 and prev_state==1):
            timer[i]=time.time()
            print(timer[i])
        elif(x[i]==1 and prev_state==0):
            duration[i]=timer[i]-time.time()
            print(duration[i]+" " +i)
            
            
parser = argparse.ArgumentParser(description="com port")
parser.add_argument('--com', dest='com', required=True)
comp = parser.parse_args()
ser=comp.com
serl = serial.Serial(ser,9600)
duration=[0,0,0]
timer=[0,0,0]
prev_state=[0,0,0]
while True:
    
    line = serl.readline()
#    line1=int(line)
    parking_valid=[int(i) for i in line.split(",")]
#    print(line)
    check(parking_valid);
#    global prev_state
    prev_state=parking_valid
    
#    if parking_valid[0]==0:
#        timer[0]=time.time()
#            
#    else:
#        print("kuch bhi")
#            