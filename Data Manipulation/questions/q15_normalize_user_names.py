# === Q15: Normalize Optional Name Fields ===
# Each user may have: userId, fullName, firstName, lastName
# Return users with:
# - userId
# - name (prefer fullName if available, otherwise build from first + last)
# Skip users that have no name fields.

from typing import List, Dict

def normalize_user_names(users: List[Dict]) -> List[Dict]:
    res = []

    for user in users:
        uid = user.get("userId")
        full = user.get("fullName")
        first = user.get("firstName", "")
        last = user.get("lastName", "")

        if full:
            name = full
        elif first or last:
            name = f"{first} {last}".strip()
        else:
            continue

        res.append({"userId": uid, "name": name})
    
    return sorted(res, key = lambda x: x["userId"])

# Optional debug run
if __name__ == "__main__":
    users = [
        {"userId": "u1", "fullName": "Alice Johnson"},
        {"userId": "u2", "firstName": "Bob", "lastName": "Smith"},
        {"userId": "u3", "firstName": "Charlie"},
        {"userId": "u4", "lastName": "Doe"},
        {"userId": "u5"}  # ❌ skip
    ]
    print(normalize_user_names(users))
