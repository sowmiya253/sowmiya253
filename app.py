from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)

# Temporary data - Replace this with actual database data in the future
products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "This is the first product.",
        "price": 19.99,
        "image": "product1.jpg",
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "This is the second product.",
        "price": 29.99,
        "image": "product2.jpg",
    },
    # Add more products here...
]

# Route for the home page
@app.route("/")
def index():
    # Fetch all products from the database
    with app.app_context():
        products = Product.query.all()
    return render_template("index.html", products=products)

# Route for product details page
@app.route("/product/<int:product_id>")
def product_details(product_id):
    # Fetch the product from the database based on the product_id
    with app.app_context():
        product = Product.query.get(product_id)
    if product:
        return render_template("product_details.html", product=product)
    else:
        return "Product not found!", 404

if __name__ == "__main__":
    # Create the database tables based on the defined models
    with app.app_context():
        db.create_all()
    app.run(debug=True)
