#!/usr/bin/env python
# script to set a new Last name in database for user
import sqlite3 as lite
from CheckEmail import checkEmail

from Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def setLast(user_email, last):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set LastName = {} WHERE Email = '{}';".format(table, last, user_email))
            return True
        else:
            return False


# print(setLast("i@gmail.com","NewLast"))
