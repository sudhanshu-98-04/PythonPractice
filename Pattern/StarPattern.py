print("hello")
# *  
# ** 
# ***
n = 3 
# for i in range(1,n+1):
#     print("*"*i)
            # or
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()
            # or
# [print("*"*i) for i in range(1,n+1)]

# ***
# **
# *
# for i in range(n,0,-1):
#     print("*"*i)
            # or
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")    
    # print()
            # or
# [print("*"*i) for i in range(n,0,-1)]
            # or

#   *
#  **
# ***
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
            # or
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# ***
#  **
#   *
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*i)

#   *
#  ***
# *****
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
            # or
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

