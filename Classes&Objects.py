# Classes are set of data that helps to create another type of data that is more personalised.
# Classes are specific data like pizzas and Objects include subdata as types of pizza consideration

from pizza import pizza1

VegPizza = pizza1("vegetarian",5,"small")
Pepeerpizza = pizza1("pepperoni",10,"large")

print(VegPizza.size)
print(Pepeerpizza.type)


