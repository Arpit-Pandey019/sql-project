from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dummy student data (no database required)
students_data = [
    {"name": "Arpit", "age": 21, "salary": 45000},
    {"name": "Rahul", "age": 22, "salary": 52000},
    {"name": "Sneha", "age": 20, "salary": 48000}
]

@app.route("/")
def home():
    # Serve the HTML page
    return render_template("index.html")

@app.route("/students")
def get_students():
    # Return JSON data to the frontend
    return jsonify(students_data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
