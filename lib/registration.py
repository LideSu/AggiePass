"""
This file contains all the functions needed for
new user registration.

Registration process:
- Create a new user id (read UID)-> store to authentication database
- Generate a random string key
- Write to rfid tag
- User create a custom password
- Generate a random salt -> store to authentication database
- Once registration done -> forge the aes key and send the user
  to the password management screen.
"""

import serial

from lib.database import mydb as database
from lib.constant import database_name, authentication_tab
import lib.encryption

# Current UID function for reading, will be changed in the future


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


def new_uid_to_database(
        uid: str, db: database, hashed_pwd: str, salt: str) -> bool:
    if (not db.uid_exist(uid)):
        db.insert(authentication_tab, )
    pass

if __name__ == '__main__':
    # Establish serial connection
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.flushInput()
    print(read_uid_from_tag(ser))

    # Establish database connection
    db = database(database_name)
    db.connect()
