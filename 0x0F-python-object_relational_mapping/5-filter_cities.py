#!/usr/bin/python3
"""5-filter_cities module"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cursor = db.cursor()
    query = ("SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4], ))
    rows = cursor.fetchall()
    new_list = list(row[0] for row in rows)
    print(", ".join(new_list))
    cursor.close()
    db.close()
