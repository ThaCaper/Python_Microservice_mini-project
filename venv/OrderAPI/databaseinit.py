import sqlite3
import datetime

conn = sqlite3.connect('order.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE Orders
         (id INTEGER PRIMARY KEY NOT NULL,
         date timestamp,
         productId INTEGER NOT NULL,
         quantity INTEGER NOT NULL
         );''')
print("Table created successfully")


conn.commit()
