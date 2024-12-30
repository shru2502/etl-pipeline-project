# MARKT-PILOT Data Engineering Challenge: ETL Pipeline
# This project implements an ETL pipeline to process MongoDB collections and transform them into a relational database schema for analytical queries.

MarktPilot/
├── etl_env/                # Virtual environment (auto-created, do not modify)
├── data/collections.zip/                   # Raw JSON data files
│   ├── clients.json
│   ├── suppliers.json
│   ├── sonar_runs.json
│   └── sonar_results.json
├── etl/                    # Source code folder
|   ├── __init__.py		  # Load environment variables from .env file
│   ├── extract.py          # Code to extract data from MongoDB
│   ├── transform.py        # Code to transform data using pandas
│   ├── load.py             # Code to load data into PostgreSQL
│   └── pipeline.py         # Entry point for the ETL process
├── scripts/	
|    ├── setup_db.py		  # Connect postgres DB and create tables
├── tests/
|    ├── test_etl_pipeline.py    # Unit tests for the ETL pipeline
├── .env
├── .gitignore
├── requirements.txt        # Python libraries required for the project
├── README.md               # Documentation for the project


## Prerequisites
- **Python** 3.8+
- **MongoDB**: To import the JSON collections.
- **PostgreSQL**: To store the transformed data.
- Required Python libraries listed in `requirements.txt`.

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>
    
   - Initialize Git Repository: git init
   - Create a .gitignore file to exclude unnecessary files from Git tracking: touch .gitignore
   - After creating project structure, 
	1. git add .
	2. git commit -m "Initial project setup with virtual environment and dependencies"

2. Install Dependencies:
pip install -r requirements.txt

3. Database Setup:
   - Create database for MongoDB for importing raw json files into collections.
   - Set up a new database in PostgreSQL for storing the transformed data.
   - Create .env file to store credentials securely.

4. Import the raw JSON files into MongoDB collections

mongoimport --db markt_pilot --collection clients --file data/collections/clients.json --jsonArray
mongoimport --db markt_pilot --collection suppliers --file data/collections/suppliers.json --jsonArray
mongoimport --db markt_pilot --collection sonar_runs --file data/collections/sonar_runs.json --jsonArray
mongoimport --db markt_pilot --collection sonar_results --file data/collections/sonar_results.json --jsonArray

5. Database Setup Script
Before running the ETL pipeline, set up the PostgreSQL database and create tables. Run the below script:

python scripts/setup_db.py	#This will create the necessary tables in your PostgreSQL database

6. Run ETL scripts
   - Extraction: Data is extracted from MongoDB collections using pymongo.
		 Collections include - clients, suppliers, sonar_runs, sonar_results
		 etl/extract.py
   - Transformation: Data transformations are performed to normalize and join data across collections.
		     Transformations ensure the relational schema is suitable for analytics.
		     etl/transform.py
   - Loading: Transformed data is loaded into PostgreSQL tables using SQLAlchemy
	      Tables include - clients, suppliers, sonar_runs, sonar_results
	      etl/load.py
   - Execution: Entry point of the pipeline.
	        Establish connection to MongoDB and start ETL process.
	        After successful execution, tables get populated with the data.
		etl/pipeline.py

To run ETL script : python etl/pipeline.py

This script will:

- Extract data from MongoDB.
- Transform it to fit the PostgreSQL schema.
- Load it into PostgreSQL.

7. Testing the Pipeline

Run below script to test the code
python -m unittest -v tests/test_etl_pipeline.py 

