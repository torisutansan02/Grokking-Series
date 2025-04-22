import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q5_flatten_user_logs import flatten_user_logs

def test_flatten_user_logs():
    logs = [
        {"user": {"id": "1", "name": "Alice"}, "action": "login"},
        {"user": {"id": "2", "name": "Bob"}, "action": "logout"}
    ]
    expected = [
        {"userId": "1", "userName": "Alice", "action": "login"},
        {"userId": "2", "userName": "Bob", "action": "logout"}
    ]
    assert flatten_user_logs(logs) == expected
    print("✅ test_flatten_user_logs passed!")

if __name__ == "__main__":
    test_flatten_user_logs()
