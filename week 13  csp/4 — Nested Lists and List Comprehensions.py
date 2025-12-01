fruits = ['apples', 'oranges', 'bananas', 'cocunuts']
vegetables = ['celeray', 'carrots', 'potatos']
meats = ['chicken', 'fish', 'turkey']

# groceries = [fruits, vegetables, meats]

# print(groceries[0][0])

groceries = [['apples', 'oranges', 'bananas', 'cocunuts']['celeray', 'carrots', 'potatos']['chicken', 'fish', 'turkey']]

for tmraid in groceries:
    for food in tmraid:
        print(food, end="")
    print()

num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")
           ]

for row in num_pad:
    for num in row:
        print(num, end="")
    print()

# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
lead = ((9,8,7),
        (6,5,4),
        (3,2,1))
# Print the first list.
print(lead[0])
# Print the second item from the third list.
print(lead[2][1])
# Use a list comprehension to extract the last item from each sub-list.
last_items = [row[-1] for row in lead]
print(last_items)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
square = [x**2 for x in range (1,11)]
for x in range (1,11):
    print(x**2)

print(square)