🚀 University Event Management SystemA sleek, modern, and robust Desktop Application built with Python and Tkinter to manage university events efficiently. This system features a dual-interface for Admins and Students, integrated with a MySQL database for real-time data management.✨ Key Features🔐 Secure AuthenticationRole-Based Access: Separate dashboards for Admin and Student.Modern Login UI: Dark-themed, centered login card with secure password masking.🛡️ Admin Dashboard (The Control Center)Post Events: Easily add new events with title, venue, date, and description.Live Event Feed: View all scheduled events in a structured table.Manage Content: Update existing event details or delete outdated events.Registration Tracking: Monitor which students have registered for specific events using SQL Joins.🎓 Student Dashboard (User Interface)Event Discovery: Browse all upcoming university events.One-Click Registration: Quick registration using Event IDs.My Schedule: View a personalized list of registered events.Self-Management: Option to cancel/delete your own registrations.🎨 UI/UX HighlightsDark Mode Aesthetic: Designed with a professional #121212 and #1E1E2E color palette.Responsive Sidebar: Clean navigation menu for seamless switching between features.Data Visualization: Uses ttk.Treeview for clean, spreadsheet-like data displays.Interactive Feedback: Uses messagebox for success/error alerts and hover-ready cursors.🛠️ Tech StackLanguage: Python 3.xFrontend: Tkinter (Standard GUI Library)Backend: MySQLDatabase Connector: mysql-connector-python⚙️ Installation & Setup1. PrerequisitesMake sure you have MySQL Server installed and running.2. Database ConfigurationCreate a database named UniEventDB and run the following tables:SQLCREATE DATABASE UniEventDB;
USE UniEventDB;

CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    role ENUM('admin', 'student')
);

CREATE TABLE Events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    venue VARCHAR(100),
    date DATE,
    description TEXT
);

CREATE TABLE Registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    event_id INT,
    FOREIGN KEY (student_id) REFERENCES Users(id),
    FOREIGN KEY (event_id) REFERENCES Events(id)
);
3. Clone & RunBash# Clone the repository
git clone https://github.com/your-username/uni-event-management.git

# Install connector
pip install mysql-connector-python

# Run the app
python Main.py
Note: Open Main.py and update the get_db_connection() function with your MySQL username and password.📸 Preview (Conceptual)Login PageAdmin PanelStudent View🤝 ContributingContributions are welcome! Feel free to fork this repo and submit a Pull Request.Developed with ❤️ by Hassan
