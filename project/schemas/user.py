from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
