import pytest

from flaskblog import create_app, db


@pytest.fixture
def app():
    app = create_app()
    app.app_context().push()

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
