import sqlite3 as lite

# create the db file
with open("UserInfo.db", "w+"):
    pass

# connect to database with sqlite
con = lite.connect('UserInfo.db')

with con:
    cur = con.cursor()

    # create user table
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT, Email TEXT, Password TEXT,\
     PIN INT, Phone INT, Friends TEXT, Connection TEXT )")

    # sample add users
    # cur.execute("INSERT INTO Users VALUES(0,'Foo', 'Foo@Bar.org', 'FooBarr', 0000, 000000000, '','NO')")

exit(0)
