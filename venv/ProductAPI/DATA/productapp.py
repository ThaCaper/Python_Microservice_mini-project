from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

productapp = Flask(__name__)
productapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productsdb.db'
db = SQLAlchemy(productapp)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    itemsInStock = db.Column(db.Integer, nullable=False)
    itemsReserved = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

product_list = [
    {
        "id": 1,
        "name": "Hammer",
        "price": 100,
        "itemsInStock": 10,
        "itemsReserved": 0
    },
    {
        "id": 2,
        "name": "Screwdriver",
        "price": 70,
        "itemsInStock": 20,
        "itemsReserved": 0
    },
    {
        "id": 3,
        "name": "Drill",
        "price": 500,
        "itemsInStock": 2,
        "itemsReserved": 0
    }]



@productapp.route('/products', methods=['POST', 'GET'])
def product():
    if request.method == 'GET':
        if len(product_list) > 0:
            return jsonify(product_list)
        else:
            'Nothing found', 404
    if request.method == 'POST':
        new_name = request.form['name']
        new_price = request.form['price']
        new_itemsInStock = request.form['itemsInStock']
        new_itemsReserved = request.form['itemsReserved']
        iD = product_list[-1]['id']+1

        new_product = {
            'id': iD,
            'name': new_name,
            'price': new_price,
            'itemsInStock': new_itemsInStock,
            'itemsReserved': new_itemsReserved
        }
        product_list.append(new_product)
        return jsonify(product_list), 201

@productapp.route('/product/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_product(id):
    if request.method == 'GET':
        for product in product_list:
            if product['id'] == id:
                return jsonify(product)
            pass
    if request.method == 'PUT':
        for product in product_list:
            if product['id'] == id:
                product['name'] = request.form['name']
                product['price'] = request.form['price']
                product['itemsInStock'] = request.form['itemsInStock']
                product['itemsReserved'] = request.form['itemsReserved']
                updated_product = {
                    'id': id,
                    'name': product['name'],
                    'price': product['price'],
                    'itemsInStock': product['itemsInStock'],
                    'itemsReserved': product['itemsReserved']
                }
                return jsonify(updated_product)
    if request.method == 'DELETE':
        for index, product in enumerate(product_list):
            if product['id'] == id:
                product_list.pop(index)
                return jsonify(product_list)

if __name__ == "__main__":
    productapp.run(debug=True)