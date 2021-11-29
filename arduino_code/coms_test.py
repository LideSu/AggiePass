import serial 
import time
import smbus


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()

# Reading from Arduino
#    while True:
#        if ser.in_waiting > 0:
#            line = ser.readline().decode('utf-8').rstrip()
#            print(line)

    while True:
        s = ser.readline()
        s = s.strip()
        print(s.decode("utf-8"))
        if(s.decode("utf-8") == "<Arduino is ready>"):
            print("sending")
            ans = 'sW6iRQE1lUMzBU2cpMtI6186tu6ruxeF\n'
            ans = ans.encode("utf-8")
            ser.write(ans)