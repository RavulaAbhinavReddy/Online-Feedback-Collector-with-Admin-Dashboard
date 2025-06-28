from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a strong secret key

# -------- Database Setup --------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    rating INTEGER NOT NULL,
                    comments TEXT,
                    date_submitted TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

init_db()

# -------- Routes --------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    rating = int(request.form['rating'])
    comments = request.form.get('comments', '')
    date_submitted = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Feedback (name, email, rating, comments, date_submitted) VALUES (?, ?, ?, ?, ?)",
              (name, email, rating, comments, date_submitted))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['admin'] = True
            return redirect('/admin-dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Feedback")
    feedback_data = c.fetchall()

    total_feedback = len(feedback_data)
    avg_rating = round(sum([row[3] for row in feedback_data]) / total_feedback, 2) if total_feedback else 0

    # Count ratings (1 to 5)
    rating_counts = [0, 0, 0, 0, 0]
    for row in feedback_data:
        rating_counts[row[3] - 1] += 1

    conn.close()

    return render_template("admin.html",
                           feedback_list=[{
                               "id": row[0],
                               "name": row[1],
                               "email": row[2],
                               "rating": row[3],
                               "comments": row[4],
                               "date_submitted": row[5]
                           } for row in feedback_data],
                           total_feedback=total_feedback,
                           avg_rating=avg_rating,
                           chart_data=rating_counts)

# -------- Main --------
if __name__ == '__main__':
    app.run(debug=True)
