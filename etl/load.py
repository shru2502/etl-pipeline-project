from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values

def get_postgres_connection(dbname: str, user: str, password: str, host: str = "localhost", port: str = "5432"):
    """
    Establishes a connection to the PostgreSQL database.

    Args:
        dbname (str): Database name.
        user (str): Username.
        password (str): Password.
        host (str): Host address.
        port (str): Port number.

    Returns:
        connection: PostgreSQL connection object.
    """
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn

def load_data(conn, table: str, data: List[Dict]):
    """
    Loads data into a specified PostgreSQL table.

    Args:
        conn: PostgreSQL connection object.
        table (str): Target table name.
        data (List[Dict]): Data to be inserted.
    """
    if not data:
        return
    
    columns = data[0].keys()
    values = [[record[col] for col in columns] for record in data]
    
    insert_query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES %s ON CONFLICT (id) DO NOTHING"
    
    with conn.cursor() as cur:
        execute_values(cur, insert_query, values)
    conn.commit()