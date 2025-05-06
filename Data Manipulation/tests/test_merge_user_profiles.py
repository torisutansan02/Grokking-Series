import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q13_merge_user_profiles import merge_user_profiles

def test_merge_user_profiles():
    basic = [
        {"userId": "u1", "email": "a@example.com"},
        {"userId": "u2", "email": "b@example.com"}
    ]
    extended = [
        {"userId": "u1", "name": "Alice"},
        {"userId": "u3", "name": "Charlie"}
    ]

    expected = [
        {"userId": "u1", "email": "a@example.com", "name": "Alice"},
        {"userId": "u2", "email": "b@example.com"},
        {"userId": "u3", "name": "Charlie"}
    ]

    assert merge_user_profiles(basic, extended) == expected
    print("✅ test_merge_user_profiles passed!")

if __name__ == "__main__":
    test_merge_user_profiles()
