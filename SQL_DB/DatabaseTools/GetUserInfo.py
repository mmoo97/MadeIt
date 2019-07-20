#!/usr/bin/env python

# returns the information needed by HandleJSON to pack and send the retJSON 
import sqlite3 as lite
from CheckEmail import checkEmail

# from .Variables import *

# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)
table = "Users"

def getUserInfo(user_email):
    """
    return [connectInfo, fromInfo]\n
    fromInfo = information packed into "From" in retJSON
    """
    
    # table = "Users"

    with con:
        cur = con.cursor()

        if checkEmail(table, user_email)[0]:

            # Insert pin to 
            connectInfo = cur.execute("SELECT Connection FROM {} WHERE Email = '{}';".format(table,user_email))
            connectInfo = connectInfo.fetchone()[0]

            userName = cur.execute("SELECT UserName FROM {} WHERE Email = '{}';".format(table,user_email))
            userName = userName.fetchone()[0]

            firstName = cur.execute("SELECT FirstName FROM {} WHERE Email = '{}';".format(table,user_email))
            firstName = firstName.fetchone()[0]

            lastName = cur.execute("SELECT LastName FROM {} WHERE Email = '{}';".format(table,user_email))
            lastName = lastName.fetchone()[0]

            # fromInfo = '{ "UserName":{}, "FirstName":{}, "LastName":{}, "Email":{} }'.format(userName, firstName, lastName, user_email)
            fromInfo = '{"UserName":"'+userName+'", "FirstName":"'+firstName+'", "LastName":"'+lastName+'", "Email":"'+user_email+'"}'
            return [connectInfo, fromInfo]
        else:
            return False


# print(getUserInfo("d@gmail.com"))

