# Python Program for Denomination

def calculate_denominations(amount, denominations):
    denomination_counts = {}
    for denom in denominations:
        if amount >= denom:
            denomination_counts[denom] = amount // denom
            amount %= denom
        else:
            denomination_counts[denom] = 0
    return denomination_counts

# Input
amount = int(input("Enter the total amount: "))
denominations = [2000, 500, 200, 100, 50, 10, 5, 2, 1]

# Calculate denominations
result = calculate_denominations(amount, denominations)

# Output
print("Denomination breakdown:")
for denom, count in result.items():
    if count > 0:
        print(f"{denom} : {count}")

