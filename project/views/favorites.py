from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import FavoriteGenresService, FavoriteMoviesService
from project.schemas.favorite_movies import FavoriteMoviesSchema
from project.schemas.favorite_genres import FavoriteGenresSchema
from project.setup_db import db
from project.tools.auth import login_required

favorites_ns = Namespace("favorites")


@favorites_ns.route("/movies")
class directorsView(Resource):
    @login_required
    def get(self, token_data):
        user_id = token_data["user_id"]
        return FavoriteMoviesSchema(many=True).dump(
            FavoriteMoviesService(db.session).get_by_user(user_id)
        )


@favorites_ns.route("/movie/<int:movie_id>")
class directorsView(Resource):
    @login_required
    def post(self, movie_id, token_data):
        # try:
        user_id = token_data["user_id"]
        print(user_id)
        FavoriteMoviesService(db.session).create(user_id, int(movie_id))
        # except:
        #     abort(400)

    def delete(self, movie_id, token_data):
        try:
            user_id = token_data["user_id"]
            FavoriteMoviesService(db.session).delete(user_id, movie_id)
        except:
            abort(400)


@favorites_ns.route("/genres")
class directorsView(Resource):
    @login_required
    def get(self, token_data):
        user_id = token_data["user_id"]
        return FavoriteGenresSchema(many=True).dump(
            FavoriteGenresService(db.session).get_by_user(user_id)
        )


@favorites_ns.route("/genre/<int:genre_id>")
class directorsView(Resource):
    @login_required
    def post(self, genre_id, token_data):
        try:
            user_id = token_data["user_id"]
            FavoriteGenresService(db.session).create(user_id, genre_id)
        except:
            abort(400)

    def delete(self, genre_id, token_data):
        try:
            user_id = token_data["user_id"]
            FavoriteGenresService(db.session).delete(user_id, genre_id)
        except:
            abort(400)
