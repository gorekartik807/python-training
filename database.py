import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'student'
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT UNIQUE NOT NULL,
        subject_code TEXT UNIQUE NOT NULL,
        teacher_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no TEXT NOT NULL,
        subject_id INTEGER,
        marks INTEGER DEFAULT 0,
        attendance INTEGER DEFAULT 0,
        created_by INTEGER,
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (created_by) REFERENCES users(id)
    )
''')

subjects = [
    ('Maths', 'MTH101', 'R.K. Sharma'),
    ('Science', 'SCI101', 'S.P. Verma'),
    ('English', 'ENG101', 'A. Gupta'),
    ('History', 'HIS101', 'M. Patel'),
    ('Java', 'JAVA101', 'T. Mehta')
]

for sub in subjects:
    cursor.execute("INSERT OR IGNORE INTO subjects (subject_name, subject_code, teacher_name) VALUES (?,?,?)", sub)

cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?,?,?)",
               ('admin', 'admin123', 'admin'))

# Dummy students insert karo testing ke liye
dummy_students = [
    ('Rahul Sharma', 'CS001', 1, 85, 90, 1),   # name, roll_no, subject_id, marks, attendance, created_by
    ('Priya Verma', 'CS002', 2, 35, 70, 1),
    ('Amit Kumar', 'CS003', 1, 65, 80, 1),
    ('Neha Gupta', 'CS004', 5, 95, 98, 1),        # Ye mai hoon 😎
    ('Sneha Patel', 'CS005', 3, 78, 72, 1),
    ('Rohit Singh', 'CS006', 4, 42, 76, 1)
]

for student in dummy_students:
    cursor.execute("INSERT OR IGNORE INTO students (name, roll_no, subject_id, marks, attendance, created_by) VALUES (?,?,?,?,?,?)", student)

conn.commit()
conn.close()
print("Database created with dummy data ✅")
print("Total Students Added: 6")
print("Default admin - Username: admin | Password: admin123")