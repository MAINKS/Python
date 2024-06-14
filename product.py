#create a app that provides the final price of product by user defined input


price_product_1=input("enter price of 1st product")
quantity_product_1=input("enter the quantity of 1st product")
price_product_2=input("enter price of 2nd product")
quantity_product_2=input("enter the quantity of 2nd product")
price_product_3=input("enter price of 3rd product")
quantity_product_3=input("enter the quantity of 3rd product")

#these input are in the form of the text , we need to change them into num to perform operators

result_product_1=float(price_product_1)*float(quantity_product_1)
print(result_product_1)

result_product_2=float(price_product_2)*float(quantity_product_2)
print(result_product_2)

result_product_3=float(price_product_3)*float(quantity_product_3)

print(result_product_3)

result = result_product_1+result_product_2+result_product_3

print(result)