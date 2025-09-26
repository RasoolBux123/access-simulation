# routers/access.py
from fastapi import APIRouter
from models import EmployeeRequest
from services import simulate_access
from db.database import get_db_connection

router = APIRouter()

@router.post("/simulate")
async def simulate_access_endpoint(employees: list[EmployeeRequest]):
    """
    Receives a list of employee requests,
    simulates access, saves results to MySQL, and returns results.
    """
    results = simulate_access(employees)  # Run simulation

    # Connect to MySQL
    conn = get_db_connection()
    if not conn:
        return {"error": "Database connection failed"}
    
    cursor = conn.cursor()

    # Save results to DB
    for res in results:
        cursor.execute(
            """
            INSERT INTO employee_requests
            (employee_id, access_level, request_time, room, decision)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (res["employee_id"], res["access_level"], res["request_time"], res["room"], res["decision"])
        )

    conn.commit()
    cursor.close()
    conn.close()

    return results
