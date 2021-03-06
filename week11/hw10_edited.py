'''
SI 507 F19, homework 11: Basic SQL statements
Developed by Gui Ruggiero
'''

import sqlite3 as sqlite

'''
NOTES TO GRADER
- Overall: I'm assuming the content of the cursor is what needs to be returned. It is a
list of tuples which I iterate to print data, after all.
- Question 8: I'm assuming  "names of customer" in this context is the company name,
not the name of the contact. It is a bit confusing since companies don't "live" in a country.
'''

conn = sqlite.connect("Northwind_small.sqlite")
cur = conn.cursor()

#----- Q1. Show all rows from the Region table 
print('-'*20 + "Question 1" + '-'*20)
def question1():
    statement = "SELECT * "
    statement += "FROM Region"
    cur.execute(statement)
    
    print("ID\t| Region")
    print("-"*19)
    for row in cur:
        print(row[0], "\t|", row[1])
    
    return cur
question1()

#----- Q2. How many customers are there? 
print('\n' + '-'*20 + "Question 2" + '-'*20)
def question2():
    statement = "SELECT Count(Id) "
    statement += "FROM Customer"
    cur.execute(statement)
    
    for row in cur:
        print("Number of customers:", row[0])

    return cur
question2()

#----- Q3. How many orders have been made? 
print('\n' + '-'*20 + "Question 3" + '-'*20)
def question3():
    statement = "SELECT Count(Id) "
    statement += "FROM [Order]"
    cur.execute(statement)
    
    for row in cur:
        print("Number of orders:", row[0])

    return cur
question3()

#----- Q4. Show the first five rows from the Product table 
print('\n' + '-'*20 + "Question 4" + '-'*20)
def question4():
    statement = "SELECT * "
    statement += "FROM Product "
    statement += "LIMIT 5"
    cur.execute(statement)
    
    print("ID\t| Name\t\t\t\t| Supplier ID\t| Category ID\t| Qty/unit\t\t| "
        "Price\t| In stock\t| On order\t| Reorder\t| Discontinued")
    print("-"*167)
    i = 0
    for row in cur:
        if i == 0:
            print(row[0], "\t|", row[1], "\t\t\t\t|", row[2], "\t\t|", row[3],
                "\t\t|", row[4], "\t|", row[5], "\t|", row[6], "\t\t|", row[7],
                "\t\t|", row[8], "\t\t|", row[9])
        elif i == 1:
            print(row[0], "\t|", row[1], "\t\t\t|", row[2], "\t\t|", row[3],
                "\t\t|", row[4], "\t|", row[5], "\t|", row[6], "\t\t|", row[7],
                "\t\t|", row[8], "\t\t|", row[9])
        elif i == 2:
            print(row[0], "\t|", row[1], "\t\t|", row[2], "\t\t|", row[3],
                "\t\t|", row[4], "\t|", row[5], "\t|", row[6], "\t\t|", row[7],
                "\t\t|", row[8], "\t\t|", row[9])
        elif i == 3:
            print(row[0], "\t|", row[1], "\t|", row[2], "\t\t|", row[3],
                "\t\t|", row[4], "\t|", row[5], "\t|", row[6], "\t\t|", row[7],
                "\t\t|", row[8], "\t\t|", row[9])
        else:
            print(row[0], "\t|", row[1], "\t|", row[2], "\t\t|", row[3],
                "\t\t|", row[4], "\t\t|", row[5], "|", row[6], "\t\t|", row[7],
                "\t\t|", row[8], "\t\t|", row[9])
        i += 1

    return cur
question4()

#----- Q5. Show the names of the five cheapest products 
print('\n' + '-'*20 + "Question 5" + '-'*20)
def question5():
    statement = "SELECT ProductName "
    statement += "FROM Product "
    statement += "ORDER BY UnitPrice "
    statement += "LIMIT 5"
    cur.execute(statement)

    print("Top5 cheapest products:")
    for row in cur:
        print("\t", row[0])
    
    return cur
question5()

#----- Q6. Show the names and number of units in stock of all products that have more than 100 units in stock  
print('\n' + '-'*20 + "Question 6" + '-'*20)
def question6():
    statement = "SELECT ProductName, UnitsInStock "
    statement += "FROM Product "
    statement += "WHERE UnitsInStock > 100"
    cur.execute(statement)

    print("Name\t\t\t\t| In stock")
    print("-"*43)
    i = 0
    for row in cur:
        if i == 0:
            print(row[0], "\t|", row[1])
        elif i == 1 or i == 5 or i == 9:
            print(row[0], "\t\t|", row[1])
        else:
            print(row[0], "\t\t\t|", row[1])
        i += 1
    
    return cur
question6()

#----- Q7. Show all column names in the Order table 
print('\n' + '-'*20 + "Question 7" + '-'*20)
def question7():
    statement = "SELECT * FROM [Order] LIMIT 0"
    cur.execute(statement)

    print("Column names in the Order table:")
    for column in cur.description:
        print("\t", column[0])
    
    return cur
question7()

#----- Q8. Show the names of all customers who lives in USA and have a fax number on record.
print('\n' + '-'*20 + "Question 8" + '-'*20)
def question8():
    statement = "SELECT CompanyName "
    statement += "FROM Customer "
    statement += "WHERE Country = 'USA' AND Fax IS NOT NULL"
    cur.execute(statement)

    print("Customers from the US with fax number:")
    for row in cur:
        print("\t", row[0])

    return cur
question8()

#----- Q9. Show the names of all the products, if any, that requires a reorder. 
# (If the units in stock of a product is lower than its reorder level but there's no units of the product currently on order, the product requires a reorder) 
print('\n' + '-'*20 + "Question 9" + '-'*20)
def question9():
    statement = "SELECT ProductName "
    statement += "FROM Product "
    statement += "WHERE UnitsInStock < ReorderLevel AND UnitsOnOrder = 0"
    cur.execute(statement)

    print("Product(s) that require a reorder:")
    for row in cur:
        print("\t", row[0])

    return cur
question9()

#----- Q10. Show ids of all the orders that ship to France where postal code starts with "44"
print('\n' + '-'*20 + "Question 10" + '-'*20)
def question10():
    statement = "SELECT Id "
    statement += "FROM [Order] "
    statement += "WHERE ShipCountry = 'France' AND ShipPostalCode LIKE '44%'"
    cur.execute(statement)

    print("IDs of orders shipped to France with postal code starting with 44:")
    for row in cur:
        print("\t", row[0])

    print('\n')
    return cur
question10()

conn.close()