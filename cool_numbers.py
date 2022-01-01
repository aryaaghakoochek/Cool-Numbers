from math import sqrt

#asks for lower range in number that has to be bigger than 1
lower_range = int(input("Please enter the starting number in your range:"))
while lower_range < 2:
    lower_range = int(input("Please enter the starting number in your range:"))

#asks for upper range
upper_range = int(input("Please enter the ending number in your range:"))

#makes sure upper range is bigger than lower range
while lower_range > upper_range:
    lower_range = int(input("Please enter the starting number in your range:"))
    upper_range = int(input("Please enter the ending number in your range:"))

#lists that hold the math
list_squares = []
list_cubed = []
#list of the cool numbers
list_same = []

#squares and cubes every number in given range
for i in range(lower_range, upper_range + 1):
    var = i ** 2
    var1 = i ** 3
    list_squares.append(var)
    list_cubed.append(var1)

#checks for numbers that can be cubed and squared
same_values = set(list_squares) & set(list_cubed)
list_same.append(same_values)

#prints out number of cool  numbers and the cool numbers
print("There are:")
print(len(list_same))
print(list_same)


