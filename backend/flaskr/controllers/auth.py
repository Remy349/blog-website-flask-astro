from flask_smorest import abort
from flaskr.extensions import db
from flask_jwt_extended import create_access_token, get_jwt_identity

from flaskr.models.user import UserModel


class AuthController:
    def signin(self, user_data):
        user = db.session.execute(
            db.select(UserModel).filter_by(username=user_data["username"])
        ).scalar_one_or_none()

        if user and user.check_password(user_data["password"]):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}

        abort(401, message="Invalid credentials.")

    def profile(self):
        user_id = get_jwt_identity()

        return db.session.execute(
            db.select(UserModel).filter_by(id=user_id)
        ).scalar_one()
