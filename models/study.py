from db import db


class Study(db.Model):
    __tablename__ = 'Studies'

    student_id = db.Column(db.Integer, db.ForeignKey('Student.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('Subject.id'))

    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id