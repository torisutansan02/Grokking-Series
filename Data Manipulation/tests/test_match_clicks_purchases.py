import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q11_match_clicks_purchases import match_click_purchase

def test_match_click_purchase():
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

    expected = ["u1"]
    assert match_click_purchase(clicks, purchases, 60) == expected
    print("✅ test_match_click_purchase passed!")

if __name__ == "__main__":
    test_match_click_purchase()
