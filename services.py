from datetime import datetime, timedelta

def simulate_access(employees):
    results = []
    for emp in employees:
        # If emp.request_time is string "HH:MM", parse it correctly
        try:
            hour, minute = map(int, emp.request_time.split(":"))
            # Use today's date + the time from the request
            req_time = datetime.today().replace(hour=hour, minute=minute, second=0, microsecond=0)
        except:
            # Fallback to now if parsing fails
            req_time = datetime.now()

        # Example access logic
        if emp.access_level >= 2:
            decision = "GRANTED"
            reason = "Access level sufficient"
        else:
            decision = "DENIED"
            reason = "Insufficient access level"

        results.append({
            "employee_id": emp.id,
            "access_level": emp.access_level,
            "request_time": req_time.strftime("%Y-%m-%d %H:%M:%S"),
            "room": emp.room,
            "decision": decision,
            "reason": reason
        })

    return results
