from flask import request, abort
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.subject import Subject


class SubjectResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str
    )

    # @jwt_required()
    def get(self, subject_id=None):
        '''
        GET /subjects/ -> get all subjects
        GET /subjects/{id}/ -> get subject with id=id
        '''
        if subject_id is not None:
            try:
                return Subject.get(id=subject_id).json()
            except:
                abort(404)
        else:
            return [
                subject.json()
                for subject in Subject.get()
            ]

    # @jwt_required()
    def post(self):
        '''POST /subjects/ -> add a new subject
        '''
        data = subjectResource.parser.parse_args()
        subject_name = data.get('name')
        subject_age = data.get('age')

        subject = Subject(subject_name, subject_age)
        subject.save()

        return subject.json(), 201
