from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

#
#Add all the REST API end-points here
#

@app.route("/products", methods=['GET'])
def get_products():
    return jsonify(products)

@app.route("/products/<id>", methods=['GET'])
def get_product(id):
    id = int(id)
    for product in products:
        if product['id'] == id:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route("/products", methods=['POST'])
def add_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product), 201

@app.route("/products/<id>", methods=['PUT'])
def update_product(id):
    id = int(id)
    update_product = json.loads(request.data)
    product = [x for x in products if x['id'] == id][0]
    for key, value in update_product.items():
        product[key] = value
    return '', 204

@app.route("/products/<id>", methods=['DELETE'])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x['id'] == id][0]
    products.remove(product)
    return '', 204

app.run(port=5000,debug=True)
