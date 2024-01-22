print("Welcome to the TIP Calculator !!!")
bill = float(input("What was the total bill ???\n$")) #500
tip = int(input("How much tip would you like to give ???\n10 ,12, 15 ???\n")) #10
people = int(input("How many people to split the bill ???\n")) #5

billtip = tip/100 * bill + bill
print(billtip) #550.0

split = billtip / people
total = round(split,2)
total = "{:.2f}".format(split) 
print(f"Per person {total}") #110.00