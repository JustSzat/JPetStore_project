import mysql.connector

import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="myuser",
    password="mypass",
    database="jpetstore"
)

cursor = conn.cursor()
cursor.execute("SELECT @@hostname")
print(cursor.fetchone())

conn.close()