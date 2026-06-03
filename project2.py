from flask import Flask

app = Flask(_name_)

# Product data (list of dictionaries)
products = [
    {"id": 101, "name": "Laptop", "price": 45000},
    {"id": 102, "name": "Mobile", "price": 18000},
    {"id": 103, "name": "Headphones", "price": 2000}
]

# Route 1 - Home Page
@app.route('/')
def home():
    return """
    <h1>Online Store Project</h1>
    <p>Welcome to our Flask-based Online Store Application.</p>
    """

# Route 2 - Products Page
@app.route('/products')
def products_page():
    result = "<h2>Available Products</h2><ul>"

    for product in products:
        result += f"""
        <li>
        Product ID: {product['id']} |
        Name: {product['name']} |
        Price: ₹{product['price']}
        </li>
        """

    result += "</ul>"
    return result

# Route 3 - Contact Page
@app.route('/contact')
def contact():
    return """
    <h2>Contact Us</h2>
    <p>Email: store@gmail.com</p>
    <p>Phone: +91 9876543210</p>
    """

# Run the Flask App
if _name_ == '_main_':
    app.run(debug=True)