from flask import Flask, jsonify
import os

app = Flask(__name__)

# Dummy data (no database)
students_data = [
    {"name": "Arpit", "age": 21, "salary": 45000},
    {"name": "Rahul", "age": 22, "salary": 52000},
    {"name": "Sneha", "age": 20, "salary": 48000}
]

@app.route("/")
def home():
    return "SQL Project is Live on Render!"

@app.route("/students")
def get_students():
    return jsonify(students_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
