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
├── tests/                  # Unit tests for the ETL pipeline
├── requirements.txt        # Python libraries required for the project
├── README.md               # Documentation for the project
└── Dockerfile              # Dockerfile (optional, for deployment)


### 1. Create Virtual environment
    - Navigate to your desired project directory and create the virtual environment
	python -m venv etl_env
    For Windows : etl_env\Scripts\activate
    For Mac/Linux : source etl_env/bin/activate

    - Upgrade pip and install essential libraries
    pip install --upgrade pip
    pip install pymongo pandas psycopg2 sqlalchemy

