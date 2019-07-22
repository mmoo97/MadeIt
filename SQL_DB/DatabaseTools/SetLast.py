#!/usr/bin/env python
# script to set a new Last name in database for user
import sqlite3 as lite
from . import CheckEmail
# from . import Variable
# from Variables.py import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

def setLast(user_email, last):


    with con:
        cur = con.cursor()

        if CheckEmail.checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set LastName = '{}' WHERE Email = '{}';".format(table, last, user_email))
            return True
        else:
            return False


# print(setLast("i@gmail.com","NewLast"))
