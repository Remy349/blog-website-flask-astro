from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers import UserController
from flaskr.schemas import UserSchema

bp = Blueprint("users", __name__, description="Operations on users")

controller = UserController()


@bp.route("/auth/signup")
class UserSignUp(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(201)
    def post(self, user_data):
        """Create a new user"""
        return controller.create_user(user_data)


@bp.route("/users/<int:user_id>")
class User(MethodView):
    @bp.response(204)
    def delete(self, user_id):
        """Delete a user by ID (Developer only)"""
        return controller.delete_user(user_id)


@bp.route("/users")
class UserList(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        """Get a list of all users (Developer only)"""
        return controller.get_users()
