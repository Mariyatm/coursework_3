from marshmallow import fields, Schema


class FavoriteGenresSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    genre_id = fields.Int(required=True)
