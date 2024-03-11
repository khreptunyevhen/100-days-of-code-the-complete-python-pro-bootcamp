height = input("Enter height in meters:\n")
weight = input("Enter weight in kilo:\n")
bmi = round(int(weight) / pow(float(height), 2), 1)
# print("Your BMI: " + str(bmi))

if bmi < 18.5:
	print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
	print(f"Your BMI is {bmi}, you are normal.")
elif bmi < 30:
	print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
	print(f"Your BMI is {bmi}, you are obese.")
else:
	print(f"Your BMI is {bmi}, you are clinically obese.")
