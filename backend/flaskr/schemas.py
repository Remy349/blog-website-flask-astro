from marshmallow import Schema, fields


class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PostSchema(PlainPostSchema):
    user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)


class PostUpdateSchema(Schema):
    title = fields.Str()
    content = fields.Str()


class UserSchema(PlainUserSchema):
    posts = fields.List(fields.Nested(PlainPostSchema()), dump_only=True)
