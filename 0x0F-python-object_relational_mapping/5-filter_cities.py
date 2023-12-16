#!/usr/bin/python3
"""filter cities"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    # take arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    query = "SELECT name FROM cities WHERE state_id = \
    (SELECT id FROM states WHERE name = '{}' LIMIT 1) ORDER BY id ASC".format(state_name)\

    db = MySQLdb.connect(
        host="localhost", user=db_user, passwd=db_pass, db=db_name, port=3306
    )
    cursor = db.cursor()
    cursor.execute(query)

    # fetch all
    rows = cursor.fetchall()

    # Display all
    tuples = []
    for row in rows:
        tuples += row
    print(", ".join(tuples))

    # close connection
    cursor.close()
    db.close()
