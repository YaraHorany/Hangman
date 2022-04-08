import random

POINTS_INITIAL = 10
HINT_LENGTH = 3

LETTER = 1
WORD = 2
HINT = 3

_rand = random.Random()
play_again_request = False


def set_seed(a=None):
    _rand.seed(a)


def load_words(file='words.txt'):
    words = []
    f_words = open(file)
    for line in f_words:
        word = line.strip()
        if(word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words


def get_random_word(words_list):
    return _rand.choice(words_list)


def get_input():
    choice = input("Enter '!*' to guess a word (replace '*' with your guess), enter '?' to ask for a hint: ")
    if choice == '?':
        return HINT, None
    elif choice and choice[0]=='!':
        return WORD, choice[1:]
    return LETTER, choice


def display_state(pattern, wrong_guess_lst, points, msg):
    print('Wrong guesses:',wrong_guess_lst)
    print('Current pattern:', " ".join(pattern))
    print('Current points:',points)
    print(msg)


def show_suggestions(matches):
    print('Some possible words are:')
    print(matches)


def play_again(msg):
    print(msg)
    print("Enter 'Y' or 'y' for YES, 'N' or 'n' for NO:")
    while True:
        choice = input()
        if choice and choice[0] in 'yY':
            return True
        if choice and choice[0] in 'nN':
            return False
