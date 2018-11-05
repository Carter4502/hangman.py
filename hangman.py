import time
import math
start = time.time()
print("WELCOME TO HANGMAN!!")
print("What would you like your word to be?")
ogword = input("input your word here: ")
word = ogword.lower()
print("Ok now give it to the player tryna guess ur word.")
time.sleep(5)
length = str(len(word))
print("Before we get started... the word given is " + length + " letters long. (including spaces)")
time.sleep(2)
print("You will get 12 guesses before you must guess the full word.")
time.sleep(1)
print("Now.. take a guess and i will tell you if the letter is in the word.")
g1 = input("first guess: ")
if g1 in word:
	position = str(word.index(g1) + 1)

	print("That is letter number " + position + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g2 = input("second guess: ")
if g2 in word:
	position2 = str(word.index(g2) + 1)

	print("That is letter number " + position2 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g3 = input("third guess: ")
if g3 in word:
	position3 = str(word.index(g3) + 1)

	print("That is letter number " + position3 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g4 = input("fourth guess: ")
if g4 in word:
	position4 = str(word.index(g4) + 1)

	print("That is letter number " + position4 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g5 = input("fifth guess: ")
if g5 in word:
	position5 = str(word.index(g5) + 1)

	print("That is letter number " + position5 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g6 = input("sixth guess: ")
if g6 in word:
	position6 = str(word.index(g6) + 1)

	print("That is letter number " + position6 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g7 = input("seventh guess: ")
if g7 in word:
	position7 = str(word.index(g7) + 1)

	print("That is letter number " + position7 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g8 = input("eighth guess: ")
if g8 in word:
	position8 = str(word.index(g8) + 1)

	print("That is letter number " + position8 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g9 = input("nineth guess: ")
if g9 in word:
	position9 = str(word.index(g9) + 1)

	print("That is letter number " + position9 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
g10 = input("LAST guess: ")
if g10 in word:
	position10 = str(word.index(g10) + 1)

	print("That is letter number " + position10 + " in the " + length + " letter long word.")
else:
	print("That is not part of the word...")
print("Now, take your guess on what you think the word is.")
guess = input("Guess: ").lower()
end = time.time()
if guess == word:
	time = end - start
	print("YOU WIN!")
	print("It took " + str(end - start) + " seconds for you to guess the word.")
else:
	print("You lose :/")