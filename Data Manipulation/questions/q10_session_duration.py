# === Q10: Users Within Sign-in Duration ===
# Given a list of logs with:
# - userId (str)
# - type (either "sign-in" or "sign-out")
# - timestamp (str or int)
#
# Return a list of userIds who:
# - Signed in AND signed out
# - And signed out within maxDuration seconds of signing in
#
# Output should be sorted alphabetically.

from typing import List, Dict

def get_users_within_duration(logs: List[Dict[str, str]], maxDuration: int) -> List[str]:
    sign_in_times = {}
    result = []

    for log in logs:
        user = log["userId"]
        log_type = log["type"]
        ts = int(log["timestamp"])  # Ensure it's an int

        if log_type == "sign-in":
            if user not in sign_in_times:
                sign_in_times[user] = ts
        elif log_type == "sign-out":
            if user in sign_in_times:
                duration = ts - sign_in_times[user]
                if duration <= maxDuration:
                    result.append(user)
                del sign_in_times[user]  # Clean up to avoid duplicates

    return sorted(result)

# Optional debug run
if __name__ == "__main__":
    logs = [
        {"userId": "u1", "type": "sign-in", "timestamp": "100"},
        {"userId": "u2", "type": "sign-in", "timestamp": "150"},
        {"userId": "u1", "type": "sign-out", "timestamp": "160"},
        {"userId": "u2", "type": "sign-out", "timestamp": "190"},
        {"userId": "u3", "type": "sign-out", "timestamp": "300"}
    ]
    print(get_users_within_duration(logs, 60))  # ['u1', 'u2']
