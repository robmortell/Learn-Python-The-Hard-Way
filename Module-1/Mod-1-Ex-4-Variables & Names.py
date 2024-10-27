# Write your code below this line 👇

from time import sleep

######### Variables ##########

cars = 100
spaces_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spaces_in_a_car
average_passengers_per_car = passengers / cars_driven

######### Variables ##########

print("There are", cars , "cars available")
sleep(2)
print("But there are only", drivers, "drivers available..!")
sleep(2)
print("There will be", cars_not_driven, "empty cars today.")
sleep(2)
print("We can transport", carpool_capacity, "people today.")
sleep(2)
print("We have", passengers, "people to carpool today")
sleep(2)
print("We need to put about", average_passengers_per_car, "in each car.")
sleep(2)
