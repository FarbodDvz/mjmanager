from db.connection import get_connection
import os

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    BASE_DIR = os.path.dirname(__file__)
    sql_path = os.path.join(BASE_DIR,"sql")

    with open(os.path.join(sql_path,"create_tables.sql"),"r") as f:
        query = f.read()
        cursor.executescript(query)
    conn.commit()
    conn.close()
