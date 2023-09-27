from flask_login import UserMixin


# Simulate user database
USERS_DB = {}


class User(UserMixin):


    def __init__(self, id_, name, email, id_token):
        self.id = id_
        self.name = name
        self.email = email
        self.id_token = id_token

    def claims(self):
        return {'name': self.name,
                'email': self.email,
                'token_id': self.id_token
                }.items()

    @staticmethod
    def get(user_id):
        return USERS_DB.get(user_id)

    @staticmethod
    def create(user_id, name, email, id_token):
        USERS_DB[user_id] = User(user_id, name, email, id_token)