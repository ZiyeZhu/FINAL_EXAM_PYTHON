# Task 5: Sum customer purchases from list of tuples
print("\nTask 5: Customer Purchases")
purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]
customer_totals = {}

for name, amount in purchases: # iterate through the list of tuples
    if name in customer_totals:
        customer_totals[name] += amount
    else:
        customer_totals[name] = amount

for customer, total in customer_totals.items(): # iterate through the dictionary of customer totals
    print(f"{customer} spent ${total}")