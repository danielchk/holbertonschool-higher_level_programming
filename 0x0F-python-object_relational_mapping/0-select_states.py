#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    conection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    curs = conection.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    conection.close()
