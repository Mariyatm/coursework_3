from project.dao.models.base import BaseMixin
from project.setup_db import db


class FavoriteMovies(BaseMixin, db.Model):
    __tablename__ = "favorite_movies"

    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    genre = db.relationship("Movie")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")