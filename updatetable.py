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
sql = "UPDATE customers SET city = %s WHERE city = %s"
value = ("Islamabad", "Lahore")

# Execute query
mycursor.execute(sql, value)

# Save changes
mydb.commit()

print(mycursor.rowcount, "record(s) updated")