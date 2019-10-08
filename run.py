from flaskblog import create_app
from PIL import Image
from flask_bcrypt import Bcrypt
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
