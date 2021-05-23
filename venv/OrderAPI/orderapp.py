from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
import json
import datetime


orderapp = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swaggerOrder.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "OrderAPI Microservice Mini Project"
    }
)
orderapp.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('order.db', detect_types=sqlite3.PARSE_DECLTYPES)
    except sqlite3.error as e:
        print(e)
    return conn


@orderapp.route('/orders', methods=['POST', 'GET'])
def order():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM Orders")
        orders = [
            dict(id=row[0], date=row[1], productId=row[2], quantity=row[3])
            for row in cursor.fetchall()
        ]
        if orders is not None:
            return jsonify(orders)

    if request.method == 'POST':
        new_date = datetime.datetime.now()
        new_product_id = request.json["productId"]
        new_quantity = request.json["quantity"]
        sql_insert_query = """INSERT INTO Orders (date, productId, quantity)
                              VALUES (?, ?, ?)"""

        cur = cursor.execute(sql_insert_query, (new_date, new_product_id, new_quantity))
        conn.commit()
        return f"orders with the id: {cur.lastrowid} created successfully", 201


@orderapp.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_order(id):
    conn = db_connection()
    cursor = conn.cursor()
    order = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM Orders WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            order = r
        if order is not None:
            return jsonify(order), 200
        else:
            return "Something went wrong", 404

    if request.method == 'PUT':
        sql_update_order = """UPDATE Orders 
                                SET date=?,
                                    productId=?,
                                    quantity=?
                                WHERE id=?"""
        date = datetime.datetime.now()
        product_id = int(request.json["productId"])
        quantity = int(request.json["quantity"])

        updated_order = {
            'id': id,
            'date': date,
            'productId': product_id,
            'quantity': quantity,
        }
        conn.execute(sql_update_order, (date, product_id, quantity, id))
        conn.commit()
        return jsonify(updated_order)

    if request.method == 'DELETE':
        sql_delete_order = """DELETE FROM Orders WHERE id=?"""
        conn.execute(sql_delete_order, (id,))
        conn.commit()
        return "The order with the id: {} has been deleted.".format(id), 200


if __name__ == "__main__":
    orderapp.run(debug=True)
