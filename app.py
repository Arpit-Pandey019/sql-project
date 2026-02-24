from flask import Flask, jsonify, render_template
import psycopg
import os

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "D4"
DB_USER = "postgres"
DB_PASSWORD = "23bcon1008"
DB_PORT = "5432"

def get_connection():
    return psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, age, salary
        FROM students_2025
        WHERE salary > (SELECT AVG(salary) FROM students_2024);
    """)

    students = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", students=students)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
