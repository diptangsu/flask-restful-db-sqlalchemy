from db import db
from models.mixins import CRUDMixin


class Study(db.Model):

    __tablename__ = 'Studies'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Students.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('Subjects.id'))

    student = db.relationship('Student')
    subject = db.relationship('Subject')

    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id

    def __repr__(self):
        return f'{self.student}: {self.subject}'
