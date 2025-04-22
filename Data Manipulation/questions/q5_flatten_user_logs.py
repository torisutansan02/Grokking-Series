# === Q5: Flatten Nested User Logs ===
# Given a list of logs with a nested 'user' object,
# return a new list of logs with flat structure containing:
# - 'userId' from user['id']
# - 'userName' from user['name']
# - 'action' from the outer object

from typing import List, Dict

def flatten_user_logs(logs: List[Dict]) -> List[Dict]:
    flattened = []

    for log in logs:
        user = log["user"]
        flattened.append({
            "userId": user["id"],
            "userName": user["name"],
            "action": log["action"]
        })
    
    return flattened

if __name__ == "__main__":
    sample_logs = [
        {"user": {"id": "1", "name": "Alice"}, "action": "login"},
        {"user": {"id": "2", "name": "Bob"}, "action": "logout"}
    ]
    print(flatten_user_logs(sample_logs))
