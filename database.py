import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_order_system"
)

cursor = conn.cursor()