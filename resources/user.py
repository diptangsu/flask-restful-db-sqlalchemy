from flask_restful import Resource
from flask import abort


class UserResource(Resource):

    def get(self, user_id=None):
        '''GET /users/{id} --> get user with id=id
        '''
        if not user_id:
            abort(404)
        # TODO: return User.get(user_id)

    def post(self, user_id=None):
        '''POST /user/ --> add new user
        '''
        if user_id:
            abort(404)
        # TODO: add User
