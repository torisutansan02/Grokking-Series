# === Q11: Match Clicks to Purchases ===
# Given two lists of logs:
# - clicks: { "userId": str, "timestamp": int }
# - purchases: { "userId": str, "timestamp": int }
#
# Return a list of userIds where:
# - The user clicked AND purchased
# - The purchase happened after the click
# - The time between click and purchase is <= maxDelay
#
# Each click can only match one purchase, and vice versa.
# Output should be sorted alphabetically.

from typing import List, Dict

def match_click_purchase(clicks: List[Dict], purchases: List[Dict], maxDelay: int) -> List[str]:
    matched = []
    used_purchases = set()

    # Preprocess: group purchases by user
    purchase_map = {}
    for i, p in enumerate(purchases):
        user = p["userId"]
        ts = p["timestamp"]
        purchase_map.setdefault(user, []).append((ts, i))  # Track original index for dedup

    for c in clicks:
        user = c["userId"]
        click_time = c["timestamp"]
        if user in purchase_map:
            for ts, idx in sorted(purchase_map[user]):
                if idx in used_purchases:
                    continue
                if ts >= click_time and ts - click_time <= maxDelay:
                    matched.append(user)
                    used_purchases.add(idx)
                    break  # Only one match per click

    return sorted(matched)

# Optional debug run
if __name__ == "__main__":
    clicks = [
        {"userId": "u1", "timestamp": 100},
        {"userId": "u2", "timestamp": 200},
        {"userId": "u3", "timestamp": 300}
    ]

    purchases = [
        {"userId": "u1", "timestamp": 150},
        {"userId": "u2", "timestamp": 300},
        {"userId": "u4", "timestamp": 310}
    ]

    print(match_click_purchase(clicks, purchases, 60))  # ['u1']
