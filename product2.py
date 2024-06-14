#Aight , we have 3 people and they have a pizza and we are gonna find out how many slices each person get and gonna calculate the price accordingly.

name_1=input("enter 1st name")
name_2=input("enter 2nd name")
name_3=input("enter 3rd name")

slices=input("enter how many slices in the pizza")
price=input("enter price of whole pizza")

percent_ate_by_person_1=input("what percentage of the pizza"+ name_1+ " ate")
percent_ate_by_person_2=input("what percentage of the pizza"+ name_2+ " ate")
percent_ate_by_person_3=input("what percentage of the pizza"+ name_3+ " ate")

number_of_slices_ate_by_person_1=float(percent_ate_by_person_1)*float(slices)
number_of_slices_ate_by_person_2=float(percent_ate_by_person_2)*float(slices)
number_of_slices_ate_by_person_3=float(percent_ate_by_person_3)*float(slices)

price_to_be_paid_by_person_1=float(percent_ate_by_person_1)*float(price)
price_to_be_paid_by_person_2=float(percent_ate_by_person_2)*float(price)
price_to_be_paid_by_person_3=float(percent_ate_by_person_3)*float(price)

print(name_1+" have ate"+str(number_of_slices_ate_by_person_1)+" slices and have paid"+str(price_to_be_paid_by_person_1)+" for his meal")
print(name_2+" have ate"+str(number_of_slices_ate_by_person_2)+" slices and have paid"+str(price_to_be_paid_by_person_2)+" for his meal")
print(name_3+" have ate"+str(number_of_slices_ate_by_person_3)+" slices and have paid"+str(price_to_be_paid_by_person_3)+" for his meal")