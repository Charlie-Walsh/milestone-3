import os
from sanctum import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=os.environ.get("ID"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )