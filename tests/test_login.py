import pytest
from registration.registration import create_db, add_user
from registration.login import login_user

@pytest.fixture(scope="module")
def setup_database():
    create_db()
    add_user("testlogin", "test@login.com", "123456")
    yield

def test_login_success(setup_database):
    assert login_user("testlogin", "123456") is True

def test_login_wrong_password(setup_database):
    assert login_user("testlogin", "salah") is False

def test_login_nonexistent_user(setup_database):
    assert login_user("tidakada", "123456") is False