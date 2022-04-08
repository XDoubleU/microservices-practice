import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        host="host.docker.internal",
        database="microservices_db",
        port=6543,
        user="postgres",
        password="example")


def get_orders():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM public.orders ORDER BY id ASC")
    orders = cur.fetchall()
    cur.close()
    conn.close()
    return orders

def get_order(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""SELECT * FROM public.orders WHERE id = %s 
    INNER JOIN public.orders_products ON public.orders.id == public.orders_products.order_id""", (id,))
    order = cur.fetchone()
    cur.close()
    conn.close()
    return order

def add_order(customer_id, product_amount_array):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("INSERT INTO public.orders (customer_id) VALUES (%s)  RETURNING *", (customer_id,))
    conn.commit()
    order = cur.fetchone()

    for x in product_amount_array:
        cur.execute("INSERT INTO public.orders_products (order_id, product_id, amount) VALUES (%s, %s, %s)", (order['id'], x['product_id'], x['amount']))
        conn.commit()

    cur.close()
    conn.close()
    return order