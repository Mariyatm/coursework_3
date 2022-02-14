from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError

from project.schemas.user import UserSchema
from project.services import UserService
from project.tools.auth import login_required
from project.setup_db import db

user_ns = Namespace('user')


class LoginValidator(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    # role = fields.Str()
    # exp = fields.Float()


@user_ns.route('/')
class UserView(Resource):
    @login_required
    def get(self, token_data):
        return UserSchema().dump(UserService(db.session).get_one(token_data["user_id"]))

    @login_required
    def patch(self, token_data):
        try:
            data = request.json
            user_id = token_data["user_id"]
            UserService(db.session).update(user_id, data)
        except:
            abort(400)

@user_ns.route('/password')
class UserPasswordView(Resource):
    @login_required
    def put(self, token_data):
        try:
            data = request.json
            password_1 = data["password_1"]
            password_2 = data["password_2"]
            user_id = token_data["user_id"]
            UserService(db.session).update_password(user_id, password_1, password_2)
        except:
            abort(400)
