# todo: search database for matching email then if found insert user ID into friend list then insert list into friend

import sqlite3 as lite

db = "UserInfo.db"
con = lite.connect(db)


def checkEmail(table, email):
    """Return: If True: (True, num)
                If False: (False, 0)
        Second value is the userId"""

    with con:
        cur = con.cursor()
        try:
            num = cur.execute("SELECT Id FROM " + str(table) + " WHERE Email = '" + str(email) + "'")
            num = num.fetchone()[0]
            return True, num
        except TypeError:
            return False, None


#Example Cases
# checkEmail("Users", "butts@yahoo.com")
#
# checkEmail("Users", "i@gmail.com")
