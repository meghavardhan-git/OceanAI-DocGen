from flask import Blueprint, jsonify, request
from backend.database import db
from backend.models import User, Project, Section

setup_bp = Blueprint("setup_bp", __name__)


@setup_bp.route("/create_project", methods=["GET","POST"])
def create_project():
    data = request.json

    username = data.get("username")
    password = data.get("password")
    topic = data.get("topic")
    project_type = data.get("project_type")
    section_titles = data.get("sections")

    # 1. create user (if not exists)
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

    # 2. create project
    project = Project(
        user_id=user.id,
        topic=topic,
        project_type=project_type
    )
    db.session.add(project)
    db.session.commit()

    # 3. create sections
    for title in section_titles:
        sec = Section(
            project_id=project.id,
            title=title,
            content="Initial placeholder..."
        )
        db.session.add(sec)

    db.session.commit()

    return jsonify({
        "message": "Project created successfully",
        "project_id": project.id
    })
