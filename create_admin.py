import sqlite3

# Connect to your database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create Admin table
c.execute('''
    CREATE TABLE IF NOT EXISTS Admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a default admin user
c.execute("INSERT INTO Admin (username, password) VALUES (?, ?)", ("admin", "admin123"))

conn.commit()
conn.close()
print("Admin user created successfully.")
