print("Welcome to Treasure island!")
print("Your mission is to find the treasure.")
road_choose = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\".\n").lower()

if road_choose == "left":
	lake_choose = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
	if lake_choose == "wait":
		room_choose = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
		if room_choose == "red":
			print("It is a room full of fire. Game over!")
		elif room_choose == "blue":
			print("You enter a room of beasts. Game over!")
		elif room_choose == "yellow":
			print("You found the treasure. You win!")
		else:
			print("You choose a door that doesn't exist. Game over!")
	else:
		print("You got attack by an hungry trout. Game over!")
else:
	print("Yo fell into a hole. Game over!")