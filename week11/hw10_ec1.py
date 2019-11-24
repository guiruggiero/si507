'''
SI 507 F19, homework 11: Basic SQL statements - EC 1
Developed by Gui Ruggiero
'''

import sqlite3 as sqlite

conn = sqlite.connect("Northwind_small.sqlite")
cur = conn.cursor()

'''
SOLUTION USING ONLY SQL - should work but it's not and I don't know why

statement = "SELECT r.CustomerId, r.OrderDate, "
statement += "LAG(r.OrderDate) OVER (ORDER BY r.CustomerId) AS PreviousOrderDate, "
statement += "DATE(r.OrderDate) - DATE(LAG(r.OrderDate) OVER (ORDER BY r.CustomerId)) AS DaysPassed "
statement += "FROM [Order] AS r "
statement += "ORDER BY r.CustomerId, r.OrderDate"
cur.execute(statement)

print("\nCustomerID,Order date,Previous order date,Days passed")
for row in cur:
    print(row[0] + ", " + row[1] + ", " + row[2] + ", " + row[3])

'''

# SOLUTION USING SQL AND PYTHON

from datetime import datetime

statement = "SELECT CustomerId, OrderDate "
statement += "FROM [Order] "
statement += "ORDER BY CustomerId, OrderDate"
cur.execute(statement)

previous_customer = "placeholder"
print("\nCustomerID,Order date,Previous order date,Days passed")
for row in cur:
    if row[0] != previous_customer:
        previous_customer = row[0]
        previous_order_date = datetime.strptime(row[1], "%Y-%m-%d").date()
        # print(previous_order_date)
    else:
        actual_order_date = datetime.strptime(row[1], "%Y-%m-%d").date()
        # print(actual_order_date)
        delta_days = abs((actual_order_date - previous_order_date).days)
        # print(delta_days)
        print(row[0] + "," + row[1] + "," + str(previous_order_date) + "," + str(delta_days))
        previous_order_date = datetime.strptime(row[1], "%Y-%m-%d").date()

conn.close()