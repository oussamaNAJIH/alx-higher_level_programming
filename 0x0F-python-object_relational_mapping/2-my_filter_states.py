#!/usr/bin/python3
import sys
import MySQLdb
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
"""
username = sys.argv[1]
password = sys.argv[2]
nameDb = sys.argv[3]
searched = sys.argv[4]
conn = MySQLdb.connect(host="localhost", port=3306,
                       user=username, passwd=password,
                       db=nameDb, charset="utf8")
cur = conn.cursor()
sql_query = "SELECT * FROM states WHERE name = '{}'".format(searched) + \
            " ORDER BY id ASC"
cur.execute(sql_query)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
