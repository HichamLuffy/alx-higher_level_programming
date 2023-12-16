#!/usr/bin/python3
"""my safe filter states"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name LIKE BINARY\
 %s ORDER BY id ASC"
    safe = (state_name,)
    db = MySQLdb.connect(
        host="localhost", user=db_user, passwd=db_pass, db=db_name, port=3306
    )

    cursor = db.cursor()
    cursor.execute(query, safe)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
