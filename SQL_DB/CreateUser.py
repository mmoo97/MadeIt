# File intended to be interface with user info database
# Functions will be created for all anticipated interactions
# Please add doc strings to any added tools or updates

import sqlite3 as lite

# import sys


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def insert(table, id_num, name, email, password, pin, phone, friends, connection):
    with con:
        cur = con.cursor()
        # num = cur.execute("SELECT MAX(Id) FROM "+str(table))
        # print(num.fetchone()[0])

        cur.execute(
            "INSERT INTO " + str(table) + " VALUES(" + str(id_num) + ",'" + str(name) + "', '" + str(email) + "', '"
            + str(password) + "', " + str(pin) + ", " + str(phone) + ", '" + str(friends) + "', '" + str(
                connection) + "')")


def createUser(username, password, email):
    # edit the table name here if we change it in the database
    table = "Users"
    pin = 1234
    phone = 1112223333
    friends = ""
    connectionInfo = "NoneYet"

    with con:
        cur = con.cursor()
        # find the id number
        try:
            num = cur.execute("SELECT MAX(Id) FROM " + str(table))
            id = num.fetchone()[0] + 1
        except TypeError:
            id = 1

        insert(table, id, username, email, password, pin, phone, friends, connectionInfo)



def createSampleUsers():
    createUser("Zack", "password", "z@gmail.com")
    createUser("Scott", "password", "s@gmail.com")
    createUser("Ishan", "password", "i@gmail.com")
    createUser("Curt", "password", "c@gmail.com")
    createUser("Daniel", "password", "d@gmail.com")
    createUser("Mitchell", "password", "m@gmail.com")
