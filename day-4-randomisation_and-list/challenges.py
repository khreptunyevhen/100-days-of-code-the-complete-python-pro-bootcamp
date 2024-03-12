# 1. Randomly tell the user "Heads" or "Tails"

import random

# result = ""
# random_number = random.randint(0, 1)

# if random_number:
# 	result = "Heads"
# else:
# 	result = "Tails"

# print(random_number)
# print(result)

# 2. Who will pay the bill?
# names_string = input("Write the names separate by the coma.\n")
# names = names_string.split(", ")

# random_index = random.randint(0, len(names) - 1)
# print(f"Today {names[random_index]} will pay the bill.")

# 3. Find the treasure

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n")
first_position_char = position[0].lower()
second_position_number = int(position[1])

# horizontal_position = 0

# if first_position_char == "a":
# 	horizontal_position = 0
# elif first_position_char == "b":
# 	horizontal_position = 1
# elif first_position_char == "c":
# 	horizontal_position = 2
# else:
# 	horizontal_position = -1
# 	print("Cannot find this position it is out of the field.")
abc = ["a", "b", "c"]
horizontal_position = abc.index(first_position_char)

map[second_position_number - 1][horizontal_position] = "X"

print(f"{line1}\n{line2}\n{line3}")