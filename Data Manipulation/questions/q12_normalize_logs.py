# === Q12: Normalize Mixed Log Sources ===
# You're given logs with:
# - userId (str)
# - timestamp (int)
# - eventType (click or view)
# - metadata (dict)
#
# Normalize each log to:
# {
#   "userId": str,
#   "timestamp": int,
#   "type": "click" or "view",
#   "details": str (elementId or page)
# }
# Skip logs missing required metadata.

from typing import List, Dict

def normalize_logs(logs: List[Dict]) -> List[Dict]:
    result = []

    for log in logs:
        user = log.get("userId")
        ts = log.get("timestamp")
        event_type = log.get("eventType")
        meta = log.get("metadata", {})

        if event_type == "click" and "elementId" in meta:
            result.append({
                "userId": user,
                "timestamp": ts,
                "type": "click",
                "details": meta["elementId"]
            })
        elif event_type == "view" and "page" in meta:
            result.append({
                "userId": user,
                "timestamp": ts,
                "type": "view",
                "details": meta["page"]
            })

    return result

# Optional debug run
if __name__ == "__main__":
    sample = [
        {"userId": "u1", "timestamp": 100, "eventType": "click", "metadata": {"elementId": "btn-1"}},
        {"userId": "u2", "timestamp": 110, "eventType": "view", "metadata": {"page": "home"}},
        {"userId": "u3", "timestamp": 120, "eventType": "click", "metadata": {}},
        {"userId": "u4", "timestamp": 130, "eventType": "view"}
    ]
    print(normalize_logs(sample))
