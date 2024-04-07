import pytest

@pytest.fixture(scope="module")
def user_data():
    users = {
        "Alice": {"age": 20, "email": "alice@example.com"},
        "Bob": {"age": 25, "email": "bob@example.com"},
        "Charlie": {"age": 30, "email": "charlie@example.com"}
    }

    print("\nsetup")
    yield users
    print("\nteardown")

def test_user_data(user_data):
    assert "Alice" in user_data
    assert user_data["Bob"]["age"] == 25
    assert user_data["Charlie"]["email"] == "charlie@example.com"


