# The

import sqlite3 as lite
from CheckEmail import checkEmail

# import sys


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def addFriend(user_email, friend_email):
    table = "Users"

    checkEmail("c@gmail.com")

    # check if friend is in table
    # try:
    #     num = cur.execute("SELECT MAX(Id) FROM " + str(table))
    #     id = num.fetchone()[0] + 1
    # except TypeError:
        id = 1



    # if not friend in table - return false



    # if in table - get friend id - add friend id to user's friend list - return true


