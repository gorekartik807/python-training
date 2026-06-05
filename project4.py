# Students data - list of dictionaries with roll_no
students = [
    {
        "roll_no": 101,
        "name": "Amit Sharma",
        "marks": 85,
        "attendance": 90,
        "branch": "CSE",
        "email": "amit@college.com"
    },
    {
        "roll_no": 102,
        "name": "Sneha Patel",
        "marks": 92,
        "attendance": 95,
        "branch": "IT",
        "email": "sneha@college.com"
    },
    {
        "roll_no": 103,
        "name": "Ravi Kumar",
        "marks": 78,
        "attendance": 80,
        "branch": "MECH",
        "email": "ravi@college.com"
    },
    {
        "roll_no": 104,
        "name": "Pooja Singh",
        "marks": 65,
        "attendance": 70,
        "branch": "CIVIL",
        "email": "pooja@college.com"
    },
    {
        "roll_no": 105,
        "name": "Kiran Desai",
        "marks": 48,
        "attendance": 60,
        "branch": "ENTC",
        "email": "kiran@college.com"
    }
]

def get_status(marks, attendance):
    if marks >= 50 and attendance >= 75:
        return "Pass"
    elif marks >= 50:
        return "Pass - Low Attendance"
    else:
        return "Fail"

# Print all students
print("=== STUDENTS LIST ===")
for s in students:
    status = get_status(s['marks'], s['attendance'])
    print(f"Roll {s['roll_no']}: {s['name']} | {s['branch']} | Marks: {s['marks']} | Att: {s['attendance']}% | Email: {s['email']} | {status}")

def search_student():
    roll = int(input("\nEnter roll no to search: "))
    for s in students:
        if s['roll_no'] == roll:
            print("\nLogin Successful")
            print("\n--- Student Details ---")
            print("Roll No:", s['roll_no'])
            print("Name:", s['name'])
            print("Branch:", s['branch'])
            print("Marks:", s['marks'])
            print("Attendance:", s['attendance'], "%")
            print("Email:", s['email'])
            print("Status:", get_status(s['marks'], s['attendance']))
            return
    print("Not found")

# Ye line add karni thi - function call
search_student()