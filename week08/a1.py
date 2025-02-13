def find_sums(target, numbers):
    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

print(find_sums(9,[0,1,3,6,7,8]))
print(find_sums(11,[0,8,3,6,7,4]))