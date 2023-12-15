#!/usr/bin/python3
"""filter states"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) < 4:
        print("wrong format")
        exit()
    # take arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(
        host="localhost", user=db_user, passwd=db_pass, db=db_name, port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
                    LIKE BINARY 'N%' ORDER BY id ASC")

    # fetch all
    rows = cursor.fetchall()

    # Display all
    for row in rows:
        print(row)

    # close connection
    cursor.close()
    db.close()
