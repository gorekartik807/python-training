students = ["kartik", "ajay", "vijay", "suresh"]
rolls = [100, 101, 102, 104]
passwords = [123, 456, 789, 321]
marks = [90, 89, 78, 85]
attendance = [92, 88, 95, 90]
notices = ["Exam on 20th June", "Project submission on 15th June"]

def show_details(name, roll, mark, att):
    print("Name:", name)
    print("Roll:", roll)
    print("Marks:", mark)
    print("Attendance:", att)

user_roll = int(input("Roll No: ")) 
user_pass = int(input("Password: "))     

for i in range(len(students)):
    if rolls[i] == user_roll and passwords[i] == user_pass:
        print("Login Success")
        show_details(students[i], rolls[i], marks[i], attendance[i])
        print("Notice Board:")
        for notice in notices:
            print(" ", notice)
        break
else:
    print("Invalid Login")