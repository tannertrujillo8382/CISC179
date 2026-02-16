# Practice Lab: User Input

## 1. User Input Programs

### a. Convert Weight from Kilograms to Pounds

```python
# ask user for weight in kg
weight_kg = float(input("Enter weight in kilograms: "))

# convert to pounds
weight_lb = weight_kg * 2.2

# show result
print("Weight in pounds:", weight_lb)

  
#b. ask user for info
net_balance = float(input("Enter net balance: "))
payment = float(input("Enter payment made: "))
d1 = int(input("Enter number of days in billing cycle: "))
d2 = int(input("Enter number of days payment was made before billing cycle: "))
interest_rate = float(input("Enter monthly interest rate (like 0.0152): "))

# calculate average daily balance
average_daily_balance = (net_balance * d1 - payment * d2) / d1

# calculate interest
interest = average_daily_balance * interest_rate

# show result
print("Interest on unpaid balance:", interest)

import math

# ask user for speeds and time
speed_a = float(input("Enter speed of Car A (mph, west): "))
speed_b = float(input("Enter speed of Car B (mph, south): "))
hours = float(input("Enter elapsed hours: "))
minutes = float(input("Enter elapsed minutes: "))

# convert minutes to hours
total_time = hours + minutes / 60

# distance each car traveled
distance_a = speed_a * total_time
distance_b = speed_b * total_time

# shortest distance using Pythagoras
distance_between = math.sqrt(distance_a ** 2 + distance_b ** 2)

# show result
print("Shortest distance between cars:", distance_between)

# hello = "hello" works
# _var = 100 works
# !var_1 = 200 does NOT work, variable names cannot start with !
# print = "print me" works but not good because it replaces Python's print function
# False = 0 does NOT work, reserved words cannot be used as variable names

# I had trouble remembering to convert user input to int or float
# The average daily balance formula was confusing at first
# Figuring out the distance between cars needed careful conversion of minutes to hours
# Remembering what makes a variable name valid was tricky
