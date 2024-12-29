from typing import List
import pandas as pd
from bson import ObjectId

def transform_clients(clients: List[dict]) -> List[dict]:
    """
    Transforms client documents for PostgreSQL insertion.

    Args:
        clients (List[dict]): List of client documents.

    Returns:
        List[dict]: Transformed client data.
    """
    transformed = []
    for client in clients:
        transformed.append({
            "id": str(client["_id"]),
            "name": client.get("name"),
            "contact_info": client.get("contact_info")
            # Add other relevant fields
        })
    return transformed

def transform_suppliers(suppliers: List[dict]) -> List[dict]:
    """
    Transforms supplier documents for PostgreSQL insertion.

    Args:
        suppliers (List[dict]): List of supplier documents.

    Returns:
        List[dict]: Transformed supplier data.
    """
    transformed = []
    for supplier in suppliers:
        transformed.append({
            "id": str(supplier["_id"]),
            "name": supplier.get("name"),
            "website": supplier.get("website")
            # Add other relevant fields
        })
    return transformed

def transform_sonar_runs(sonar_runs: List[dict]) -> List[dict]:
    """
    Transforms sonar_run documents for PostgreSQL insertion.

    Args:
        sonar_runs (List[dict]): List of sonar_run documents.

    Returns:
        List[dict]: Transformed sonar_run data.
    """
    transformed = []
    for run in sonar_runs:
        transformed.append({
            "id": str(run["_id"]),
            "client_id": str(run.get("client_id")),
            "run_date": pd.to_datetime(run.get("run_date"))
            # Add other relevant fields
        })
    return transformed

def transform_sonar_results(sonar_results: List[dict]) -> List[dict]:
    """
    Transforms sonar_result documents for PostgreSQL insertion.

    Args:
        sonar_results (List[dict]): List of sonar_result documents.

    Returns:
        List[dict]: Transformed sonar_result data.
    """
    transformed = []
    for result in sonar_results:
        try:
            # Ensure that ObjectId is converted to string for any field
            transformed.append({
                "id": str(result.get("_id", "")) if isinstance(result.get("_id"), ObjectId) else str(result.get("_id", "")),
                "sonar_run_id": str(result.get("sonar_run_id", "")) if isinstance(result.get("sonar_run_id"), ObjectId) else str(result.get("sonar_run_id", "")),
                "part_id": str(result.get("part_id", "")) if isinstance(result.get("part_id"), ObjectId) else str(result.get("part_id", "")),
                "supplier_id": str(result.get("supplier_id", "")) if isinstance(result.get("supplier_id"), ObjectId) else str(result.get("supplier_id", "")),
                "price": float(result.get("price") or 0.0),
                "lead_time": int(result.get("lead_time", 0)),
                "timestamp": pd.to_datetime(result.get("timestamp"), errors="coerce"),
            })
        except Exception as e:
            print(f"Error transforming document {result}: {e}")
    return transformed