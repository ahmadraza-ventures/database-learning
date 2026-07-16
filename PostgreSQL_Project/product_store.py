import psycopg2
import tensorflow as tf
import numpy as np




connection = psycopg2.connect(
    host="localhost",
    database="product_store",
    user="postgres",
    password="ahmad@1122"
)

cursor = connection.cursor()

print("Database Connected Successfully!")