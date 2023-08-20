from flaskr.controllers import PostController
from werkzeug.exceptions import NotFound


def test_get_posts_empty_list(app):
    controller = PostController()

    posts = controller.get_posts()

    assert len(posts) == 0


def test_get_posts(app):
    controller = PostController()

    for _ in range(3):
        controller.create_post(
            {
                "title": "Title for all posts",
                "content": "Content for all posts",
            }
        )

    posts = controller.get_posts()

    assert len(posts) == 3


def test_get_post_not_found(app):
    controller = PostController()

    try:
        controller.get_post(1)
    except NotFound as e:
        assert e.code == 404
        assert e.name == "Not Found"


def test_get_post(app):
    controller = PostController()

    controller.create_post(
        {
            "title": "Title 1",
            "content": "Content for the post 1",
        }
    )

    post = controller.get_post(1)

    assert post is not None


def test_create_post(app):
    controller = PostController()

    post = controller.create_post(
        {
            "title": "Title 1",
            "content": "Content for the post 1",
        }
    )

    assert post is not None


def test_update_post(app):
    controller = PostController()

    controller.create_post(
        {
            "title": "Title 1",
            "content": "Content for the post 1",
        }
    )

    post = controller.update_post(
        post_data={
            "title": "Updating title 1",
            "content": "Content for the post 1",
        },
        post_id=1,
    )

    assert post.title == "Updating title 1"


def test_delete_post(app):
    controller = PostController()

    controller.create_post(
        {
            "title": "Title 1",
            "content": "Content for the post 1",
        }
    )

    response = controller.delete_post(1)

    assert response.get("message") == "Post deleted."
