import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Get subject IDs
subjects = cursor.execute("SELECT id, subject_name FROM subjects").fetchall()
subject_dict = {name: id for id, name in subjects}

# Sample students data: name, roll_no, subject_name, marks, attendance
students = [
    ('Rahul Sharma', 'CS001', 'Java', 85, 92),
    ('Priya Patel', 'CS002', 'Python', 78, 88),
    ('Amit Kumar', 'CS003', 'Maths', 45, 65),
    ('Sneha Gupta', 'CS004', 'Science', 92, 95),
    ('Vikash Singh', 'CS005', 'C++', 38, 55),
    ('Anjali Verma', 'CS006', 'English', 76, 82),
    ('Rohit Yadav', 'CS007', 'History', 65, 70),
    ('Pooja Mehta', 'CS008', 'Java', 88, 90)
]

print("Adding sample students...")
admin_id = cursor.execute("SELECT id FROM users WHERE role='admin' LIMIT 1").fetchone()
admin_id = admin_id[0] if admin_id else 1

for student in students:
    name, roll_no, subject_name, marks, attendance = student
    subject_id = subject_dict.get(subject_name)
    if subject_id:
        try:
            cursor.execute("""
                INSERT INTO students (name, roll_no, subject_id, marks, attendance, created_by)
                VALUES (?,?,?,?,?,?)
            """, (name, roll_no, subject_id, marks, attendance, admin_id))
            print(f"Added: {name} - {subject_name}")
        except sqlite3.IntegrityError:
            print(f"Skipped: {name} already exists")

conn.commit()
conn.close()
print("\n8 sample students added ✅")