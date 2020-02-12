from db import db
from models.mixins.CRUDMixin import CRUDMixin


class User(db.Model, CRUDMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'{self.username}'
