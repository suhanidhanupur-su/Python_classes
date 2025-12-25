# ⭐ 9. LIST METHODS (VERY IMPORTANT)
# List methods Python me सबसे ज़्यादा पूछे जाते हैं।
#  आज तीन main methods:
# append()
# extend()
# insert() (कल या आगे आएगा but mention कर दिया)

# 🔥 1. append()
# → List के end में एक ही element add करता है।

# ❌ गलत:
# my_listt.append(388,77)
# Because append → takes only one argument.

# 🔥 2. extend()
# → List के end में multiple elements add करता है।
#  → extend हमेशा list, tuple, string जैसे iterable लेता है.
# Correct:


# ❌ गलत:
# my_listt.extend(33333,99999)

# Error:
#  list.extend() takes exactly one argument (2 given)


# ⭐ 3. insert()
# Purpose: Adds an element at a specific index.
# example

# ⭐ 4. remove()
# Purpose: Removes a specific element from the list.
#  Removes only the first occurrence.


# ⭐ 5. pop()
# Purpose:
# By default → removes last element


# With index → removes element at that specific index
# example:



# ⭐ 6. index()
# Purpose: Returns the index of a specific element.


# ❌ If element not found → ValueError
# my_list.index(500)  
# # Error: 500 is not in list

# ⭐ 7. count()
# Purpose: Returns how many times an element appears in the list.


# ⭐ 8. sort()
# Purpose: Sorts the list in ascending order.



# ⭐ 9. reverse()
# Purpose: Reverses the list order.
# # example:
# ⭐ 10. copy()
# Purpose: Creates a duplicate copy of the list.


# ⭐ 11. clear()
# Purpose: Removes all elements from the list.
# # example: