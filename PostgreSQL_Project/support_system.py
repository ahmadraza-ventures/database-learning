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







 

