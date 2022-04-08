from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_products():
    return jsonify(db.get_products())

@app.route("/<id>", methods=['GET'])
def get_product(id):
    return jsonify(db.get_product(id))

@app.route("/<id>", methods=['PATCH'])
def update_product_stock(id):
    json = request.json
    return jsonify(db.update_product_stock(id, json['used']))

@app.route("/", methods=['POST'])
def add_product():
    json = request.json
    return jsonify(db.add_product(json['name'], json['price'], json['stock']))

