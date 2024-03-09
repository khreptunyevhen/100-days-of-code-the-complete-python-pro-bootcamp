# 1. Input 39
# Output 12

# initial_num = input("Two digit number: ")
# first_digit = int(initial_num[0])
# second_digit = int(initial_num[1])
# digits_sum = first_digit + second_digit
# print(digits_sum)

# 2. Calculate BMI

# height = input("Enter height in meters:\n")
# weight = input("Enter weight in kilo:\n")
# bmi = int(weight) / pow(float(height), 2)
# print("Your BMI: " + str(bmi))

# 3. Your life in weeks

max_age = 90
weeks_in_year = 52
current_age = int(input("Your age:\n"))
# Converting age into weeks
max_age_in_weeks = max_age * weeks_in_year
current_age_in_weeks = current_age * weeks_in_year
left_weeks = max_age_in_weeks - current_age_in_weeks

print(f"You have {left_weeks} weeks left.")