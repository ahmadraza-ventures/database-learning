import psycopg2
import pandas
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
 