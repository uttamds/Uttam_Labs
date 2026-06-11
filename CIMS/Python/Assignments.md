Challenge 1: Reverse a Number
Write a program to reverse the digits of a number.

num = 12345

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)
Input: 12345
Output: 54321
Challenge 2: Check if a Number is Palindrome
A palindrome number remains the same when reversed.

num = 121
original = num

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
Examples:
121 → Palindrome
1331 → Palindrome
123 → Not Palindrome
Challenge 3: Count Digits in a Number
num = 987654

count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits =", count)
Challenge 4: Sum of Digits
num = 1234

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum =", total)
Input: 1234
Output: 10
Challenge 5: Multiplication Table Using Nested Loop
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()
Challenge 6: Print Star Pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
*
**
***
****
*****
Challenge 7: Find Largest of Three Numbers
a = 10
b = 25
c = 15

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
Challenge 8: Prime Number Check
num = 13

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
Challenge 9: Factorial Using Function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
Challenge 10: Fibonacci Series Using Function
def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        temp = a + b
        a = b
        b = temp

fibonacci(10)
