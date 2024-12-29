from pymongo import MongoClient
from typing import dict, List

def get_mongo_client(uri: str = "mongodb://localhost:27017/") -> MongoClient:
    """
    Establishes a connection to the MongoDB server.

    Args:
        uri (str): MongoDB connection string.

    Returns:
        MongoClient: MongoDB client instance.
    """
    client = MongoClient(uri)
    return client

def extract_collection(client: MongoClient, db_name: str, collection_name: str) -> List[dict]:
    """
    Extracts all documents from a specified MongoDB collection.

    Args:
        client (MongoClient): MongoDB client instance.
        db_name (str): Name of the database.
        collection_name (str): Name of the collection.

    Returns:
        List[dict]: List of documents.
    """
    db = client[db_name]
    collection = db[collection_name]
    documents = list(collection.find())
    return documents