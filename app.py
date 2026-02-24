from flask import Flask, jsonify
import psycopg2  # Note: changed from psycopg to psycopg2
import os

app = Flask(__name__)

# Get database connection from environment variable (set this in Render)
DB_URL = os.environ.get('DATABASE_URL')

# Alternative: If you want to use individual parameters (uncomment and set in Render)
# DB_HOST = os.environ.get('DB_HOST')
# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DB_PORT = os.environ.get('DB_PORT')

@app.route("/")
def home():
    return "SQL Project is Live on Render!"

@app.route("/students")
def get_students():
    try:
        # Connect using the DATABASE_URL from environment
        conn = psycopg2.connect(DB_URL, sslmode='require')
        
        # Alternative connection method (if using separate parameters):
        # conn = psycopg2.connect(
        #     host=DB_HOST,
        #     dbname=DB_NAME,
        #     user=DB_USER,
        #     password=DB_PASSWORD,
        #     port=DB_PORT,
        #     sslmode='require'
        # )
        
        cur = conn.cursor()

        # Your query - make sure these tables exist in your database
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
        return str(e), 500  # Added error code

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=False)  # Set debug=False in production
