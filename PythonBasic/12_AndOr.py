"""
1. Update the code below to solve the problem

a = 15

# a%7 returns the remainder when a is divided by 7
if (a%7 == 0) and (a%5 == 0):       
    print(___)
else:
    print(___)
"""
a = 15

if (a%7 == 0) and (a%5 == 0):       
    print("The number is divisible by both 5 & 7")
else:
    print("The number is not divisible by both 5 & 7")

"""
2. The following helps accept multiple user input
z, x, c = map(int, input().split())

# Update your code below this line to compare c with z and x
"""
z, x, c = map(int, input().split())

if (c > x) or (c > z):
    print("PASS")
else:
    print("FAIL")

"""
3. Make an auto-reply program that takes input from the user as an integer variable x
Do the above for 2 separate input values
    x = 69
    x = 70

Compute and output the following to the console
Print "Order Confirmed" only if 
    x < 70
    else Print "Order Limit reached"
    In both cases, the program must print "Thank YOU!" on a separate line.
"""
x = int(input())
if x < 70:
    print("Order Confirmed")
else:
    print("Order Limit reached")
print("Thank YOU!")


x = int(input())
if x < 70:
    print("Order Confirmed")
else:
    print("Order Limit reached")
print("Thank YOU!")