# Employee Access Simulation

**Author:** Rasool Bux  
**Project Type:** Internal Tool (HR/Security)  
**Tech Stack:** Python, FastAPI, MySQL, HTML/CSS/JS  

---

## Overview

This application simulates employee access to secure rooms in a building. Each room has:

- Minimum access level  
- Open and close times  
- Cooldown period per employee  

HR managers can:

1. Load employee access requests (from a static JSON or MySQL database).  
2. Click **Simulate Access**.  
3. See a result table showing which employees were **granted** or **denied** access, including the reason.  

The simulation rules ensure access is only granted if:  

- Employee meets the room's minimum access level.  
- Request is within room hours.  
- Employee has not accessed the same room in the last cooldown period.  

---

## Features

- Load employee requests from MySQL.  
- Simulate access and save results to database.  
- Dynamically display results in a table.  
- Color-coded decisions:  
  - **Green** → GRANTED  
  - **Red** → DENIED  

---

## Tech Stack

**Backend:**  
- Python 3.x  
- FastAPI  
- MySQL  



**Frontend:**  
- HTML/CSS/JS (Vanilla)  

 
venv\Scripts\activate   active the virtual enviroemnt
**Run commad**
uvicorn main:app --reload

**Database:**  
- MySQL  
- Tables: `employee_requests`, `rooms`, `users`  

---

## Installation & Setup

1. **Clone repository**

```bash
git clone https://github.com/yourusername/access-simulation.git
cd access-simulation
git checkout dev
