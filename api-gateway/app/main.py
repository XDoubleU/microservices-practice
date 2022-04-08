from fastapi import FastAPI, Request
import requests, json

app = FastAPI()


@app.get("/products")
async def get_products():
    return requests.get('http://host.docker.internal:4010').json()

@app.get("/products/{product_id}")
async def get_product(product_id):
    return requests.get('http://host.docker.internal:4010/' + str(product_id)).json()

@app.post("/products")
async def add_product(request: Request):
    data = await request.json()
    return requests.post('http://host.docker.internal:4010', json=data).json()

@app.get("/customers")
async def get_customers():
    return requests.get('http://host.docker.internal:4020').json()

@app.get("/customers/{customer_id}")
async def get_customer(customer_id):
    return requests.get('http://host.docker.internal:4020/' + str(customer_id)).json()

@app.get("/orders")
async def get_orders():
    return requests.get('http://host.docker.internal:4030').json()

@app.get("/orders/{order_id}")
async def get_order(order_id):
    return requests.get('http://host.docker.internal:4030/' + str(order_id)).json()

@app.post("/orders")
async def add_order(request: Request):
    data = await request.json()
    return requests.post('http://host.docker.internal:4030', json=data).json()