# Write your code below this line 👇

# Maths & Numbering

# Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction).
# Next comes the relational operators.
# Finally, the logical operators are done last.

# (%)
# Here X and Y are two integer numbers, and the modulus (%) is used in between
# to get the remainder where the first number (X) is divided by the second number (Y).
# For example, 5 % 2, will give you 1, because 2 into 5 goes twice, with 1 remaining.

from time import sleep

print("I will now count my chickens")
sleep(1)
print("Hens", 25 + 30 / 6)
sleep(1)
print("Roosters", 100 - 25 * 2) # so here the order is 25 times 2, then take that from 100 - giving you 50
sleep(1)
print("Roosters", 100 - 25 * 3 % 4) # the order here is 25 by 3, then whats left when you divide 75 by 4, which is 3, and take the 3 from 100 - giving you 97
sleep(1)
print("Now I will count the eggs:")
sleep(1)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # division first here, and the 4 % 2 gives 0, so 3+2+1=6 -5=1 +0=1 -.25=.75 +6=6.75
sleep(1)
print("Is it true that 3 + 2 < 5 -7?")
sleep(1)
print(3 + 2 < 5 - 7)