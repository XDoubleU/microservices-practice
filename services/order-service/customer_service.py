import requests

def get_all_customers():
    r = requests.get('http://localhost:4002')
    return r.json()

def add_customer(firstname, lastname):
    r = requests.post('http://localhost:4002', json={"firstname": firstname, "lastname": lastname})
    return r.json()