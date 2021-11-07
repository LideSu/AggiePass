"""
This library contains all the functions needed to 
setup the database system for the password manager.
The mydb class is based on: 
https://www.tutorialspoint.com/postgresql/index.htm

"""


import psycopg2
import pandas as pd


from lib.constant import (
    authentication_tab, authentication_primary_key,
    database_account)

# Connect to the database
# Create tables
# Read from database (return a pandas dataframe)
# Write to database


class mydb:
    def __init__(self, db):
        self.db = db
        self.conn = None

    def connect(self, user=database_account):
        self.user = user
        self.conn = psycopg2.connect(
            "dbname={} user={} password=".format(self.db, user))
        self.conn.autocommit = True

    def new_table(self, tb_name, columns, col_type, primary_key,
                  constraints=[]):
        if len(columns) != len(col_type) or (
                len(constraints) > 0 and len(col_type) != len(columns)):
            raise Exception(
                "columns, col_type, and constaints (if any) should have the same length!")
        create = "CREATE TABLE {}( ".format(tb_name)
        for i, (col, t) in enumerate(zip(columns, col_type)):
            if len(constraints):
                c = " " + constraints[i] + ','
            else:
                c = ','
            create = create + col + " " + t + c
        if primary_key:
            pk = ""
            for k in primary_key:
                pk = pk+k+','
            pk = pk[:-1]
            create = create + "PRIMARY KEY({}));".format(pk)
        else:
            create = create[:-1] + ");"
        cur = self.conn.cursor()
        cur.execute(create)
        self.conn.commit()
        cur.close()

    def delete_table(self, tb_name):
        delete = "DROP TABLE {}".format(tb_name)
        cur = self.conn.cursor()
        cur.execute(delete)
        self.conn.commit()
        cur.close()

    def check_table_exist(self, tb_name):
        cur = self.conn.cursor()
        cur.execute(
            "select * from information_schema.tables where table_name='{}'".format(tb_name))
        return bool(cur.rowcount)

    def insert(self, tb_name, dic, additional_commands=""):
        col = "("
        val = "("
        for k, v in dic.items():
            col = col + str(k) + ','
            if type(v) == str:
                v = "\'" + v + "\'"
            val = val + str(v) + ','
        col = col[:-1] + ')'
        val = val[:-1] + ')'
        insert = "INSERT INTO {name} {columns} VALUES {values} ".format(
            name=tb_name, columns=col, values=val) + additional_commands + ";"
        cur = self.conn.cursor()
        cur.execute(insert)
        self.conn.commit()
        cur.close()

    def update(self, tb_name, dic, condition=""):
        SET = ""
        for k, v in dic.items():
            if type(v) == str:
                v = "\'" + v + "\'"
            SET = SET + str(k) + ' = ' + str(v) + ','
        up = "UPDATE {name} SET {SET}".format(name=tb_name, SET=SET[:-1])
        if condition:
            up = up + " WHERE " + condition + ';'
        else:
            up = up + ';'
        cur = self.conn.cursor()
        cur.execute(up)
        self.conn.commit()
        cur.close()

    def select(self, tb_name, columns, condition="", additional_commands=""):
        col = ""
        for c in columns:
            col = col + str(c) + ','
        select = "SELECT {col} FROM {name}".format(col=col[:-1], name=tb_name)
        if condition:
            select = select + " WHERE " + condition
        if additional_commands:
            select = select + " " + additional_commands + ';'
        else:
            select = select + ';'
        cur = self.conn.cursor()
        cur.execute(select)
        rows = cur.fetchall()
        cur.close()
        return rows

    def delete_row(self, tb_name, condition=""):
        delete = "DELETE FROM {}".format(tb_name)
        if condition:
            delete = delete + " WHERE " + condition + ';'
        else:
            delete = delete + ';'
        cur = self.conn.cursor()
        rows_deleted = cur.rowcount
        cur.execute(delete)
        self.conn.commit()
        cur.close()
        return rows_deleted

    def add_column(self, tb_name, columns, col_type, constraints=[]):
        if len(columns) != len(col_type) or (
                len(constraints) > 0 and len(col_type) != len(columns)):
            raise Exception(
                "columns, col_type, and constraints (if any) should have the same length!")
        create = "ALTER TABLE {}".format(tb_name)
        for i, (col, t) in enumerate(zip(columns, col_type)):
            if len(constraints):
                c = " " + constraints[i] + ','
            else:
                c = ','
            create = create + " ADD COLUMN " + col + " " + t + c
        create = create[:-1] + ';'
        cur = self.conn.cursor()
        cur.execute(create)
        self.conn.commit()
        cur.close()

    def command(self, comm, fetch=False):
        cur = self.conn.cursor()
        cur.execute(comm)
        self.conn.commit()
        result = None
        if fetch:
            result = cur.fetchall()
        cur.close()
        return result

    def helpme(self):
        import webbrowser
        print("https://www.tutorialspoint.com/postgresql/index.htm")
        webbrowser.get("firefox").open(
            "https://www.tutorialspoint.com/postgresql/index.htm")

    def close(self):
        self.conn.close()

    def reset(self):
        """Close the database connection and reconnect to the same database."""
        self.conn.close()
        self.conn = psycopg2.connect(
            "dbname={} user={} password=".format(self.db, self.user))

    def uid_exist(self, uid) -> bool:
        cur = self.conn.cursor()
        cur.execute("SELECT {} FROM {} WHERE {} = {}".format(
            authentication_primary_key, authentication_tab,
            authentication_primary_key, uid))
        return cur.fetchone() is not None

    def user_vault(self, uid) -> pd.DataFrame:
        pass