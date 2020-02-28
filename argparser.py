import serial,argparse
import requests
import threading
import time
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


def argu():
    
    global parking_valid,prev_state,req_need,st_url
    while True:
#        print(req_need)
#        if req_need==False:
            
        line = str(serl.readline())
        #        i=0
        print(parking_valid)
        parking_valid=[int(i) for i in line.split(",")]
        if prev_state != parking_valid:
            req_need=True
            prev_state=parking_valid
        time.sleep(2)
def requ():
    
    global parking_valid,prev_state,req_need,st_url
    
    while True:
#        print(req_need)
#        print("hii")
#        global parking_valid,prev_state
        if req_need == True:
            
            st_url=st_url+str(parking_valid[0])+"&q="+str(parking_valid[1])+"&r="+str(parking_valid[2])
            requests.get(url=st_url)
            
            req_need == False
        time.sleep(6)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="com port")
      # add expected arguments
    parser.add_argument('--com', dest='com', required=True)

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
    req_need=False            
   
    t1 = threading.Thread(target=argu)
    t2 = threading.Thread(target=requ)  
    t1.setDaemon(True)
    t2.setDaemon(False)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
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
    
    
    