import pytest
from seeker_api_foundation import create_app

@pytest.fixture
def app():
    yield create_app({
        "TESTING": True
    })

@pytest.fixture
def client(app):
    yield app.test_client()
