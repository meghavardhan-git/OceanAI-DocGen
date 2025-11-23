
from flask import Blueprint, jsonify, request
from backend.services.refine_service import refine_section, update_feedback, add_comment


refine_bp = Blueprint("refine_bp", __name__)

@refine_bp.route("/refine/<int:section_id>", methods=["POST"])
def refine(section_id):
    instruction = request.json.get("instruction")
    refined_text = refine_section(section_id, instruction)
    return jsonify({"refined": refined_text})


@refine_bp.route("/feedback/<int:section_id>", methods=["POST"])
def feedback(section_id):
    feedback_value = request.json.get("feedback")
    update_feedback(section_id, feedback_value)
    return jsonify({"message": "Feedback saved"})


@refine_bp.route("/comment/<int:section_id>", methods=["POST"])
def comment(section_id):
    comment = request.json.get("comment")
    add_comment(section_id, comment)
    return jsonify({"message": "Comment saved"})
