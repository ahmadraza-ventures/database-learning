import psycopg2
import tensorflow as tf
import numpy as np
import math


connection = psycopg2.connect(
    host="localhost",
    database="product_store",
    user="postgres",
    password="ahmad@1122"
)


cursor = connection.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100)
)
""")

connection.commit()

# Create UNIQUE INDEX
cursor.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS idx_product_name
ON products(product_name);
""")

connection.commit()

# Insert Data
cursor.execute("""
INSERT INTO products VALUES
(1,'Laptop','Electronics'),
(2,'Smartphone','Electronics'),
(3,'Headphones','Electronics'),
(4,'Office Chair','Furniture'),
(5,'Study Table','Furniture')
ON CONFLICT (id) DO NOTHING;
""")

connection.commit()

# Retrieve All Products
cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

# Store Product Names in a Python List
product_names = []

for product in products:
    product_names.append(product[1])

# Print Product Name with Category
for product in products:
    print("Product Name:", product[1])
    print("Category:", product[2])
    print()

print(products)

# Create a TensorFlow Embedding layer with:

embedding_layer = tf.keras.layers.Embedding(
    input_dim=5,
    output_dim=4
)

# Convert the product indices into embedding vectors

indices = np.array([0, 1, 2, 3, 4])
embedding_vectors = embedding_layer(indices)


# Print the embedding vector for every product.

print(product_names[0])
print(embedding_vectors[0].numpy())
print()

print(product_names[1])
print(embedding_vectors[1].numpy())
print()

print(product_names[2])
print(embedding_vectors[2].numpy())
print()

print(product_names[3])
print(embedding_vectors[3].numpy())
print()

print(product_names[4])
print(embedding_vectors[4].numpy())
print()


# Euclidean distance hm na math.dist sa kia ha 
laptop = embedding_vectors[0].numpy()
smartphone = embedding_vectors[1].numpy()
office_chair = embedding_vectors[3].numpy()


# Calculate the Euclidean distance between Laptop and Smartphone.
distance1 = math.dist(laptop, smartphone)
print("Euclidean Distance (Laptop and Smartphone):", distance1)


# Calculate the Euclidean distance between Laptop and Office Chair.
distance2 = math.dist(laptop, office_chair)
print("Euclidean Distance (Laptop and  Office Chair):", distance2)


# conddition
if distance1 < distance2:
    print("Smartphone is closer to Laptop.")
else:
    print("Office Chair is closer to Laptop.")



# Insert a new product named Tablet with the category Electronics

cursor.execute("""
INSERT INTO products (id, product_name, category)
VALUES (6, 'Tablet', 'Electronics')
       ON CONFLICT (id) DO NOTHING;
""")

# connection.commit()
# print("Tablet inserted successfully.")



# Retrieve and print the updated product lis
cursor.execute("SELECT * FROM products")
updated_products = cursor.fetchall()
print("\nUpdated Product List:\n")


for product in updated_products:
    print(product)

connection.commit()

print("Tablet inserted successfully.")

# Close the PostgreSQL cursor and database connection properly.
cursor.close()
connection.close()

print("PostgreSQL cursor and database connection closed successfully.")

