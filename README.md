<div align="center">
  <h1 style="border-bottom: none;">🎓 University Event Management System</h1>
  <p><i>A Premium, Dark-Themed Desktop Solution for Modern Campus Management.</i></p>
</div>

<hr />

<details open>
  <summary><h3 style="display: inline-block;">⚙️ 2. Environment Configuration</h3></summary>
  <p>Security is a priority. Create a <code>.env</code> file in the root directory to store your credentials securely:</p>
  <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px; border: 1px solid #333;">
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=UniEventDB</pre>
  <blockquote style="border-left: 5px solid #ff5f57; background: #fff5f5; padding: 10px; color: #333;">
    <strong>⚠️ IMPORTANT:</strong> Never share your <code>.env</code> file on GitHub. Add it to your <code>.gitignore</code> to keep your database safe.
  </blockquote>
</details>

<br />

<details open>
  <summary><h3 style="display: inline-block;">🚀 3. Installation & Launch</h3></summary>
  <p>Follow these simple steps to get the application running:</p>
  
  <strong>Step 1: Install Dependencies</strong>
  <pre style="background: #1e1e1e; color: #4ade80; padding: 15px; border-radius: 8px;">pip install mysql-connector-python python-dotenv</pre>

  <strong>Step 2: Start Application</strong>
  <pre style="background: #1e1e1e; color: #4ade80; padding: 15px; border-radius: 8px;">python Main.py</pre>
</details>

<br />

<h3 align="left">📂 Project Architecture</h3>
<p>A structured look at the project's organization:</p>

<table style="width: 100%; border-collapse: collapse; background: #121212; color: white;">
  <tr style="border-bottom: 1px solid #333;">
    <th align="left" style="padding: 10px;">File/Folder</th>
    <th align="left" style="padding: 10px;">Description</th>
  </tr>
  <tr>
    <td style="padding: 10px;">📂 <code>Main.py</code></td>
    <td style="padding: 10px;">Core Logic & UI Classes</td>
  </tr>
  <tr>
    <td style="padding: 10px;">🔑 <code>.env</code></td>
    <td style="padding: 10px; color: #ff5f57;">Encrypted DB Credentials (HIDDEN)</td>
  </tr>
  <tr>
    <td style="padding: 10px;">🖼️ <code>assets/</code></td>
    <td style="padding: 10px;">Optional UI Icons & Media</td>
  </tr>
  <tr>
    <td style="padding: 10px;">📄 <code>README.md</code></td>
    <td style="padding: 10px;">Project Documentation</td>
  </tr>
</table>

<br />

<h3 align="left">🤝 Contributing</h3>
<p>Contributions make the open-source community an amazing place to learn and create. To contribute:</p>
<ol>
  <li><b>Fork</b> the Project</li>
  <li><b>Create</b> your Feature Branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li><b>Commit</b> your Changes (<code>git commit -m 'Add AmazingFeature'</code>)</li>
  <li><b>Push</b> to the Branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li><b>Open</b> a Pull Request</li>
</ol>

<hr />

<div align="center">
  <p>Developed with ❤️ by <b>Hassan</b></p>
  <a href="https://github.com/hassanzzzj">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github" alt="GitHub" />
  </a>
</div>