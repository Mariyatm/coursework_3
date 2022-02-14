from project.dao.models import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(User).get(id)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, id, data):
        user = self.get_one(id)
        if data.get("name"):
            user.name = data.get("name")
        if data.get("surname"):
            user.surname = data.get("surname")
        self.session.add(user)
        self.session.commit()

    def update_pass_hash(self, id, phash):
        user = self.get_one(id)
        user.password = phash
        self.session.add(user)
        self.session.commit()
