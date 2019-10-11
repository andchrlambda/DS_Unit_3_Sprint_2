import os
import sqlite3

CONN = sqlite3.connect('demo_datasqlite3')
cursor = CONN.cursor()

delete_table = "DROP TABLE IF EXISTS demo"
cursor.execute(delete_table)

create_table = """
CREATE TABLE demo(
    "s" TEXT,
    "x" INT,
    "y" INT
    )"""
cursor.execute(create_table)

insert_info = """
    INSERT INTO demo(
    s, x, y
    )
    VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""
cursor.execute(insert_info)
cursor.close()
CONN.commit()

cursor2 = CONN.cursor()
query1 = 'SELECT COUNT (*) FROM demo;'
rows = cursor2.execute(query1).fetchall()
rows = str(rows).strip('[](),')
print("There are", rows, "rows.")

query2 = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;'
five_plus = cursor2.execute(query2).fetchall()
five_plus = str(five_plus).strip('[](),')
print("There are ", five_plus, "rows where both 'x' and 'y' are at least five.")

query3 = 'SELECT COUNT (DISTINCT y) FROM demo'
distinct = cursor2.execute(query3).fetchall()
distinct = str(distinct).strip('[](),')
print("There are ", distinct, "values of 'y'.")

cursor2.close()
CONN.commit()
