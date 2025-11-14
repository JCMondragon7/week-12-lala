# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections family
My_list = [1, 2, 3, 4, 5]
print(My_list) #5
print(len(My_list))# class list
print(type(My_list[0]))
print(My_list[1:4]) #2-4
print(My_list[1:]) #2-5
print(My_list[:-1]) #1-4
print(My_list[::-1]) #reverse list
My_list.append(6) #adds one number
print(My_list)
My_list.extend([7, 8, 9, 10, 11]) #adding numbers shortcut
print(My_list) #prints new list 1-11
My_list.pop(2) #takes out 2* num(third in sequence)
print(My_list)
My_list.sort() #list in ascending
print(My_list)
My_list.reverse #remove scpecific value
print(My_list)
My_list.remove(4) #remove last item using negatiove inden
print(My_list)
new_list = range(12, 220)# this is how to add a lot more characters without the extra work
print(new_list)
My_list.extend(new_list)
print(My_list)
print(len(My_list))
print(My_list[ : : 3]) #every third num
print(My_list[ : : 10]) #Every tenth number
del My_list[ : : 3]
print(len(My_list))
print(My_list)
#NOTESSSSSSSSSSSSSSSSSSSSSSSSS
# .append - adds an item to the end of a list
# .extend - adds multiple items to the end of a list
# .pop - removes and returns a given item from index 
# .remove - remove specific item
# .sort - sorts list by ascending order
# .reverse - reverses the order of my list

# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.