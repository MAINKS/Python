#small app to validate passwords / no of try / access denied
#We need numbers and strings

pwd="pass123"
your_answer=""
no_of_trys=3
number_max_of_try=5
max_try="not reached"

while your_answer!=pwd and max_try!="Reached":
    if no_of_trys<number_max_of_try:
        your_answer=input("enter your password")
        no_of_trys=no_of_trys+1
    else:
        max_try="Reached"

if max_try=="Reached":
    print("Account blocked")
else:
    print("Access granted")   

