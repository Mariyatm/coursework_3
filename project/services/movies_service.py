from project.dao import MovieDAO
from project.services.base import BaseService
from project.exceptions import ItemNotFound

class MovieService(BaseService):
    def get_one(self, bid):
        movie =  MovieDAO(self._db_session).get_one(bid)
        if not movie:
            raise ItemNotFound
        return movie

    def get_all(self, filters={"status": None, "page": None}):
        if  filters.get("status") == "new":
            movies = MovieDAO(self._db_session).get_new(filters.get("page"))
        else:
            movies = MovieDAO(self._db_session).get_all(filters.get("page"))
        return movies

    def create(self, movie_d):
        return MovieDAO(self._db_session).create(movie_d)

    def delete(self, rid):
        self.MovieDAO(self._db_session).delete(rid)
