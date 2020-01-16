from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'test', 'name': 'testman', 'password': '111111'},
    {'id':'Michael', 'username': 'Michael', 'password': '123456'}
]

def getUser(user_id):
    for user in users:
        if user_id == user['id']:
            return user