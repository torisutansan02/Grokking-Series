import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q4_active_streak import get_active_streak_users

def test_active_streak_users():
    logs = [
        "alice 2025-04-01",
        "alice 2025-04-02",
        "alice 2025-04-02",
        "bob 2025-04-01",
        "bob 2025-04-03",
        "carol 2025-04-10",
        "carol 2025-04-11",
        "carol 2025-04-12",
        "carol 2025-04-14"
    ]
    expected = ["carol"]
    assert get_active_streak_users(logs, 3) == expected
    print("✅ test_active_streak_users passed!")

if __name__ == "__main__":
    test_active_streak_users()