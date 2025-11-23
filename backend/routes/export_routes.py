from flask import Blueprint, send_file
from backend.services.export_service import export_docx, export_pptx

export_bp = Blueprint("export_bp", __name__)

@export_bp.route("/docx/<int:project_id>", methods=["GET"])
def download_docx(project_id):
    buffer = export_docx(project_id)
    return send_file(buffer,
                     as_attachment=True,
                     download_name=f"project_{project_id}.docx",
                     mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

@export_bp.route("/pptx/<int:project_id>", methods=["GET"])
def download_pptx(project_id):
    buffer = export_pptx(project_id)
    return send_file(buffer,
                     as_attachment=True,
                     download_name=f"project_{project_id}.pptx",
                     mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation")
