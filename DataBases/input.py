import sqlite3 as lite
# import sys

# create the db file
with open("UserInfo.db", "w+"):
    pass

# connect to the database using sqlite
con = lite.connect('UserInfo.db')

with con:
    cur = con.cursor()    

    # create a table and add three elements
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")

    # create a table and add three elements
    cur.execute("CREATE TABLE Clients(Phone INT, Name TEXT, Friends INT)")
    cur.execute("INSERT INTO Clients VALUES(2056961123,'Michelle',2057961123)")
    cur.execute("INSERT INTO Clients VALUES(2057961123,'Sonya',2056961123)")
    cur.execute("INSERT INTO Clients VALUES(2025961123,'Greg',2057961123)")

    # deletes a table
    cur.execute("DROP TABLE Users")
    cur.execute("DROP TABLE Clients")

