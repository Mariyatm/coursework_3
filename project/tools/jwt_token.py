from calendar import timegm
import jwt
from marshmallow import Schema, fields
from datetime import timedelta, datetime
from flask import current_app

class JwtSchema(Schema):
    user_id = fields.Int(required=True)
    # role = fields.Str(required=True)


class JwtToken:
    def __init__(self, data):
        self.data = data
        self.now = datetime.now()
        self.access_token_expiration = 10
        self.refresh_token_expiration = 30

    def _get_token(self, time_delta):
        self.data["exp"] = timegm((self.now + time_delta).timetuple())
        return jwt.encode(self.data, current_app.config["SECRET_KEY"], algorithm="HS256")

    @property
    def acess_token(self):
        return self._get_token(timedelta(minutes=self.access_token_expiration))

    @property
    def refresh_token(self):
        return self._get_token(timedelta(days=self.refresh_token_expiration))

    def get_tokens(self):
        return {"acess_token": self.acess_token, "refresh_token": self.refresh_token}

    @staticmethod
    def decode_token(token):
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])



