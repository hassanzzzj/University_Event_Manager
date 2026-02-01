# 🎓 University Event Management System
> A modern, dark-themed Desktop Application for seamless event planning and student participation.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)

---

## 📸 Overview
Yeh project university ke events ko manage karne ke liye banaya gaya hai. Ismein **Admin** ke paas pure control hota hai aur **Students** asani se events browse aur register kar sakte hain. Iska UI fully dark-themed aur responsive hai.

---

## 🔥 Key Features

### 🔐 Multi-User Authentication
* **Admin Login:** Full access to manage events and view registrations.
* **Student Login:** Personalized dashboard based on the logged-in user.

### 🛠 Admin Capabilities
* **Event Creation:** Title, Venue, Date, aur Description ke sath naye events post karein.
* **Live Monitoring:** Tamam registered students ki list real-time mein dekhein.
* **Data Management:** Purane events ko update ya delete karne ki mukammal sahulat.

### 🎓 Student Experience
* **Discovery:** University mein hone wale tamam events ki list dekhein.
* **Quick Registration:** Sirf Event ID enter karke registration karein.
* **Personalized View:** Apni registered events ki list aur unhe cancel (delete) karne ka option.

---

## 🎨 UI Design Details
* **Theme:** Deep Dark Aesthetic (`#121212`).
* **Sidebar:** Professional navigation menu with interactive buttons.
* **Visual Feedback:** Success/Error popups ke liye `messagebox` ka behtareen use.
* **Data Tables:** Clean aur organized data display ke liye `ttk.Treeview` ka istemal.

---

## 🛠️ Installation & Setup

### 1. Database Setup
Pehle MySQL mein `UniEventDB` banayein aur ye tables create karein:

```sql
CREATE DATABASE UniEventDB;
USE UniEventDB;

-- Users Table
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    role ENUM('admin', 'student')
);

-- Events Table
CREATE TABLE Events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    venue VARCHAR(100),
    date DATE,
    description TEXT
);

-- Registrations Table
CREATE TABLE Registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    event_id INT,
    FOREIGN KEY (student_id) REFERENCES Users(id),
    FOREIGN KEY (event_id) REFERENCES Events(id)
);
```
2. Configure Python
```
Main.py mein get_db_connection() function ke andar apna MySQL password aur user set karein:

Python
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Apna user
    password="your_password", # Apna password
    database="UniEventDB"
)
```
3. Run Application
````
Bash
pip install mysql-connector-python
python Main.py
````
📂 Project Structure
```
Main.py: Main application code containing Login, Admin, and Student classes.

mysql.connector: Database connectivity module.

tkinter: GUI Framework.
```

🤝 Contributing
If you want to add your contribution in this project then, open a new Pull Request!

Developed with ❤️ by Your Hassan
