import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q2_group_transactions import group_transactions

def test_group_transactions():
    transactions = [
        "apple", "banana", "apple",
        "orange", "banana", "apple"
    ]
    expected = [
        "apple 3",
        "banana 2",
        "orange 1"
    ]
    assert group_transactions(transactions) == expected
    print("✅ test_group_transactions passed!")

if __name__ == "__main__":
    test_group_transactions()
