import requests

def update_product_stock(product_id, used):
    r = requests.patch('http://0.0.0.0:4002/' + str(product_id), json={"used": used})
    return r.json()