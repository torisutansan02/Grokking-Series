# === main.py ===
# You can use this to manually test any of the data manipulation functions

from questions.q1_user_time_ranges import get_user_time_ranges
from questions.q2_group_transactions import group_transactions
from questions.q3_process_logs import processLogs
from questions.q4_active_streak import get_active_streak_users
from questions.q5_flatten_user_logs import flatten_user_logs
from questions.q6_deduplicate_user_events import deduplicate_user_events
from questions.q7_clean_products import clean_product_data
from questions.q8_filter_malformed import filter_valid_logs
from questions.q9_aggregate_expenses import aggregate_monthly_expenses
from questions.q10_session_duration import get_users_within_duration
from questions.q11_match_clicks_purchases import match_click_purchase

def run_q1_example():
    print("=== Q1: User Time Ranges ===")
    logs = [
        {"userId": "u1", "timestamp": "2025-04-16T12:00:00Z"},
        {"userId": "u1", "timestamp": "2025-04-16T12:04:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:01:00Z"},
        {"userId": "u2", "timestamp": "2025-04-16T12:02:00Z"},
    ]
    output = get_user_time_ranges(logs)
    print(output)

def run_q2_example():
    print("\n=== Q2: Group Transactions ===")
    transactions = [
        "apple", "banana", "apple",
        "orange", "banana", "apple"
    ]
    result = group_transactions(transactions)
    for line in result:
        print(line)

def run_q3_example():
    print("\n=== Q3: Process Logs ===")
    logs = [
        "88 200",
        "99 300",
        "88 220",
        "99 340",
        "77 150",
        "77 149"
    ]
    maxSpan = 30
    print(processLogs(logs, maxSpan))

def run_q4_example():
    print("\n=== Q4: Active Streak Users ===")
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
    result = get_active_streak_users(logs, 3)
    print(result)

def run_q5_example():
    print("\n=== Q5: Flatten Nested User Logs ===")
    logs = [
        {"user": {"id": "1", "name": "Alice"}, "action": "login"},
        {"user": {"id": "2", "name": "Bob"}, "action": "logout"}
    ]
    result = flatten_user_logs(logs)
    for r in result:
        print(r)

def run_q6_example():
    print("\n=== Q6: Deduplicate User Events ===")
    logs = [
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "login"},
        {"userId": "a", "event": "purchase"},
        {"userId": "b", "event": "logout"},
        {"userId": "b", "event": "login"}
    ]
    print(deduplicate_user_events(logs))

def run_q7_example():
    print("\n=== Q7: Clean Product Data ===")
    products = [
        {"id": "p1", "price": "$10.00", "stock": "3"},
        {"id": "p2", "price": "$5.00", "stock": "0"},
        {"id": "p3", "price": "$7.25", "stock": "2"}
    ]
    result = clean_product_data(products)
    for r in result:
        print(r)

def run_q8_example():
    print("\n=== Q8: Filter Malformed Logs ===")
    logs = [
        {"userId": "u1", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "", "timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"timestamp": "2025-04-01T12:00:00Z", "action": "login"},
        {"userId": "u2", "timestamp": "", "action": "logout"},
        {"userId": "u3", "timestamp": "2025-04-01T13:00:00Z", "action": "click"}
    ]
    result = filter_valid_logs(logs)
    for r in result:
        print(r)

def run_q9_example():
    print("\n=== Q9: Aggregate Monthly Expenses ===")
    expenses = [
        {"userId": "alice", "amount": 10.0, "date": "2025-04-01"},
        {"userId": "alice", "amount": 20.0, "date": "2025-04-15"},
        {"userId": "bob", "amount": 5.0, "date": "2025-04-10"},
        {"userId": "bob", "amount": 7.5, "date": "2025-05-01"}
    ]
    result = aggregate_monthly_expenses(expenses)
    print(result)

def run_q10_example():
    print("\n=== Q10: Users Within Sign-in Duration ===")
    logs = [
        {"userId": "u1", "type": "sign-in", "timestamp": "100"},
        {"userId": "u2", "type": "sign-in", "timestamp": "150"},
        {"userId": "u1", "type": "sign-out", "timestamp": "160"},
        {"userId": "u2", "type": "sign-out", "timestamp": "190"},
        {"userId": "u3", "type": "sign-out", "timestamp": "300"}
    ]
    result = get_users_within_duration(logs, 60)
    print(result)

def run_q11_example():
    print("\n=== Q11: Match Clicks to Purchases ===")
    clicks = [
        {"userId": "u1", "timestamp": 100},
        {"userId": "u2", "timestamp": 200},
        {"userId": "u3", "timestamp": 300}
    ]

    purchases = [
        {"userId": "u1", "timestamp": 150},
        {"userId": "u2", "timestamp": 300},
        {"userId": "u4", "timestamp": 310}
    ]

    result = match_click_purchase(clicks, purchases, 60)
    print(result)


if __name__ == "__main__":
    run_q1_example()
    run_q2_example()
    run_q3_example()
    run_q4_example()
    run_q5_example()
    run_q6_example()
    run_q7_example()
    run_q8_example()
    run_q9_example()
    run_q10_example()
    run_q11_example()