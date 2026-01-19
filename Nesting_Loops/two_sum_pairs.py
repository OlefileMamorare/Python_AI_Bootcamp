# Write a function `two_sum_pairs(numbers, target)` that returns all unique pairs from
# numbers that sum to target.

def two_sum_pairs(numbers, target):
    pairs_matrix = []
    #first_num = numbers[0]


    for num in range(len(numbers)):
        pairs = []
        for i in range(num + 1, len(numbers)):
            if (numbers[num] != numbers[i] and numbers[num] + numbers[i]) == target:
                pairs.append(numbers[num])
                pairs.append(numbers[i])
                pairs_matrix.append(pairs)

    return pairs_matrix

two_sum_pairs([2, 3, 4, 6, 5], 8)  # [[2, 6], [3, 5]]
print(two_sum_pairs([10, 7, 4, 5, 2], 12))  # [[10, 2], [7, 5]]
print(two_sum_pairs([3, 9, 8], 11))  # [[3, 8]]
print(two_sum_pairs([3, 9, 8], 10))  # []

