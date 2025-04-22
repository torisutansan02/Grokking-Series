# === Q2: Group Transactions ===
# Given a list of transaction strings representing item names,
# count how many times each item appears.
# Return a list of strings in the format "item count",
# sorted by descending count, then alphabetically by item name.

from typing import List

def group_transactions(transactions: List[str]) -> List[str]:
    # Empty hash map for item count
    count = {}

    # Iterate through items in transactions
    for item in transactions:
        count[item] = 1 + count.get(item, 0)
    
    sorted_count = sorted(count.items(), key = lambda x: (-x[1], x[0]))

    # "item count"
    return [
        f"{item} {amount}"
        for (item, amount) in sorted_count
    ]

if __name__ == "__main__":
    sample = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print(group_transactions(sample))
