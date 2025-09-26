from models import EmployeeRequest

# Helper: HH:MM → minutes since midnight
def to_minutes(time_str: str) -> int:
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

# Room rules
ROOMS = {
    "ServerRoom": {
        "min_level": 2,
        "open_time": to_minutes("09:00"),
        "close_time": to_minutes("11:00"),
        "cooldown": 15,
    },
    "Vault": {
        "min_level": 3,
        "open_time": to_minutes("09:00"),
        "close_time": to_minutes("10:00"),
        "cooldown": 30,
    },
    "R&D Lab": {
        "min_level": 1,
        "open_time": to_minutes("08:00"),
        "close_time": to_minutes("12:00"),
        "cooldown": 10,
    },
}

# Track last access: (employee_id, room) → last_access_time in minutes
last_access = {}

def simulate_access_logic(req: EmployeeRequest) -> str:
    """Simulates access for a single employee request."""
    room = ROOMS.get(req.room)
    if not room:
        return f"DENIED: Room {req.room} does not exist"

    emp_id = req.employee_id
    req_time = to_minutes(req.request_time)

    # Rule 1: Access level check
    if req.access_level < room["min_level"]:
        return "DENIED: Insufficient access level"

    # Rule 2: Time window check
    if not (room["open_time"] <= req_time <= room["close_time"]):
        return "DENIED: Outside room hours"

    # Rule 3: Cooldown check
    key = (emp_id, req.room)
    if key in last_access:
        prev_time = last_access[key]
        if req_time - prev_time < room["cooldown"]:
            return "DENIED: Cooldown violation"

    # ✅ Granted → Update last access
    last_access[key] = req_time
    return f"GRANTED: Access to {req.room}"


def simulate_access(requests: list[EmployeeRequest]) -> list[dict]:
    """
    Takes a list of EmployeeRequest objects and applies simulation rules.
    Resets cooldown tracking for this batch.
    Returns a list of results with decisions.
    """
    global last_access
    last_access = {}  # Reset cooldown tracking for this batch

    results = []
    for req in requests:
        decision = simulate_access_logic(req)
        results.append({
            "employee_id": req.employee_id,
            "access_level": req.access_level,
            "request_time": req.request_time,
            "room": req.room,
            "decision": decision
        })
    return results
