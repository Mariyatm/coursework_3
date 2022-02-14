from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import ValidationError, Schema, fields

from project.services import UserService
from project.tools.jwt_token import JwtSchema, JwtToken
from project.views.users import LoginValidator
from project.setup_db import db


auth_ns = Namespace('auth')
class LoginValidator(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    # role = fields.Str()
    # exp = fields.Float()


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        try:
            data = LoginValidator().load(request.json)
            UserService(db.session).create(**data)
        except ValidationError:
            abort(400)

@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        try:
            data = LoginValidator().load(request.json)
            user = UserService(db.session).get_by_email(data["email"])
            if not user:
                abort(404)
            token_data = JwtSchema().load({"user_id": user.id})
            return JwtToken(token_data).get_tokens(), 201
        except ValidationError:
            abort(400)

    def put(self):
        try:
            refresh_token = request.json["refresh_token"]
            data = JwtToken.decode_token(refresh_token)
            data.pop("exp", None)
            token_data = JwtSchema().load(data)
            user = UserService(db.session).get_one(token_data["user_id"])
            if not user:
                abort(404)
            token_data = JwtSchema().load({"user_id": user.id, "role": user.role})
            return JwtToken(token_data).get_tokens(), 201
        except Exception as e:
            abort(400)
