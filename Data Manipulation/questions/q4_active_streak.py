# === Q4: Active Streak Users ===
# Given a list of login events in the format "userId YYYY-MM-DD",
# return all users whose longest streak of consecutive login days
# is greater than or equal to the given threshold.
# A streak is defined as uninterrupted daily logins.
# Output should be sorted alphabetically.

from typing import List
from collections import defaultdict
from datetime import datetime, timedelta

def get_active_streak_users(logs: List[str], threshold: int) -> List[str]:
    user_dates = defaultdict(set)

    # Collect unique login dates per user
    for log in logs:
        user, date_str = log.strip().split()
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        user_dates[user].add(date_obj)

    qualifying_users = []

    for user, dates in user_dates.items():
        sorted_dates = sorted(dates)
        max_streak = streak = 1

        for i in range(1, len(sorted_dates)):
            if sorted_dates[i] - sorted_dates[i - 1] == timedelta(days=1):
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1

        if max_streak >= threshold:
            qualifying_users.append(user)

    return sorted(qualifying_users)

if __name__ == "__main__":
    logs = [
        "alice 2025-04-01",
        "alice 2025-04-02",
        "alice 2025-04-02",
        "bob 2025-04-01",
        "bob 2025-04-03",
        "carol 2025-04-10",
        "carol 2025-04-11",
        "carol 2025-04-12",
        "carol 2025-04-14"
    ]
    print(get_active_streak_users(logs, 3))