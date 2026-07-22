import psycopg2
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt



connection = psycopg2.connect(
    host="localhost",
    database="support_system",
    user="postgres",
    password="ahmad@1122"
)
cursor = connection.cursor()
print(" Database Connected Successfully!")

# Create a table named tickets with the following columns:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(
    id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    category VARCHAR(100),
    priority VARCHAR(20),
    resolution_time INT
)
""")

connection.commit()

# Insert the following records:
cursor.execute("""
INSERT INTO tickets
(id, customer_name, category, priority, resolution_time)
VALUES
(1,'Ali','Login Issue','High',5),
(2,'Sara','Payment Issue','High',8),
(3,'John','Login Issue','Medium',4),
(4,'Emma','App Crash','High',12),
(5,'David','Payment Issue','Low',6),
(6,'Ahmed','App Crash','Medium',10)
ON CONFLICT (id) DO NOTHING;
""")

connection.commit()

# Retrieve all records from the tickets table.
cursor.execute("SELECT * FROM tickets")
records = cursor.fetchall()


# Convert the retrieved records into a Pandas DataFrame.
df = pd.read_sql_query(
    "SELECT * FROM tickets",connection
)
print(df)


# Check whether the DataFrame contains any missing values.
print(df.isnull().sum())



# Calculate and print the average resolution time for each ticket category.
average_time = df.groupby("category")["resolution_time"].mean()
print(average_time)


# Find and print the ticket with the highest resolution time.
cursor.execute("""
SELECT *
FROM tickets
ORDER BY resolution_time DESC
LIMIT 1;
""")

highest_ticket = cursor.fetchone()

print("Ticket with Highest Resolution Time:")
print(highest_ticket)




# Convert each unique ticket category into an integer index.
# hmm na sql sa panadda library sa kia ha 

category_df = pd.read_sql_query("""
SELECT
    id,
    customer_name,
    category,
    CASE
        WHEN category = 'Login Issue' THEN 0
        WHEN category = 'Payment Issue' THEN 1
        WHEN category = 'App Crash' THEN 2
              ELSE 3                   
    END AS category_index
FROM tickets;
""", connection)

print(category_df)

# Create a TensorFlow embedding layer using:

number_of_unique_categories = 4

embedding_layer = tf.keras.layers.Embedding(
    input_dim=number_of_unique_categories,
    output_dim=4
)




# Category indices ko NumPy array mein convert karo
category_indices = np.array(category_df["category_index"])

# TensorFlow tensor mein convert karo
category_indices = tf.constant(category_indices)

# Embedding vectors generate karo
embedding_vectors = embedding_layer(category_indices)

# NumPy array mein convert karo
embedding_vectors = embedding_vectors.numpy()

print("Embedding Vectors:")
print(embedding_vectors)


# Add each generated embedding vector to the DataFrame.

category_df["Embedding_1"] = embedding_vectors[:, 0]
category_df["Embedding_2"] = embedding_vectors[:, 1]
category_df["Embedding_3"] = embedding_vectors[:, 2]
category_df["Embedding_4"] = embedding_vectors[:, 3]

print(category_df)



# Ticket 1 aur Ticket 3 ki similarity direct calculate karo
similarity = cosine_similarity(
    [embedding_vectors[0]],
    [embedding_vectors[2]]
)

print("Cosine Similarity:", similarity[0][0])

# given conditoin
if similarity[0][0] > 0.8:
    print("The tickets are similar.")
else:
    print("The tickets are not similar.")



# Use NumPy to calculate the average resolution time of all tickets.
average_resolution_time = np.average(df["resolution_time"])
print("Average resolution time : ", average_resolution_time)




# Display a bar chart using Matplotlib showing:
# Ticket categories on the x-axis
# Average resolution time on the y-axis

categories = np.array(["Login Issue", "Payment Issue", "App Crash"])
average_time = np.array([4.5, 7.0, 11.0])

plt.bar(categories, average_time)

plt.xlabel("Ticket Categories")
plt.ylabel("Average Resolution Time")
plt.title("Average Resolution Time of Ticket Categories")
plt.show()


# Ask the user to enter a priority level such as High, Medium, or Low.
priority = input("Enter the priority level (High, Medium, Low): ")
print("Priority Level:", priority)


# retrieve and display only the tickets matching that priority.


cursor.execute("""
SELECT * FROM tickets
WHERE priority = %s;
""", (priority,))

tickets = cursor.fetchall()

for ticket in tickets:
    print(ticket)


# Insert a new ticket into PostgreSQL using values entered by the user.
# User se values lo
ticket_id = int(input("Enter Ticket ID: "))
customer_name = input("Enter Customer Name: ")
category = input("Enter Category: ")
priority = input("Enter Priority (High/Medium/Low): ")
resolution_time = int(input("Enter Resolution Time: "))

# Database mein insert karo
cursor.execute("""
INSERT INTO tickets
(id, customer_name, category, priority, resolution_time)
VALUES (%s, %s, %s, %s, %s);
""", (ticket_id, customer_name, category, priority, resolution_time))

connection.commit()
print("Ticket inserted successfully!")



# Retrieve and display the updated ticket list.
updated_df = pd.read_sql_query("SELECT * FROM tickets;", connection)
print(updated_df)


# Update the priority of one selected ticket.
ticket_id = int(input("Enter Ticket ID: "))
priority = input("Enter New Priority: ")

query = "UPDATE tickets SET priority=%s WHERE id=%s"

cursor.execute(query, (priority, ticket_id))
connection.commit()

print("Updated!")




# Delete a ticket by its ID.
ticket_id = int(input("Enter Ticket ID to delete: "))

cursor.execute("""
DELETE FROM tickets
WHERE id = %s;
""", (ticket_id,))

connection.commit()

print("Ticket deleted successfully!")


#  Close the PostgreSQL cursor and connection properly.
cursor.close()
connection.close()

print("PostgreSQL cursor and connection closed successfully!")
