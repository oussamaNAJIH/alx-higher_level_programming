#!/usr/bin/python3
import sys
import MySQLdb
"""
script that takes in the name of a state as an argument
and lists all cities of that state
"""
username = sys.argv[1]
password = sys.argv[2]
nameDb = sys.argv[3]
state_name = sys.argv[4]
conn = MySQLdb.connect(host="localhost", port=3306,
                       user=username, passwd=password,
                       db=nameDb, charset="utf8")
cur = conn.cursor()
sql_query = "SELECT cities.name FROM cities JOIN states ON " +\
        "cities.state_id = states.id " +\
        "WHERE states.name = '{}' ORDER BY cities.id ASC".format(state_name)
cur.execute(sql_query)
query_rows = cur.fetchall()
cities = ""
for row in query_rows:
    cities += row[0] + ", "
cities = cities[:-2]
print(cities)
cur.close()
conn.close()
