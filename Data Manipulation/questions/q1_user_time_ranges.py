from typing import List, Dict

# === Q1: User Time Ranges ===
# Given a list of logs with userId and timestamp,
# return a dict mapping each user to their start-end range (as strings)

def get_user_time_ranges(logs: List[Dict[str, str]]) -> Dict[str, str]:
    user_times = {}

    for log in logs:
        uid = log["userId"]
        ts = log["timestamp"]

        if uid not in user_times:
            user_times[uid] = [ts, ts]
        else:
            user_times[uid][0] = min(user_times[uid][0], ts)
            user_times[uid][1] = min(user_times[uid][1], ts)
    
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
