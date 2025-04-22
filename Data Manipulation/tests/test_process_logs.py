import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q3_process_logs import processLogs

def test_process_logs():
    logs = [
        "88 200",
        "99 300",
        "88 220",
        "99 340",
        "77 150",
        "77 149"
    ]
    maxSpan = 30
    expected = ["77", "88"]
    assert processLogs(logs, maxSpan) == expected
    print("✅ test_process_logs passed!")

if __name__ == "__main__":
    test_process_logs()
