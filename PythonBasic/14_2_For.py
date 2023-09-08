"""
1. Print each item of the list on a separate line
"""
numbers = [1, 6, 4, 3, 2, 5]
for item in numbers:
    print(item)

"""
2. Count how many '0's are present in the string using a 'for' loop and 'if' condition
"""
string = 'bolloon'
count_o = 0

for char in string:
    if char == 'o':
        count_o += 1

print(count_o)

"""
3. Accept a user-defined input as the variable num
Output all positive integers from 1 till num (inclusive) on a separate line
"""
num = int(input())
for i in range(1, num + 1): 
    print(i)

"""
4. Create a variable n and store the user defined input from console in n
Output to the console the multiplication table for n upto 10
"""
n = int(input())

for i in range(1, 11):
    print(n, "x", i, "=", n*i)

"""
5. Declare an integer variable num and initialise it to a user defined input
Output to the console the factorial of num
"""
n = int(input())

i = 1
factorial = 1

while i <= n:
    factorial = i * factorial
    i = i + 1
    
print("The factorial of the given number is:", factorial)