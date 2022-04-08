from flask import Flask, jsonify, request
import db

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
    return jsonify(db.add_order(json['customer_id'], json['products']))