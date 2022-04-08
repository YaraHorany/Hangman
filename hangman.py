import hangman_helper

def update_word_pattern(word, pattern, letter):
	start = 0
	for i in range (word.count(letter)):
		index = word.index(letter)
		pattern = pattern[:start+index] + letter + pattern[start+index+1:]
		word = word[index+1:]
		start += index+1
	return pattern


def filter_words_list(words, pattern, wrong_guess_lst):
	possible_words = []
	for i in range(len(words)):
		possible = True
		if len(words[i]) == len(pattern):
			for j in range(0, len(pattern)):
				if pattern[j] != '_': 
					if pattern[j] != words[i][j]:
						possible = False
				if words[i][j] in wrong_guess_lst:
					possible = False
			if possible == True: 
				possible_words.append(words[i])
	return possible_words


def run_single_game(words_list, score):
	word = hangman_helper.get_random_word(words_list)
	pattern = '_' * len(word)
	wrongGuesses = []

	while '_' in pattern and score != 0:
		hangman_helper.display_state(pattern, wrongGuesses, score, 'Keep playing..')
		(choice, guess) = hangman_helper.get_input()

		if(choice == 1): 
			if(len(guess) > 1 or guess.isalpha() == False or guess.islower() == False):
				print('Incorrect input.')
			elif(guess in pattern or guess in wrongGuesses):
				print('You already chose this letter.')
			else: 
				score -= 1
				if(guess in word):
					pattern = update_word_pattern(word, pattern, guess)
					n = word.count(guess)
					score += int((n * (n + 1)) / 2)
				else:
					if guess not in wrongGuesses:
						wrongGuesses.append(guess)

		elif(choice == 2):
			score -= 1
			if(guess == word):
				n = 0
				for i in range(len(word)):
					if(word[i] != pattern[i]):
						n += 1
				score += int((n * (n + 1)) / 2)
				pattern = guess

		elif(choice == 3):
			score -= 1
			possible_words = filter_words_list(words_list, pattern, wrongGuesses)
			n = len(possible_words)
			if n > hangman_helper.HINT_LENGTH:
				hangman_helper.show_suggestions((possible_words[0], possible_words[int(n/hangman_helper.HINT_LENGTH)], possible_words[int((2*n)/hangman_helper.HINT_LENGTH)]))
			else: 
				hangman_helper.show_suggestions(possible_words)

	if score > 0:
		hangman_helper.display_state(pattern, wrongGuesses, score, 'Congratulation!! you won.')
	else: # score = 0
		hangman_helper.display_state(pattern, wrongGuesses, score, f'Game over!! Hidden word: {word}')
		
	return score	



def main():
	words = hangman_helper.load_words()
	numPoints = hangman_helper.POINTS_INITIAL

	# run the first game
	numPoints = run_single_game(words, numPoints)
	numGames = 1 

	while numPoints >= 0:
		answer = hangman_helper.play_again(f'Number of games: {numGames}\nCurrent points: {numPoints}\nDo you want to start a new game?')
		if answer == False:
			break
		else: # answer = true
			if numPoints > 0:
				numPoints = run_single_game(words, numPoints)
				numGames += 1
			else: # numPoints = 0
				numPoints = hangman_helper.POINTS_INITIAL
				numPoints = run_single_game(words, numPoints)
				numGames = 1

if __name__== "__main__" :
	main()