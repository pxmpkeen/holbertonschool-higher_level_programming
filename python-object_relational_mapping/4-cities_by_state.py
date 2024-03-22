#!/usr/bin/python3
"""
Connecting to database and listing it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name \
            FROM `cities` c INNER JOIN `states` s \
            ON c.states_id = s.id ORDER BY c.id ASC""")

    [print(c) for c in cur.fetchall()]

    cur.close()
    db.close()
