year = int(input("Please enter the year:\n"))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap")
		else:
			print("No leap")
	else:
		print("Leap")
else:
		print("No leap")
