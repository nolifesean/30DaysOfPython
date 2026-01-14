# Day 2: 30 Days of Python Programming

# Exercise Level 1
first_name = "Sean"
last_name = "De Guzman"
full_name = "Sean Luigi D. De Guzman"
country = "Philippines"
city = "Dinalupihan"
age = 20
year = 2005
is_married = False
is_True = True
is_light_on = False

hobby, player, F1_team, sport = "Gaming", "Raphinha", "Sauber", "Football"

# Exercise Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))

print("Length of First Name:", len(first_name))
print("Length of Last Name:", len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one//num_two

print("=========================================")
print("Num 1:", num_one)
print("Num 2:", num_two)
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Quotient:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)
print("=========================================")

radius = input("Enter Radius of a circle:")
circum_of_circle = 2 * 3.14 * float(radius)
area_of_circle = 3.14 * float(radius) ** 2
print("Circumference of a circle:", circum_of_circle)
print("Area of a circle:", area_of_circle)
print("=========================================")

first_name = input("Enter First Name:")
last_name = input("Enter Last Name:")
country = input("Enter Country:")
age = input("Enter Age:")
print("=========================================")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

help('keywords')