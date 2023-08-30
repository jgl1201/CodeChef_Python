"""
1. Find out if a person is old enough to vote
    Find out if the age is <, > or == to 18
    Make the program creating 2 variables
    Say if the age is enough to vote
"""
age = 25
vage = 18

if age >= vage:
    print("Old enough to vote")
else:
    print("Not old enough to vote")

# 2. Run the given code and fix it
r = 1000
w = 3222
if r > w:
#This code will not run due to improper indentation
    print("White balls are out of stock")  
else:
#Fix the error by putting a space before both print
    print("Your order is Confirmed")

"""
3. Write a program that:
    Takes an input for variables a and b
    Output "Coding is Fun!" if a > b
    Output nothing for other cases
"""
print("A: ")
a = int(input())
print("B: ")
b = int(input())

if a > b:
    print("Coding is Fun!")

"""
4. Write a program which:
    Creates variables b and r
    b = 23 || r = 45
    Print who scored more, Bob or Rob
"""
b = 23
r = 45

if b > r:
    print("Bob Scored higher marks than Rob")
else:
    if b == r:
        print("Bob & Rob both scored the same")
    else:
        print("Rob Scored higher marks than Bob")

b = 15
r = 15

if b > r:
    print("Bob Scored higher marks than Rob")
else:
    if b == r:
        print("Bob & Rob both scored the same")
    else:
        print("Rob Scored higher marks than Bob")

"""
5. Complete the code: 
    r = 24
k = 32

if r _ k:
    print("Ram is heavier than Karan")
elif r _ k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")
    
r = 78
k = 78

if r _ k:
    print("Ram is heavier than Karan")
____ r _ k:
    print("Karan is heavier than Ram")
____:
    print("Ram & Karan have the same weight!")
"""

r1 = 24
k = 32

if r1 > k:
    print("Ram is heavier than Karan")
elif r1 < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")
    
r1 = 78
k = 78

if r1 > k:
    print("Ram is heavier than Karan")
elif r1 < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")