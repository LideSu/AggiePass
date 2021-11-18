"""
This file contains all the functions needed for
new user registration.

Registration process:
- Create a new user id (read UID)-> store to authentication database
- Generate a random string key
- Write to rfid tag
- User create a custom pin
- Generate a random salt -> store to authentication database
- Once registration done -> forge the aes key and send the user
  to the password management screen.
"""

from database import mydb as database
from constant import database_name, authentication_tab, password_vault_tab
import encrypt_tools as enc

import psycopg2

# Current UID function for reading, will be changed in the future


def new_uid_to_db(
        db: database, uid: str, salt: str, pin: str) -> bool:
    """
    This functon returns True if we successfully add the
    new user into the database. Else returns False.
    """
    if (not db.uid_exist(uid)):
        db.insert(
            authentication_tab,
            {'uid': uid, 'salt': salt, 'pin': pin})
        return True
    return False


if __name__ == '__main__':

    # Creating a new account

    # Connect to database
    db = database(database_name)
    db.connect()

    # Read tag to get UID, check if it is new (Jack doing it)
    new_uid = 'ASSSASSA'
    if (not db.uid_exist(new_uid)):
        print('New UID detected, you want to register?')
    else:
        print('UID recognized! Logging you in...')

    # Generate a random string key
    rand_str = enc.random_str_gen()
    # Write it to rfid tag (Jack doing it)

    # Get a pin entry from user (Lide working on it)
    new_pin = 'RANDOM123'  # <-- placeholder

    # Generate a salt -> store it in DB
    rand_salt = enc.generate_pin_salt()

    # Forge the secret key and pass it to the password manager screen
    secret_key = enc.forge_secret_key(tag_random_str=rand_str, pin=new_pin)
    print(secret_key)

    # Test
    acc_des = 'This is a test account.'
    acc_username = 'minh.luu@tamu.edu'
    acc_password = 'Abc123123123'
    secret_msg = 'Hello :)'
    enc_acc_dess = enc.encrypt_data(
        'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
        data=acc_des)
    enc_username = enc.encrypt_data(
        'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
        data=acc_username)
    enc_acc_password = enc.encrypt_data(
        'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
        data=acc_password)
    
    try:
        db.insert(
            password_vault_tab,
            {'uid': '123123', 'acc_description': enc_acc_dess,
            'acc_username': enc_username, 'acc_password': enc_acc_password})
    except psycopg2.Error as e:
        print(e, end='')


    # VERY DANGEROUS, DELETE EVERYTHING WITH THE SAME UID
    # db.delete_row(password_vault_tab, condition='uid=\'{}\''.format('123123'))

    # print('{}\n{}\n{}'.format(secret_msg, encrypted_msg, decrypted_msg))
    # salt = enc.generate_pin_salt()
    # print(new_uid_to_db(db=db, uid='ASDASDAS', salt=salt, pin='LKAJSDLKSAMDASDA'))
