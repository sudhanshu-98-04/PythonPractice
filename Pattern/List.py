# Q. Find the largest Number
# num = [10,5,20,8]
# lar = num[0]
# # print(max(num))
# for i in num:
#     if(i >= lar):
#         lar = i
# print(lar)

# Q. Find the second largest number
# num = [10,5,20,8]
# largest = second = float('-inf')

# for i in num:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i
# print(second)

# print(sorted(set(num)[-2]))

# Q. Remove duplicates 
# nums = [1,2,2,3,4,4]
# print(list(set(nums)))

# result = []
# for i in nums:
#     if i not in result:
#         result.append(i)
# print(result)

# Q Reverse list
num = [1,2,2,3,4,4]

print(num[::-1])
