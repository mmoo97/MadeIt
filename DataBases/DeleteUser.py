
import sqlite3 as lite
from Variables import *
from CheckEmail import checkEmail

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


# this function will delete the user from the database by their email
def deleteUser(email):

    if checkEmail(table, email):
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM {} WHERE Email = '{}'".format(table, email))

        return True

    # should never get here
    return False

deleteUser("tonyboy@gmail.com")