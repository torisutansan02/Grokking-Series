import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q15_normalize_user_names import normalize_user_names

def test_normalize_user_names():
    users = [
        {"userId": "u1", "fullName": "Alice Johnson"},
        {"userId": "u2", "firstName": "Bob", "lastName": "Smith"},
        {"userId": "u3", "firstName": "Charlie"},
        {"userId": "u4", "lastName": "Doe"},
        {"userId": "u5"}
    ]

    expected = [
        {"userId": "u1", "name": "Alice Johnson"},
        {"userId": "u2", "name": "Bob Smith"},
        {"userId": "u3", "name": "Charlie"},
        {"userId": "u4", "name": "Doe"}
    ]

    assert normalize_user_names(users) == expected
    print("✅ test_normalize_user_names passed!")

if __name__ == "__main__":
    test_normalize_user_names()
