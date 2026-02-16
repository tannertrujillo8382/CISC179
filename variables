# Examples of different types
var_int = 100         # integer
var_float = 1000.0    # float
var_str = "Hello World"  # string
var_str2 = 'Hello again' # single quotes also work
# Assign initial value
var1 = 10
# Check memory address
print("Memory address of var1 (10):", hex(id(var1)))

# Change value of var1
var1 = 100
# Check memory address again
print("Memory address of var1 (100):", hex(id(var1)))

# Explanation:
# The addresses are different because assigning a new value creates a new object in memory.
# var1 now points to this new object, and the previous object (10) remains in memory until Python cleans it up.

# Assign var2 the same value as var1
var2 = 100
# Check memory address of var2
print("Memory address of var2 (100):", hex(id(var2)))

# Explanation:
# Python sometimes reuses memory for small integers (like 100), so var2 may share the same memory address as var1.
# This is called integer interning, an optimization in Python.
str1 = "Hello"
str2 = "World"

# Check memory addresses of individual characters
print("str1[0], str1[1]:", hex(id(str1[0])), hex(id(str1[1])))
print("str1[2], str1[3]:", hex(id(str1[2])), hex(id(str1[3])))
print("str1[4], str2[0]:", hex(id(str1[4])), hex(id(str2[0])))
print("str2[1], str2[2]:", hex(id(str2[1])), hex(id(str2[2])))
print("str2[3], str2[4]:", hex(id(str2[3])), hex(id(str2[4])))
x = "dog"
y = "cat"

# 1. Concatenation
print(x + y)  # dogcat

# 2. Sentence
print("the " + x + " chases the " + y)  # the dog chases the cat

# 3. Repetition
print(x * 4)  # dogdogdogdog

# Incrementing a number
x = 50
x += 1  # x is now 51
print(x)

# hello = "hello"  Works
# _var = 100  Works 
# !var_1 = 200  Does not work. Variable names cannot start with !
# print = "print me"  Works but is not adviced because it replaces Python's built-in print function
# False = 0  Does not work. Reserved keywords cannot be used as variable names

#The main challenge I faced was understanding Python data types and memory addresses.
#I initially struggled with remembering which objects share memory and which get new addresses.
#Also, using id() to check memory addresses was new to me, but it helped clarify how Python handles variables.
