product_name  = "\"Toilet Paper\""
product_price = 5.00
delivery_cost = 50


print("##########################")
print(product_name, ":",product_price)

answer = input("Do you want to buy ? ")
# HW1: upgrade the condition 
#      "yes", "y"
#      "Yes", "Y"
if answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":
    order_quantity = int(input("How many ? "))
    order_cost = order_quantity * product_price

    print("--------------------------")
    print("Order Info")
    print(product_name,"x",order_quantity,"=",order_cost)
    print("--------------------------")
    print("Delivery cost >>>", delivery_cost)
    answer = input("Do you want delivery ?>>> " )
    if answer =="yes" or answer == "y" or answer == "Yes" or answer == "Y":
        order_cost += delivery_cost
        print("Order cost (including delivery)",order_cost)
    else:
        print("Order cost (not including delivery)",order_cost)
        print("-----------Thank you--------------") 
else:
    print("Too bad :( ")        
