import os
from flask import Flask
from flask_jwt_extended import JWTManager
from app.models import db
from routes.auth import authBp
from routes.books import bookBp
from routes.reviews import reviewBp
from dotenv import load_dotenv
app = Flask(__name__)

# Inits
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

# configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'bookReview.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Init Database and JWT
db.init_app(app)
jwt = JWTManager(app)


# Register Blueprints
app.register_blueprint(authBp)
app.register_blueprint(bookBp)
app.register_blueprint(reviewBp)

# default / main route
@app.route('/')
def index():
    return "Book Review API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=3100, host='0.0.0.0')