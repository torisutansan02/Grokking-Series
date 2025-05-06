# === Q14: Resolve User Conflicts by Timestamp ===
# You're given two lists of user events:
# - sourceA and sourceB each contain:
#     - userId (str)
#     - name (str)
#     - timestamp (int)
#
# For each userId, choose the most recent name based on the highest timestamp.
# If a user only appears in one source, keep that version.
# Return a list of user profiles with 'userId' and 'name', sorted by userId.

from typing import List, Dict

def resolve_user_conflicts(sourceA: List[Dict], sourceB: List[Dict]) -> List[Dict]:
    latest = {}

    for entry in sourceA + sourceB:
        uid = entry["userId"]
        ts = entry["timestamp"]
        name = entry["name"]

        if uid not in latest or ts > latest[uid]["timestamp"]:
            latest[uid] = {"userId": uid, "name": name, "timestamp": ts}

    return sorted(
        [{"userId": v["userId"], "name": v["name"]} for v in latest.values()],
        key=lambda x: x["userId"]
    )

# Optional debug run
if __name__ == "__main__":
    a = [
        {"userId": "u1", "name": "Alice", "timestamp": 100},
        {"userId": "u2", "name": "Bob", "timestamp": 120}
    ]
    b = [
        {"userId": "u1", "name": "Alicia", "timestamp": 130},
        {"userId": "u3", "name": "Charlie", "timestamp": 125}
    ]
    print(resolve_user_conflicts(a, b))
