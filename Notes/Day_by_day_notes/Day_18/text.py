# Day: 18

# LISTS + FOR LOOP ON SEQUENCE + LIST METHODS

# 1. List क्या होती है?
# List = Python का ऐसे container जो multiple elements store कर सकता है.
#  List में अलग-अलग type का data भी store कर सकते हैं:
# Example:


# 2. Indexing in List (बहुत जरूरी)
# Index:     0   1    2    3   4   5
# my_list = [11, 22, 333, 43, 66, 77]

# Access:
print(my_list[2])   # 333


# 3. Printing complete list
# Example


# 4. FOR LOOP using Range on List
# example

# यहाँ loop सिर्फ index print कर रहा है, list elements नहीं।

# 5. For Loop Directly on List (IMPORTANT)
# Sequence पर loop → element-by-element चलता है.
#  Sequence = List, Tuple, String, Dictionary, Set
# Example:

# → Output list के सारे elements.

# ⭐ 6. Variable name कुछ भी रख सकते हो
# Example:

# ⭐ 7. FOR LOOP on String
# Index:   0 1 2 3 4
# String = R O H I T

# Example:


# ⭐ 8. Basic Repeating Loop
# Example:



















⭐ 9. LIST METHODS (VERY IMPORTANT)
List methods Python me सबसे ज़्यादा पूछे जाते हैं।
 आज तीन main methods:
append()
extend()
insert() (कल या आगे आएगा but mention कर दिया)

🔥 1. append()
→ List के end में एक ही element add करता है।
my_listt = [11,22,33,44]
print("before:", my_listt)

my_listt.append(99)
print("after:", my_listt)

❌ गलत:
my_listt.append(388,77)

Because append → takes only one argument.

🔥 2. extend()
→ List के end में multiple elements add करता है।
 → extend हमेशा list, tuple, string जैसे iterable लेता है.
Correct:
my_listt = [11,22,33,44]
print("before:", my_listt)

my_listt.extend([33333,99999])
print("after:", my_listt)


❌ गलत:
my_listt.extend(33333,99999)

Error:
 list.extend() takes exactly one argument (2 given)

