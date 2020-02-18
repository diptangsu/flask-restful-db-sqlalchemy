from db import db
from models.mixins.CRUDMixin import CRUDMixin
from models.study import Study


class Student(db.Model, CRUDMixin):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.id}: {self.name}'

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'subjects': [
                s.subject.json()
                for s in Study.query.filter_by(student_id=self.id)
            ]
        }
