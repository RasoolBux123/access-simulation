const employees = [
  { "employee_id": "EMP001", "access_level": 2, "request_time": "09:15", "room": "ServerRoom" },
  { "employee_id": "EMP002", "access_level": 1, "request_time": "09:30", "room": "Vault" },
  { "employee_id": "EMP003", "access_level": 3, "request_time": "10:05", "room": "ServerRoom" },
  { "employee_id": "EMP004", "access_level": 3, "request_time": "09:45", "room": "Vault" },
  { "employee_id": "EMP005", "access_level": 2, "request_time": "08:50", "room": "R&D Lab" },
  { "employee_id": "EMP006", "access_level": 1, "request_time": "10:10", "room": "R&D Lab" },
  { "employee_id": "EMP007", "access_level": 2, "request_time": "10:18", "room": "ServerRoom" },
  { "employee_id": "EMP008", "access_level": 3, "request_time": "09:55", "room": "Vault" },
  { "employee_id": "EMP001", "access_level": 2, "request_time": "09:28", "room": "ServerRoom" },
  { "employee_id": "EMP006", "access_level": 1, "request_time": "10:15", "room": "R&D Lab" }
];

document.getElementById("simulateBtn").addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8000/api/simulate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(employees)
    });

    const data = await response.json();
    const tbody = document.querySelector("#resultsTable tbody");
    tbody.innerHTML = ""; // Clear previous results

    data.forEach(emp => {
        const row = document.createElement("tr");

        // Color code GRANTED (green) and DENIED (red)
        const decisionClass = emp.decision.startsWith("GRANTED") ? "granted" : "denied";

        row.innerHTML = `
            <td>${emp.employee_id}</td>
            <td>${emp.access_level}</td>
            <td>${emp.request_time}</td>
            <td>${emp.room}</td>
            <td class="${decisionClass}">${emp.decision}</td>
        `;

        tbody.appendChild(row);
    });
});
