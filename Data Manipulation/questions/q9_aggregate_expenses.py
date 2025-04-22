# === Q9: Aggregate Monthly Expenses ===
# Given a list of expense records with:
# - userId (str)
# - amount (float)
# - date (YYYY-MM-DD)
#
# Return a dictionary mapping each user to another dictionary
# of monthly totals in the format:
#
# {
#     "userA": {
#         "2025-04": 50.0,
#         "2025-05": 12.5
#     },
#     "userB": {
#         "2025-04": 20.0
#     }
# }

from typing import List, Dict

def aggregate_monthly_expenses(expenses: List[Dict]) -> Dict[str, Dict[str, float]]:
    # Your implementation here
    pass

# Optional debug test
if __name__ == "__main__":
    sample = [
        {"userId": "alice", "amount": 10.0, "date": "2025-04-01"},
        {"userId": "alice", "amount": 20.0, "date": "2025-04-15"},
        {"userId": "bob", "amount": 5.0, "date": "2025-04-10"},
        {"userId": "bob", "amount": 7.5, "date": "2025-05-01"},
    ]
    print(aggregate_monthly_expenses(sample))
