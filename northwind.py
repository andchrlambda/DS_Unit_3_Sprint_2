import os
import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')
cursor = CONN.cursor()

#Generating list of available tables
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
print("The available tables are: ", tables)

#What are the 10 most expensive items?
query1 = '''SELECT ProductName, UnitPrice FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10;'''

expensive = cursor.execute(query1).fetchall()
print(expensive)

#What is the average age of an employee at the time of their hiring?
query2 = '''SELECT AVG (HireDate - BirthDate) FROM Employee'''
avg_age_hire = cursor.execute(query2).fetchall()
avg_age_hire = str(avg_age_hire).strip('[](),')
print("The average age of an employee at the time of hiring is", avg_age_hire, ".")
# fix decimals as time permits.
#query3 = return for stretch as time permits

#Questions from next section
#What are the ten most expesive items(per unit price) and their suppliers?
query2_1 =  '''SELECT ProductName, SupplierID,
            UnitPrice FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10'''
supply = cursor.execute(query2_1).fetchall()
print("The ten most expensive items their supplier numbers, and prices are as follows:", supply)

query2_2 = '''SELECT CategoryID, COUNT (DISTINCT ProductName)
    FROM Product
    INNER JOIN Category
    on Product.ID=Category.Id
    GROUP BY (CategoryId)
    ORDER BY COUNT(DISTINCT ProductName) DESC
    Limit 1;'''
cat_with_prod = cursor.execute(query2_2).fetchall()
print(cat_with_prod)
print ("The category with the largest number and its number of products are: ", cat_with_prod)

cursor.close()
CONN.commit()
