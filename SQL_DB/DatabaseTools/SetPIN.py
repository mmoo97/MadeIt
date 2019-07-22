# Add a friends ID to the Frei

import sqlite3 as lite
from CheckEmail import checkEmail

from Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def addPIN(user_email, pin):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            cur.execute("UPDATE {} Set PIN = {} WHERE Email = '{}';".format(table, pin, user_email))
            return True
        else:
            return False


# print(addPIN("i@gmail.com",9999))
