

from backend.models import Section
from backend.services.llm_service import generate_refined_content
from backend.database import db

def refine_section(section_id, instruction):
    sec = Section.query.get(section_id)

    if not sec:
        return None

    refined = generate_refined_content(instruction, sec.content)
    sec.refined_content = refined
    db.session.commit()

    return refined


def update_feedback(section_id, feedback):
    sec = Section.query.get(section_id)
    sec.feedback = feedback
    db.session.commit()


def add_comment(section_id, comment):
    sec = Section.query.get(section_id)
    sec.comments = (sec.comments or "") + "\n" + comment
    db.session.commit()
