# File intended to be interface with user info database
# Functions will be created for all anticipated interactions
# Please add doc strings to any added tools or updates

import sqlite3 as lite
# import sys


# connect to database with sqlite
db = "UserInfo.db"
con = lite.connect(db)


def insert(table, id_num, name, email, password, pin, phone, friends, connection):
    """
    Intended to allow inserting of client information into the client table
    :param table:
    :param id_num:
    :param name:
    :param email:
    :param password:
    :param pin:
    :param phone:
    :param friends:
    :param connection:
    :return:
    """

    with con:
        cur = con.cursor()
        num = cur.execute("SELECT count(*) FROM "+str(table))
        print(num)
        cur.execute("INSERT INTO "+str(table)+" VALUES("+str(id_num)+",'"+str(name)+"', '"+str(email)+"', '"
                    + str(password)+" ', "+str(pin)+", "+str(phone)+", "+str(friends)+", '"+str(connection)+"')")


# to test the insert function
insert('Users', 2, 'Michelle', 'mich@yahoo.org', 'MissMich1', 4321, 111222333, '','nopers')
