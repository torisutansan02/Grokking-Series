# === Q7: Clean Product Data ===
# Given a list of products with price as a string (e.g. "$10.00")
# and stock as a string (e.g. "0" or "5"),
# return a cleaned list where:
# - price is a float
# - stock is an int
# - products with stock == 0 are removed

from typing import List, Dict, Any

def clean_product_data(products: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    cleaned = []

    for product in products:
        price = float(product["price"].replace("$", ""))
        stock = int(product["stock"])

        cleaned.append({
            "id": product["id"],
            "price": price,
            "stock": stock
        })

    return cleaned

# Optional debug
if __name__ == "__main__":
    products = [
        {"id": "p1", "price": "$10.00", "stock": "3"},
        {"id": "p2", "price": "$5.00", "stock": "0"}
    ]
    print(clean_product_data(products))
