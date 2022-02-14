from project.dao.models.base import BaseMixin
from project.setup_db import db


class FavoriteGenres(BaseMixin, db.Model):
    __tablename__ = "favorite_genres"

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")

