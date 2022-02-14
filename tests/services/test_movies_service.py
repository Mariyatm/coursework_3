from unittest.mock import Mock, patch

import pytest

from project.dao.models import Movie
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.services import MovieService


class TestmoviesService:
    @pytest.fixture(autouse=True)
    def service(self, db):
        self.service = MovieService(db.session)

    @pytest.fixture
    def movie(self):
        return Movie(id=1, title="movie_1")

    @pytest.fixture
    def movie_dao_mock(self, movie):
        with patch("project.services.movies_service.MovieDAO") as mock:
            mock.return_value = Mock(
                get_one=Mock(return_value=movie),
                get_all=Mock(return_value=[movie])
            )
            yield mock

    def test_get_all_movies(self, movie_dao_mock, movie):
        assert self.service.get_all() == [movie]
        movie_dao_mock().get_all.assert_called_once()

    def test_get_item_by_id(self, movie_dao_mock, movie):
        assert self.service.get_one(movie.id) == movie
        movie_dao_mock().get_one.assert_called_once_with(movie.id)

    def test_get_item_by_id_not_found(self, movie_dao_mock):
        movie_dao_mock().get_one.return_value = None

        with pytest.raises(ItemNotFound):
            self.service.get_one(1)
