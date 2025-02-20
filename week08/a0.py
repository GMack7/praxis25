DENOMINATIONS = [100,20,10,5,1,0.25,0.1,0.05,0.01]

def change(cost, payment):
    change = []
    remaining_change = payment - cost
    for denomination in DENOMINATIONS:
        while (remaining_change >= denomination):
            remaining_change -= denomination
    return change

# Test cases
print(change(5,2.55))
print(change(2.55,5))
print(change(5,5))
print(change(0,5))