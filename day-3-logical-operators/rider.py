height = int(input("What is your height in cm?\n"))
max_height = 120
bill = 0

if height >= max_height:
	age = int(input("What is your age?\n"))
	if age < 12:
		bill = 5
	elif age < 18:
		bill = 7
	else:
		bill = 12
	photo = input("Do you want photos? Yes/No\n")
	if photo == "Yes":
		bill += 3
		print(f"The total bill is {bill}$")
	else:
		print(f"The total bill is {bill}$")
else:
	print("You cannot ride.")