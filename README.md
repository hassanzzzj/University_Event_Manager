# 🎓 University Event Management System
> **A Premium, Dark-Themed Desktop Solution for Modern Campus Management.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 🌟 Project Spotlight
This application is designed to streamline university event coordination. Built with a focus on **User Experience (UX)** and **Security**, it provides a seamless bridge between administrative organizers and the student body.



### 🎯 Why Use This?
* **Aesthetic UI:** Fully custom dark-themed interface built with Tkinter.
* **Role-Based Access:** Separate environments for Admins and Students.
* **Data Integrity:** Secure MySQL backend with Foreign Key constraints.

---

## 🛠️ Key Functionalities

### 👨‍💼 Admin Dashboard (The Control Room)
* **Event Lifecycle:** Create, Read, Update, and Delete (CRUD) events in real-time.
* **Analytics:** Track registration counts and student details via SQL Joins.
* **Management:** Complete control over the university's event schedule.

### 🎓 Student Dashboard (The Hub)
* **Live Feed:** Browse all upcoming university events with a single click.
* **Quick Enroll:** Instant registration system using unique Event Identifiers.
* **Personalized View:** Manage your own registrations and opt-out whenever needed.

---

## 🎨 Design Elements
* **Palette:** Modern Graphite (`#121212`) & Royal Blue (`#3B82F6`) accents.
* **Layout:** Persistent sidebar navigation for effortless multitasking.
* **Feedback:** Interactive dialogue boxes and real-time data table updates.

---

## 🚀 Getting Started

### 1. Database Setup
Create your database environment by executing these commands in your MySQL terminal:

```sql
CREATE DATABASE UniEventDB;
USE UniEventDB;

CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    role ENUM('admin', 'student') NOT NULL
);

CREATE TABLE Events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    venue VARCHAR(100),
    date DATE,
    description TEXT
);

CREATE TABLE Registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    event_id INT,
    FOREIGN KEY (student_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES Events(id) ON DELETE CASCADE
);