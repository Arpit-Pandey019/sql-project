-- subquery.sql

-- Create tables
CREATE TABLE IF NOT EXISTS students_2024 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary NUMERIC
);

CREATE TABLE IF NOT EXISTS students_2025 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary NUMERIC
);

-- Insert sample data
INSERT INTO students_2024 (name, age, salary) VALUES
('Alice', 22, 50000),
('Bob', 23, 60000),
('Charlie', 21, 55000);

INSERT INTO students_2025 (name, age, salary) VALUES
('David', 22, 65000),
('Eve', 23, 58000),
('Frank', 21, 54000);

-- Your original queries
SELECT AVG(salary) FROM students_2024;

SELECT name, age, salary
FROM students_2025
WHERE salary > (SELECT AVG(salary) FROM students_2024);