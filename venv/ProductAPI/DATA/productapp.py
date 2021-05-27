from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
import json
import pika

productapp = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ProductAPI Microservice Mini Project"
    }
)


productapp.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###




def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('product.db')
    except sqlite3.error as e:
        print(e)
    return conn

@productapp.route('/products', methods=['POST', 'GET'])
def product():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM Product")
        products = [
            dict(id=row[0], name=row[1], price=row[2], itemInStock=row[3], itemsReserved=row[4])
            for row in cursor.fetchall()
        ]
        if products is not None:
            return jsonify(products)

    if request.method == 'POST':
        new_name = request.json["name"]
        new_price = request.json["price"]
        new_itemsInStock = request.json["itemsInStock"]
        new_itemsReserved = request.json["itemsReserved"]
        sql_insert_query = """INSERT INTO Product (name, price, itemsInStock, itemsReserved)
                              VALUES (?, ?, ?, ?)"""
        cur = cursor.execute(sql_insert_query, (new_name, new_price, new_itemsInStock, new_itemsReserved))
        conn.commit()
        return f"Product with the id: {cur.lastrowid} created successfully", 201

@productapp.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_product(id):
    conn = db_connection()
    cursor = conn.cursor()
    product = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM Product WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            product = r
        if product is not None:
            return jsonify(product), 200
        else:
            return "Something went wrong", 404

    if request.method == 'PUT':
        sql_update_product = """UPDATE Product 
                                SET name=?,
                                    price=?,
                                    itemsInStock=?,
                                    itemsReserved=?
                                WHERE id=?"""
        name = request.json["name"]
        price = request.json["price"]
        itemsInStock = request.json["itemsInStock"]
        itemsReserved = request.json["itemsReserved"]
        updated_product = {
            'id': id,
            'name': name,
            'price': price,
            'itemsInStock': itemsInStock,
            'itemsReserved': itemsReserved
            }
        conn.execute(sql_update_product, (name, price, itemsInStock, itemsReserved, id))
        conn.commit()
        return jsonify(updated_product)

    if request.method == 'DELETE':
        sql_delete_product = """DELETE FROM Product WHERE id=?"""
        conn.execute(sql_delete_product, (id,))
        conn.commit()
        return "The Product with the id: {} has been deleted.".format(id), 200





@productapp.route('/products/check/<int:prodid>/<int:amount>', methods=['GET'])
def check_product(prodid, amount):
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM Product where id ="+ str(prodid))
    rows = cursor.fetchone()
    instock = rows[3]
    if instock > amount:
        return "true"
    else:
        return "false"


if __name__ == "__main__":
    productapp.run(port=5000, host="0.0.0.0")