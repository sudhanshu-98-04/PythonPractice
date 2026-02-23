# Q1.Write a Python program to generate a text-based histogram from a given list of integers. The program should display each unique integer in the list alongside a row of stars (*) representing its frequency.
# Example Input:
# A list of integers: [1, 2, 1, 3, 2, 2, 4, 1]
# Expected Output:

# 1: ***     [ 1 is 3 times in the list ]
# 2: ***     [ 2 is also 3 times ]
# 3: *         [ 3 is once ]
# 4: *         [ 4 is once ]

# list = [1, 2, 1, 3, 2, 2, 4, 1]
# freq = {}

# for num in list:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)

# for key in sorted(freq):
#     print(f"{key}:{"*"*freq[key]}")

# # Optimize way 
# from collections import Counter

# freq = Counter(list)

# for key in sorted(freq):
#     print(f"{key}:{"*"*freq[key]}")
