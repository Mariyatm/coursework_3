from .genres import genres_ns
from .movies import movies_ns
from .directors import directors_ns
from .users import user_ns
from .auth import auth_ns
from .favorites import favorites_ns

__all__ = [
    "genres_ns",
    "movies_ns",
    "directors_ns",
    "user_ns",
    "auth_ns",
    "favorites_ns"
]
