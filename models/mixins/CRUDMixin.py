from db import db


class CRUDMixin:
    '''Mixin class to add CRUD operations to Model classes
    '''
    @classmethod
    def get(cls, **kwargs):
        if kwargs:
            return cls.query.filter_by(**kwargs).first_or_404()
        else:
            return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
