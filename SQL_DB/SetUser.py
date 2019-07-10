#!/usr/bin/env python
# script to set a new username in database for user
import sqlite3 as lite
from CheckEmail import checkEmail

from Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def setUser(user_email, username):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set UserName = {} WHERE Email = '{}';".format(table, username, user_email))
            return True
        else:
            return False


# print(setUser("i@gmail.com","NewUser"))
