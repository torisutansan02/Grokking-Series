import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q6_deduplicate_user_events import deduplicate_user_events

def test_deduplicate_user_events():
    logs = [
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "purchase"},
        {"userId": "b", "event": "logout"},
        {"userId": "b", "event": "login"}
    ]
    expected = {
        "a": ["login", "purchase"],
        "b": ["login", "logout"]
    }
    assert deduplicate_user_events(logs) == expected
    print("✅ test_deduplicate_user_events passed!")

if __name__ == "__main__":
    test_deduplicate_user_events()
