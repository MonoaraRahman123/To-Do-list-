-- SQL Schema for Student + To-Do Management System
-- Database: student_management_db

CREATE TABLE IF NOT EXISTS accounts_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) NOT NULL,
    password VARCHAR(128) NOT NULL,
    role VARCHAR(10) NOT NULL DEFAULT 'student',
    is_superuser BOOLEAN NOT NULL,
    is_staff BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS students_student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    department VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    user_id INT UNIQUE,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES accounts_user(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tasks_task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    due_date DATE,
    user_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES accounts_user(id) ON DELETE CASCADE
);
