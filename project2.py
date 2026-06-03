from flask import Flask

app = Flask(__name__)

# List of dictionaries (Voting Records)
voters = [
    {"id": 101, "name": "kartik sharma", "age": 22, "city": "Nanded", "voted": "Yes"},
    {"id": 102, "name": "ajay shukla", "age": 19, "city": "pune", "voted": "No"},
    {"id": 103, "name": "yogesh more", "age": 20, "city": "nanded", "voted": "Yes"},
    {"id": 104, "name": "yash rajput", "age": 19, "city": "paithan", "voted": "Yes"},
    {"id": 105, "name": "sunita patil", "age": 18, "city": "pune", "voted": "No"}
]

# Route 1 - Homepage
@app.route("/")
def home():
    return """
    <h1>ONLINE VOTING SYSTEM</h1>
    <p>This project is used for online voting and voter record management.</p>
    """

# Route 2 - Records Page
@app.route("/records")
def records():
    output = "<h2>Voter Records</h2>"
    
    for voter in voters:
        output += f"""
        <p>
        ID: {voter['id']} <br>
        Name: {voter['name']} <br>
        City: {voter['city']} <br>
        Voted: {voter['voted']}
        </p>
        <hr>
        """
    return output

# Route 3 - Voting Status
@app.route("/status")
def status():
    total_voters = len(voters)
    voted_count = 0
    
    for voter in voters:
        if voter["voted"] == "Yes":
            voted_count += 1
            
    return f"""
    <h2>Voting Status</h2>
    Total Voters: {total_voters}<br>
    Votes Cast: {voted_count}
    """

if __name__ == "__main__":
    app.run(debug=True)