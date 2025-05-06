import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q12_normalize_logs import normalize_logs

def test_normalize_logs():
    logs = [
        {"userId": "u1", "timestamp": 100, "eventType": "click", "metadata": {"elementId": "btn-1"}},
        {"userId": "u2", "timestamp": 110, "eventType": "view", "metadata": {"page": "home"}},
        {"userId": "u3", "timestamp": 120, "eventType": "click", "metadata": {}},
        {"userId": "u4", "timestamp": 130, "eventType": "view"}
    ]
    expected = [
        {"userId": "u1", "timestamp": 100, "type": "click", "details": "btn-1"},
        {"userId": "u2", "timestamp": 110, "type": "view", "details": "home"}
    ]
    assert normalize_logs(logs) == expected
    print("✅ test_normalize_logs passed!")

if __name__ == "__main__":
    test_normalize_logs()
