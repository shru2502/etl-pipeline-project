import unittest
from unittest.mock import MagicMock, patch
from etl.extract import get_mongo_client, extract_collection
from etl.transform import (
    transform_clients,
    transform_suppliers,
    transform_sonar_runs,
    transform_sonar_results
)

class TestETLPipeline(unittest.TestCase):

    @patch("etl.extract.MongoClient")
    def test_extract_collection(self, mock_mongo_client):
        # Mock MongoDB client and collection
        mock_db = MagicMock()
        mock_collection = MagicMock()
        
        # Mock the 'find' method to return the documents as a cursor
        mock_collection.find.return_value = iter([
            {"_id": "1", "name": "Client A", "contact_info": "info@example.com"},
            {"_id": "2", "name": "Client B", "contact_info": "contact@example.com"}
        ])
        
        # Configure the mock client to return our mock database when accessed
        mock_mongo_client.return_value.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection

        # Now test the extraction function
        client = get_mongo_client()  # This should use the mock MongoClient
        documents = extract_collection(client, "test_db", "clients")  # Should use the mock collection

        # Assert that the function returns the correct number of documents
        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[0]["name"], "Client A")
        self.assertEqual(documents[1]["name"], "Client B")

    def test_transform_clients(self):
        raw_data = [
            {"_id": "1", "name": "Client A", "contact_info": "info@example.com"},
            {"_id": "2", "name": "Client B", "contact_info": "contact@example.com"}
        ]

        transformed = transform_clients(raw_data)

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed[0]["id"], "1")
        self.assertEqual(transformed[0]["name"], "Client A")

    def test_transform_suppliers(self):
        raw_data = [
            {"_id": "1", "name": "Supplier A", "website": "http://example.com"},
            {"_id": "2", "name": "Supplier B", "website": "http://example.org"}
        ]

        transformed = transform_suppliers(raw_data)

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed[0]["id"], "1")
        self.assertEqual(transformed[0]["name"], "Supplier A")

    def test_transform_sonar_runs(self):
        raw_data = [
            {"_id": "1", "client_id": "100", "run_date": "2024-01-01T12:00:00Z"},
            {"_id": "2", "client_id": "200", "run_date": "2024-01-02T15:30:00Z"}
        ]

        transformed = transform_sonar_runs(raw_data)

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed[0]["id"], "1")
        self.assertEqual(transformed[0]["client_id"], "100")

        # Strip the timezone information for comparison
        self.assertEqual(transformed[0]["run_date"].strftime("%Y-%m-%d %H:%M:%S"), "2024-01-01 12:00:00")


    def test_transform_sonar_results(self):
        raw_data = [
            {
                "_id": "1",
                "sonar_run_id": "1000",
                "part_id": "P123",
                "supplier_id": "S123",
                "price": "50.75",
                "lead_time": "10",
                "timestamp": "2024-01-01T12:00:00Z"
            },
            {
                "_id": "2",
                "sonar_run_id": "1001",
                "part_id": "P124",
                "supplier_id": "S124",
                "price": "100.50",
                "lead_time": "20",
                "timestamp": "2024-01-02T15:30:00Z"
            }
        ]

        transformed = transform_sonar_results(raw_data)

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed[0]["id"], "1")
        self.assertEqual(transformed[0]["sonar_run_id"], "1000")
        self.assertEqual(transformed[0]["price"], 50.75)
        self.assertEqual(transformed[0]["lead_time"], 10)
        # Expecting the timestamp with timezone +00:00
        self.assertEqual(str(transformed[0]["timestamp"]), "2024-01-01 12:00:00+00:00")

if __name__ == "__main__":
    unittest.main()