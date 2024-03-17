import random

words_list = ["camel", "random", "word", "baboon"]
chosen_word = words_list[random.randint(0, len(words_list) - 1)]
max_attempts = 6

print(chosen_word)

display = []
is_blank = True
end = ""

for _ in range(0, len(chosen_word)):
		display.append("_")

while is_blank:
	guess = input("Please, guess a letter:\n").lower()

	if guess in display:
		print(f"You have already picked the letter {guess}")
	else:
		for index, letter in enumerate(chosen_word):
			if letter == guess:
				display[index] = letter

	if guess not in chosen_word:
		print(f"Sorry, but the letter {guess} does not exist! You lose a life.")
		max_attempts -= 1
		if max_attempts == 0:
			end = f"You lose! The word was {chosen_word}."
			is_blank = False

	print(f"You have: {max_attempts} lives.")
	print(display)

	if "_" not in display:
		is_blank = False
		end = f"You won! The word was {chosen_word}."

print(end)

