import requests

def get_all_customers():
    r = requests.get('http://host.docker.internal:4020')
    return r.json()

def add_customer(firstname, lastname):
    r = requests.post('http://host.docker.internal:4020', json={"firstname": firstname, "lastname": lastname})
    return r.json()