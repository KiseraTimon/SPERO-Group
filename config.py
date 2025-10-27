import os
from settings import env

DB_USER = os.getenv("DB_USER", env.DB_USER)
DB_PASS = os.getenv("DB_PASSWORD", env.DB_PASS)
DB_HOST = os.getenv("DB_HOST", env.DB_HOST)
DB_NAME = os.getenv("DB_NAME", env.DB_NAME)
DB_PORT = os.getenv("DB_PORT", env.DB_PORT)
DB_URL = (f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4") or env.SQLALCHEMY_DATABASE_URI

class Defaults:
    # App Settings
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False
    TESTING = True
    SECRET_KEY=env.SECRET_KEY

    # Mail Settings
    MAIL_SERVER =  os.getenv("MAIL_SERVER", env.MAIL_SERVER)
    MAIL_PORT = os.getenv("MAIL_PORT", env.MAIL_PORT)
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", env.MAIL_USE_TLS)
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", env.MAIL_USE_SSL)
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", env.MAIL_USERNAME)
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", env.MAIL_PASSWORD)
    MAIL_SENDER = os.getenv("MAIL_SENDER", env.MAIL_SENDER)
    MAIL_RECEIVER = ''
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", env.MAIL_DEFAULT_SENDER)
    MAIL_MAX_EMAILS = os.getenv("MAIL_MAX_EMAILS", env.MAIL_MAX_EMAILS)
    MAIL_ASCII_ATTACHMENTS = os.getenv("MAIL_ASCII_ATTACHMENTS", env.MAIL_ASCII_ATTACHMENTS)

    # Upload Settings
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", env.UPLOAD_FOLDER)
    BASE_DIR = env.BASE_DIR

class Development(Defaults):
    DEBUG=True
    TEMPLATES_AUTO_RELOAD=True
    TESTING=False
    MAIL_SUPPRESS_SEND = False
    SQLALCHEMY_DATABASE_URI = env.SQLALCHEMY_DATABASE_URI
    WKHTMLTOPDF_BIN_PATH = env.WKHTMLTOPDF_BIN_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = env.SQLALCHEMY_TRACK_MODIFICATIONS
    SQLALCHEMY_ENGINE_OPTIONS={
        "pool_size": env.SQLALCHEMY_POOL_SIZE or 10,
        "max_overflow": env.SQLALCHEMY_MAX_OVERFLOW or 20,
        "pool_timeout": env.SQLALCHEMY_POOL_TIMEOUT or 20,
        "pool_recycle": env.SQLALCHEMY_POOL_RECYCLE or 300,
        "pool_pre_ping": env.SQLALCHEMY_POOL_PRE_PING or True,
        "pool_use_lifo": env.SQLALCHEMY_POOL_USE_LIFO or True,
        "echo_pool": env.SQLALCHEMY_ECHO_POOL or False,
        "echo": env.SQLALCHEMY_ECHO or False
    }
    PRESERVE_CONTEXT_ON_EXCEPTION=False

class Production(Defaults):
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    WKHTMLTOPDF_BIN_PATH = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS={
        "pool_size": os.getenv("SQLALCHEMY_POOL_SIZE", env.SQLALCHEMY_POOL_SIZE,),
        "max_overflow": os.getenv("SQLALCHEMY_MAX_OVERFLOW", env.SQLALCHEMY_MAX_OVERFLOW,),
        "pool_timeout": os.getenv("SQLALCHEMY_POOL_TIMEOUT", env.SQLALCHEMY_POOL_TIMEOUT,),
        "pool_recycle": os.getenv("SQLALCHEMY_POOL_RECYCLE", env.SQLALCHEMY_POOL_RECYCLE, ),
        "pool_pre_ping": os.getenv("SQLALCHEMY_POOL_PRE_PING", env.SQLALCHEMY_POOL_PRE_PING),
        "pool_use_lifo": os.getenv("SQLALCHEMY_POOL_USE_LIFO", env.SQLALCHEMY_POOL_USE_LIFO),
        "echo_pool": os.getenv("SQLALCHEMY_ECHO_POOL", env.SQLALCHEMY_ECHO_POOL),
        "echo": os.getenv("SQLALCHEMY_ECHO", env.SQLALCHEMY_ECHO)
    }
    PRESERVE_CONTEXT_ON_EXCEPTION=False