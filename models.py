# models.py
from pydantic import BaseModel
from datetime import time

class EmployeeRequest(BaseModel):
    id: str
    access_level: int
    request_time: str  # keep as string "HH:MM"
    room: str
