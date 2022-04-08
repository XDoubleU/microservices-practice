import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        host="host.docker.internal",
        database="microservices_db",
        port=6543,
        user="postgres",
        password="example")


def get_products():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM public.products ORDER BY id ASC")
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def get_product(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM public.products WHERE id = %s", (id,))
    product = cur.fetchone()
    cur.close()
    conn.close()
    return product

def add_product(name, price, stock):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("INSERT INTO public.products (name, price, stock) VALUES (%s, %s, %s) RETURNING *", (name, price, stock))
    conn.commit()
    product = cur.fetchone()
    cur.close()
    conn.close()
    return product

def update_product_stock(id, used):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE public.products SET stock = stock - %s WHERE id = %s RETURNING *", (used,id,))
    conn.commit()
    product = cur.fetchone()
    cur.close()
    conn.close()
    return product