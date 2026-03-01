# CISC179: Practice Lab – Dictionaries

## 1. Creating and accessing dictionaries

# 1a) Create a dictionary of 10 Marvel characters and their attributes

marvel_dict = {
    "Hero1": "Spider-Man",
    "Alias1": "Peter Parker",
    "Power1": "Spider-Sense",
    "Hero2": "Iron Man",
    "Alias2": "Tony Stark",
    "Power2": "Powered Armor Suit",
    "Hero3": "Black Widow",
    "Alias3": "Natasha Romanoff",
    "Power3": "Martial Arts",
    "Hero4": "Hulk"
}

print("Marvel dictionary with 10 attributes:", marvel_dict)

# 1b) Take user input to add new heroes into my_user_dict
# Ask for Hero Name and Alias, continue until user chooses N

my_user_dict = {}

while True:
    hero_name = input("Enter Hero Name: ")
    hero_alias = input("Enter Hero Alias: ")
    
    if hero_name in my_user_dict:
        print("This hero already exists. Please enter a different hero.")
        continue
    
    my_user_dict[hero_name] = hero_alias
    
    cont = input("Do you want to continue (Y/N)? ").strip().upper()
    if cont == "N":
        break

print("User-created Marvel dictionary:", my_user_dict)

# 1c) Convert a list of tuples into a dictionary and handle duplicate heroes
marvel_tuples = [
    ("Spider-Man", "Peter Parker"),
    ("Iron Man", "Tony Stark"),
    ("Captain America", "Steve Rogers"),
    ("Spider-Man", "Miles Morales")  # Duplicate key
]

marvel_user_dict = {}
for hero, alias in marvel_tuples:
    if hero in marvel_user_dict:
        print(f"Duplicate hero detected: {hero}. Adding suffix '_2'.")
        hero = hero + "_2"
    marvel_user_dict[hero] = alias

print("Marvel dictionary after duplicates handled:", marvel_user_dict)

# 1d) Convert a list of tuples into dictionary using a loop
marvel_list = [("Thor", "God of Thunder"), ("Hawkeye", "Clint Barton"), ("Black Panther", "T'Challa")]
marvel_dict_from_list = {}
for k, v in marvel_list:
    marvel_dict_from_list[k] = v

print("Marvel dictionary from list of tuples:", marvel_dict_from_list)

# 1e) Count words in a Marvel description
marvel_text = """Spider-Man is a superhero appearing in Marvel Comics. Peter Parker gained spider-like abilities after being bitten by a radioactive spider. 
He uses his powers to fight crime in New York City, and is known for his witty humor and strong sense of responsibility."""

# Normalize text and count words
words = marvel_text.replace("(", "").replace(")", "").replace(",", "").replace(".", "").split()
word_count = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1

print("Word frequency in Marvel description:", word_count)

# 2. Troubleshooting

# 2a) Make a copy of a dictionary without affecting original
d_orig = {"Iron Man": "Tony Stark"}
d_copy = d_orig.copy()  # Shallow copy

d_copy["Iron Man"] = "Ironheart"  # Change only the copy

print("Original dictionary:", d_orig)
print("Modified copy:", d_copy)

# 2b) Explanation
# Assigning d_copy = d_orig would create a reference; changes affect both.
# Using .copy() creates a separate dictionary, changes do not affect the original.

# 2c) Generate TypeError: unhashable type: 'list'
# Dictionary keys must be immutable
try:
    d_error = {["Spider-Man", "Peter Parker"]: "Hero"}  # List as key fails
except TypeError as e:
    print("Error:", e)

# 3. Challenges
# - Understanding shallow copy vs reference copy required attention to prevent unwanted changes.
# - Handling duplicate keys in tuples required adding suffixes to avoid overwriting.
