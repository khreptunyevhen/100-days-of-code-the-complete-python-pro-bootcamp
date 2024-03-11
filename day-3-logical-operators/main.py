# 1

height = int(input("What is your height in cm?\n"))
max_height = 120
check_age = 18

if height >= max_height:
	print("You can ride.")
	age = int(input("What is your age?\n"))
	if age <= check_age:
		print("Please pay $7")
	else:
		print("Please pay $12")
else:
	print("You cannot ride.")

# 2
# number = int(input("Please give me a decimal number:\n"))

# if number % 2 == 0:
# 	print("Even")
# else:
# 	print("Odd")
