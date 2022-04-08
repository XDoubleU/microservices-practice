from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_customers():
    return jsonify(db.get_customers())

@app.route("/<id>", methods=['GET'])
def get_customer(id):
    return jsonify(db.get_customer(id))

@app.route("/", methods=['POST'])
def add_customer():
    json = request.json
    return jsonify(db.add_customer(json['firstname'], json['lastname']))
