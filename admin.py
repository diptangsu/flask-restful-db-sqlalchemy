from flask_admin.contrib.sqla import ModelView

from db import db

from models.student import Student
from models.study import Study
from models.subject import Subject
from models.user import User


def add_admin_views(admin):
    admin.add_view(ModelView(Student, db.session))
    admin.add_view(ModelView(Study, db.session))
    admin.add_view(ModelView(Subject, db.session))
    admin.add_view(ModelView(User, db.session))
