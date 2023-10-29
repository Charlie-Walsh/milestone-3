import os
from sanctum import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("ID"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )
