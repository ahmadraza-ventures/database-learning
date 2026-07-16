import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="mydatabase"
)

# Create cursor
mycursor = mydb.cursor()

# SQL query
sql = "SELECT * FROM customers LIMIT 5"

# Execute query
mycursor.execute(sql)

# Fetch records
result = mycursor.fetchall()

# Print records
for row in result:
    print(row)