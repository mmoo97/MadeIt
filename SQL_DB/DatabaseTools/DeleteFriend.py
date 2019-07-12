#!/usr/bin/env python

# Add a friends ID to the Frei

import sqlite3 as lite
from CheckEmail import checkEmail


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def deleteFriend(user_email, friend_email):
    table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, friend_email)[0]:
            # get the users friends
            user_friends = cur.execute("SELECT Friends FROM {} WHERE Email = '{}';".format(table,user_email))
            user_friends = str(user_friends.fetchone()[0])

            # get new friend's ID
            friendID = str(checkEmail(table,friend_email)[1])

            # delete new friend to all friends
            user_friends = user_friends.split("_")
            user_friends.remove(friendID)
            user_friends = "_".join(user_friends)

            # Insert updated friends to user
            cur.execute("UPDATE {} Set Friends = '{}' WHERE Email = '{}';".format(table, user_friends, user_email))
            return True
        else:
            return False


# print(deleteFriend("i@gmail.com", "s@gmail.com"))
