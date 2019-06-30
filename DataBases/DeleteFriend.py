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

            user_friends = user_friends.split("_")
            user_friends.remove(friendID)
            user_friends =  "_".join(user_friends)

            # Insert updated friends to user
            cur.execute("UPDATE {} Set Friends = '{}' WHERE Email = '{}';".format(table, user_friends, user_email))
            return True
        else:
            return False


#Demo Cases
# print(deleteFriend("c@gmail.com","s@gmail.com"))
# print(deleteFriend("c@gmail.com","i@gmail.com"))
# print(deleteFriend("c@gmail.com","d@gmail.com"))
