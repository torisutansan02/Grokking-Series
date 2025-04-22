import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q9_aggregate_expenses import aggregate_monthly_expenses

def test_aggregate_monthly_expenses():
    expenses = [
        {"userId": "alice", "amount": 10.0, "date": "2025-04-01"},
        {"userId": "alice", "amount": 20.0, "date": "2025-04-15"},
        {"userId": "bob", "amount": 5.0, "date": "2025-04-10"},
        {"userId": "bob", "amount": 7.5, "date": "2025-05-01"}
    ]
    expected = {
        "alice": {
            "2025-04": 30.0
        },
        "bob": {
            "2025-04": 5.0,
            "2025-05": 7.5
        }
    }
    assert aggregate_monthly_expenses(expenses) == expected
    print("✅ test_aggregate_monthly_expenses passed!")

if __name__ == "__main__":
    test_aggregate_monthly_expenses()
