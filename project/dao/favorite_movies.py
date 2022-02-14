from project.dao.models import FavoriteMovies


class  FavoriteMoviesrDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id, movie_id):
        return self.session.query(FavoriteMovies).filter(
            FavoriteMovies.user_id == user_id,
            FavoriteMovies.movie_id == movie_id
        ).one_or_none()

    def get_by_user(self, user_id):
        return self.session.query(FavoriteMovies).filter(
            FavoriteMovies.user_id == user_id
        ).all()

    def create(self, user_id, movie_id):
        ent = FavoriteMovies(user_id=user_id, movie_id=movie_id)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, user_id, movie_id):
        ent = self.get_one(user_id, movie_id)
        self.session.delete(ent)
        self.session.commit()
