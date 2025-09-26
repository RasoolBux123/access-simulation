CREATE DATABASE IF NOT EXISTS access_simulation;

USE access_simulation;

CREATE TABLE IF NOT EXISTS employee_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL,
    access_level INT NOT NULL,
    request_time DATETIME NOT NULL,
    room VARCHAR(50) NOT NULL,
    decision VARCHAR(10) NOT NULL,
    reason VARCHAR(255) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL,
    min_access_level INT NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL,
    cooldown_minutes INT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    access_level INT NOT NULL
);
