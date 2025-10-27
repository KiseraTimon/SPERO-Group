from flask import Blueprint

# Blueprint Object
auth = Blueprint("auth", __name__)


# Signin
@auth.route("/signin")
def signin():
    return "Signin route is working"

# Signup
@auth.route("/signup")
def signup():
    return "Signup route is working"

# Logout
@auth.route("/logout", methods=['GET'])
def logout():
    return "Logout route is working"

# Verification
@auth.route("/verify")
def verify():
    return "Verification route is working"

# Password Reset
@auth.route("/reset")
def reset():
    return "Password reset route is working"