from db import db


class Student(db.Model):

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
            'age': self.age
        }

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
