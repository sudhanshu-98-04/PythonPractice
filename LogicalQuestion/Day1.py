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

# 2. Write a Python program to concatenate all elements in a list into a string
# and return it.   
# lst = ['H', 'e', 'l', 'l', 'o']
# result = " "

# for str in lst:
#     result += str
# print(result)

# optimize way 

# result = " ".join(lst)
# print(result)

# lst = [1, 2, 3, 4]
# result = "".join(map(str, lst))
# print(result)

# 3. Write a Python program to print all even numbers from a given list of numbers in the same order. 
# Stop printing if any number that comes after 237 in the sequence is encountered.
# Sample 
# numbers list : 
# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 237, 412, 566, 731, 210, 912, 216, 244, 896, 101, 867, 355, 430 ]

# expected output:
# 386 462 418 344 236 566 978 328 162 758

# for num in numbers:
#     if num == 237:
#         break 
#     if num % 2 == 0:
#         print(num , end=" ")

# Q4. Write a Python program to print out a set containing all the colour from color_list_1 which are not present in color_list_2.   

# color_list_1  = {"Red", "Green", "Blue", "Yellow"}
# color_list_2  = {"Blue", "Black", "Yellow", "White"}
# # expected output:  {"Red", "Green"}

# result = color_list_1 - color_list_2
# print(result)

# 5. Write a Python program that will accept the base and height of a triangle and compute the 
# area.   
# Formula for Area of a Triangle
# "Area of a triangle"=1/2×"base"×"height" 

# base = int(input("Enter the no."))
# hight = int(input("Enter the no."))

# Area = 1/2 * base * hight
# print(Area)

# 6. Write a program to accept a number N from the user and print all twin prime pairs between 1 and N.
# [ Twin prime numbers are a pair of prime numbers whose difference is exactly 2.
# In other words, two numbers are called twin primes if both are prime and the gap between them is 2. ]

# e.g.
# The twin prime pairs between 1 and 20 are:
# •	(3, 5)
# •	(5, 7)
# •	(11, 13)
# •	(17, 19)
# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Accept input
N = int(input("Enter N: "))

print("Twin prime pairs between 1 and", N, "are:")

for i in range(2, N - 1):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i+2})")
