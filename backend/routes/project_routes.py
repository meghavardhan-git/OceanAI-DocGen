from flask import Blueprint, jsonify, request
from backend.services.project_service import generate_content_for_project
from backend.models import Project, Section
from backend.database import db

project_bp = Blueprint("project_bp", __name__)

@project_bp.route("/generate/<int:project_id>", methods=["POST"])
def generate(project_id):
    msg = generate_content_for_project(project_id)
    return jsonify({"message": msg})
@project_bp.route("/<int:project_id>/sections", methods=["GET"])
def get_project_sections(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    sections = Section.query.filter_by(project_id=project_id).all()

    data = {
        "project_id": project.id,
        "topic": project.topic,
        "project_type": project.project_type,
        "sections": []
    }

    for sec in sections:
        data["sections"].append({
            "id": sec.id,
            "title": sec.title,
            "content": sec.content,
            "refined_content": sec.refined_content,
            "feedback": sec.feedback,
            "comments": sec.comments
        })

    return jsonify(data)
