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
        """ Create a new user """
        return controller.create_user(user_data)
