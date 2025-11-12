# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4

print(a == b)   # checks for equality # False
print(a != b)   # checks for not equal # True
print(a > b)    # checks greater than # False
print(a < b)    # Checks less than # True
print(a >= b)   # checks greater than or equal to # False
print(a <= b)   # checks less than or equal to # True


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.
8 > 6 #true
5 == 2 + 3 #true
6 >= 2 + 4 #true
3 < 7 - 4  #false
6 == 2 #false
2 > 6 #false

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

score = int(input("what is your score?"))
#ask for a password
#if the score is between 90 to 100 you get an A
#if its 80 to 89 you get a B
# 70 to 79 is a C
if score >= 60:
    print("You passed the test")
else:
    print("sucks, you didnt pass")
# password = input("What is your password?")

if score >= 90 and score <= 100:
    print("you got an A, nice work")

elif score >= 80 and score <=89:
    print("you got a B, thats ight")

elif score >= 70 and score <= 79:
    print("You got a C, cutting it close i C")

elif score >= 60 and score <= 69:
    print("You got a d, lock in")

else:
    print("You failed. Come see me during aclab.")