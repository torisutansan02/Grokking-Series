# === Q13: Merge User Profiles Across Logs ===
# You're given two lists of logs:
# - basic_profiles: contains userId and email
# - extended_profiles: contains userId and name
#
# Return a merged list of user profiles:
# - Each entry must include userId
# - Include email if available
# - Include name if available
# - Sorted alphabetically by userId

from typing import List, Dict

def merge_user_profiles(basic: List[Dict], extended: List[Dict]) -> List[Dict]:
    merged = {}

    for profile in basic:
        uid = profile["userId"]
        email = profile["email"]

        merged[uid] = {"userId": uid, "email": email}

    for profile in extended:
        uid = profile["userId"]
        name = profile["name"]

        if uid not in merged:
            merged[uid] = {"userId": uid}
        
        merged[uid]["name"] = name
    
    return sorted(merged.values(), key = lambda x: x["userId"])

# Optional debug run
if __name__ == "__main__":
    basic = [
        {"userId": "u1", "email": "a@example.com"},
        {"userId": "u2", "email": "b@example.com"}
    ]

    extended = [
        {"userId": "u1", "name": "Alice"},
        {"userId": "u3", "name": "Charlie"}
    ]

    print(merge_user_profiles(basic, extended))
