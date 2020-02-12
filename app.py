from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.security import authenticate, identity
from resources.student import StudentResource
from resources.user import UserResource
from resources.subject import SubjectResource


app = Flask(__name__)
app.secret_key = '$%^uke45f78v4ei#$%^&ydfg12734vgn35y65o2!@#$&^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(
    StudentResource,
    '/students/',
    '/students/<int:student_id>/'
)
api.add_resource(
    UserResource,
    '/users/<int:user_id>/'
)
api.add_resource(
    SubjectResource,
    '/subjects/',
    '/subjects/<int:subject_id>/'
)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
