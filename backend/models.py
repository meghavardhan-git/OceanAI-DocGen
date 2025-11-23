from backend.database import db
from backend.database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    projects = db.relationship("Project", back_populates="user")



class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    project_type = db.Column(db.String(10))     # docx / pptx
    topic = db.Column(db.String(300))

    user = db.relationship("User", back_populates="projects")
    sections = db.relationship("Section", back_populates="project")


class Section(db.Model):
    __tablename__ = "sections"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))

    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    refined_content = db.Column(db.Text)
    feedback = db.Column(db.String(20))
    comments = db.Column(db.Text)

    project = db.relationship("Project", back_populates="sections")
