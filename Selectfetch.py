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

# Execute SELECT query
mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT name, city FROM customers")


# Fetch all records
result = mycursor.fetchall()
result = mycursor.fetchall()


# Print records
for row in result:
    print(row)