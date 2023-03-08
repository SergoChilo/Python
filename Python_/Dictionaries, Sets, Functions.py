
""" Dictionaries, Sets """

# 1. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.

# s = input('Entre the key : ')
# v = 150
# l = {
#     'A': 15,
#     'B': 17,
#     'C': 20,
#     'D': 50,
# }
# if s in l:
#     print('You have this key')
# else:
#     l.update({s: v})
# print(l)


# 2. Loop through the values of a dictionary and add them to a new list.
#
# l = {
#     'A': 15,
#     'B': 17,
#     'C': 20,
#     'D': 50,
# }
# s = []
# for value in l.values():
#     s.append(value)
# print(s)


# 3. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys. Do this using loops and comprehensions.

# d = dict()
# for x in range(1, 16):
#     d[x] = x ** 2
# print(d)

# 4. Create 2 sets and find their symmetric difference without using the dedicated method.

# set_A = {1, 2, 3, 4, 5}
# set_B = {6, 7, 3, 9, 4}
# print(set_A ^ set_B)


# 5․ Write a Python program to remove the intersection of a 2nd set from the 1st set.

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print("Original sets:")
# print(set1)
# print(set2)
# print("\nRemove the intersection of a 2nd set from the 1st set:")
# set1 -= set2
# print("set1: ", set1)
# print("set2: ", set2)

""" Functions """

# 1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.

# def two():
#     target = int(input('Entre the target : '))
#     nums = range(1000)
#     for i in nums:
#         for j in nums:
#             if nums[i] + nums[j] == target:
#                 print(i, j)
# two()

# 2․ You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# def prices():
#     House = 35000
#     print('House for sale for $ 35000 ')
#     s = int(input('Choose a day for buying stock : '))
#     t = int(input('Choose a day to selling stock : '))
#     sale_1 = (House * s) / 100
#     sale_2 = (House * t) / 100
#     prices = range(0, 32, 1)
#     if sale_2 > sale_1 and 1 <= s <= 31 and 1 <= t <= 31 :
#         print(f'You have a {s}% stock in {s}-rd day if wou will buy')
#         print(f'You have a {t}% stock in {t}-rd day')
#         print('Your profit : $', sale_2 - sale_1)
#     else:
#         return 0
# prices()

# 3. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# (Optional) You must write an algorithm that runs in O(n) time and without using the division operation.

# def Array(arr, n):
#     if (n == 1):
#         print(0)
#         return
#     left = [0] * n
#     right = [0] * n
#     prod = [0] * n
#     left[0] = 1
#     right[n - 1] = 1
#     for i in range(1, n):
#         left[i] = arr[i - 1] * left[i - 1]
#     for j in range(n - 2, -1, -1):
#         right[j] = arr[j + 1] * right[j + 1]
#     for i in range(n):
#         prod[i] = left[i] * right[i]
#     for i in range(n):
#         print(prod[i], end=' ')
# arr = [10, 3, 5, 6, 2]
# n = len(arr)
# print("The product array is:")
# Array(arr, n)

# 4. You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
#   Input: n = 3
#   Output: 3
#   Explanation: There are three ways to climb to the top.
#     1. 1 step + 1 step + 1 step
#     2. 1 step + 2 steps
#     3. 2 steps + 1 step

# def fib(n):
#     l = []
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# def countWays(s):
#     return fib(s + 1)
# s = int(input('Enter the steps : '))
# print("Number of ways = ", countWays(s))


# 5. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.
# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:
# Guess a letter!
# _ a _
# and so on.

# import random
# print("Let's play Hangman!")
# name = input("What is your name? ")
# print("Good Luck ! ", name)
# words = ['rainbow', 'computer', 'science', 'programming',
#          'python', 'mathematics', 'player', 'condition',
#          'reverse', 'water', 'board', 'geeks']
# word = random.choice(words)
# guesses = ''
# turns = len(word) + 5
# while turns > 0:
#     guess = input("Enter a letter: ")
#     if guess in word:
#         print(f"Correct! There is one or more {guess} in the secret word.")
#     else:
#         turns -= 1
#         print(f"Incorrect. There are no {guess} in the secret word. {turns} turn(s) left.")
#     guesses = guesses + guess
#     wrongLetterCount = 0
#     for letter in word:
#         if letter in guesses:
#             print(f"{letter} ", end="")
#         else:
#             print("_ ", end="")
#             wrongLetterCount += 1
#     if wrongLetterCount == 0:
#         print(f"Congrats, you guessed the word!. The secret words was : {word}. You won!")
#         print('\n')
#         print('   ⠱   ⠎ ')
#         print('  ⠕  ✲  ⠪      ⠱   ⠎ ')
#         print('   ⠜   ⠣      ⠕  ✲  ⠪')
#         print('               ⠜    ⠣ ')
#         print('    ⠱   ⠎ ')
#         print('   ⠕  ✲  ⠪  ')
#         print('    ⠜   ⠣      ⠱    ⠎ ')
#         print('               ⠕  ✲  ⠪')
#         print('               ⠜     ⠣ ')
#         break
# else:
#     print(f"Sorry, you didn't win this time. The secret words was : {word} \n T R Y    A G A  I N !")
#     print(' ╔════════════════╗')
#     print(' ║                ║')
#     print(' ║   ###     ###  ║')
#     print(' ║    ◍       ◍   ║')
#     print(' ║                ║')
#     print(' ║        ∠       ║')
#     print(' ║   # # # # #    ║')
#     print(' ║    #  ∬   #    ║')
#     print(' ║      ####      ║')
#     print(' ╚════════════════╝')