print("Welcome to the tip calculator!")

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = float(input("What was the total bill? $"))

tip_in_per = tip / 100
total_with_tip = total_bill + total_bill * tip_in_per
bill_per_person = round(total_with_tip / people, 2)

print(f"Each person should pay: ${bill_per_person}")