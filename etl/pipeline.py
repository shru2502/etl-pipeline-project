# etl/pipeline.py
from etl.extract import get_mongo_client, extract_collection
from etl.transform import (
    transform_clients,
    transform_suppliers,
    transform_sonar_runs,
    transform_sonar_results
)
from etl.load import get_postgres_connection, load_data
from __init__ import MONGO_URI, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT

def run_etl():
    # MongoDB connection
    mongo_client = get_mongo_client(MONGO_URI)
    db_name = "markt_pilot"
    
    # Extract
    clients = extract_collection(mongo_client, db_name, "clients")
    suppliers = extract_collection(mongo_client, db_name, "suppliers")
    sonar_runs = extract_collection(mongo_client, db_name, "sonar_runs")
    sonar_results = extract_collection(mongo_client, db_name, "sonar_results")
    
    # Transform
    transformed_clients = transform_clients(clients)
    transformed_suppliers = transform_suppliers(suppliers)
    transformed_sonar_runs = transform_sonar_runs(sonar_runs)
    transformed_sonar_results = transform_sonar_results(sonar_results)
    
    # Load
    postgres_conn = get_postgres_connection()
    
    load_data(postgres_conn, "clients", transformed_clients)
    load_data(postgres_conn, "suppliers", transformed_suppliers)
    load_data(postgres_conn, "sonar_runs", transformed_sonar_runs)
    load_data(postgres_conn, "sonar_results", transformed_sonar_results)
    
    postgres_conn.close()
    mongo_client.close()
    print("ETL process completed successfully.")

if __name__ == "__main__":
    run_etl()