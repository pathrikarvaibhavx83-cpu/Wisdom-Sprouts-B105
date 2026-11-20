# Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".
def is_even(n):
   if n % 2 == 0:
      return "Even"
   else:
      return "Odd"
print(f"Number is : {is_even(4)}")

# Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.
def largest(a,b):
    if a > b:
        return a
    else:
        return b
print(f"Largest Number is : {largest(10, 20)}")

# Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
def print_numbers(n):
    for i in range (1,n+1):
        print(i)

print_numbers(10)

# Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    sum = 0
    for i in range (0,n+1):
        sum = sum + i
    return sum
print(sum_n(10))


# Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.
def table(n):
    for i in range (1,11):
        print(f"{i} x {n} = {i*n}")
print("Multiplication Table of 10:")
table(10)
# Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def count_even(list):
    count = 0
    for i in list:
        if i % 2 == 0 :
            count += 1
        else :
            pass
    return count 

print(f"count of the even in list :{count_even(list)}")


# Find Maximum
# Without using max(), write a function that returns the largest number in a list.
def find_max(numbers):
    # Handle an empty list just in case
    if not numbers:
        return None
        
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

my_list = [12, 45, 7, 89, 23]
print(f'Maximum number in the list is: {find_max(my_list)}')
 
# FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

# Palindrome Checker
# Write a function that returns True if a string is a palindrome.
def palindrome(text):
    # You only need to check up to the halfway point
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            print(f"The given string '{text}' is not a palindrome")
            return  # Stop immediately if a mismatch is found
            
    print(f"The given string '{text}' is a palindrome")

palindrome("vav")

# Count Vowels
# Write a function that counts the vowels in a string.
def countvowels(str):
    count = 0
    for character in str:
        if character in 'aeiou':
            count += 1
    return count

# Second Largest Number
# Write a function that returns the second largest number in a list without using sort().
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest
        
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(second_largest(my_list))


# Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

guessing_game()


#Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

def grade(marks):
    match marks:
        case marks if marks >= 90:
            return "A"
        case marks if marks >= 80:
            return "B"
        case marks if marks >= 70:
            return "C"
        case marks if marks >= 60:
            return "D"
        case _:
            return "F"
  
 
print(f"Your grade is : {grade(99)}")