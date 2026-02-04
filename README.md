🎓 University Event Management System
A sleek, dark-themed Desktop Application built with Python and MySQL for seamless event planning and student participation.

📸 Overview
The University Event Management System is a robust tool designed to bridge the gap between campus organizers and students. It features a modern Dark Mode UI and a Role-Based Access Control (RBAC) system, ensuring that admins and students have dedicated dashboards tailored to their needs.

🔥 Key Features
🔐 Secure Multi-User Authentication
Role-Based Logic: Dynamically redirects users to either the Admin or Student dashboard upon login.

Environment Security: Uses .env files to keep sensitive database credentials secure and out of the source code.

🛠 Admin Command Center
Event Management: Create, Read, Update, and Delete (CRUD) events with real-time database syncing.

Registration Monitoring: View a centralized list of all student registrations using advanced SQL Joins.

Data Visualization: Clean, organized data display using ttk.Treeview.

🎓 Student Experience
Event Discovery: Browse through all upcoming university events with detailed descriptions.

Instant Registration: Register for events instantly using unique Event IDs.

Personal Portfolio: View personal registrations and cancel/delete them if needed.

🎨 UI/UX Design Details
Theme: Deep Dark Aesthetic (#121212) for reduced eye strain and a modern feel.

Navigation: Sidebar-based navigation for a professional "dashboard" experience.

User Feedback: Comprehensive use of messagebox for error handling and success confirmations.

🛠️ Installation & Setup
1. Database Configuration
Run the following SQL script in your MySQL workbench to set up the environment:

SQL
CREATE DATABASE UniEventDB;
USE UniEventDB;

-- Users Table
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    role ENUM('admin', 'student') NOT NULL
);

-- Events Table
CREATE TABLE Events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    venue VARCHAR(100),
    date DATE,
    description TEXT
);

-- Registrations Table
CREATE TABLE Registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    event_id INT,
    FOREIGN KEY (student_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES Events(id) ON DELETE CASCADE
);
2. Environment Setup
Create a .env file in the root directory and add your credentials:

Code snippet
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password
DB_NAME=UniEventDB
3. Execution
Bash
# Install required libraries
pip install mysql-connector-python python-dotenv

# Launch the application
python Main.py
🚀 Future Improvements
[ ] Password Hashing: Implement bcrypt for secure password storage.

[ ] Email Notifications: Automatic email alerts for new event registrations.

[ ] Search Filter: Add a search bar to filter events by name or date.

📂 Project Structure
Main.py: The entry point of the application containing the UI logic.

.env: (Hidden) Local configuration for database security.

requirements.txt: List of dependencies.

🤝 Contributing Contributions are welcome! Feel free to fork this repository, open an issue, or submit a Pull Request.

Developed with ❤️ by Hassan