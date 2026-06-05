from flask import Flask, render_template

app = Flask(__name__)

# Student records - list of dictionaries
students_data = [
    {"roll": 101, "name": "Rohit Kumar", "marks": 85},
    {"roll": 102, "name": "Priya Sharma", "marks": 92},
    {"roll": 103, "name": "Aman Singh", "marks": 78},
    {"roll": 104, "name": "Neha Gupta", "marks": 88}
]

# Route 1: Homepage - project name + description
@app.route('/')
def home():
    return render_template('home.html', project_name="Student Portal")

# Route 2: Records page - list of dictionaries
@app.route('/records')
def records():
    return render_template('records.html', project_name="Student Portal", students=students_data)

# Route 3: Extra route - About page
@app.route('/about')
def about():
    return render_template('about.html', project_name="Student Portal")

# Route 4: Login page - bonus
@app.route('/login')
def login():
    return render_template('login.html', project_name="Student Portal")

if __name__ == '__main__':
    app.run(debug=True)