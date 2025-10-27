from __future__ import annotations
from flask import Flask

# Flask Extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_login import LoginManager

# Custom Packages
from settings import env

# Configurations
from config import Defaults, Production, Development


# Alembic Naming Convention
namingConvention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Metadata Object
meta = MetaData(naming_convention=namingConvention)

# SQLAlchemy Object
db = SQLAlchemy(metadata=meta)

# Migrate Object
migrate = Migrate()

# Login Manager Object
loginManager = LoginManager()

# Variables & Objects Available for Import
__all__ = ['db', 'loginManager', 'migrate', 'create_app']

# App Factory
def create_app(FLASK_MODE: str | None = None):
    mode = (str(FLASK_MODE) or str(env.FLASK_MODE) or "").strip().lower()

    global app
    app = Flask(__name__)

    print(f"FLASK MODE: {mode}")

    # Prod App Config
    if mode == "production":
        app.config.from_object(Production)

    # Dev App Config
    elif mode == "development":
        app.config.from_object(Development)

    # Undefined App Access
    else:
        app.config.from_object(Defaults)

    # Bindings
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    # Login Manager Settings
    loginManager.login_view = ""
    loginManager.login_message = "You are not authorized to view this page"

    loginManager.init_app(app)

    # Importing Blueprints
    from website.modules.authentication.auth import auth
    from website.modules.routing.pages import pages

    # Registering Blueprints
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(pages, url_prefix="/")

    # User Loader
    @loginManager.user_loader
    def loadUser(id: int):
        return None

    try:
        return app

    except Exception as e:
        errhandler(e, log="__init__", path="server")

    else:
        syshandler(F"App Initializer Triggered with Debug Mode: {app.config.get("DEBUG")}", log="__init__", path="server")