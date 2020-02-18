from flask import Flask
from flask_admin import Admin
from flask_jwt import JWT
from flask_restful import Api

from admin import add_admin_views
from auth.security import authenticate, identity
from resources.student import StudentResource
from resources.subject import SubjectResource
from resources.user import UserResource


app = Flask(__name__)
app.config.from_pyfile('config.py')

admin = Admin(app, name='microblog', template_mode='bootstrap3')
add_admin_views(admin)

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
    app.run(debug=True, host='0.0.0.0')
