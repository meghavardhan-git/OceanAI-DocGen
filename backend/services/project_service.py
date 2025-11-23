
from backend.models import Project, Section
from backend.services.llm_service import generate_section_content
from backend.database import db


def generate_content_for_project(project_id):
    project = Project.query.get(project_id)
    sections = Section.query.filter_by(project_id=project_id).all()

    if not project or not sections:
        return "Project or sections missing."

    for sec in sections:
        content = generate_section_content(sec.title, project.topic)
        sec.content = content

    db.session.commit()
    return "Content generation complete."
