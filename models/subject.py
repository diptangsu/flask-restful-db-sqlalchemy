from db import db
from models.mixins.CRUDMixin import CRUDMixin


class Subject(db.Model, CRUDMixin):

    __tablename__ = 'Subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.id}: {self.name}'

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
