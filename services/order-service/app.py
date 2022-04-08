from flask import Flask, jsonify, request
import db
import customer_service, product_service

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_orders():
    return jsonify(db.get_orders())

@app.route("/<id>", methods=['GET'])
def get_order(id):
    return jsonify(db.get_order(id))

@app.route("/", methods=['POST'])
def add_order():
    json = request.json

    customers = customer_service.get_all_customers()
    customer = None

    for x in customers:
        if(x['firstname'] == json['firstname'] and x['lastname'] == json['lastname']):
            customer = x

    if customer is None:
        customer = customer_service.add(json['firstname'], json['lastname'])

    for x in json['products']:
        product_service.update_product_stock(x['product_id'], x['amount'])

    return jsonify(db.add_order(customer['id'], json['products']))
