# !/usr/bin/python

import sqlite3


conn = sqlite3.connect('ORDERSDB.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE ORDERS
         (OrderId INT PRIMARY KEY     NOT NULL,
         Date           DATE    NOT NULL,
         ProductID            INT     NOT NULL,
         Quantity        int
         );''')
print("Table created successfully");

conn.execute("INSERT INTO ORDERS (OrderId,Date,ProductID,Quantity) \
      VALUES (1, 2008-11-11, 1, 2 )");

conn.execute("INSERT INTO ORDERS (OrderId,Date,ProductID,Quantity) \
      VALUES (2, 2008-9-8, 2, 5 )");

conn.commit()
conn.close()
