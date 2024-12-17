import random
class Letter:
	def __init__(self, value, position):
		self.value = value
		self.position = position

fin = open('words.txt')
t = []
for line in fin:
	word = line.strip()
	if len(word) == 5:
		t.append(word)	
length = len(t)
x = random.randint(0,length)
word_to_guess = "slate"

for guess_num in range(1,8):
	print("")
	print("Guess number", guess_num)
	guess = input("Enter a five letter word: ").lower()
	while not(guess.isalpha()) or len(guess) != 5 or not(guess.lower() in t):
		guess = input("Try again: ")
	zxx = guess
	
	objs = list()
	for i in range(len(guess)):
		objs.append(Letter(guess[i],i))
	#removed enumarate and replaced it with this


	def in_twice(word_to_guess, letter_in_word, guess):
		return (guess.count(letter_in_word.value) > word_to_guess.count(letter_in_word.value) and letter_in_word.value in word_to_guess)





	for i in word_to_guess:
		pain = Letter(i,word_to_guess.index(i))
		if in_twice(word_to_guess, pain, guess):
			bad_letter = Letter(i,word_to_guess.index(i))
			break
		else:
			bad_letter = Letter("q",0)



	def check(word_to_guess, letter_in_word, guess):
		new_guess = guess
		if in_twice(word_to_guess, letter_in_word, guess):
			x = guess.rfind(letter_in_word.value)
			z = guess.index(letter_in_word.value)
			if x == letter_in_word.position:
				new_guess = (guess[:z] + "ã" + guess[z+1:])
				return new_guess		
			else:
				new_guess = (guess[:x] + "ã" + guess[x+1:])
				return new_guess

		return new_guess


	new_guess = check(word_to_guess, bad_letter, guess)
	jobjs = list()

	for idx, v in enumerate(new_guess):
		jobjs.append(Letter(str(v),idx))

	for i in range(len(word_to_guess)):
		if (jobjs[i].value == word_to_guess[i]
			and jobjs[i].position == i):
			print("🟩", end="")
		elif jobjs[i].value in word_to_guess:
			print("🟨", end="")
		else:
			print("🟥", end="")
			
	if zxx == word_to_guess:
		print("")
		print("you guessed it!")
		break
	if guess_num == 6:
		print("")
		print("You lost :(, the word was", word_to_guess)
		break
	


