print("The toppings available are\n1. Onions\n2. Lettuce\n3. Tomato\n4. Olives\n5. Peppers\n6. Tomatoes")
lst =[int(x) for x in input("Enter the S.No of three of your favourite toppings separated by comma:").split(",")]
print(lst)
totNo = int(input("Enter total number of sandwiches you would like to order:"))
totCost = totNo * 5
print("You have ordered {} sandwiches and your order total is: {}$".format(totNo,totCost))
