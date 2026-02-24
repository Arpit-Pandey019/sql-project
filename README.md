# SQL Project – Internship Student Salary Dashboard

[🚀 **View Live Project on Render**](https://sql-project-3.onrender.com/)

This project demonstrates a **SQL-based dashboard** showing **students doing internships and their salary**.  
It uses **PostgreSQL / pgAdmin** for data management locally (or dummy data on Render) with a Flask backend and a simple frontend table display.

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

- Displays students doing internships with their salary  
- Fetches student data from a SQL-like structure (dummy or live DB)  
- Clean table format with name, age, and salary  
- Fully deployed on Render  
- Frontend & backend integrated via Flask API  

---

## ⚡ How It Works

1. **SQL / pgAdmin** – Tables `students_2024` and `students_2025` store student data (local or Render DB).  
2. **Flask backend** (`app.py`) provides API `/students` to fetch internship data.  
3. **Frontend** (`index.html`) fetches data via `fetch()` and displays it in a table.  

> Note: In this deployed version, dummy data is used to simulate SQL queries without requiring a live database.

---

## 📂 Project Structure



