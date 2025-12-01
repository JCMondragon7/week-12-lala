# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temp = int(input("whats the temp outside?"))
#if the temp is between 70 to 150 it is hot
#if its 50 to 69 you its warm
# -20 to 49 cold

if temp >= 70 and temp <= 150:
    print("thats really toatsy")

elif temp >= 50 and temp <=59:
    print("thats decently warm")

elif temp >= 0 and temp <= 49:
    print("yikes thats cold")
