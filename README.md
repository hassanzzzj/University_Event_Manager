<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=auto&height=250&section=header&text=University%20Event%20System&fontSize=60&animation=fadeIn&fontAlignY=40" width="100%" />

  <p align="center">
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" /></a>
    <a href="https://www.mysql.com/"><img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" /></a>
    <a href="#"><img src="https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge" /></a>
    <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" /></a>
  </p>

  <h3>🚀 A Premium, Dark-Themed Desktop Solution for Modern Campus Management</h3>
</div>

<hr />

<table style="width: 100%; border: none; border-collapse: collapse;">
  <tr>
    <td style="padding: 20px; border: none; vertical-align: top;">
      <h2 style="color: #3B82F6;">🌟 Project Spotlight</h2>
      <p>This application is designed to streamline university event coordination. Built with a focus on <b>User Experience (UX)</b> and <b>Security</b>, it provides a seamless bridge between administrative organizers and the student body.</p>
      <h3>🎯 Why Use This?</h3>
      <ul>
        <li><b>Aesthetic UI:</b> Fully custom dark-themed interface built with Tkinter.</li>
        <li><b>Role-Based Access:</b> Separate environments for Admins and Students.</li>
        <li><b>Data Integrity:</b> Secure MySQL backend with Foreign Key constraints.</li>
      </ul>
    </td>
    <td style="padding: 20px; border: none; vertical-align: middle;" width="40%">
      <img src="https://img.icons8.com/fluency/240/event-accepted-tentatively.png" />
    </td>
  </tr>
</table>

<hr />

<h2 style="color: #3B82F6;">🛠️ Key Functionalities</h2>

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <th style="background-color: #1E1E2E; color: white; padding: 15px; border-radius: 10px 0 0 0;">👨‍💼 Admin Dashboard (The Control Room)</th>
    <th style="background-color: #2D2D44; color: white; padding: 15px; border-radius: 0 10px 0 0;">🎓 Student Dashboard (The Hub)</th>
  </tr>
  <tr>
    <td style="padding: 15px; border: 1px solid #333; vertical-align: top;">
      <ul>
        <li><b>Event Lifecycle:</b> CRUD events in real-time.</li>
        <li><b>Analytics:</b> Track registration via SQL Joins.</li>
        <li><b>Management:</b> Control the university schedule.</li>
      </ul>
    </td>
    <td style="padding: 15px; border: 1px solid #333; vertical-align: top;">
      <ul>
        <li><b>Live Feed:</b> Browse events with a single click.</li>
        <li><b>Quick Enroll:</b> Register using Event Identifiers.</li>
        <li><b>Personal View:</b> Manage your registrations easily.</li>
      </ul>
    </td>
  </tr>
</table>

<br />

<details open>
  <summary style="font-size: 22px; font-weight: bold; cursor: pointer; color: #3B82F6;">🚀 Getting Started</summary>
  
  <h3>1. Database Setup</h3>
  <p>Run these commands in your MySQL terminal:</p>
  <pre style="background: #121212; color: #4ade80; padding: 15px; border-radius: 10px; border: 1px solid #333;">
CREATE DATABASE UniEventDB;
USE UniEventDB;

-- Create Users, Events, and Registrations Tables
-- (Ensure Foreign Key constraints are active)</pre>

  <h3>2. Environment Configuration</h3>
  <p>Create a <code>.env</code> file in your root folder:</p>
  <div style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px; border-left: 5px solid #3B82F6;">
    <code>
      DB_HOST=localhost<br>
      DB_USER=root<br>
      DB_PASSWORD=your_password_here<br>
      DB_NAME=UniEventDB
    </code>
  </div>
</details>

<br />

<details>
  <summary style="font-size: 22px; font-weight: bold; cursor: pointer; color: #3B82F6;">📦 Installation & Architecture</summary>
  
  <h3>Installation Commands</h3>
  <pre style="background: #121212; color: #3B82F6; padding: 15px; border-radius: 10px;">
# Install dependencies
pip install mysql-connector-python python-dotenv

# Run the app
python Main.py</pre>

  <h3>📂 Project Architecture</h3>
  <pre style="background: #f4f4f4; color: #333; padding: 15px; border-radius: 10px; font-family: monospace;">
├── Main.py              # Main Application Entry
├── .env                 # Database Credentials (HIDDEN)
├── assets/              # Icons and Images (Optional)
└── README.md            # Documentation</pre>
</details>

<hr />

<h2 align="center">🤝 Contributing</h2>
<p align="center">
  Fork the Project ➔ Create Feature Branch ➔ Commit Changes ➔ Push to Branch ➔ Open Pull Request
</p>

<div align="center" style="margin-top: 50px; background: #1E1E2E; padding: 20px; border-radius: 15px;">
  <p>Developed with ❤️ by <b>Hassan</b></p>
  <p><i>Let's build something great together!</i></p>
  <a href="https://github.com/hassanzzzj"><img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github" /></a>
</div>