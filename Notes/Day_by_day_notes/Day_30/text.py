# Day 30:- 

# Nested Loop
# A nested loop means a loop inside another loop.
# 👉 Outer loop runs first
#  👉 Inner loop runs completely for each iteration of outer loop

# Example 1: Simple Nested Loop


# Output
# the value of i : 0
# the value of i : 0

# The inner loop runs every time the outer loop runs.

# Example 2: Normal For Loop

# Output
# 0
# Shivam
# 1
# Shivam
# 2
# Shivam
# 3
# Shivam


# How For Loop Works (Step by Step)
# for i in range(0, 4):
#     print(i)

# Execution Steps
# 1️⃣ Initialization
# i = 0
# starting point = 0
# ending point = 4

# 2️⃣ Condition Check
# i < 4

# 3️⃣ Execute Code
# print(i)

# 4️⃣ Increment
# i = i + 1

# This process repeats until the condition becomes False.

# Example 3: Nested Loop with i and j

# Output
# the value of i : 0 the value of j 0
# the value of i : 0 the value of j 1
# the value of i : 0 the value of j 2
# the value of i : 0 the value of j 3
# the value of i : 0 the value of j 4
# the value of i : 1 the value of j 0
# the value of i : 1 the value of j 1
# the value of i : 1 the value of j 2
# the value of i : 1 the value of j 3
# the value of i : 1 the value of j 4


# Nested Loop Execution (Phase-wise Explanation)
# Phase 1 (Outer Loop)
# 1️⃣ Initialization
# i = 0

# 2️⃣ Condition check
# i < 2  →  TRUE

# 3️⃣ Inner loop starts

# Phase A (Inner Loop)
# 1️⃣ Initialization
# j = 0

# 2️⃣ Condition check
# j < 1  → TRUE

# 3️⃣ Execute
# print(i, j)

# 4️⃣ Increment
# j = j + 1


# Phase B
# 1️⃣ Condition check
# j < 1 → FALSE

# ➡ Exit inner loop

# Back to Outer Loop
# 4️⃣ Increment
# i = i + 1


# Phase 2 (Outer Loop)
# 1️⃣ Initialization
# i = 1

# 2️⃣ Condition check
# i < 2 → TRUE

# 3️⃣ Inner loop runs again

# Phase 3
# 1️⃣ Condition check
# i < 2 → FALSE

# ➡ Exit outer loop completely

# Example 4: Nested Loop Output Example
# # the value of i : 0  the value of j : 0
# # the value of i : 1  the value of j : 0


# Example 5: Simple Loop (No Nesting)

# Output
# Nisha
# this is normal for loop
# Nisha
# this is normal for loop
# Nisha
# this is normal for loop


# Correct Nested Loop Example (Recommended)

# Output
# the value of i : 0 the value of j 0
# the value of i : 1 the value of j 0
