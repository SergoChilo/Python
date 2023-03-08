"""RECURSION"""

# 0. Write a recursive function that will print odd numbers from 'start' to 'stop'.

# def odd(start,stop):
#     if start == stop:
#         exit()
#     if start % 2 == 1:
#         print(start, end=" ")
#     return odd(start + 1, stop)
# print(odd(10, 30))


# 1. Write the Fibonacci function using recursion.
# (Optional) The algorithm must have a time complexity of O(n)

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(20))

# 2. Write a function to calculate the factorial of n recursively.

# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x - 1) * x
# print(fact(64))

# 3. Write a recursive function to calculate the sum of elements of a list.

# def sum_list(n):
#    if len(n) == 1:
#         return n[0]
#    else:
#         return n[0] + sum_list(n[1:])
# print(sum_list([1, 3, 5, 7, 9, 11, 13]))

# 4. Write a recursive function to calculate the geometric sum of n.
# a * r + a * r ^ 2 + a * r ^ 3 + ...

# def Geometric(a, r, n):
#     if n <= 0:
#         return 0
#     return pow(r, n) + Geometric(a, r, n - 1)
# print(Geometric(2, 2, 4))

# 5. Write a recursive function to calculate the sum of reciprocals of powers of 2.

# def Geometric(a, r , n):
#     if n <= 0:
#         return 0
#     return pow(r, n) + Geometric(a, r, n - 1)
# print(Geometric(2, 0.5, 50))

# 6. Write a recursive function to calculate n-th power of a.

# def powf(a, n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return a
#     else:
#         return (a * powf(a, n - 1))
# print(powf(2, 10))

#Antesel##############################################
# 7. Write a recursive function that evaluates a mathematical expression. Example input - "5 + 6"
######################################################


# 8. Write a recursive function that reverses a string

# def reverse(string):
#     if len(string) == 0:
#         return string
#     return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))

# 9. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved
# to the end of the string.

# def endX(str):
#     if len(str) <= 1 :
#         return str
#     if str[0] == 'x':
#         return endX(str[1:]) + str[0]
#     return str[0] + endX(str[1:])
# print(endX('xyzxyzxyzyxyzyxyzyxyzyxyxyzyxyxyzyxyxyzxy'))