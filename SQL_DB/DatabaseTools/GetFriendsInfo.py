#!/usr/bin/env python
# returns a list of tuples containing the friends names and connection info
# The returned friends list can be iterated over and all retJSONs passed through connectToClient function
import sqlite3 as lite
from .CheckEmail import checkEmail

# from .Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

def getFriendInfo(user_email):
    """
    Pass in User email and get info about user's freinds \n
    returns a list of tuples containing the friends names, email, and connection info
    """

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:
            
            retList = []

            friendIDs = cur.execute("SELECT Friends FROM {} WHERE Email = '{}';".format(table, user_email))
            friendIDs = friendIDs.fetchone()[0].split("_")

            print(friendIDs)
            # loop over freinds and build list of tuples
            for friendID in friendIDs:
                friendName = cur.execute("SELECT UserName FROM {} WHERE Id = '{}';".format(table, friendID))
                friendName = friendName.fetchone()[0]

                friendConnection = cur.execute("SELECT Connection FROM {} WHERE Id = '{}';".format(table, friendID))
                friendConnection = friendConnection.fetchone()[0]

                friendEmail = cur.execute("SELECT Email FROM {} WHERE Id = '{}';".format(table, friendID))
                friendEmail = friendEmail.fetchone()[0]

                retList.append(tuple([friendName, friendEmail,friendConnection]))

            return retList

# print(getFriendInfo("c@gmail.com"))


