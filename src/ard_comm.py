"""
This file contains all the functions needed for Arduino communication.

"""

import serial


def read_uid_from_tag(ser: serial.Serial) -> str:
    while True:
        try:
            ser_byte = (ser.readline().decode(
                'utf-8').strip('\n').strip().split(':'))
            if 'Card UID' in ser_byte:
                UID = ''.join(ser_byte[1].split())
                return UID
            return None

        except KeyboardInterrupt as e:
            print(e)
            return None


def write_string_to_tag(ser: serial.Serial) -> bool:
    return False


if __name__ == '__main__':

    # Establish serial connection
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.flushInput()
    print(read_uid_from_tag(ser))
