import random

chooses = ["Rock", "Paper", "Scissors"]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random_index = random.randint(0, len(chooses) - 1)
computer_choose = chooses[random_index]

if user_choose >= 3:
	print("You typed invalid number.")
else:
	print(f"Your chose is:\n{chooses[user_choose]}")
	print(f"Computer chose is:\n{computer_choose}")

	result = ""

	if user_choose == random_index:
		result = "Draw"
	elif user_choose == 0 and random_index == 2:
		result = "You win"
	elif random_index == 0 and user_choose == 2:
		result = "Computer win"
	elif user_choose > random_index:
		result = "You win"
	else:
		result = "You typed invalid number."

	print(f"Result: {result}")