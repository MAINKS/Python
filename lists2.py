food=["hamburger","pizza","pizza","juice","fries","sushi"]
prices=[5.64,3.92,7.29,4.95,3.20]
food.insert(2,"spaghetti")
#food.clear()  #deletes all list data

food.extend(prices) #adding data of price list to food list.
print(food.index("pizza")) #provides element index asked
print(food.count("pizza")) #count no of times pizza present

random=food.copy()+prices.copy()
print
print(food)