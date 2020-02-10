from models.user import User


def authenticate(username, password):
    user = User.get(username=username)
    if user and user.password == password:
        return user


def identity(payload):
    return User.get(id=payload['identity'])
