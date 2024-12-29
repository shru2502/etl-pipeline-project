# etl/load.py
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values
from . import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT  # Import PostgreSQL config

def get_postgres_connection() -> psycopg2.extensions.connection:
    """
    Establishes a connection to the PostgreSQL database using credentials from the config.

    Returns:
        connection: PostgreSQL connection object.
    """
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
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
