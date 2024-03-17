#!/usr/bin/python3
"""
Connecting to database and listing it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
    a = argv[4]
    query = """SELECT * FROM states WHERE name = {} ORDER BY id""".format(a)
    try:
        cur.execute(query)
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        print(row)

    cur.close()
    db.close()
