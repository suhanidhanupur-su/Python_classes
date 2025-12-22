
# Day: 13
# List Slicing

# my_list = [ 111, 222, 444,44, 55, 66]

#   0      1     2     3     4   5     
#  111, 222, 444,44, 55, 66


#  111, 222, 444,44, 55, 66
#   -6    -5    -4    -3   -2  -1


# Slicing :-
# Types: two 
# (a) Two parameter slicing (b) three parameter

# => first parameter => Starting point
# => second parameter => ending point ( excluded)
# => by default the starting point will be 0.
# => by default the ending point will be the last index.



# print("without using starting point :", my_list[ : ])
# starting point => 0
# ending point => last index (if not mentioned ending point then it will not excluded).

# print("without using starting point :", my_list[ :4])
# starting point => 0
# ending point => 4 
# output 0-3 => [111, 222, 444,44]

# Three parameter slicing:-
# 1. starting point 
# 2. ending point 
# 3. GAP (n-1) , by default gap will 1


# 0   1    2   3   4   5   6   7   8    9
# 11 22 33 44 55 66 77 88 99 100  
# my_new_list[0:9:2]

# starting point => 0
# ending point => 9  (excluded)
# GAP = 2 , n-1 , => 2-1 => 1 , we have to skip 1 elementes.

# output => 11,33,55,77,99

# print(my_new_list[ : : 3]) => 11, 44, 77, 100
# startin point => 0
# ending point => last index (not excluded)
# gap = 3, n-1 => 2 , that's why we have skipp 2 elements .

# output => => 11, 44,77,100



# 0   1    2  3    4  5    6   7  8    9
# 11 22 33 44 55 66 77 88 99 100  




# print(my_new_list[ : : -1])

# startin point => 0
# ending point => last index (not excluded)
# gap = -1 

# gap => Negative

# print(my_new_list[4:1:-1])=> [55, 44, 33]


# Note: 
# => When you give a negative gap (-1):

# Python traverses the list from right to left instead of left to right.


# # --------------------------------------------------------------------------------
