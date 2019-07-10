#!/usr/bin/env python
# script to set a new first name in database for user
import sqlite3 as lite
from CheckEmail import checkEmail

from Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def setFirst(user_email, first):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set FirstName = {} WHERE Email = '{}';".format(table, first, user_email))
            return True
        else:
            return False


# print(setFirst("i@gmail.com","NewFirst"))
