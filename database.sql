CREATE DATABASE hospital;

USE hospital;

CREATE TABLE doctors(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
specialization VARCHAR(100)
);

CREATE TABLE patients(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
age INT,
gender VARCHAR(10)
);

CREATE TABLE appointments(
id INT AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
FOREIGN KEY(patient_id) REFERENCES patients(id),
FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);