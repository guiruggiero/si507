'''
SI 507 F19, homework 11: Basic SQL statements - 
Developed by Gui Ruggiero
'''

import sqlite3 as sqlite

conn = sqlite.connect("Northwind_small.sqlite")
cur = conn.cursor()

'''
For EC1, we are going to see the number of days passed between orders for
each customer. Identify each customer id, order date, previous order date,
and the number of days passed between two order dates in order of Customer’s
Id and then the order date. Output should look like below.
'''

statement = "SELECT CompanyName "
statement += "FROM Customer "
statement += "WHERE Country = 'USA' AND Fax IS NOT NULL"
cur.execute(statement)

print("\nCustomerID,Order date,Previous order date,Days passed")
for row in cur:
    print(row)

conn.close()