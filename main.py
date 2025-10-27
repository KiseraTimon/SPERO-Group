import os
from settings import env
from website import create_app

# App Object
app = create_app(FLASK_MODE=os.getenv("FLASK_MODE", env.FLASK_MODE))

# Starting Flask Server
if __name__ == "__main__":
    app.run()
