# File intended to be interface with user info database
# Functions will be created for all anticipated interactions
# Please add doc strings to any added tools or updates

import sqlite3 as lite

from Variables import *
from CheckEmail import checkEmail


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def insert(table, id_num, first, last, username, email, password, pin, phone, friends, connection):
    with con:
        cur = con.cursor()
        # num = cur.execute("SELECT MAX(Id) FROM "+str(table))
        # print(num.fetchone()[0])

        cur.execute(
            "INSERT INTO " + str(table) + " VALUES(" + str(id_num) + ", '" + str(first)+ "', '" + str(last) 
            + "', '" + str(username) + "', '" + str(email) + "', '" + str(password) + "', " + str(pin) + ", " 
            + str(phone) + ", '" + str(friends) + "', '" + str(connection) + "')")


def createUser(first, last, username, password, email):
    # edit the table username here if we change it in the database
    # table = "Users"
    # pin = 1234
    # phone = 1112223333
    # friends = ""
    # connectionInfo = "NoneYet"

    with con:
        cur = con.cursor()
        # find the id number
        try:
            num = cur.execute("SELECT MAX(Id) FROM " + str(table))
            id = num.fetchone()[0] + 1
        except TypeError:
            id = 1

        # check to see if the user is already in the db
        if checkEmail(table, email)[0]:
            return False

        # if the user isn't in db, add them
        insert(table, id, first, last, username, email, password, pin, phone, friends, connectionInfo)
        return True


# print(createUser("Johnny", "Mathis", "jmat", "password", "j@gmail.com"))


def createSampleUsers():
    createUser("Zack","Attack","zatack", "password", "z@gmail.com")
    createUser("Scott", "Bot", "sbot", "password", "s@gmail.com")
    createUser("Ishan", "Mymon", "imon", "password", "i@gmail.com")
    createUser("Curt", "inYurt", "curtisimo", "password", "c@gmail.com")
    createUser("Daniel", "Spaniel", "skiman", "password", "d@gmail.com")
    createUser("Mitchell", "Schnitzel", "itchy", "password", "m@gmail.com")
    createUser("Tony", "de Coney", "islander"," password", "t@gmail.com")

# createSampleUsers()