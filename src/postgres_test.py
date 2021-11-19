import psycopg2

from database import mydb as database
from constant import database_name
from constant import (password_vault_tab, authentication_tab)
from encrypt_tools import forge_secret_key, encrypt_data, decrypt_data


password_manager_db = database(database_name)
password_manager_db.connect()
print()
df = password_manager_db.user_vault('123123')
print(password_manager_db.update_user_vault('123123', df))
# try:
#     # password_manager_db.insert(
#     #     password_vault_tab,
#     #     {'uid': '123123', 'acc_description': 'adsdadas',
#     #     'acc_username': 'adasddasd', 'acc_password': 'asdadadasdsa'})
#     password_manager_db.insert(
#         authentication_tab,
#         {'uid': '123123', 'salt': 'adsdadas',
#          'pin': 'adasddasd'})
# except psycopg2.Error as e:
#     print(e, end='')



# print(
#     # password_manager_db.select(
#     #     password_vault_tab,
#     #     ['uid', 'acc_description', 'acc_username', 'acc_password'])
#     password_manager_db.select(
#         authentication_tab,
#         ['uid', 'salt', 'pin']))
