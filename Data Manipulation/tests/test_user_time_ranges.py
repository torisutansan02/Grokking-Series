import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q1_user_time_ranges import get_user_time_ranges

def test_user_time_ranges():
    logs = [
        {"userId": "u1", "timestamp": "2025-04-16T12:00:00Z"},
        {"userId": "u1", "timestamp": "2025-04-16T12:05:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:01:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:03:00Z"},
    ]
    expected = {
        "u1": "2025-04-16T12:00:00Z - 2025-04-16T12:05:00Z",
        "u2": "2025-04-16T12:01:00Z - 2025-04-16T12:03:00Z"
    }
    assert get_user_time_ranges(logs) == expected
    print("✅ test_user_time_ranges passed!")

if __name__ == "__main__":
    test_user_time_ranges()
