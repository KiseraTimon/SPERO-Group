from flask import Blueprint

# Blueprint Object
pages = Blueprint("pages", __name__)

# Homepage
@pages.route("/", methods=['GET'])
def homepage():
    return "Home route is ready"

# About
@pages.route("/about", methods=['GET'])
def about():
    return "About route is ready"

# Services
@pages.route("/services", methods=['GET'])
def services():
    return "Services route is working"

# Products
@pages.route("/products", methods=['GET'])
def products():
    return "Products route is working"

# Careers
@pages.route("/careers", methods=['GET'])
def careers():
    return "Careers route is working"

# Contact
@pages.route("/contact", methods=['GET'])
def contact():
    return "Contact route is working"

# Blogs/Updates
@pages.route("/blogs", methods=['GET'])
def blogs():
    return "Blogs & updates route is working"