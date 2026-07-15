# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

import mysql.connector

try:
    # Connect to MySQL Server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"   # Replace with your MySQL password
    )

    # Create a cursor object
    cursor = conn.cursor()

    # SQL query to create a database
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")

    print("Database 'student_db' created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection closed.")