# Q1. Find the data type of every value in a mixed list.

data = [10, 3.14, "Python", True, None, [1, 2], (3, 4)]

for item in data:
    print(item, "->", type(item).__name__)

# Q2. Convert a nested list into a tuple of tuples.

data = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(item) for item in data)

print(result)

# Q4. Check whether a number is a power of 2 using operators.

n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")

# Q5. Swap two numbers using bitwise XOR.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)

# Q6. Find whether a number is divisible by both 4 and 6 using logical operators.

n = int(input("Enter a number: "))

if n % 4 == 0 and n % 6 == 0:
    print("Number is divisible by both 4 and 6")
else:
    print("Number is not divisible by both 4 and 6")

## Q7. Calculate the total electricity bill using different unit rates.

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 3
    print("Total Electricity Bill:", bill)

elif units <= 200:
    bill = (100 * 3) + (units - 100) * 5
    print("Total Electricity Bill:", bill)

else:
    bill = (100 * 3) + (100 * 5) + (units - 200) * 8
    print("Total Electricity Bill:", bill)

# Q8. Check whether three sides can form a triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
# Q9. Determine the type of triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")

elif a == b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")

# Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).

balance = 5000

while True:
    print("\n----- ATM MENU -----")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter withdrawal amount: "))

        if 0 < amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance or Invalid Amount")

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == 3:
        print("Available Balance:", balance)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

# Q11. Calculate income tax based on different tax slabs.

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid Income")

elif income <= 300000:
    tax = 0

elif income <= 600000:
    tax = (income - 300000) * 0.05

elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10

elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15

else:
    tax = 90000 + (income - 1200000) * 0.20

if income >= 0:
    print("Total Income Tax:", tax)
# Q12. Create a menu-driven calculator using if-elif.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n----- CALCULATOR -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition:", a + b)

elif choice == 2:
    print("Subtraction:", a - b)

elif choice == 3:
    print("Multiplication:", a * b)

elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice")

# Q13. Print all prime numbers between 1 and n.

n = int(input("Enter a number: "))

for num in range(2, n + 1):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
# Q14. Find the factorial of a number using a loop.

n = int(input("Enter a number: "))

fact = 1

if n < 0:
    print("Factorial is not defined for negative numbers")

else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

# Q15. Print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Q16. Check whether a number is an Armstrong number.

n = int(input("Enter a number: "))

temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10

if n >= 0 and total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Q17. Reverse a number and check whether it is a palindrome.

n = int(input("Enter a number: "))

temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reversed Number:", reverse)

if n >= 0 and n == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")

# Q18. Find the Greatest Common Divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

while y != 0:
    x, y = y, x % y

print("GCD:", x)

# Q19. Write a function to check if a string is a palindrome.

def is_palindrome(text):
    return text == text[::-1]

value = input("Enter a string: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")

# Q20. Write a function to count vowels and consonants in a string.

def count_letters(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

text = input("Enter a string: ")

v, c = count_letters(text)

print("Vowels:", v)
print("Consonants:", c)

# Q21. Write a function to calculate Simple Interest and Compound Interest.

def calculate_interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    return si, ci

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si, ci = calculate_interest(p, r, t)

print("Simple Interest:", si)
print("Compound Interest:", round(ci, 2))
# Q22. Write a function to find all factors of a number.

def find_factors(n):
    if n == 0:
        return None

    factors = []

    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append(i)

    return factors

num = int(input("Enter a number: "))

result = find_factors(num)

if result is None:
    print("Zero has infinitely many factors.")
else:
    print("Factors:", result)

# Q23. Write a function to find the second largest element in a list.

def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]

numbers = list(map(int, input("Enter list elements: ").split()))

result = second_largest(numbers)

if result is None:
    print("Second largest element does not exist.")
else:
    print("Second largest element:", result)

# Q24. Write a program to find the largest and smallest elements in a list.

numbers = list(map(int, input("Enter list elements: ").split()))

print("Largest element:", max(numbers))
print("Smallest element:", min(numbers))

# Q25. Write a program to remove all even numbers from a list.

numbers = list(map(int, input("Enter list elements: ").split()))

result = []

for num in numbers:
    if num % 2 != 0:
        result.append(num)

print("List after removing even numbers:", result)

# Q26. Write a program to merge two lists and sort the result.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)

# Q27. Write a program to rotate a list to the right by K positions.

numbers = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter rotation count: "))

if numbers:
    k = k % len(numbers)
    rotated_list = numbers[-k:] + numbers[:-k] if k else numbers[:]
else:
    rotated_list = []

print("Rotated list:", rotated_list)

# Q28. Write a program to find the common elements between two lists.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)

# Q29. Write a program to convert a tuple into a list and vice versa.

my_tuple = (10, 20, 30, 40)

my_list = list(my_tuple)
print("Tuple converted into list:", my_list)

new_tuple = tuple(my_list)
print("List converted into tuple:", new_tuple)

# Q30. Write a program to find the union, intersection, and difference of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
# Q31. Write a program to check whether two sets are disjoint or not.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets are disjoint.")
else:
    print("Sets are not disjoint.")

# Q32. Write a program to merge two dictionaries.

dict1 = {"name": "Vaibhav", "age": 21}
dict2 = {"city": "Nashik", "course": "Computer Engineering"}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged dictionary:", merged_dict)

# Q33. Write a program to sort a dictionary by its values.

marks = {
    "Rahul": 75,
    "Amit": 90,
    "Priya": 85,
    "Sneha": 65
}

sorted_dict = dict(sorted(marks.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:", sorted_dict)

# Q34. Write a program to count the frequency of each character in a string using a dictionary.

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)

# Q35. Write a program to read a file and count the number of words, lines, and characters.

with open("sample.txt", "r") as file:
    content = file.read()

words = len(content.split())
lines = len(content.splitlines())
characters = len(content)

print("Number of words:", words)
print("Number of lines:", lines)
print("Number of characters:", characters)

# Q36. Write a program to copy the contents of one file into another file.

with open("source.txt", "r") as source:
    content = source.read()

with open("destination.txt", "w") as destination:
    destination.write(content)

print("File copied successfully!")

# Q37. Write a program to handle division by zero using exception handling.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Division:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

# Q38. Write a program to handle multiple exceptions using try-except.

try:
    numbers = [10, 20, 30]

    index = int(input("Enter list index: "))
    divisor = int(input("Enter divisor: "))

    result = numbers[index] / divisor

    print("Result:", result)

except IndexError:
    print("Error: List index is out of range.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid integer.")

except Exception as e:
    print("An unexpected error occurred:", e)

# Q39. Create a custom module with functions for addition and subtraction.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
# Import and use the custom module.

import mymodule

print("Addition:", mymodule.add(10, 5))
print("Subtraction:", mymodule.subtract(10, 5))

# Q40. Use the math module to perform mathematical operations.

import math

num = int(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
print("Power (number raised to 2):", math.pow(num, 2))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))

