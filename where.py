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


# Execute SELECT with WHERE
sql = "SELECT * FROM customers WHERE city = 'Lahore'"
mycursor.execute(sql)

# Fetch records
result = mycursor.fetchall()

# Print records
for row in result:
    print(row)