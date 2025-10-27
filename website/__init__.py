from flask import Flask

# App Factory
def create_app():
    # App Object
    app = Flask(__name__)

    # App Secret Key Config
    app.config['SECRET_KEY'] = "sperogrp"

    # Returning App
    return app

