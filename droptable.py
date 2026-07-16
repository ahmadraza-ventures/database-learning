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
sql = "DROP TABLE customers"

# Execute query
mycursor.execute(sql)

print("Table dropped successfully")