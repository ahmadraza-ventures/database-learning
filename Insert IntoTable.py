import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost", 
    user="root",
      password="your_password", 
      database="studentdb" )

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age, city) VALUES (%s, %s, %s)"
data = [ ("Ali", 20, "Karachi"),
         ("Sara", 21, "Islamabad"), 
         ("Ayesha", 23, "Faisalabad") ]



mycursor.execute(sql, data)

mydb.commit()

print(mycursor.rowcount, "records inserted successfully!")