print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

final_bill = 0

if size == "S":
	final_bill += 15
elif size == "M":
	final_bill += 20
elif size == "L":
	final_bill += 25
else:
	print("We dont have this size of pizza.")

if add_pepperoni == "Y":
	if size == "S":
		final_bill += 2
	else:
		final_bill += 5

if extra_cheese == "Y":
	final_bill += 5
print(f"Your total bill is: {final_bill}$")

