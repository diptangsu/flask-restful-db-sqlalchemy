from flask import request, abort
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.student import Student


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str
    )
    parser.add_argument(
        'age',
        type=int,
        required=True,
        help="This is a required field"
    )

    # @jwt_required()
    def get(self, student_id=None):
        '''
        GET /students/ -> get all students
        GET /students/{id}/ -> get student with id=id
        '''
        if student_id is not None:
            return Student.get(id=student_id).json() or abort(404)
        else:
            return [
                student.json()
                for student in Student.get()
            ]

    # @jwt_required()
    def post(self):
        '''POST /students/ -> add a new student
        '''
        data = StudentResource.parser.parse_args()
        student_name = data.get('name')
        student_age = data.get('age')

        student = Student(student_name, student_age)
        student.save()

        return student.json(), 201

    # @jwt_required()
    def put(self, student_id=None):
        '''PUT /students/{id} -> update student with id=id
        '''
        data = StudentResource.parser.parse_args()
        name = data.get('name')
        age = data.get('age')

        if student_id is not None:
            student = Student.get(student_id)
            if student:
                if name:
                    student.name = name
                if age:
                    student.age = age
                student.save()
                return student.json()
        else:
            if name and age:
                student = Student(name, age)
                student.save()
                return student.json(), 201

    # @jwt_required()
    def delete(self, student_id=None):
        '''DELETE /students/{id} -> delete student with id=id
        '''
        if student_id is not None:
            Student.get(id=student_id).delete()
            return {'message': 'Student has been deleted'}
        abort(404)
