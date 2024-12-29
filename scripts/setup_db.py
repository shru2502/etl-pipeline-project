import psycopg2
from psycopg2 import sql

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS clients (
            id VARCHAR(24) PRIMARY KEY,
            name VARCHAR(255),
            contact_info TEXT
            -- Add other relevant fields
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS suppliers (
            id VARCHAR(24) PRIMARY KEY,
            name VARCHAR(255),
            website VARCHAR(255)
            -- Add other relevant fields
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS sonar_runs (
            id VARCHAR(24) PRIMARY KEY,
            client_id VARCHAR(24) REFERENCES clients(id),
            run_date TIMESTAMP
            -- Add other relevant fields
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS sonar_results (
            id VARCHAR(24) PRIMARY KEY,
            sonar_run_id VARCHAR(24) REFERENCES sonar_runs(id),
            part_id VARCHAR(255),
            supplier_id VARCHAR(24) REFERENCES suppliers(id),
            price NUMERIC,
            lead_time INTEGER,
            timestamp TIMESTAMP
            -- Add other relevant fields
        )
        """
    )
    
    conn = None
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="MarktPilotDB",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        # Create tables
        for command in commands:
            cur.execute(command)
        # Commit changes
        conn.commit()
        cur.close()
        print("Tables created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()
