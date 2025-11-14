# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections family

# My_list = [1, 2, 3, 4, 5]
# print(My_list) #5
# print(len(My_list))# class list
# print(type(My_list[0]))
# print(My_list[1:4]) #2-4
# print(My_list[1:]) #2-5
# print(My_list[:-1]) #1-4
# print(My_list[::-1]) #reverse list
# My_list.append(6) #adds one number
# print(My_list)
# My_list.extend([7, 8, 9, 10, 11]) #adding numbers shortcut
# print(My_list) #prints new list 1-11
# My_list.pop(2) #takes out 2* num(third in sequence)
# print(My_list)
# My_list.sort() #list in ascending
# print(My_list)
# My_list.reverse #remove scpecific value
# print(My_list)
# My_list.remove(4) #remove last item using negatiove inden
# print(My_list)
# new_list = range(12, 220)# this is how to add a lot more characters without the extra work
# print(new_list)
# My_list.extend(new_list)
# print(My_list)
# print(len(My_list))
# print(My_list[ : : 3]) #every third num
# print(My_list[ : : 10]) #Every tenth number
# del My_list[ : : 3]
# print(len(My_list))
# print(My_list)

# #NOTESSSSSSSSSSSSSSSSSSSSSSSSS
# # .append - adds an item to the end of a list
# # .extend - adds multiple items to the end of a list
# # .pop - removes and returns a given item from index 
# # .remove - remove specific item
# # .sort - sorts list by ascending order
# # .reverse - reverses the order of list
#############################################################
# #why is a list more useful than a variable
# #A list can hold multiple values
# #while a variable can only hold one at a time
# cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
# print(cakes)
# #acces first iten
# print(cakes[0])
# # access last item
# print(cakes[-1])
# #want choc instead vanilla
# cakes[0] = 'strawberry'
# print(cakes) #choc to strawberry
# cakes.append('lemon')
# #add cake to end
# cakes[1] = choc
# print(cakes)
# cakes.pop()
# print(cakes)
# #remove last value
# cakes.insert(2, 'finfetti')
# print(cakes)

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fo_list = ['pizza', 'nuggets', 'pasta', 'burgers', 'beef']

# Print the second and last item.
print(fo_list[1])

# Add a new item using .append().
fo_list.append('apples')
print(fo_list)

# Remove the first item using .pop(0).
fo_list.pop(0)
print(fo_list)

# Reverse your list using .reverse().
fo_list.reverse()
print(fo_list)

# Create a list of 3 lists (matrix), and access the middle element.
tri_list = ['one', 'two', 'three']
print(tri_list[1])


#sets are unordered collectoin of unique items
#do not support indexing or slicing
#mutable meaning u can add or remove items
#created using curly brace
#sets do not allow duplicate items
my_set = {1, 2, 3, 4, 5}
print(my_set) #up
print(type(my_set)) #class set
#add an item
my_set.add(6)
print(my_set)

#tuples are ordered collection of items
#immutable cant modify
#created using paranthesis
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[1])
print(my_tuple[1:4])