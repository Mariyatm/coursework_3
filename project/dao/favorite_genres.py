from project.dao.models import FavoriteGenres


class  FavoriteGenresrDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id, genre_id):
        return self.session.query(FavoriteGenres).filter(
            FavoriteGenres.user_id == user_id,
            FavoriteGenres.genre_id == genre_id
        ).one_or_none()

    def get_by_user(self, user_id):
        return self.session.query(FavoriteGenres).filter(
            FavoriteGenres.user_id == user_id
        ).all()

    def create(self, user_id, genre_id):
        ent = FavoriteGenres(user_id=user_id, genre_id=genre_id)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, user_id, genre_id):
        ent = self.get_one(user_id, genre_id)
        self.session.delete(ent)
        self.session.commit()
