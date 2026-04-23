
import sqlite3


# ---------------- CREATE TABLES ----------------

def create_tables():

    conn = sqlite3.connect("healthguard.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Prediction history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age REAL,
        bmi REAL,
        highbp INTEGER,
        highchol INTEGER,
        smoker INTEGER,
        risk TEXT,
        percentage REAL
    )
    """)

    conn.commit()
    conn.close()


# ---------------- SAVE PREDICTION ----------------

def save_prediction(name, age, bmi, highbp, highchol, smoker, risk, percentage):

    conn = sqlite3.connect("healthguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (name, age, bmi, highbp, highchol, smoker, risk, percentage)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, age, bmi, highbp, highchol, smoker, risk, percentage))

    conn.commit()
    conn.close()


# ---------------- GET HISTORY ----------------

def get_history():

    conn = sqlite3.connect("healthguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name, age, bmi, highbp, highchol, smoker, risk, percentage
    FROM predictions
    """)

    data = cursor.fetchall()

    conn.close()

    return data



# -------------- Delete Prediction ---------------

def delete_prediction(id):

    conn = sqlite3.connect("healthguard.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions WHERE id=?", (id,))

    conn.commit()
    conn.close()












