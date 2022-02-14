from project.dao import FavoriteMoviesrDAO
from project.schemas.favorite_movies import FavoriteMoviesSchema
from project.services.base import BaseService


class FavoriteMoviesService(BaseService):
    def get_by_user(self, user_id):
        ents = FavoriteMoviesrDAO(self._db_session).get_by_user(user_id)
        return FavoriteMoviesSchema(many=True).dump(ents)

    def delete(self, user_id, movie_id):
        FavoriteMoviesrDAO(self._db_session).delete(user_id, movie_id)

    def create(self, user_id, movie_id):
        FavoriteMoviesrDAO(self._db_session).create(user_id, movie_id)
