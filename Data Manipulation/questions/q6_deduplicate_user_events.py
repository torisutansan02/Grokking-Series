# === Q6: Deduplicate User Events ===
# Given a list of logs with 'userId' and 'event',
# return a dictionary mapping each user to a list of
# unique events they triggered (sorted alphabetically).

from typing import List, Dict
from collections import defaultdict

def deduplicate_user_events(logs: List[Dict[str, str]]) -> Dict[str, List[str]]:
    user_events = defaultdict(set)

    for log in logs:
        user = log["userId"]
        event = log["event"]
        user_events[user].add(event)

    return {
        user: sorted(events)
        for user, events in user_events.items()
    }

if __name__ == "__main__":
    logs = [
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "purchase"},
        {"userId": "b", "event": "logout"},
        {"userId": "b", "event": "login"}
    ]
    print(deduplicate_user_events(logs))
