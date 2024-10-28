# Write your code below this line 👇

from time import sleep

######### Variables ##########

name = 'Rob Mortell'
age = 42 # not a lie
height = 69 # inches
height_in_cm = round(height * 2.54)
weight = 200 # lbs
weight_in_kg = round(weight * 0.45359237)
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

######### Variables ##########

print(f"Let's talk about {name}.")
sleep(1)
print(f"He's {height} inches tall.")
sleep(1)
print(f"That is {height_in_cm} cm's.")
sleep(1)
print(f"He weighs {weight} pounds.")
sleep(1)
print(f"That is {weight_in_kg} kilo's.")
sleep(1)
print("Actually that's not too heavy.")
sleep(1)
print(f"He's got {eyes} eyes and {hair} hair.")
sleep(1)
print(f"His teeth are usually {teeth}, depending on the coffee.")
sleep(1)

total = age + height + weight

print(f"If I add {age}, {height} and {weight} I get {total}.")