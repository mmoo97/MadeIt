# Add a friends ID to the Frei

import sqlite3 as lite
from CheckEmail import checkEmail


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def addFriend(user_email, friend_email):
    table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, friend_email)[0]:
            # get the users friends
            user_friends = cur.execute("SELECT Friends FROM {} WHERE Email = '{}';".format(table,user_email))
            user_friends = user_friends.fetchone()[0]

            # get new friend's ID
            friendID = checkEmail(table,friend_email)[1]


            # add new friend to all friends
            user_friends = str(user_friends)+"_"+str(friendID)
            if user_friends[0] == "_":
                user_friends = user_friends[1:]


            # Insert updated friends to user
            cur.execute("UPDATE {} Set Friends = '{}' WHERE Email = '{}';".format(table, user_friends, user_email))
            return True
        else:
            return False


# print(addFriend("i@gmail.com","d@gmail.com"))
