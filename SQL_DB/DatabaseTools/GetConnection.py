 #!/usr/bin/env python
# script to get connection info for a user in database
import sqlite3 as lite
from .CheckEmail import checkEmail

# from .Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

def getConnection(user_email):
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            connectInfo = cur.execute("SELECT Connection FROM {} WHERE Email = '{}';".format(table,user_email))
            connectInfo = connectInfo.fetchone()[0]
            return connectInfo
        else:
            return False


# print(setFirst("i@gmail.com","NewFirst"))

