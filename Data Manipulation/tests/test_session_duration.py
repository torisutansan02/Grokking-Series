import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q10_session_duration import get_users_within_duration

def test_get_users_within_duration():
    logs = [
        {"userId": "u1", "type": "sign-in", "timestamp": "100"},
        {"userId": "u2", "type": "sign-in", "timestamp": "150"},
        {"userId": "u1", "type": "sign-out", "timestamp": "160"},
        {"userId": "u2", "type": "sign-out", "timestamp": "190"},
        {"userId": "u3", "type": "sign-out", "timestamp": "300"}
    ]
    maxDuration = 60
    expected = ["u1", "u2"]
    assert get_users_within_duration(logs, maxDuration) == expected
    print("✅ test_get_users_within_duration passed!")

if __name__ == "__main__":
    test_get_users_within_duration()
