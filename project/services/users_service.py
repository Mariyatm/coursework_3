from project.dao import UserDAO
from project.tools.security import get_password_hash, check_password
from project.services.base import BaseService


class UserService(BaseService):

    def get_one(self, id):
        return UserDAO(self._db_session).get_one(id)

    def get_by_email(self, email):
        return UserDAO(self._db_session).get_by_email(email)

    def create(self, email, password, name=None, surname=None):
        return UserDAO(self._db_session).create(
            {"email": email,
             "password": get_password_hash(password),
             "name": name,
             "surname": surname
             })

    def update_password(self, id, password_old, password_new):
        user = self.get_one(id)
        if check_password(user.password, password_old):
            return UserDAO(self._db_session).update_pass_hash(
                get_password_hash(password_new)
            )
        raise Exception('Incorrect password')

    def update(self, id, data):
        return UserDAO(self._db_session).update(id, data)
