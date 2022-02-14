from flask import request
from flask_restx import Resource, Namespace

from project.schemas.movie import MovieSchema
from project.services import MovieService
from project.setup_db import db


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page
        }
        all_movies = MovieService(db.session).get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@movies_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        b = MovieService(db.session).get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200
