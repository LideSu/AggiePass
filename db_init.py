from lib.database import mydb as database
from lib.constant import database_name
from lib.constant import (
    password_vault_tab, password_vault_col, password_vault_col_typ,
    password_vault_primary_key)
from lib.constant import (
    authentication_tab, authentication_col, authentication_col_typ,
    authentication_primary_key)


if __name__ == '__main__':
    db = database(database_name)
    db.connect()
    if (not db.check_table_exist(password_vault_tab)):
        db.new_table(
            password_vault_tab, password_vault_col, password_vault_col_typ,
            primary_key=password_vault_primary_key)

    if (not db.check_table_exist(authentication_tab)):
        db.new_table(
            authentication_tab, authentication_col, authentication_col_typ,
            primary_key=authentication_primary_key)
