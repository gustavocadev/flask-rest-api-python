import uuid
from flask import Flask, request
from productsModule import products

app = Flask(__name__)


@app.route('/products')
def getProducts():
    return {
        'products': products
    }


@app.route('/products/<string:id>')
def getProduct(id):
    productFound = {}

    for product in products:
        if product['id'] == id:
            productFound = product
            break

    return {
        'product': productFound
    }


@app.route('/products', methods=['POST'])
def createProduct():
    newProduct = {
        'name': '',
        'price': 0,
        'id': str(uuid.uuid4())
    }

    newProduct['name'] = request.json['name']
    newProduct['price'] = request.json['price']

    products.append(newProduct)

    return {
        'product': newProduct
    }


@app.route('/products/<string:id>', methods=['PUT'])
def updateProduct(id):
    productFound = {}

    for product in products:
        if product['id'] == id:
            productFound = product
            break

    productFound['name'] = request.json['name']
    productFound['price'] = request.json['price']

    return {
        'product': productFound
    }


@app.route('/products/<string:id>', methods=['DELETE'])
def deleteProduct(id):
    productFound = {}

    for product in products:
        if product['id'] == id:
            productFound = product
            break

    products.remove(productFound)

    return {
        'product': productFound
    }


if __name__ == "__main__":
    app.run(debug=True, port=4000)
