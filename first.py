item = input("what item would you like to buy ?")
quantity = int(input("how many would you like ?"))
price = float(input("what is the price ?"))
total = quantity * price 
print(f"you have bought : {quantity} x {item}")
print(f"the total cost is : ${total}")