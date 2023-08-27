import sqlalchemy as sa
from flaskr.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(80), nullable=False, unique=True)
    password = sa.Column(sa.String(180), nullable=False)

    posts = db.relationship(
        "PostModel",
        back_populates="user",
        lazy="dynamic",
        cascade="all, delete",
    )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
