# === Q2: Group Transactions ===
# Given a list of transaction strings representing item names,
# count how many times each item appears.
# Return a list of strings in the format "item count",
# sorted by descending count, then alphabetically by item name.

from typing import List

def group_transactions(transactions: List[str]) -> List[str]:
    count = {}

    for item in transactions:
        count[item] = count.get(item, 0) + 1

    sorted_items = sorted(count.items(), key = lambda x: (-x[1], x[0]))
    
    return [
        f"{item} {amount}"
        for (item, amount) in sorted_items
    ]

if __name__ == "__main__":
    sample = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print(group_transactions(sample))
