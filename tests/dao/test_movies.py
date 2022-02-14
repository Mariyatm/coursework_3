import pytest

from project.dao import MovieDAO
from project.dao.models import Movie


class TestmovieDAO:
    @pytest.fixture(autouse=True)
    def dao(self, db):
        self.dao = MovieDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(title="фильм1")
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(title="фильм2")
        db.session.add(m)
        db.session.commit()
        return m

    def test_get_one(self, movie_1):
        assert self.dao.get_one(movie_1.id) == movie_1

    def test_get_one_not_found(self):
        assert self.dao.get_one(1) is None

    def test_get_all_movies(self, movie_1, movie_2):
        assert self.dao.get_all() == [movie_1, movie_2]
