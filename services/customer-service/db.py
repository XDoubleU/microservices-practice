import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        host="host.docker.internal",
        database="microservices_db",
        port=6543,
        user="postgres",
        password="example")


def get_customers():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM public.customers ORDER BY id ASC")
    customers = cur.fetchall()
    cur.close()
    conn.close()
    return customers

def get_customer(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM public.customers WHERE id = %s", (id,))
    customer = cur.fetchone()
    cur.close()
    conn.close()
    return customer

def add_customer(firstname, lastname):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("INSERT INTO public.customers (firstname, lastname) VALUES (%s, %s) RETURNING *", (firstname, lastname))
    conn.commit()
    customer = cur.fetchone()
    cur.close()
    conn.close()
    return customer