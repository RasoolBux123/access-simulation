document.getElementById("simulateBtn").addEventListener("click", async () => {
    const employees = [
        { id: "EMP001", access_level: 2, request_time: "2025-09-26T09:15:00", room: "ServerRoom" },
        { id: "EMP002", access_level: 1, request_time: "2025-09-26T09:30:00", room: "Vault" },
        { id: "EMP003", access_level: 3, request_time: "2025-09-26T10:05:00", room: "ServerRoom" },
        { id: "EMP004", access_level: 3, request_time: "2025-09-26T09:45:00", room: "Vault" },
        { id: "EMP005", access_level: 2, request_time: "2025-09-26T08:50:00", room: "R&D Lab" },
        { id: "EMP006", access_level: 1, request_time: "2025-09-26T10:10:00", room: "R&D Lab" },
        { id: "EMP007", access_level: 2, request_time: "2025-09-26T10:18:00", room: "ServerRoom" },
        { id: "EMP008", access_level: 3, request_time: "2025-09-26T09:55:00", room: "Vault" },
        { id: "EMP001", access_level: 2, request_time: "2025-09-26T09:28:00", room: "ServerRoom" },
        { id: "EMP006", access_level: 1, request_time: "2025-09-26T10:15:00", room: "R&D Lab" }
    ];

    const response = await fetch("http://127.0.0.1:8000/api/simulate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(employees)
    });

    const data = await response.json();
    const tbody = document.querySelector("#resultTable tbody");
    tbody.innerHTML = "";

    data.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.employee_id}</td>
            <td>${item.access_level}</td>
            <td>${item.request_time}</td>
            <td>${item.room}</td>
            <td class="${item.decision.toLowerCase()}">${item.decision}</td>
            <td>${item.reason}</td>
        `;
        tbody.appendChild(row);
    });
});
