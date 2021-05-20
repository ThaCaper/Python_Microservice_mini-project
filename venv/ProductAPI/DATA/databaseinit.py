import sqlite3

CREATE_PRODUCT_TABLE = """CREATE TABLE Product 
         (id integer PRIMARY KEY NOT NULL,
         name text NOT NULL,
         price integer NOT NULL,
         itemsInStock integer NOT NULL,
         itemsReserved integer NOT NULL)"""

conn = sqlite3.connect("product.db")

cursor = conn.cursor()

cursor.execute(CREATE_PRODUCT_TABLE)

