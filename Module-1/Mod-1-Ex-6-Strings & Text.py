# Write your code below this line 👇

from time import sleep

######### Variables ##########

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not =  "don't"
y = (f"Those who know {binary} and those who {do_not}.")

hillarious = False
joke_evaluation = "Isn't that joke so funny..?! {}"

w = "This is the left side of..."
e = "a string with a right side."

######### Variables ##########

print(x)
sleep(1)
print(y)
sleep(1)
print(f"I said: {x}")
sleep(1)
print(f"I also said: '{y}'")
sleep(1)
print(joke_evaluation.format(hillarious))
sleep(1)
print(w + e)