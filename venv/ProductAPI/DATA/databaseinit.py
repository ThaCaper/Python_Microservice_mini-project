import sqlite3

CREATE_PRODUCT_TABLE = """CREATE TABLE IF NOT EXIST Product 
         (Id INT PRIMARY KEY     NOT NULL,
         NAME           NVCHAR(MAX)    NOT NULL,
         Price          INT     NOT NULL,
         ItemsInStock   INT,
         ItemsReserved  INT);"""

def connect():
    return sqlite3.connect("Product.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_PRODUCT_TABLE)
