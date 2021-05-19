from flask import Flask
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


@productapp.route('/', methods='POST', '')
def index():
    return "Hello World"

if __name__ == "__main__":
    productapp.run(debug=True)