from project.dao import FavoriteGenresrDAO
from project.schemas.favorite_genres import FavoriteGenresSchema
from project.services.base import BaseService


class FavoriteGenresService(BaseService):
    def get_by_user(self, user_id):
        ents = FavoriteGenresrDAO(self._db_session).get_by_user(user_id)
        return FavoriteGenresSchema(many=True).dump(ents)

    def delete(self, user_id, genre_id):
        FavoriteGenresrDAO(self._db_session).delete(user_id, genre_id)

    def create(self, user_id, genre_id):
        FavoriteGenresrDAO(self._db_session).create(user_id, genre_id)
