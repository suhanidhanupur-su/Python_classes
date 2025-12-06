# String Methods in Python
#Group of characters./ group of words => String 
# -> A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

# String methods: -
# len() => to find length of string
# lower() => to convert string to lowercase
# upper() => to convert string to uppercase
# title() => to convert first character of each word to uppercase
# strip() => to remove leading and trailing  extra spceces
# split() => to split a string into a list of substrings
# replace() => to replace a substring with another substring
# capitalize() => to capitalize the first character of a string
# find() => to find the index of a substring within a string (returns -1 if not found)
# count() => to count occurrences of a substring in a string
# index() => to find the index of a substring (raises error if not found)

my_string = "    hello world "
print("Original String: '", my_string)
print("After using strip(): '", my_string.strip())


my_name = "ZIyarat"
my_second_name = "xyz"
print("Length of my_name:", len(my_name))
print("Lowercase my_name:", my_name.lower())
print("Uppercase my_name:", my_name.upper())
print("Title Case my_name:", my_string.title())
print("Capitalized my_string:", my_second_name.capitalize())


my_name = "Ujjwal"
my_variable = "python programming"

print("Original String: '", my_variable)
print("After using replace(): '", my_variable.replace("python", "java"))
print(" count of 'm' in my_variable: ", my_variable.count("m"))
print("Index of 'Ujjwal' in my_variable: ", my_name.index("a"))
special_string = "Weclommmmmme"
print("Original String: ", special_string)
print("After using strip(): '", special_string.strip())
print(" after applying split method : ", my_variable.split(" "))
print(" index of m in my_special_string: ", special_string.index("m"))





