# 30 Days of Python Programming

# Exercises

age = 20
height = 1.80
comp_num = 23 + 4j

# Script for area of a triangle
print('===========Area of a Triangle====================')
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is:", area_of_triangle)

# Script for permimeter of a triangle
print('===========Perimeter of a Triangle====================')
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_of_triangle)

# Script for area and perimeter of a rectangle
print('===========Area and Perimeter of a Rectangle====================')
rec_length = float(input("Enter length: "))
rec_width = float(input("Enter width: "))
area_of_rectangle = rec_length * rec_width
perimeter_of_rectangle = 2 * (rec_length + rec_width)
print("The area of the reactangle is:",area_of_rectangle)
print("The perimeter of the rectangle is:", perimeter_of_rectangle)

# Script for area of a circle
print('===========Radius of a Circle====================')
radius = float(input("Enter radius: "))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("The area of the circle is:", area_of_circle)
print("The circumference of the circle is:", circum_of_circle)

# Solving for slope, x and y intercept
print('===========Calculate for Slope====================')
# equation of a line: y = 2x-2
slope = 2 #slope
y_intercept = -2
x_intercept = -y_intercept / slope
print("The slope is:", slope)
print("The y-intercept is:", y_intercept)   
print("The x-intercept is:", x_intercept)

# slope between two points
print('===========Calculate for Slope between two points====================')
print("Point 1:", (2, 2))
print("Point 2:", (6, 10))
slope_between_points = (10 - 2)/(6-2)
distance = (((6 - 2)**2) + ((10 - 2)**2)) ** 0.5
print("The slope between the two points is:", slope_between_points)
print("The distance between the two points is:", distance)

# Compare slope
print('===========Compare slope====================')
slope1 = slope
slope2 = slope_between_points
print("Is slope 1 less than or equal to slope 2?:", slope1 <= slope2)

# Calculate the value of y
print('===========Calculate the value of y====================')
x = -3
y = (x ** 2) + (6 * x) + 9
print("Value of y is ", y)

# Find the length
print('===========Find the length====================')
str1_length = len("python")
str2_length = len("dragon")
print("Python string length:", str1_length)
print("Dragon string length:", str2_length)
print("Is the length of 'python' greater than 'dragon'?:", str1_length > str2_length)

print("Is 'on' found in both 'python and 'dragon'?:",  'on' in 'python' and 'on' in 'dragon')
print("==============================================")
statement = "I hope this course is not full of jargon."
print(statement)
print("Is 'jargon' in the statement?:", 'jargon' in statement)
print("Is there no 'on' in both 'python' and 'dragon'?:", 'on' not in 'python' and 'on' not in 'dragon')

# Convert length to float and string
print("===================Converting===========================")
python_str_float = float(str1_length)
python_str = str(python_str_float)
print("Length converted to float:", python_str_float)
print("Length converted to string:", python_str)

# Check if number is even or odd
print("=================Even or Odd=============================")
num = float(input("Enter a number:"))
is_even = num % 2 == 0
print("Is the number even?:", is_even)

# floor division
print("=================Floor Division=============================")
floor_div = 7//3
is_equal = floor_div == int(2.7)
print("Floor division of 7//3 is:", floor_div)
print("Is the floor division value equal to the int value of 2.7?:", is_equal)

# Check if string is equal to int
print("=================Compare=============================")
str_num = '10'
num1 = 10
is_equal_str_int = type(str_num) == type(num1)
print("Is the string '10' equal to the type integer 10?:", is_equal_str_int)

# Check and compare
print("=================Compare=============================")
num2 = int(9.8)
num3 = 10
is_equal_num = num2 == num3
print("Converted int value is:", num2)
print("Is the int value equal to 10?:", is_equal_num)

# Calculate Pay 
print("=================Calculate Pay=============================")
hours = float(input("Enter hours:"))
rate = float(input("Enter rate per hour:"))
pay = hours * rate
print("Your weekly earning is",pay)

# Calculate number os=f seconds a person can live
print("=================Calculate Seconds Lived=============================")
years = int(input("Enter number of years you have lived:"))
seconds_lived = 365 * 24 * 60 * 60 * years
print("You have lived for", seconds_lived, "seconds.")

# display the following table 
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("=======================Display Table===============================")
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
