import psycopg2
import psycopg2.extras
import sys


try:
    connection = psycopg2.connect("dbname='bssdb_admin' user='postgres' host='192.168.42.223'")
    print("Connecting to database\n ->%s" % (connection))
except:
    print("I am unable to connect to the database")

cur = connection.cursor()

try:
    cur.execute("""select * from users where active > 0""")
except:
    print("Fail")

rows = cur.fetchall()

for row in rows:
    name = row[1]
    if 'sorin' in name.lower():
        for i in range(len(row)):
            if row[i] is not None:
                print(row[i], flush=True)
    else:
        pass
connection.close()
