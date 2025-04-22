import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from questions.q7_clean_products import clean_product_data

def test_clean_product_data():
    products = [
        {"id": "p1", "price": "$10.00", "stock": "3"},
        {"id": "p2", "price": "$5.00", "stock": "0"},
        {"id": "p3", "price": "$7.25", "stock": "2"}
    ]
    expected = [
        {"id": "p1", "price": 10.0, "stock": 3},
        {"id": "p3", "price": 7.25, "stock": 2}
    ]
    assert clean_product_data(products) == expected
    print("✅ test_clean_product_data passed!")

if __name__ == "__main__":
    test_clean_product_data()
