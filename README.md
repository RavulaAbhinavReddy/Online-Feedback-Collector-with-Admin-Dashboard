# 📝 Online Feedback Collector with Admin Dashboard

🚀 A full-stack web application built using **Flask**, **SQLite**, **HTML/CSS**, and **Bootstrap** that collects feedback from users and displays it in an admin dashboard with visual summaries.

---

## 📌 Features

### ✅ User Interface
- 🏠 Home page with welcome message
- 📋 Feedback form:
  - 🙍 Name
  - 📧 Email
  - ⭐ Rating (1 to 5)
  - 💬 Comments

### ✅ Admin Dashboard
- 🔐 Admin login page
- 📊 View all feedback
- 📈 Average rating and total feedback
- 🧮 Rating-wise summary chart
- 📥 Download feedback as CSV

---

## 🛠️ Tech Stack

| Layer      | Technologies Used                              |
|------------|-------------------------------------------------|
| Frontend   | HTML, CSS, Bootstrap, JavaScript                |
| Backend    | Python, Flask                                   |
| Database   | SQLite                                          |
| Templates  | Jinja2 for dynamic rendering                    |
| Charts     | Matplotlib or Chart.js                          |

---

## 🧩 Project Structure

OnlineFeedbackCollector/
│
├── app.py # Flask backend
├── requirements.txt # Python dependencies
├── database.db # SQLite DB
│
├── static/
│ ├── css/
│ │ └── style.css # Custom styles
│ └── js/
│ └── script.js # (Optional) JS for validation
│
├── templates/
│ ├── index.html # Feedback form
│ ├── login.html # Admin login
│ ├── admin.html # Admin dashboard
│ └── layout.html # Base layout template
│
└── README.md # You're here!

yaml
Copy
Edit

---

## 📦 How to Run

1. 🔽 **Clone the repository**

```bash
git clone https://github.com/RavulaAbhinavReddy/Online-Feedback-Collector-with-Admin-Dashboard.git
cd OnlineFeedbackCollector
🐍 Create Virtual Environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
📦 Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
🚀 Run the Flask App

bash
Copy
Edit
python app.py
App will be available at: http://localhost:5000

🔑 Admin Login
Use this to access the dashboard:

Username: admin

Password: admin123

💡 You can insert this user manually in the database using SQLite tools or a script.

📊 Sample Dashboard
Total Feedback Count

Average Ratings

Rating Distribution Chart

Feedback Table

✨ Future Enhancements
🛡️ Add authentication hashing

📧 Email notifications on feedback

☁️ Deploy to Render or Railway

🧠 Skills You’ll Learn
Flask & Routing

HTML Forms and POST methods

Connecting Frontend with Backend

CRUD with SQLite

Dashboard & Data Visualization

Hosting a Web Project
