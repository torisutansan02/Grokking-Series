# === Q8: Filter Malformed User Logs ===
# Given a list of user log dictionaries, return a new list
# that only includes logs which have all of:
# - 'userId': non-empty string
# - 'timestamp': non-empty string
# - 'action': non-empty string
#
# Any logs missing keys or containing None/"" values for those fields
# should be filtered out.
#
# Do not modify the original logs. Return a new list.

from typing import List, Dict

def filter_valid_logs(logs: List[Dict]) -> List[Dict]:
    filtered = []

    for log in logs:
        if (
            "userId" in log and log["userId"] and
            "timestamp" in log and log["timestamp"] and
            "action" in log and log["action"]
        ):
            filtered.append(log)
    
    return filtered

# Optional manual run
if __name__ == "__main__":
    logs = [
        {"userId": "u1", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "u2", "timestamp": "", "action": "logout"},
        {"userId": "u3", "timestamp": "2025-04-01T13:00:00Z", "action": "click"}
    ]
    print(filter_valid_logs(logs))
