from flaskr.extensions import db
from flask_smorest import abort

from flaskr.models import UserModel


class UserController:
    def get_users(self):
        return db.session.execute(db.select(UserModel)).scalars()

    def get_user(self, user_id):
        return db.get_or_404(UserModel, user_id)

    def create_user(self, user_data):
        if db.session.execute(
            db.select(UserModel).filter_by(username=user_data["username"])
        ).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(username=user_data["username"])
        user.set_password(user_data["password"])

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}

    def delete_user(self, user_id):
        user = db.get_or_404(UserModel, user_id)

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted."}
