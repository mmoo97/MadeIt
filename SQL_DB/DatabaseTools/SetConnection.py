#!/usr/bin/env python
# script to set connection infor for a user in database
import sqlite3 as lite
from .CheckEmail import checkEmail

# from .Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

def setConnection(user_email, connection):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set Connection = '{}' WHERE Email = '{}';".format(table, connection, user_email))
            return True
        else:
            return False


# print(setFirst("i@gmail.com","NewFirst"))
