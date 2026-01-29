# Day 2: 30 Days of python programming

import math

first_name = 'Abdul'
last_name = 'Banire' 
full_name = 'Abdul Banire' 
country = 'England' 
city = 'Liverpool' 
age = 22
year = 2003
is_married = False  
is_true = True      
is_light_on = True  

Personal_info = {
  'first_name': 'Abdul',
  'last_name': 'Banire',
  'full_name': 'Abdul Banire', 
  'country': 'England',  
  'city': 'Liverpool', 
  'age': 22,
  'year': 2003,
  'is_married': False,   
  'is_true': True,       
  'is_light_on': True,   
}

print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("full_name:", type(full_name))
print("country:", type(country))
print("city:", type(city))
print("age:", type(age))
print("year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("Personal_info:", type(Personal_info))

# Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4 

# Add num_one and num_two and assign the value to a variable total
variable_total = num_one + num_two 
print(variable_total)

# Subtract num_two from num_one and assign the value to a variable diff
variable_diff = num_two - num_one
print(variable_diff)

# Multiply num_two and num_one and assign the value to a variable product
variable_product = num_one * num_two 
print(variable_product)

# Divide num_one by num_two and assign the value to a variable division
variable_division = num_two / num_one 
print(variable_division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
variable_remainder = num_two % num_one 
print(variable_remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
variable_exp = num_one ** num_two
print(variable_exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
variable_floor_division = num_two // num_one 
print(variable_floor_division)

# The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#Take radius as user input and calculate the area.

# The radius of a circle is 30 meters.
# Take radius as user input and calculate the area.
radius = float(input("Enter the radius: "))   
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print(area_of_circle)
print(circum_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
