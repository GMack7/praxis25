def find_pairs(arr, target):
    pairs = []

    # Iterate over all possible pairs of elements
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))

    return pairs

# Example usage
arr = [2, 4, 5, 3, 6, 8]
target = 9
result = find_pairs(arr, target)
print("Pairs that sum up to", target, "are:", result)

