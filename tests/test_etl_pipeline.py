import unittest
from unittest.mock import MagicMock, patch
from etl.extract import get_mongo_client, extract_collection
from etl.transform import (
    transform_clients,
    transform_suppliers,
    transform_sonar_runs,
    transform_sonar_results
)
from etl.load import load_data

class TestETLPipeline(unittest.TestCase):
    
    @patch("extract.MongoClient")
    def test_extract_collection(self, mock_mongo_client):
        # Mock MongoDB client and collection
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_collection.find.return_value = [
            {"_id": "1", "name": "Client A", "contact_info": "info@example.com"},
            {"_id": "2", "name": "Client B", "contact_info": "contact@example.com"}
        ]
        mock_db["clients"].return_value = mock_collection
        mock_mongo_client.return_value.__getitem__.return_value = mock_db

        client = get_mongo_client()
        documents = extract_collection(client, "test_db", "clients")

        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[0]["name"], "Client A")

    # def test_transform_clients(self):
    #     raw_data = [
    #         {"_id": "1", "name": "Client A", "contact_info": "info@example.com"},
    #         {"_id": "2", "name": "Client B", "contact_info": "contact@example.com"}
    #     ]

    #     transformed = transform_clients(raw_data)

    #     self.assertEqual(len(transformed), 2)
    #     self.assertEqual(transformed[0]["id"], "1")
    #     self.assertEqual(transformed[0]["name"], "Client A")

    # def test_transform_suppliers(self):
    #     raw_data = [
    #         {"_id": "1", "name": "Supplier A", "website": "http://example.com"},
    #         {"_id": "2", "name": "Supplier B", "website": "http://example.org"}
    #     ]

    #     transformed = transform_suppliers(raw_data)

    #     self.assertEqual(len(transformed), 2)
    #     self.assertEqual(transformed[0]["id"], "1")
    #     self.assertEqual(transformed[0]["name"], "Supplier A")

    # def test_transform_sonar_runs(self):
    #     raw_data = [
    #         {"_id": "1", "client_id": "100", "run_date": "2024-01-01T12:00:00Z"},
    #         {"_id": "2", "client_id": "200", "run_date": "2024-01-02T15:30:00Z"}
    #     ]

    #     transformed = transform_sonar_runs(raw_data)

    #     self.assertEqual(len(transformed), 2)
    #     self.assertEqual(transformed[0]["id"], "1")
    #     self.assertEqual(transformed[0]["client_id"], "100")
    #     self.assertEqual(str(transformed[0]["run_date"]), "2024-01-01 12:00:00")

    # def test_transform_sonar_results(self):
    #     raw_data = [
    #         {
    #             "_id": "1",
    #             "sonar_run_id": "1000",
    #             "part_id": "P123",
    #             "supplier_id": "S123",
    #             "price": "50.75",
    #             "lead_time": "10",
    #             "timestamp": "2024-01-01T12:00:00Z"
    #         },
    #         {
    #             "_id": "2",
    #             "sonar_run_id": "1001",
    #             "part_id": "P124",
    #             "supplier_id": "S124",
    #             "price": "100.50",
    #             "lead_time": "20",
    #             "timestamp": "2024-01-02T15:30:00Z"
    #         }
    #     ]

    #     transformed = transform_sonar_results(raw_data)

    #     self.assertEqual(len(transformed), 2)
    #     self.assertEqual(transformed[0]["id"], "1")
    #     self.assertEqual(transformed[0]["sonar_run_id"], "1000")
    #     self.assertEqual(transformed[0]["price"], 50.75)
    #     self.assertEqual(transformed[0]["lead_time"], 10)
    #     self.assertEqual(str(transformed[0]["timestamp"]), "2024-01-01 12:00:00")

    # @patch("psycopg2.connect")
    # def test_load_data(self, mock_connect):
    #     # Mock PostgreSQL connection
    #     mock_conn = MagicMock()
    #     mock_cursor = MagicMock()
    #     mock_conn.cursor.return_value = mock_cursor
    #     mock_connect.return_value = mock_conn

    #     data = [
    #         {"id": "1", "name": "Client A", "contact_info": "info@example.com"},
    #         {"id": "2", "name": "Client B", "contact_info": "contact@example.com"}
    #     ]

    #     load_data(mock_conn, "clients", data)

    #     self.assertTrue(mock_cursor.execute.called)
    #     self.assertTrue(mock_conn.commit.called)

if __name__ == "__main__":
    unittest.main()