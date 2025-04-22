from typing import List, Dict

# === Q1: User Time Ranges ===
# Given a list of logs with userId and timestamp,
# return a dict mapping each user to their start-end range (as strings)

def get_user_time_ranges(logs: List[Dict[str, str]]) -> Dict[str, str]:
    # Set an empty hash map for user id's and their correlated timestamps
    user_times = {}

    for log in logs:
        # Assign UID to userId and ts to timestamp
        uid, ts = log["userId"], log["timestamp"]

        # Add uid to hash map
        if uid not in user_times:
            user_times[uid] = [ts, ts]
        # Min = Start, Max = End
        else:
            user_times[uid][0] = min(user_times[uid][0], ts)
            user_times[uid][1] = max(user_times[uid][1], ts)
        
    # 'uid': 'start - end'
    return {
        uid: f"{start} - {end}"
        for uid, (start, end) in user_times.items()
    }

if __name__ == "__main__":
    example_logs = [
        {"userId": "u1", "timestamp": "2025-04-16T12:00:00Z"},
        {"userId": "u1", "timestamp": "2025-04-16T12:05:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:01:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:03:00Z"},
    ]
    print(get_user_time_ranges(example_logs))
