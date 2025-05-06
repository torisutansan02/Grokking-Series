"""
Problem 1: Normalize Login Events

Output:
[
  {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z", "source": "web"},
  {"user_id": "u1", "timestamp": "2025-04-26T09:05:00Z", "source": "mobile"},
  {"user_id": "u2", "timestamp": "2025-04-26T09:10:00Z", "source": "desktop"}
]
"""

# Typing library, import List and Dict
from typing import List, Dict

# Function Signature
def normalize_login_events(events: List[Dict]) -> List[Dict]:
    normalized = []

    for event in events:
        # Normalize Aliased Keys
        uid = event.get("user_id") or event.get("uid") or event.get("userId")
        ts = event.get("timestamp") or event.get("time") or event.get("ts")
        src = event.get("source") or event.get("src") or event.get("platform")

        # Append Normalized Key: Value
        normalized.append({"user_id": uid, "timestamp": ts, "source": src})
    
    return normalized

# Input
login_events = [
  {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z", "source": "web"},
  {"uid": "u1", "time": "2025-04-26T09:05:00Z", "src": "mobile"},
  {"userId": "u2", "ts": "2025-04-26T09:10:00Z", "platform": "desktop"}
]

# Print the function call
print("\n")
print("NORMALIZED LOGIN EVENTS")
print(normalize_login_events(login_events), "\n")

"""
Problem 2: Merge Partial User Profiles

Output:
[
  {"user_id": "u1", "name": "Alice", "email": "alice@new.com"},
  {"user_id": "u2", "name": "Bob"},
  {"user_id": "u3", "name": "Charlie"}
]
"""

from typing import List, Dict

def merge_user_profiles(sourceA: List[Dict], sourceB: List[Dict]) -> List[Dict]:
    merged = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]

            # Merge Dictionaries By User_ID
            if uid not in merged:
                merged[uid] = user.copy()
            else:
                merged[uid].update(user)
    
    merge(sourceA)
    merge(sourceB)

    return list(merged.values())


sourceA = [{"user_id": "u1", "name": "Alice"}, {"user_id": "u2", "name": "Bob"}]
sourceB = [{"user_id": "u1", "email": "alice@new.com"}, {"user_id": "u3", "name": "Charlie"}]

print("MERGED USER PROFILES")
print(merge_user_profiles(sourceA, sourceB), "\n")

"""
Problem 3: Group Logins Per User

Output:
{
  "u1": 1,
  "u2": 2
}
"""

from typing import List, Dict

def group_logins_by_user(events: List[Dict]) -> Dict[str, int]:
    users = {}

    for event in events:
        uid = event["user_id"]

        # Group and Count
        users[uid] = users.get(uid, 0) + 1
    
    return users

logins = [
    {"user_id": "u1"},
    {"user_id": "u2"},
    {"user_id": "u2"}
]

print("GROUP LOGINS BY USER")
print(group_logins_by_user(logins), "\n")

"""
Problem 4: Top N Active Users

Output:
["u1", "u2"]
"""

from typing import List, Dict

def top_n_active_users(events: List[Dict], n: int) -> List[str]:
    users = {}
    result = []

    for event in events:
        uid = event["user_id"]

        # Group and Count
        users[uid] = users.get(uid, 0) + 1
    
    # Sort by descending frequency
    sorted_users = sorted(users.items(), key = lambda x : -x[1])
    
    i = 0
    while i < n and i < len(users):
        result.append(sorted_users[i][0])
        i += 1
    
    return result
        

active_users = [
    {"user_id": "u1"}, 
    {"user_id": "u1"}, 
    {"user_id": "u2"}, 
    {"user_id": "u3"}, 
    {"user_id": "u1"}, 
    {"user_id": "u2"}
]

print("TOP N ACTIVE USERS")
print(top_n_active_users(active_users, 2), "\n")

"""
Problem 5: Filter Valid Records

Output:
[{"user_id": "u1", "name": "Alice", "email": "alice@example.com"}]
"""

from typing import List, Dict

def filter_valid_profiles(profiles: List[Dict]) -> List[Dict]:
    filtered = []

    for profile in profiles:
        if "user_id" in profile and "name" in profile and "email" in profile:
            filtered.append({
                "user_id": profile["user_id"],
                "name": profile["name"],
                "email": profile["email"]
            })
    
    return filtered

records = [
    {"user_id": "u1", "name": "Alice", "email": "alice@example.com"},
    {"user_id": "u2", "name": "Bob"},
    {"user_id": "u3", "email": "charlie@example.com"}
]

print("FILTERED VALID PROFILES")
print(filter_valid_profiles(records), "\n")

"""
Problem 6: Flatten Nested Event Details

Output:
[
  {"user_id": "u1", "os": "iOS", "version": "16.3"},
  {"user_id": "u2", "os": "Android", "version": "13"}
]
"""

from typing import List, Dict

def flatten_event_details(events: List[Dict]) -> List[Dict]:
    flattened = []

    for event in events:
        # Flatten Nested Fields
        flat = dict(event)
        details = flat.pop("details", {})
        flat.update(details)

        # Append flat dictionary to flattened list
        flattened.append(flat)
    
    return flattened

events = [
    {"user_id": "u1", "details": {"os": "iOS", "version": "16.3"}},
    {"user_id": "u2", "details": {"os": "Android", "version": "13"}}
]

print("FLATTENED EVENT DETAILS")
print(flatten_event_details(events), "\n")

"""
Problem 7: Merge Events by User

Output:
{
    "u1": {"user_id": "u1", "timestamp": "2025-04-26T10:00:00Z", "source": "mobile"},
    "u2": {"user_id": "u2", "timestamp": "2025-04-26T09:30:00Z", "source": "desktop"}
}
"""

from typing import List, Dict

def merge_events_by_user(events: List[Dict]) -> Dict[str, Dict]:
    latest = {}

    for event in events:
        uid = event["user_id"]
        ts = event["timestamp"]

        if uid not in latest:
            latest[uid] = event
        else:
            latest[uid]["timestamp"] = max(ts, latest[uid]["timestamp"])
    
    return latest

events = [
    {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z", "source": "web"},
    {"user_id": "u1", "timestamp": "2025-04-26T10:00:00Z", "source": "mobile"},
    {"user_id": "u2", "timestamp": "2025-04-26T09:30:00Z", "source": "desktop"}
]

print("MERGED EVENTS BY USER")
print(merge_events_by_user(events), "\n")

"""
Problem 8: Normalize and Aggregate Purchases

Output:
{"u1": 15.5, "u2": 20.0}
"""

from typing import List, Dict

def normalize_and_aggregate_purchases(purchases: List[Dict]) -> Dict[str, float]:
    totals = {}

    for purchase in purchases:
        uid = purchase["user_id"]
        amt = float(purchase["amount"])

        totals[uid] = totals.get(uid, 0) + amt
    
    return totals

purchases = [
    {"user_id": "u1", "amount": "10.5"},
    {"user_id": "u1", "amount": 5.0},
    {"user_id": "u2", "amount": "20"}
]

print("NORMALIZED AND AGGREGATED PURCHASES")
print(normalize_and_aggregate_purchases(purchases), "\n")

"""
Problem 9: Merge Nested Profiles

Output:
[
    {"user_id": "u1", "preferences": {"theme": "dark", "font": "large"}},
    {"user_id": "u2", "preferences": {"lang": "en"}},
    {"user_id": "u3", "preferences": {"theme": "blue"}}
]
"""

from typing import List, Dict

def merged_nested_profiles(sourceA: List[Dict], sourceB: List[Dict]) -> List[Dict]:
    merged = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]
            prefs = user.get("preferences", {})
            
            if uid not in merged:
                merged[uid] = {
                    "user_id": uid, 
                    "preferences": prefs.copy()
                }
            else:
                merged[uid]["preferences"].update(prefs)

    merge(sourceA)
    merge(sourceB)

    return list(merged.values())

sourceA = [
    {"user_id": "u1", "preferences": {"theme": "light"}},
    {"user_id": "u2", "preferences": {"lang": "en"}}
]

sourceB = [
    {"user_id": "u1", "preferences": {"theme": "dark", "font": "large"}},
    {"user_id": "u3", "preferences": {"theme": "blue"}}
]

print("MERGED NESTED PROFILES")
print(merged_nested_profiles(sourceA, sourceB), "\n")

"""
Problem 10: Identify Inactive Users

Output:
["u2"]
"""

from typing import List, Dict

def find_inactive_users(events: List[Dict], threshold: int) -> List[str]:
    users = {}
    inactive = []

    for event in events:
        uid = event["user_id"]
        users[uid] = users.get(uid, 0) + 1
    
    for uid, count in users.items():
        if count < threshold:
            inactive.append(uid)

    return inactive

events = [
    {"user_id": "u1"},
    {"user_id": "u1"},
    {"user_id": "u2"},
    {"user_id": "u3"},
    {"user_id": "u3"}
]

print("FOUND INACTIVE USERS")
print(find_inactive_users(events, 2), "\n")

"""
Problem 11: Normalize Addresses with Optional Fields

Output:
[
    {"street": "123 Main St", "city": "Springfield", "zip": "12345"},
    {"street": "456 Oak St", "city": "Greenville", "zip": "67890"},
    {"street": "789 Elm St", "city": "Riverdale", "zip": "54321"}
]
"""

from typing import List, Dict

def normalize_addresses(addresses: List[Dict]) -> List[Dict]:
    normalized = []

    for a in addresses:
        street = a.get("street") or a.get("street_address") or a.get("address")
        city = a.get("city")
        zip = a.get("zip") or a.get("postal_code") or a.get("zip_code")

        normalized.append(
            {"street": street, "city": city, "zip": zip}
        )
    
    return normalized

addresses = [
    {"street": "123 Main St", "city": "Springfield", "zip": "12345"},
    {"street_address": "456 Oak St", "city": "Greenville", "postal_code": "67890"},
    {"address": "789 Elm St", "city": "Riverdale", "zip_code": "54321"}
]

print("NORMALIZED ADDRESSES")
print(normalize_addresses(addresses), "\n")

"""
Problem 12: Merge Users by ID and Sum Purchases

Output:
[
    {"user_id": "u1", "amount": 125},
    {"user_id": "u2", "amount": 50},
    {"user_id": "u3", "amount": 75}
]
"""

from typing import List, Dict

def merge_and_sum_purchases(sourceA: List[Dict], sourceB: List[Dict]) -> List[Dict]:
    merged = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]
            amt = user["amount"]

            merged[uid] = merged.get(uid, 0) + amt
    
    merge(sourceA)
    merge(sourceB)

    return [{"user_id": uid, "amount": amt} for uid, amt in merged.items()]

sourceA = [{"user_id": "u1", "amount": 100}, {"user_id": "u2", "amount": 50}]
sourceB = [{"user_id": "u1", "amount": 25}, {"user_id": "u3", "amount": 75}]

print("MERGED AND SUMMED PURCHASES")
print(merge_and_sum_purchases(sourceA, sourceB), "\n")

"""
Problem 13: Find Users With No Logins

Output:
["u3", "u4"]
"""

from typing import List, Dict

def find_users_with_no_logins(all_users: List[str], events: List[Dict]) -> List[str]:
    users = {uid for uid in all_users}
    res = []

    for event in events:
        uid = event["user_id"]

        if uid in users:
            users.discard(uid)
    
    for user in users:
        res.append(user)

    return res


all_users = ["u1", "u2", "u3", "u4"]
events = [{"user_id": "u1"}, {"user_id": "u2"}, {"user_id": "u1"}]

print("FOUND USERS WITH NO LOGINS")
print(find_users_with_no_logins(all_users, events), "\n")


"""
Problem 14: Top K Users with Tiebreaker by Timestamp

Output:
["u2", "u1"]
"""

def top_k_users(events: List[Dict], k: int) -> List[str]:
    top_users = {}
    res = []

    for event in events:
        uid = event["user_id"]
        ts = event["timestamp"]

        if uid not in top_users:
            top_users[uid] = {
                "count": 1, 
                "timestamp": ts
            }
        else:
            top_users[uid]["count"] += 1
            top_users[uid]["timestamp"] = max(ts, top_users[uid]["timestamp"])
    
    sorted_users = sorted(
        top_users.items(),
        key=lambda x: (-x[1]["count"], -int(x[1]["timestamp"].replace("-", "").replace("T", "").replace(":", "").replace("Z", "")))
    )

    i = 0
    while i < k and i < len(sorted_users):
        res.append(sorted_users[i][0])
        i += 1
    
    return res

events = [
    {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z"},
    {"user_id": "u2", "timestamp": "2025-04-26T09:05:00Z"},
    {"user_id": "u1", "timestamp": "2025-04-26T09:10:00Z"},
    {"user_id": "u3", "timestamp": "2025-04-26T09:15:00Z"},
    {"user_id": "u2", "timestamp": "2025-04-26T09:20:00Z"}
]

print("TOP K USERS")
print(top_k_users(events, 2), "\n")

"""
Problem 15: Update User Settings with Partial Fields

Output:
[
    {"user_id": "u1", "settings": {"theme": "dark", "lang": "en"}}
]
"""

from typing import List, Dict

def update_user_settings(existing: List[Dict], updates: List[Dict]) -> List[Dict]:
    users = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]
            settings = user.get("settings", {})
        
        if uid not in users:
            users[uid] = {
                "user_id": uid,
                "settings": settings.copy()
            }
        else:
            users[uid]["settings"].update(settings)

    merge(existing)
    merge(updates)

    return list(users.values())

existing = [{"user_id": "u1", "settings": {"theme": "light", "lang": "en"}}]
updates = [{"user_id": "u1", "settings": {"theme": "dark"}}]

print("UPDATING USER SETTINGS")
print(update_user_settings(existing, updates), "\n")

"""
Problem 16: Merge Three Sources with Priority

Output:
[
  {"user_id": "u1", "name": "Alicia", "email": "new@a.com"},
  {"user_id": "u2", "name": "Robert"},
  {"user_id": "u3", "name": "Charlie"}
]
"""

from typing import List, Dict

def merge_user_data(base: List[Dict], updates: List[Dict], overrides: List[Dict]) -> List[Dict]:
    users = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]

            if uid not in users:
                users[uid] = user.copy()
            else:
                users[uid].update(user)

    merge(base)
    merge(updates)
    merge(overrides)
    
    return list(users.values())

base = [
  {"user_id": "u1", "name": "Alice", "email": "old@a.com"},
  {"user_id": "u2", "name": "Bob"}
]

updates = [
  {"user_id": "u1", "email": "new@a.com"},
  {"user_id": "u2", "name": "Robert"}
]

overrides = [
  {"user_id": "u1", "name": "Alicia"},
  {"user_id": "u3", "name": "Charlie"}
]

print("MERGED THREE SOURCES WITH PRIORITY")
print(merge_user_data(base, updates, overrides), "\n")

"""
Problem 17: Filter and Format Logs

Output:

["[2025-04-26T09:01:00Z] u2: Error loading profile"]
"""

def filter_and_format_logs(logs: List[Dict], keyword: str) -> List[str]:
    result = []

    for log in logs:
        if keyword in log.get("message", ""):
            line = f"[{log['timestamp']}] {log['user_id']}: {log['message']}"
            result.append(line)
    
    return result

logs = [
  {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z", "message": "Login success"},
  {"user_id": "u2", "timestamp": "2025-04-26T09:01:00Z", "message": "Error loading profile"},
  {"user_id": "u3", "timestamp": "2025-04-26T09:02:00Z", "message": "Logged out"}
]

print("FILTERED AND FORMATTED LOGS")
print(filter_and_format_logs(logs, "Error"), "\n")

"""
Problem 18: Track Field Updates Per User

Output:
{
  "u1": {"theme": 2, "lang": 1},
  "u2": {"lang": 1}
}
"""

from typing import List, Dict
from collections import defaultdict

def track_field_updates(updates: List[Dict]) -> Dict[str, Dict[str, int]]:
    result = defaultdict(lambda: defaultdict(int))

    for update in updates:
        uid = update["user_id"]
        for key in update:
            if key != "user_id":
                result[uid][key] += 1

    return {uid: dict(fields) for uid, fields in result.items()}


updates = [
  {"user_id": "u1", "theme": "dark"},
  {"user_id": "u1", "lang": "fr"},
  {"user_id": "u1", "theme": "light"},
  {"user_id": "u2", "lang": "en"}
]

print("TRACKED FIELD UPDATES")
print(track_field_updates(updates), "\n")

"""
Problem 19: Top Spenders with Tiebreakers

Output:
["u2", "u3"]
"""

from typing import List, Dict

def top_spenders(transactions: List[Dict], k: int) -> List[str]:
    users = {}

    for txn in transactions:
        uid = txn["user_id"]
        amt = float(txn["amount"])
        ts = txn["timestamp"]

        if uid not in users:
            users[uid] = {"total": amt, "count": 1, "latest": ts}
        else:
            users[uid]["total"] += amt
            users[uid]["count"] += 1
            users[uid]["latest"] = max(users[uid]["latest"], ts)

    sorted_users = sorted(
        users.items(),
        key=lambda x: (-x[1]["total"], -x[1]["count"], x[1]["latest"]),
    )

    return [uid for uid, _ in sorted_users[:k]]

transactions = [
  {"user_id": "u1", "amount": 50, "timestamp": "2025-04-26T09:00:00Z"},
  {"user_id": "u2", "amount": 75, "timestamp": "2025-04-26T09:10:00Z"},
  {"user_id": "u1", "amount": 25, "timestamp": "2025-04-26T09:20:00Z"},
  {"user_id": "u2", "amount": 25, "timestamp": "2025-04-26T09:30:00Z"},
  {"user_id": "u3", "amount": 100, "timestamp": "2025-04-26T09:15:00Z"}
]

print("TOP SPENDERS")
print(top_spenders(transactions, 2), "\n")

"""
Problem 20: Normalize and Join Users with Locations

Output:
[
  {"user_id": "u1", "city": "Tokyo"},
  {"user_id": "u2", "city": "Paris"},
  {"user_id": "u3"}
]
"""

from typing import List, Dict

def normalize_and_join(users: List[Dict], locations: List[Dict]) -> List[Dict]:
    result = []
    location_map = {loc["user_id"]: loc for loc in locations}

    def merge(source):
        for user in source:
            uid = user.get("user_id") or user.get("userId") or user.get("uid")
            if uid:
                record = {"user_id": uid}
                if uid in location_map:
                    record.update(location_map[uid])
                result.append(record)

    merge(users)
    return result

users = [
  {"uid": "u1"},
  {"userId": "u2"},
  {"user_id": "u3"}
]

locations = [
  {"user_id": "u1", "city": "Tokyo"},
  {"user_id": "u2", "city": "Paris"},
  {"user_id": "u4", "city": "Berlin"}
]

print("NORMALIZED AND JOINED")
print(normalize_and_join(users, locations), "\n")

"""
Problem 21: User Action Tracker

Output:
{ "u1": "view", "u2": "login" }
"""

def user_action_tracker(users: List[Dict]) -> Dict[str, str]:
    userActs = {}

    for user in users:
        uid = user["user_id"]
        act = user["action"]
        ts = user["timestamp"]

        if uid not in userActs or ts > userActs[uid]["timestamp"]:
            userActs[uid] = {"timestamp": ts, "action" : act}
    
    return { uid: action["action"] for uid, action in userActs.items() }

users = [
  {"user_id": "u1", "action": "login", "timestamp": "2025-04-26T09:00:00Z"},
  {"user_id": "u1", "action": "view", "timestamp": "2025-04-26T09:05:00Z"},
  {"user_id": "u2", "action": "login", "timestamp": "2025-04-26T09:02:00Z"}
]

print("TRACKED USER ACTIONS")
print(user_action_tracker(users), "\n")

"""
Problem 22: List All Actions Per Use Chronologically

Output:
{
    "u1": ["login", "click"],
    "u2": ["view"]
}
"""

from collections import defaultdict

def list_user_actions(events: List[Dict]) -> Dict[str, List[str]]:
    user_actions = defaultdict(list)

    events.sort(key = lambda x: x["timestamp"])

    for event in events:
        uid = event["user_id"].strip()
        act = event["action"]

        user_actions[uid].append(act)

    return user_actions

events = [
  {"user_id": "u1", "action": "login", "timestamp": "2025-04-26T09:00:00Z"},
  {"user_id": "u1", "action": "click", "timestamp": "2025-04-26T09:10:00Z"},
  {"user_id": "u2", "action": "view", "timestamp": "2025-04-26T09:05:00Z"}
]

print("LISTED USER ACTIONS")
print(list_user_actions(events), "\n")

"""
Problem 23: Unique Users Per Action Type

Output:
{
    "login": ["u1", "u2"],
    "view": ["u1"]
}
"""

from collections import defaultdict

def users_per_action(events: List[Dict]) -> Dict[str, List[str]]:
    actions = defaultdict(set)

    for event in events:
        uid = event["user_id"]
        act = event["action"]

        actions[act].add(uid)

    return { action: list(uid) for action, uid in actions.items() }

events = [
    {"user_id": "u1", "action": "login"},
    {"user_id": "u2", "action": "login"},
    {"user_id": "u1", "action": "view"}
]

print("USERS PER ACTION")
print(users_per_action(events), "\n")

"""
Problem 24: Most Active Time Per User

Output:
{
    "u1": "2025-04-26T09:00:00Z",
    "u2": "2025-04-26T07:00:00Z"
}
"""

def most_recent_times(events: List[Dict]) -> Dict[str, str]:
    latest = {}

    for event in events:
        uid = event["user_id"]
        ts = event["timestamp"]

        if uid not in latest or ts > latest[uid]:
            latest[uid] = ts

    return latest

events = [
  {"user_id": "u1", "timestamp": "2025-04-26T08:00:00Z"},
  {"user_id": "u1", "timestamp": "2025-04-26T09:00:00Z"},
  {"user_id": "u2", "timestamp": "2025-04-26T07:00:00Z"}
]

print("MOST RECENT TIMES")
print(most_recent_times(events), "\n")

"""
Problem 25: Merge Users by Name Case Insensitive

Output:
{
    "alice": {"user_id": "u2", "name": "alice", "email": "a@example.com", "phone": "123-456"},
    "bob": {"user_id": "u3", "name": "Bob", "email": "b@example.com"}
}
"""

def merge_users_by_name(users: List[Dict]) -> Dict[str, Dict]:
    merged = {}

    for user in users:
        name = user["name"].strip().lower()

        # Merge Dictionaries
        if name not in merged:
            merged[name] = user.copy()
        else:
            merged[name].update(user)

    return merged

users = [
  {"user_id": "u1", "name": "Alice", "email": "a@example.com"},
  {"user_id": "u2", "name": "alice", "phone": "123-456"},
  {"user_id": "u3", "name": "Bob", "email": "b@example.com"}
]

print("MERGED USERS BY NAME")
print(merge_users_by_name(users), "\n")

"""
Problem 26: Merge Settings But Only Overwrite None Fields

Output:
[{"user_id": "u1", "theme": "dark", "lang": "en"}]
"""

from typing import List, Dict

def merge_user_settings(base: List[Dict], updates: List[Dict]) -> List[Dict]:
    merged = {}

    def merge(source):
        for user in source:
            uid = user["user_id"]

            if uid not in merged:
                merged[uid] = user.copy()
            else:
                # Update only None Fields
                for key, val in user.items():
                    if merged[uid].get(key) is None:
                        merged[uid][key] = val

    merge(base)
    merge(updates)

    return list(merged.values())

base = [
  {"user_id": "u1", "theme": None, "lang": "en"}
]
updates = [
  {"user_id": "u1", "theme": "dark"}
]

print("MERGED USER SETTINGS")
print(merge_user_settings(base, updates), "\n")

"""
Problem 27: Normalize ZIP Field with Aliases

Output:
[{"user_id": "u1", "zip": "12345"}, {"user_id": "u2", "zip": "54321"}]
"""

def normalize_zip_fields(records: List[Dict]) -> List[Dict]:
    normalized = []

    for record in records:
        uid = record["user_id"]

        # Normalize Aliased Key (ZIP)
        zip = record.get("ZIP") or record.get("postal")

        # Append User ID and ZIP to Normalized Array
        normalized.append({"user_id": uid, "zip": zip})
    
    return normalized

records = [
  {"user_id": "u1", "ZIP": "12345"},
  {"user_id": "u2", "postal": "54321"}
]

print("NORMALIZED ZIP FIELDS")
print(normalize_zip_fields(records), "\n")

"""
Problem 28: Flatten Nested Profile Object

Output:
[{"user_id": "u1", "name": "Alice", "email": "a@example.com"}, {"user_id": "u2", "name": "Bob"}]
"""

def flatten_profiles(users: List[Dict]) -> List[Dict]:
    flattened = []

    for user in users:

        # Flatten Nested Fields
        flat = dict(user)
        profile = flat.pop("profile", {})
        flat.update(profile)

        # Append to flattened array
        flattened.append(flat)

    return flattened

users = [
  {"user_id": "u1", "profile": {"name": "Alice", "email": "a@example.com"}},
  {"user_id": "u2", "profile": {"name": "Bob"}}
]

print("FLATTENED PROFILES")
print(flatten_profiles(users), "\n")

"""
Problem 29: Filter Malformed Records

Output:
[{"user_id": "u1", "email": "a@example.com"}]
"""

def filter_malformed(records: List[Dict], required: List[str]) -> List[Dict]:
    result = []

    for record in records:
        # Validation Pattern (Required Fields)
        if all(field in record for field in required):
            result.append(record)
    
    return result

records = [
  {"user_id": "u1", "email": "a@example.com"},
  {"user_id": "u2"}
]

print("FILTERED MALFORMED RECORDS")
print(filter_malformed(records, ["user_id", "email"]), "\n")

"""
Problem 30: Filter Then Group By Regoin

Output:
{"west": ["u1", "u3"]}
"""

from collections import defaultdict

def active_users_by_region(users: List[Dict], min_logins: int) -> Dict[str, List[str]]:
    region = defaultdict(list)

    for user in users:
        if user.get("logins", 0) >= min_logins:
            region[user.get("region", "unknown")].append(user["user_id"])
    
    return dict(region)

users = [
  {"user_id": "u1", "region": "west", "logins": 5},
  {"user_id": "u2", "region": "east", "logins": 1},
  {"user_id": "u3", "region": "west", "logins": 3}
]

print("ACTIVE USERS BY REGION")
print(active_users_by_region(users, 3), "\n")