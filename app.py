from flask import Flask, render_template, request, redirect
import mysql.connector
import config

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    return conn


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_doctor", methods=["GET","POST"])
def add_doctor():

    if request.method == "POST":

        name = request.form["name"]
        specialization = request.form["specialization"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO doctors(name,specialization) VALUES(%s,%s)",
            (name,specialization)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("add_doctor.html")


@app.route("/add_patient", methods=["GET","POST"])
def add_patient():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO patients(name,age,gender) VALUES(%s,%s,%s)",
            (name,age,gender)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("add_patient.html")


@app.route("/appointment", methods=["GET","POST"])
def appointment():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    if request.method == "POST":

        doctor = request.form["doctor"]
        patient = request.form["patient"]
        date = request.form["date"]

        cursor.execute(
        "INSERT INTO appointments(patient_id,doctor_id,appointment_date) VALUES(%s,%s,%s)",
        (patient,doctor,date)
        )

        conn.commit()

        return redirect("/view_appointments")

    return render_template(
        "appointment.html",
        doctors=doctors,
        patients=patients
    )


@app.route("/view_appointments")
def view_appointments():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT a.id,
    p.name as patient,
    d.name as doctor,
    appointment_date

    FROM appointments a
    JOIN patients p ON a.patient_id=p.id
    JOIN doctors d ON a.doctor_id=d.id
    """

    cursor.execute(query)

    appointments = cursor.fetchall()

    return render_template(
        "view_appointments.html",
        appointments=appointments
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)