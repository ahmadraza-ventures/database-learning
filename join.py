import mysql.connector

# Connect to MySQL Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ahmadraza1122",  
    database="join"      
)

# Check connection
if mydb.is_connected():
    print("Connected to MySQL Database")

# Create cursor
mycursor = mydb.cursor()

# SQL JOIN Query
sql = """
SELECT
    customers.id,
    customers.name,
    customers.city,
    orders.order_id,
    orders.product
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
"""

# Execute query
mycursor.execute(sql)

# Fetch all records
result = mycursor.fetchall()

# Display results
print("\nCustomers and Their Orders:\n")

for row in result:
    print(f"Customer ID : {row[0]}")
    print(f"Name        : {row[1]}")
    print(f"City        : {row[2]}")
    print(f"Order ID    : {row[3]}")
    print(f"Product     : {row[4]}")
    print("-" * 30)

# Close connection
mycursor.close()
mydb.close()

print("Connection Closed")