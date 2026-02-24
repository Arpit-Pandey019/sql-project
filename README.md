# SQL Project – Student Salary Dashboard

[🚀 **View Live Project on Render**](https://sql-project-3.onrender.com/)

This project demonstrates a **SQL-based student salary dashboard** using **PostgreSQL / pgAdmin** (locally or for learning) with a Flask backend and a simple frontend.

---

## 💻 Technology Stack

- **Backend:** Python, Flask  
- **Database (optional):** PostgreSQL (managed with pgAdmin locally or Render DB)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** [Render](https://render.com)

---

## 🔗 Live Demo

Click here to view the project live:  
[https://sql-project-3.onrender.com/](https://sql-project-3.onrender.com/)

---

## 📋 Features

- Fetches student data from a SQL-like structure (dummy or live DB)
- Displays students with salary above a certain threshold
- Clean table format with name, age, and salary
- Fully deployed on Render
- Frontend & backend integrated with Flask API

---

## ⚡ How It Works

1. **SQL / pgAdmin** – Tables `students_2024` and `students_2025` store student data (local or on Render DB).  
2. **Flask backend** (`app.py`) provides API `/students` to fetch data.  
3. **Frontend** (`index.html`) fetches data via `fetch()` and displays in a table.  

> Note: In this deployed version, dummy data is used to simulate SQL queries without requiring a live database.

---


