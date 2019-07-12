import sqlite3 as lite
# import sys


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

# checks if the email (and therefore user) is present in the data base (true or false)
def checkEmail(table, email):
    with con:
        cur = con.cursor()
        try:
            num = cur.execute("SELECT Id FROM " + str(table) + " WHERE Email = '" + str(email) + "';")
            num = num.fetchone()[0]
            return True, num
        except TypeError:
            return False, None

