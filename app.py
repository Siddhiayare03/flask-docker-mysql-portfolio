from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# ------------------ MySQL Connection ------------------

db = None

for i in range(10):
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="siddhi",
            password="siddhi123",
            database="portfolio_db"
        )
        print("✅ Connected to MySQL")
        break

    except Exception:
        print("Waiting for MySQL...")
        time.sleep(5)

# ------------------ Create Table ------------------

if db:
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()

# ------------------ Home Page ------------------

@app.route("/")
def home():
    return render_template("index.html")

# ------------------ Contact Form ------------------

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO contacts(name, email, message)
        VALUES (%s, %s, %s)
        """,
        (name, email, message)
    )

    db.commit()

    return redirect("/")

# ------------------ Run App ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)