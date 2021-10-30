"""
This file contains all the functions needed for
new user registration.

Registration process:
- Create a new user id -> store to authentication database
- Generate a random string key
- Write to rfid tag
- User create a custom password
- Generate a random salt -> store to authentication database
- Once registration done -> forge the aes key and send the user
  to the password management screen.
"""





