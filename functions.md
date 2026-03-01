'''python

# CISC179: Practice Lab – Functions

## 1. Creating and using functions

# 1a) Unit conversion function: KPL <-> MPG
# Conversion factor: 1 kpl ≈ 2.35215 mpg

def convert_fuel(units, *values):
    """
    Convert fuel efficiency between kpl and mpg.
    units: string, either 'kpl' or 'mpg'
    values: one or more numbers to convert
    """
    converted = []
    for val in values:
        # Input validation
        if not isinstance(val, (int, float)):
            print(f"Invalid input: {val}. Skipping.")
            continue
        
        if units.lower() == "kpl":
            converted_val = val * 2.35215
            print(f"{val} kpl = {converted_val:.2f} mpg")
            converted.append(converted_val)
        elif units.lower() == "mpg":
            converted_val = val / 2.35215
            print(f"{val} mpg = {converted_val:.2f} kpl")
            converted.append(converted_val)
        else:
            print(f"Invalid unit: {units}")
            return None
    return converted

# Example usage
convert_fuel("kpl", 10, 15, 20)

# 1b) Function taking any number of unnamed arguments and printing in reverse

def print_reverse(*args):
    """
    Prints all arguments in reverse order
    """
    reversed_args = args[::-1]
    print("Arguments in reverse:", reversed_args)

# Example usage
print_reverse("Iron Man", "Spider-Man", "Thor")

# 1c) Effect of modifying mutable parameters inside a function

def modify_list(lst):
    """
    Appends a value to the list. Changes will reflect outside the function.
    """
    lst.append("Modified")

def modify_dict(d):
    """
    Changes a dictionary key. Changes will reflect outside the function.
    """
    d["Hero"] = "Hulk"

my_list = ["Spider-Man", "Thor"]
my_dict = {"Hero": "Iron Man"}

modify_list(my_list)
modify_dict(my_dict)

print("Modified list:", my_list)   # ['Spider-Man', 'Thor', 'Modified']
print("Modified dict:", my_dict)   # {'Hero': 'Hulk'}

# To avoid changes outside, create a copy
def modify_copy(lst):
    new_lst = lst.copy()
    new_lst.append("Changed")
    return new_lst

new_list = modify_copy(my_list)
print("Original list:", my_list)
print("New copied list:", new_list)

# 1d) Global vs local variable example

x = 5

def funct_1():
    x = 3    # Local variable, does not affect global x

def funct_2():
    global x
    x = 2    # Changes global x

funct_1()
print("x after funct_1():", x)  # 5

funct_2()
print("x after funct_2():", x)  # 2

## 2. Troubleshooting

# 2a) Correct the function call using **kwargs for extra arguments
def my_func(a, b, *args):
    print("Extra args:", args)

# Call the function
my_func(1, 2, 3, 4, 5, 6)

# 2b) Correct use of global variable
x = 10

def my_func_global():
    global x
    x = 100

my_func_global()
print("Value of x:", x)  # 100

## 3. Challenges

# - Ensuring changes to mutable types (lists/dicts) do not unintentionally affect the original variable was important to understand.
# - Debugging global vs local variable issues helped reinforce scope concepts.
