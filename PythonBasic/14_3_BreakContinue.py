"""
1. Iterate the given list.
Break if finding an element which is not 30 or 31
"""
days = [30, 31, 30, 30, 31, 30, 20, 30, 31, 30, 31, 30]
for day in days:
    if (day != 30) and (day != 31) : 
        print(day)
        break

"""
2. Declare a variable n and set it to a user defined input
Print from 1 to 10 skipping the inserted number
"""
n = int(input())
for i in range(1, 11) :
    if i == n:
        continue
    print(i)