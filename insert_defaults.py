import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Meeting me bola tha - ye 2 subjects for-loop se add karne hai
extra_subjects = [
    ('Python', 'PY101', 'V. Kumar'),
    ('C++', 'CPP101', 'S. Singh')
]

print("Adding extra subjects using for-loop...")
for subject in extra_subjects:
    try:
        cursor.execute("INSERT INTO subjects (subject_name, subject_code, teacher_name) VALUES (?,?,?)", subject)
        print(f"Added: {subject[0]} - {subject[1]}")
    except sqlite3.IntegrityError:
        print(f"Skipped: {subject[0]} already exists")

conn.commit()
conn.close()
print("\nDone ✅ Run this after database.py")