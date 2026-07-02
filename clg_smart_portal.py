from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

students_data = [
    {"roll": 101, "name": "Rohit Kumar", "marks": 85, "email": "rohit@college.com"},
    {"roll": 102, "name": "Priya Sharma", "marks": 92, "email": "priya@college.com"},
    {"roll": 103, "name": "Aman Singh", "marks": 78, "email": "aman@college.com"},
    {"roll": 104, "name": "Neha Gupta", "marks": 88, "email": "neha@college.com"}
]

@app.route('/')
def home():
    return render_template('home.html', project_name="Student Portal")

@app.route('/records')
def records():
    return render_template('records.html', project_name="Student Portal", students=students_data)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        roll = request.form.get('roll')
        name = request.form.get('name')
        marks = request.form.get('marks')
        email = request.form.get('email')
        
        if not roll or not name or not marks or not email:
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_student'))
        
        try:
            students_data.append({
                "roll": int(roll), 
                "name": name, 
                "marks": int(marks), 
                "email": email
            })
            flash('Student added successfully!', 'success')
            return redirect(url_for('records'))
        except:
            flash('Roll No and Marks must be numbers!', 'danger')
            return redirect(url_for('add_student'))
    
    return render_template('add_student.html', project_name="Student Portal")

@app.route('/about')
def about():
    return render_template('about.html', project_name="Student Portal")

@app.route('/login')
def login():
    return render_template('login.html', project_name="Student Portal")

if __name__ == '__main__':
    app.run(debug=True)