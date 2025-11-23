from flask import Blueprint, request, jsonify, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models import User
from backend.database import db
from flask_login import LoginManager, login_user, logout_user, login_required

auth_bp = Blueprint("auth_bp", __name__)

# -------- SIGNUP --------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Check if exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    hashed = generate_password_hash(password)
    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


# -------- LOGIN --------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid username or password"}), 401

    login_user(user)
    return jsonify({"message": "Login successful", "user_id": user.id})


# -------- LOGOUT --------
@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})
