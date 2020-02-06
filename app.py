from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.security import authinticate, identity
from resources.student import StudentResource
from resources.user import UserResource


app = Flask(__name__)
app.secret_key = '$%^uke45f78v4ei#$%^&ydfg12734vgn35y65o2!@#$&^'
api = Api(app)
jwt = JWT(app, authinticate, identity)


api.add_resource(
    StudentResource,
    '/students/',
    '/students/<int:student_id>/'
)
api.add_resource(
    UserResource,
    '/user/',
    '/users/<int:user_id>/'
)


if __name__ == '__main__':
    app.run(debug=True)
