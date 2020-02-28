import argparse
 # from serial import Serial
import serial
parser = argparse.ArgumentParser(description="com port")
parser.add_argument('--com', dest='com', required=True)
comp = parser.parse_args()
ser = comp.com
ser2 = serial.Serial(ser,9600)
while True:
    line = ser2.readline()
    print(line)