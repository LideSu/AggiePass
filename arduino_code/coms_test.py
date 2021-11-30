import serial 
import time
import smbus


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

# Reading from Arduino
#    while True:
#        if ser.in_waiting > 0:
#            line = ser.readline().decode('utf-8').rstrip()
#            print(line)

    while True:
            s = ser.readline()
            s = s.strip()
            print(s.decode("utf-8"))
            if(s.decode("utf-8") == "Arduino is ready"):
                ans = '=y-ZJvvNagaB5b6UVGC66OZYZ40T8Sg_C\n'
                ans = ans.encode("utf-8")
                ser.write(ans)