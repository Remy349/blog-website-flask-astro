from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flaskr.schemas import UserSchema
from flaskr.controllers import AuthController

bp = Blueprint("auth", __name__, description="Authentication with JWT")

controller = AuthController()


@bp.route("/auth/signin")
class SignIn(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(200)
    def post(self, user_data):
        """Sign In and create access token"""
        return controller.signin(user_data)


@bp.route("/auth/profile")
class Profile(MethodView):
    @jwt_required()
    @bp.response(200, UserSchema)
    def get(self):
        """Get user´s profile usign the access token"""
        return controller.profile()
