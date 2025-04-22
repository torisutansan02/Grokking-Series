import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q8_filter_malformed import filter_valid_logs

def test_filter_valid_logs():
    logs = [
        {"userId": "u1", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "u2", "timestamp": "", "action": "logout"},
        {"userId": "u3", "timestamp": "2025-04-01T13:00:00Z", "action": "click"}
    ]
    expected = [
        {"userId": "u1", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "u3", "timestamp": "2025-04-01T13:00:00Z", "action": "click"}
    ]
    assert filter_valid_logs(logs) == expected
    print("✅ test_filter_valid_logs passed!")

if __name__ == "__main__":
    test_filter_valid_logs()
