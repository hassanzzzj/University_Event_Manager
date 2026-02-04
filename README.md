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
```

⚙️ 2. Environment Configuration
Security is a priority. Create a .env file in the root directory to store your credentials securely:


# Database Connection Details
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=UniEventDB
[!IMPORTANT] Never share your .env file on GitHub. Add it to your .gitignore to keep your database safe.

🚀 3. Installation & Launch
Follow these simple steps to get the application running on your local machine:

Step 1: Install Dependencies


pip install mysql-connector-python python-dotenv
Step 2: Start Application

python Main.py
📂 Project Architecture
A clean look at the projects organization:


graph TD
    A[Root Directory] --> B(Main.py)
    A --> C[.env]
    A --> D[assets/]
    A --> E[README.md]
    
    style B fill:#3B82F6,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#EF4444,stroke:#fff,stroke-width:2px,color:#fff

├── Main.py              # Core Logic & UI Classes
├── .env                 # Encrypted DB Credentials (HIDDEN)
├── assets/              # Optional UI Icons & Media
└── README.md            # Project Documentation
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project (Click the Fork button at the top)

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

<p align="center"> Developed with ❤️ by <b>Hassan</b>


<i>"Let's build something great together!"</i> </p>