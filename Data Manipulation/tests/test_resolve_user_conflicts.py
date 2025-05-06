import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q14_resolve_user_conflicts import resolve_user_conflicts

def test_resolve_user_conflicts():
    sourceA = [
        {"userId": "u1", "name": "Alice", "timestamp": 100},
        {"userId": "u2", "name": "Bob", "timestamp": 120}
    ]
    sourceB = [
        {"userId": "u1", "name": "Alicia", "timestamp": 130},
        {"userId": "u3", "name": "Charlie", "timestamp": 125}
    ]

    expected = [
        {"userId": "u1", "name": "Alicia"},
        {"userId": "u2", "name": "Bob"},
        {"userId": "u3", "name": "Charlie"}
    ]

    assert resolve_user_conflicts(sourceA, sourceB) == expected
    print("✅ test_resolve_user_conflicts passed!")

if __name__ == "__main__":
    test_resolve_user_conflicts()
