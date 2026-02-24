from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

# Replace these with your Render PostgreSQL credentials
DB_HOST = "localhost"      # e.g., db-abc123.render.com
DB_NAME = "D4"
DB_USER = "postgres"
DB_PASSWORD = "23bcon1008"
DB_PORT = "5432"

@app.route("/")
def home():
    return "SQL Project is Live on Render!"

@app.route("/students")
def get_students():
    try:
        conn = psycopg.connect(
            host= DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()

        # Run your query
        cur.execute("""
            SELECT name, age, salary
            FROM students_2025
            WHERE salary > (SELECT AVG(salary) FROM students_2024);
        """)
        rows = cur.fetchall()
        result = [{"name": r[0], "age": r[1], "salary": float(r[2])} for r in rows]

        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
