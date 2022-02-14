from .genre import GenreDAO
from .movie import MovieDAO
from .director import DirectorDAO
from .user import UserDAO
from .favorite_movies import FavoriteMoviesrDAO
from .favorite_genres import FavoriteGenresrDAO

__all__ = [
    "GenreDAO",
    "MovieDAO",
    "DirectorDAO",
    "UserDAO",
    "FavoriteMoviesrDAO",
    "FavoriteGenresrDAO"
]
