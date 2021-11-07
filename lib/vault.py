"""

"""
from lib.database import mydb as database
from lib.constant import (
    password_vault_tab, password_vault_col, password_vault_col_typ,
    password_vault_primary_key)

# Notes:
#   - There should be some forms of error handling when the user leaves a field blank


class Vault:
    def __init__(self, uid):
        self.uid = uid
        self.decryption_key = ''
        self.password_vaults_db = database(password_vault_tab)
        self.password_vaults_db.connect()

    def insert_account(self) -> bool:
        pass

    def edit_account(self) -> bool:
        pass

    def delete_account(self) -> bool:
        pass

    def save_changes(self) -> bool:
        pass

    def write_vault(self):
        pass

    def read_vault(self):
        pass
