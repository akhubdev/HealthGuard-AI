

from flask import Flask, render_template, request, redirect, session, send_file, Response
from database import create_tables, save_prediction, get_history, delete_prediction

import sqlite3
import joblib
import random
import os
import csv
from io import StringIO
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = "healthguard_secret"

create_tables()

model = joblib.load("diabetes_model.pkl")


# ---------------- DOCTOR DATABASE ----------------

doctors = {

"Low Risk":[
{
"name":"No Doctor Required",
"hospital":"Maintain Healthy Lifestyle",
"specialist":"Preventive Care"
}
],

"Medium Risk":[
{
"name":"Dr Rajesh Sharma",
"hospital":"City Care Clinic",
"specialist":"General Physician"
},
{
"name":"Dr Ankit Verma",
"hospital":"Apollo Clinic",
"specialist":"General Physician"
}
],

"High Risk":[
{
"name":"Dr Mehta",
"hospital":"Apollo Hospital",
"specialist":"Diabetes Specialist"
},
{
"name":"Dr Reddy",
"hospital":"AIIMS Diabetes Center",
"specialist":"Endocrinologist"
}
]

}


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("landing.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")

        else:
            return "Invalid Login"

    return render_template("login.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/login")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    data = get_history()

    total = len(data)

    low = 0
    medium = 0
    high = 0

    highest_risk = 0
    highest_name = "None"

    timeline_labels = []
    timeline_values = []

    recent = data[-5:][::-1]

    count = 0

    high_bmi_count = 0
    high_bp_count = 0
    age_list = []

    for row in data:

        count += 1
        timeline_labels.append(f"P{count}")
        timeline_values.append(row[8])

        risk_percent = row[8]

        if risk_percent > highest_risk:
            highest_risk = risk_percent
            highest_name = row[1]

        if row[7] == "Low Risk":
            low += 1
        elif row[7] == "Medium Risk":
            medium += 1
        else:
            high += 1

        age_list.append(row[2])

        if row[3] > 30:
            high_bmi_count += 1

        if row[4] == 1:
            high_bp_count += 1

    risk_list = [row[8] for row in data]

    lowBMI = low
    mediumBMI = medium
    highBMI = high

    avg_risk = round(sum(risk_list) / len(risk_list), 2) if risk_list else 0

    # -------- High Risk Alert System --------

    if high > medium and high > low:
        risk_alert = "⚠ High Risk Patients Increasing"

    elif medium > high and medium > low:
        risk_alert = "⚠ Moderate Risk Trend"

    else:
        risk_alert = "✅ Risk Levels Stable"

    model_accuracy = 91.2

    # -------- Risk Trend Detection --------

    if avg_risk > 60:
        risk_trend = "Increasing"

    elif avg_risk > 30:
        risk_trend = "Moderate"

    else:
        risk_trend = "Stable"

    avg_age = round(sum(age_list)/len(age_list),2) if age_list else 0

    ai_insights = [
        f"{high_bmi_count} patients have BMI above 30 which increases diabetes risk.",
        f"{high_bp_count} patients have high blood pressure which correlates with diabetes risk.",
        f"Average patient age in dataset is {avg_age} years."
    ]

    return render_template(
    "dashboard.html",
    total=total,
    low=low,
    medium=medium,
    high=high,
    avg_risk=avg_risk,
    highest_name=highest_name,
    highest_risk=highest_risk,
    timeline_labels=timeline_labels,
    timeline_values=timeline_values,
    recent=recent,
    ai_insights=ai_insights,
    model_accuracy=model_accuracy,
    risk_trend=risk_trend,
    risk_alert=risk_alert,
    lowBMI=lowBMI,
    mediumBMI=mediumBMI,
    highBMI=highBMI

)

    


# ---------------- PREDICT ----------------

@app.route("/predict", methods=["GET","POST"])
def predict():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"]
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        highbp = int(request.form["highbp"])
        highchol = int(request.form["highchol"])
        smoker = int(request.form["smoker"])

        data = [[age, bmi, highbp, highchol, smoker]]

        probability = model.predict_proba(data)[0][1]

        percentage = round(probability * 100,2)


        # -------- AI Doctor Recommendation --------

        if percentage < 30:
            doctor_recommendation = "No doctor consultation required. Maintain healthy lifestyle."

        elif percentage < 70:
            doctor_recommendation = "Recommended: Routine checkup with a general physician."

        else:
            doctor_recommendation = "⚠ Immediate consultation with a diabetes specialist is strongly advised."


        # -------- Risk Classification --------

        if percentage < 30:
            risk = "Low Risk"
            advice = [
                "Maintain healthy diet",
                "Exercise regularly",
                "Maintain normal BMI"
            ]

        elif percentage < 70:
            risk = "Medium Risk"
            advice = [
                "Reduce sugar intake",
                "Exercise daily",
                "Monitor blood sugar regularly"
            ]

        else:
            risk = "High Risk"
            advice = [
                "Consult doctor immediately",
                "Strict diet control",
                "Regular blood sugar monitoring"
            ]


        save_prediction(name, age, bmi, highbp, highchol, smoker, risk, percentage)
        
        doctor_list = doctors[risk]
        return render_template(
            "result.html",
            risk=risk,
            percentage=percentage,
            advice=advice,
            name=name,
            doctor_recommendation=doctor_recommendation,
            doctor_list=doctor_list
        )

    return render_template("predict.html")

# ---------------- HISTORY ----------------

@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login")

    data = get_history()

    return render_template("history.html", data=data)


# ---------------- REPORTS ----------------

@app.route("/reports")
def reports():

    if "user" not in session:
        return redirect("/login")

    return render_template("reports.html")


# ---------------- SETTINGS ----------------

@app.route("/settings")
def settings():

    if "user" not in session:
        return redirect("/login")

    return render_template("settings.html")


# ---------------- DOWNLOAD CSV ----------------

@app.route("/download_csv")
def download_csv():

    if "user" not in session:
        return redirect("/login")

    data = get_history()

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "ID","Name","Age","BMI","High BP",
        "High Cholesterol","Smoker","Risk Level","Risk Percentage"
    ])

    for row in data:
        writer.writerow(row)

    output.seek(0)

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition":"attachment;filename=prediction_history.csv"}
    )


# ---------------- DELETE HISTORY ----------------

@app.route("/delete/<int:id>")
def delete(id):

    delete_prediction(id)

    return redirect("/history")


# ---------------- ADMIN ANALYTICS ----------------

@app.route("/admin")
def admin():

    conn = sqlite3.connect("healthguard.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM predictions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM predictions WHERE risk='Low Risk'")
    low = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM predictions WHERE risk='Medium Risk'")
    medium = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM predictions WHERE risk='High Risk'")
    high = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "admin.html",
        total=total,
        low=low,
        medium=medium,
        high=high
    )


# ---------------- DOWNLOAD MEDICAL REPORT ----------------

@app.route("/download_report/<risk>/<percentage>/<name>")
def download_report(risk, percentage, name):

    if "user" not in session:
        return redirect("/login")

    percentage = float(percentage)

    report_id = "HG-" + str(random.randint(1000,9999))

    now = datetime.now()

    date = now.strftime("%d %B %Y")
    time = now.strftime("%I:%M %p")

    if "Low" in risk:
        meter_image = os.path.join("static","meter","low.png")
        advice = [
            "Maintain healthy diet",
            "Exercise regularly",
            "Maintain normal BMI"
        ]

    elif "Medium" in risk:
        meter_image = os.path.join("static","meter","medium.png")
        advice = [
            "Reduce sugar intake",
            "Exercise daily",
            "Monitor blood sugar regularly"
        ]

    else:
        meter_image = os.path.join("static","meter","high.png")
        advice = [
            "Consult doctor immediately",
            "Strict diet control",
            "Regular blood sugar monitoring"
        ]

    filename = "HealthGuard_Report.pdf"

    logo = os.path.join("static","images","hospital_logo.png")

    c = canvas.Canvas(filename, pagesize=letter)

    c.drawImage(logo, 100, 740, width=80, height=40)

    # HEADER
    c.setFont("Helvetica-Bold",18)
    c.drawCentredString(330,750,"HEALTHGUARD AI MEDICAL REPORT")

    c.line(100,735,500,735)

    c.setFont("Helvetica",12)
    c.drawString(100,700,f"Report ID : {report_id}")
    c.drawString(100,680,f"Date : {date}")
    c.drawString(100,660,f"Time : {time}")

    c.setFont("Helvetica-Bold",13)
    c.drawString(100,620,"Patient Information")

    c.setFont("Helvetica",12)
    c.drawString(100,590,f"Patient Name : {name}")

    c.setFont("Helvetica-Bold",13)
    c.drawString(100,550,"Prediction Result")

    c.setFont("Helvetica",12)
    c.drawString(100,520,f"Risk Level : {risk}")
    c.drawString(100,500,f"Risk Percentage : {percentage}%")

    c.drawImage(meter_image,200,350,width=200,height=120)

    # RECOMMENDATION
    c.setFont("Helvetica-Bold",13)
    c.drawString(100,320,"Medical Recommendation")

    c.setFont("Helvetica",11)

    y = 290

    for a in advice:
        c.drawString(120,y,"- " + a)
        y -= 25

    c.line(100,150,500,150)

    c.setFont("Helvetica",10)
    c.drawCentredString(300,130,"Generated by HealthGuard AI System")
    c.drawCentredString(300,115,"AI Powered Health Risk Prediction")

    c.save()


    return send_file(filename, as_attachment=True)


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)
