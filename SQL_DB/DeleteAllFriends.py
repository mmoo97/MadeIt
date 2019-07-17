
import sqlite3 as lite
from CheckEmail import checkEmail


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def deleteAllFriends(user_email):
    table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            user_friends = ""

            # Insert updated friends to user
            cur.execute("UPDATE {} Set Friends = '{}' WHERE Email = '{}';".format(table, user_friends, user_email))
            return True
        else:
            return False


# print(deleteAllFriends("i@gmail.com" ))
