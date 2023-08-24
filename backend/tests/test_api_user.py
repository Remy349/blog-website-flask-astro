from flaskr.controllers import UserController
from werkzeug.exceptions import HTTPException


def test_do_not_create_user_twice(app):
    controller = UserController()

    try:
        for _ in range(2):
            controller.create_user(
                {
                    "username": "user1",
                    "password": "user1234",
                }
            )
    except HTTPException as e:
        assert e.code == 409


def test_create_user(app):
    controller = UserController()

    user = controller.create_user(
        {
            "username": "user1",
            "password": "user1234",
        }
    )

    assert user.get("message") == "User created successfully."
