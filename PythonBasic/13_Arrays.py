"""
1. Create an Array of the first 5 positive integers - name it 'integers'
Once the array is define - output "Done" to the console.
"""
integers = [1, 2, 3, 4, 5]
print("Done")

"""
2. Output the 3rd element from the given array to the console.
num = [1, 2, 3, 4, 5]
"""
num = [1, 2, 3, 4, 5]
print(num[2])

"""
3. The 3rd month in the given list is incorrect
Update the 3rd month in the given array with the correct one - "Mar"
Once the 3rd array element is updated, output the entire list to the console
"""
months = ["Jan", "Feb", "Dec", "Apr"]
months[2] = "Mar"
print(months)

"""
4. Create a string array for the following values "Monday", "Tuesday", "Wednesday", and "Thursday".
Output the last two elements of the array on separate lines
"""
days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
print(days[2])
print(days[3])

"""
5. Create an int array containing the elements - 10, 20, 30, 40, 50, 60
Compile and output to the console the accurate count of the number of integer elements in the given array.
"""
numbers = [10, 20, 30, 40, 50, 60]
print(len(numbers))

"""
6. Create a list containing the elements - "lock", "key", "barrier", "sign" and "door"
Print the 2nd last element from the given list.
i.e. - reading from right to left, print the 2nd element
"""
list = ["lock","key","barrier","sign","door"]
print(list[ -2 ])

"""
7. Create a list m of the first 7 months in a year
Output the following to the console on separate lines
    Print the first 6 months of the year
    Print the 2nd to 5th month of the year - both included
"""
months = ["January", "February", "March", "April", "May", "June", "July"]
print(months[0:6])
print(months[1:5])