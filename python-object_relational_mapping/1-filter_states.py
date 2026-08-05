#!/usr/bin/python3
"""Module that lists all states starting with N from the database."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'"
    query += " ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
