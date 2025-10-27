# Modules
import os
from settings import env
from utils import errhandler, syshandler


try:
    # Importing App Factory
    from website import create_app

    # App Factory Object
    app = create_app(FLASK_MODE=os.getenv("FLASK_MODE", env.FLASK_MODE))

    # Starting App Server
    if __name__ == "__main__":
        app.run()

# Logging System Start Failed Events
except Exception as e:
    errhandler(e, log="main", path="server")

# Logging System Start Success Events
else:
    syshandler("Application Started", log="main", path="server")