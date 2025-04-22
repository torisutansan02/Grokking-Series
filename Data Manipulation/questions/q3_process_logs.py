# === Q3: Process Logs ===
# Given a list of log entries in the format "userId timestamp",
# return all userIds whose activity span (max - min timestamp) is
# less than or equal to the given maxSpan.
# Output should be sorted alphabetically.

from typing import List

def processLogs(logs: List[str], maxSpan: int) -> List[str]:
    user_times = {}

    for log in logs:
        uid, ts = log.strip().split()
        ts = int(ts)

        if uid not in user_times:
            user_times[uid] = [ts, ts]
        else:
            user_times[uid][0] = min(user_times[uid][0], ts)
            user_times[uid][1] = max(user_times[uid][1], ts)

    return sorted([
        uid
        for uid, (start, end) in user_times.items()
        if end - start <= maxSpan
    ])

if __name__ == "__main__":
    logs = [
        "88 200",
        "99 300",
        "88 220",
        "99 340",
        "77 150",
        "77 149"
    ]
    print(processLogs(logs, 30))