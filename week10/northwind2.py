import sqlite3

conn = sqlite3.connect("Northwind_small.sqlite")
cur = conn.cursor()

# Exercise 1
# statement = "SELECT r.Id, r.ShippedDate, Shipper.CompanyName, Shipper.Phone "
# statement += "FROM [Order] AS r JOIN Shipper ON r.ShipVia = Shipper.Id"

# Exercise 2
# statement = "SELECT r.Id, r.Freight "
# statement += "FROM [Order] AS r JOIN Shipper ON r.ShipVia = Shipper.Id "
# statement += "WHERE r.Freight > 100 AND Shipper.CompanyName = 'United Package'"

# Exercise 3
# statement = "SELECT Customer.CompanyName, Customer.Country "
# statement += "FROM Customer JOIN [Order] AS r ON Customer.Id = r.CustomerId "
# statement += "WHERE r.ShippedDate LIKE '2012-10%'"

# Exercise 4
statement = "SELECT e.FirstName, e.LastName "
statement += "FROM Employee AS e JOIN Employee AS boss "
statement += "ON e.ReportsTo = boss.Id "
statement += "WHERE boss.Title LIKE '%Vice President%'"

cur.execute(statement)

for row in cur:
    print(row)

conn.close()