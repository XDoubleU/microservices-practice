import requests, json

def update_product_stock(product_id, used):
    r = requests.patch('http://host.docker.internal:4010/' + str(product_id), data=json.dumps({"used": used}))
    return r.json()