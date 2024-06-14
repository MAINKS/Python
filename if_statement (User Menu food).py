#works on boolean data type :- true and false

I_want_to_eat=True
I_want_to_drink=False

if I_want_to_eat:     #simple if command
    print("Lets have a pizza")
else:
    print("i am good")

if not I_want_to_eat:  #not command opp of if
    print("i am good")
else:
    print("i am fine")    



if I_want_to_eat==False:   #assigning true value as false in if statement
    print("Lets have a pizza")
else:
    print("i am good")



if I_want_to_eat and I_want_to_drink:   #and command in if
    print("Lets have a pizza")
else:
    print("i am good")


if I_want_to_eat or I_want_to_drink:   #or command
    print("Lets have a pizza")
else:
    print("i am good")   


if I_want_to_eat:    #additional elif command
    print("Lets have a pizza")
elif I_want_to_drink:
    print("lets have a drink")    
else:
    print("i am good")