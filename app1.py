from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {"roll": 1, "name": "Rohit", "email": "rohit@test.com", "password": "123", "marks": 85},
    {"roll": 2, "name": "Priya", "email": "priya@test.com", "password": "456", "marks": 90},
    {"roll": 3, "name": "Amit", "email": "amit@test.com", "password": "789", "marks": 78}
]

@app.route('/')
def home():
    return render_template('home.html', project_name="Student Portal")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for student in students:
            if student['email'] == email and student['password'] == password:
                return redirect(url_for('records'))
        return "Invalid email or password"
    return render_template('login.html', project_name="Student Portal")

@app.route('/records')
def records():
    return render_template('records.html', project_name="Student Portal", students=students)

if __name__ == '__main__':
    app.run(debug=True)