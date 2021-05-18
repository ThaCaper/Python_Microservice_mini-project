import sqlite3

conn = sqlite3.connect('order.db')

conn.execute('''CREATE TABLE Order
         (ID INT PRIMARY KEY     NOT NULL,
         Date           Date    NOT NULL,
         Productid         INT     NOT NULL,
         Quantity        INT
         );''')

print("Opened database successfully")

