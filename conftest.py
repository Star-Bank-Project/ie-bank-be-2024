import pytest
from iebank_api import app, db

@pytest.fixture(scope='module')
def test_client():
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table(s)
    db.create_all()

    yield db  # this is where the testing happens!

    db.drop_all()