import serial 
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB5', 9600, timeout=1)
    ser.flush();

# Reading from Arduino
#    while True:
#        if ser.in_waiting > 0:
#            line = ser.readline().decode('utf-8').rstrip()
#            print(line)

    while True:
        ser.write(b"Read\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)