def total_cost(**kwargs):
    total = kwargs.get("price", 0) * kwargs.get("quantity", 0)
    return f"Total cost is {total}"

print(total_cost(price=100, quantity=3))
