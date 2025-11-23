from flask import Flask
from flask_cors import CORS
from backend.database import db ,init_db
from backend.routes.project_routes import project_bp
from backend.routes.refine_routes import refine_bp
from flask_login import LoginManager
from backend.routes.setup_routes import setup_bp
from backend.auth import auth_bp
from flask import render_template
from backend.models import User
from backend.routes.export_routes import export_bp

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
init_db(app)
app.config["SESSION_COOKIE_SECURE"] = False
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_HTTPONLY"] = False

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(project_bp, url_prefix="/project")
app.register_blueprint(refine_bp, url_prefix="/section")
app.register_blueprint(setup_bp, url_prefix="/setup")
app.register_blueprint(export_bp, url_prefix="/export")

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup-page")
def signup_page():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
