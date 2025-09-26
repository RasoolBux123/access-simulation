from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    employee_id: str      # Must match "EMP001" style IDs
    access_level: int
    request_time: str     # Format "HH:MM"
    room: str
