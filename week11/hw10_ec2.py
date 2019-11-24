'''
SI 507 F19, homework 11: Basic SQL statements - EC 2
Developed by Gui Ruggiero
'''

import sqlite3 as sqlite
import sys

initial_shipcity = sys.argv[1]
chars_employee_name = sys.argv[2]

conn = sqlite.connect("Northwind_small.sqlite")
cur = conn.cursor()

print("\nSearched for")
print("1) ShipCity starts with:", initial_shipcity)
print("2) The number of characters in employee's first name:", chars_employee_name)

statement = "SELECT COUNT([Order].Id) "
statement += "FROM [Order] "
statement += "JOIN Employee ON [Order].EmployeeId = Employee.Id "
statement += "WHERE ShipCity LIKE '" + initial_shipcity + "%' "
statement += "AND LENGTH(FirstName) = " + str(chars_employee_name)
cur.execute(statement)

for row in cur:
    orders = row[0]
print("The number of orders:", orders)

print("\n*Reference: the", orders, "orders captured by the query are as follows.")

statement = "SELECT ShipCity, FirstName "
statement += "FROM [Order] "
statement += "JOIN Employee ON [Order].EmployeeId = Employee.Id "
statement += "WHERE ShipCity LIKE '" + initial_shipcity + "%' "
statement += "AND LENGTH(FirstName) = " + str(chars_employee_name)
cur.execute(statement)

for row in cur:
    print(row)

print("\n")

conn.close()