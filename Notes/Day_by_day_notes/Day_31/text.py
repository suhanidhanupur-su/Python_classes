# Day: 31:- 
# Star Pattern
# Pattern to print:
# *
# **
# ***
# ****



# Here:
# Rows (i) = 4


# Columns (j) = 4



# Understanding the Pattern
# Step 1: Convert pattern into numbers
# 1
# 1 2
# 1 2 3
# 1 2 3 4



# Step 2: Row-wise and Column-wise Indexing
# Row (i)   Column (j)

# 1         1
# 2         1 2
# 3         1 2 3
# 4         1 2 3 4



# Step 3: Find the Middle Logic
# Observe carefully:
# Row 1 → j ≤ 1


# Row 2 → j ≤ 2


# Row 3 → j ≤ 3


# Row 4 → j ≤ 4



# Step 4: Relation Between i and j
# Row (i)
# Condition
# 1
# j ≤ i
# 2
# j ≤ i
# 3
# j ≤ i
# 4
# j ≤ i

# 📌 Final Condition:
# j <= i



# Final Code (Nested Loop)
# code:-
# Output
# *
# **
# ***
# ****


# Why end="" is Used?
# end="" → prints stars in the same line


# print() → moves cursor to next line after each row



# General Steps to Solve Any Star Pattern
# 1️⃣ Write the pattern in numbers (1, 2, 3 …)
# 2️⃣ Apply row (i) and column (j) indexing
# 3️⃣ Identify the middle pattern / condition
# 4️⃣ Create a relation between i and j
# 5️⃣ Apply condition inside nested loop

# 🧠 Extra Concept Example
# Question:
#  Which number is added to 7 to get 12?
# 7 + x = 12
# x = 12 - 7
# x = 5

# Same logic is used in pattern problems → finding relation & condition

