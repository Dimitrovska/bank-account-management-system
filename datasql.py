import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",         # mysql username
    password="", # празна парола
    database="bank_db"    # името на базата данни
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table")
results = cursor.fetchall()
print(results)

conn.close()
