#Check if a number is positive, negative, or zero.
from re import match


number = int(input("Enter number "))

if number > 0 :
  print("Given number is positive ")

elif number == 0 :
  print("Given number is zero ")

else :
  print("given number is negative")

#Check whether a number is even or odd.

number = int(input("Enter number "))
if number % 2 == 0 :
  print("Given number is even")
else :
  print("given number is odd")

#Find the greater of two numbers.
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
if num1 > num2 :
  print(f"{num1} is greater than {num2}")
else :
  print(f"{num2} is greater than {num1}")

#Find the greatest of three numbers.
n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
n3 = int(input("Enter third number "))
if n1 > n2 :
  print(f"{n1} is greater")

elif n2>n1:
  print(f"{n2}is greater")
else :
  print(f"{n3}is greater")

#Check if a person is eligible to vote (age ≥ 18)

age = input(int("Enter age "))
if age >= 18:
  print("person is eligible for vote ")

else:
  print("not eliigible")

#Check whether a year is a leap year.
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")

#Check if a character is a vowel or consonant.
char = input("Enter character")
match char:
  case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
    print("Given character is a vowel")
  case _:
    print("Given character is a consonant")
  

#Check whether a number is divisible by 5 and 11
n = int(input("Enter number"))
if n % 5 == 0 and n % 11 == 0:
  print("given number is divisible")

else :
  print("not divisible")

#Check if a number is a multiple of both 3 and 7.
mnum = int(input("Enter the number "))
if mnum % 3 == 0 and mnum % 7 == 0:
  print("Given number is multiple of both 3 and 7")
else:
  print("Given number is not multiple of both 3 and 7")

#Assign grades based on marks:
#90–100: A
#80–89: B
#70–79: C
#60–69: D
#Below 60: F
marks = int(input("Enter marks "))
match marks:
  case marks if 90 <= marks <= 100:
    print("Grade A")
  case marks if 80 <= marks <= 89:
    print("Grade B")
  case marks if 70 <= marks <= 79:
    print("Grade C")
  case marks if 60 <= marks <= 69:
    print("Grade D")
  case marks if marks < 60:
    print("Grade F")
#Find whether the entered alphabet is a vowel using if-elif.
char = input("Enter character: ")
if char in "aeiouAEIOU":
    print("Given character is a vowel")
else:
    print("Given character is a consonant")
#Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a + b > c and a + c > b and b + c > a:
    print("The three sides can form a triangle.")
else:
    print("The three sides cannot form a triangle.")

#Determine the type of triangle (Equilateral, Isosceles, Scalene).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b == c:
    print("The triangle is Equilateral.")
else:
    if a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
#Find the largest among four numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print(f"{n1} is the largest.")
elif n2 >= n3 and n2 >= n4:
    print(f"{n2} is the largest.")
elif n3 >= n4:
    print(f"{n3} is the largest.")
else:
    print(f"{n4} is the largest.")
#Check whether a number is a three-digit number.
num = int(input("Enter a number: "))
if 100 <= num <= 999:
    print(f"{num} is a three-digit number.")
else:
    print(f"{num} is not a three-digit number.")
#Calculate electricity bill using slab rates.
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4.5
print(f"The electricity bill is: Rs. {bill:.2f}")

#Calculate income tax based on income slabs.
income = float(input("Enter your income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.1
elif income <= 1000000:
    tax = 25000 + (income - 500000) * 0.2
else:
    tax = 75000 + (income - 1000000) * 0.3
print(f"The income tax is: Rs. {tax:.2f}")
#Check if a student passes (minimum 35 marks in each subject).
marks1 = int(input("Enter marks in subject 1: "))
marks2 = int(input("Enter marks in subject 2: "))
marks3 = int(input("Enter marks in subject 3: "))
if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    print("The student has passed.")
else:
    print("The student has failed.")
#Find whether a number is within a given range.
num = int(input("Enter a number: "))
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
if lower <= num <= upper:
    print(f"{num} is within the range.")
else:
    print(f"{num} is not within the range.")
#Build a simple calculator using if-elif-else (+, -, *, /).
print("Simple Calculator")
print("Options: +, -, *, /")
operation = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation.")
print(f"Result: {result}")
#Check if a year is a century leap year.
year = int(input("Enter the year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a century leap year.")
    else:
        print(f"{year} is not a century leap year.")
else:
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
#Determine the season based on the month number.
month = int(input("Enter the month number (1-12): "))
if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"
print(f"The season for month {month} is {season}.")
#Find the number of days in a month.
month = int(input("Enter the month number (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 28
print(f"The number of days in month {month} is {days}.")
#Check whether a password meets minimum conditions (length, digits, etc.).
password = input("Enter a password: ")
if len(password) >= 8:
    if any(c.isdigit() for c in password):
        if any(c.isupper() for c in password):
            if any(c.islower() for c in password):
                print("The password meets all minimum conditions.")
            else:
                print("The password must contain at least one lowercase letter.")
        else:
            print("The password must contain at least one uppercase letter.")
    else:
        print("The password must contain at least one digit.")
else:
    print("The password must be at least 8 characters long.")
#Determine ticket price based on age category.
age = int(input("Enter your age: "))
if age < 0 or age > 150:
    print("Invalid age.")
elif age <= 5:
    price = 0
elif age <= 12:
    price = 5
elif age <= 65:
    price = 10
else:
    price = 7
print(f"The ticket price is: Rs. {price}")
#Calculate discount based on purchase amount.
amount = float(input("Enter the purchase amount: "))
if amount >= 1000:
    discount = amount * 0.2
elif amount >= 500:
    discount = amount * 0.1
else:
    discount = 0
print(f"The discount is: Rs. {discount:.2f}")
#Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter your age: "))
eyesight_condition = input("Do you have good eyesight? (yes/no): ")
if age >= 18 and eyesight_condition == "yes":
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")
#Create a login system with username and password validation.

username = input("Enter username: ")
password = input("Enter password: ")
if username == "Vaibhav" and password == "password123":
    print("Login successful.")
else:
    print("Invalid username or password.")

#Create a menu-driven program using if-elif-else with options like:
#Addition
#Subtraction
#Multiplication
#Division
#Exit
while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting ......")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Cannot divide by zero.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
