import sqlite3

conn = sqlite3.connect("Northwind_small.sqlite")
cur = conn.cursor()

#cur.execute("SELECT * FROM Employee")
#cur.execute("SELECT LastName, FirstName FROM Employee")
#cur.execute("SELECT LastName, FirstName FROM Employee WHERE Title='Sales Representative'")

# statement = "SELECT LastName, FirstName "
# statement += "FROM Employee "
# statement += "WHERE Title = 'Sales Representative'"

# Exercise 1
# statement = "SELECT companyname "
# statement += "FROM customer "
# statement += "WHERE region = 'Western Europe'"

# Exercise 2
# statement = "SELECT productname "
# statement += "FROM product "
# statement += "WHERE discontinued = 1"

# Exercise 3
# statement = "SELECT firstname "
# statement += "FROM employee "
# statement += "WHERE reportsto = 2"

# Exercise 4
# statement = "SELECT orderdate,shippeddate "
# statement += "FROM [order] "
# statement += "WHERE shipcountry = 'USA'"

# Exercise 5
# statement = "SELECT companyname "
# statement += "FROM customer "
# statement += "WHERE region <> 'North America'"

# Exercise 6
# statement = "SELECT productname "
# statement += "FROM product "
# statement += "WHERE unitsinstock < 25"

# Exercise 7
# statement = "SELECT firstname "
# statement += "FROM employee "
# statement += "WHERE birthdate BETWEEN '1980-01-01' AND '1989-12-31'"

# Exercise 8
# statement = "SELECT id "
# statement += "FROM [order] "
# statement += "WHERE ShippedDate LIKE '2014-04-__'"

# Exercise 9
# statement = "SELECT companyname "
# statement += "FROM customer "
# statement += "WHERE region LIKE '%Europe'"
# statement += "WHERE region IN ('Eastern Europe', 'Northern Europe', 'Southern Europe', 'Western Europe')"

# Exercise 10
statement = "SELECT shipname,shipaddress,shipcity,shipcountry,shippostalcode "
statement += "FROM [order] "
statement += "WHERE shipregion LIKE '%Europe' AND employeeid = 4"

cur.execute(statement)

for row in cur:
    print(row)

conn.close()