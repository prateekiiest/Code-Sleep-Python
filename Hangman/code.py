import random  # import random library

# method to draw hangman
def draw_hangman(i):
    Graphics =['''_____\n|/  |\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  /\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|\n|''',
    '''_____\n|/\n|   O\n|  /|\n|\n|''',
    '''_____\n|/\n|   O\n|   |\n|\n|''',
    '''_____\n|/\n|   O\n|\n|\n|''',
    '''_____\n|/\n|\n|\n|\n|''',
    '']
    print(Graphics[i])

def pick_random_word():
    # This function picks a random word from the SOWPODS dictionary.
    # open the sowpods dictionary as a text file in readable format
    # for more information on opening files visit https://pythontips.com/2014/01/15/the-open-function-explained/

    with open("sowpods.txt", 'r') as f:
        words = f.readlines()

    # generate a random index
    # -1 because len(words) is not a valid index into the list `words`
    index = random.randint(0, len(words) - 1)

    # print out the word at that index
    # the .strip() function removes all trailing spaces before and after the word
    word = words[index].strip()
    return word


def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")

    # creates a string from the members of the list by using whitespace as a separator
    return " ".join(output)


# make sure that the module is being run standalone and not imported by another user
# visit http://ibiblio.org/g2swap/byteofpython/read/module-name.html for more information
if __name__ == '__main__':
    WORD = pick_random_word()

    # creates a set containing the letters of WORD
    letters_to_guess = set(WORD)

    # creates an empty set
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    # since the classic order for hangman game takes 8 lost chances to hang the man
    num_guesses = 8

    print("Welcome to Hangman!")
    while (len(letters_to_guess) > 0) and num_guesses > 0:
        guess = ask_user_for_next_letter()

        # check if we already guessed that
        # letter
        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            # print out a message
            print("You already guessed that letter.")
            continue

        # if the guess was correct
        if guess in letters_to_guess:
            # update the letters_to_guess
            letters_to_guess.remove(guess)
            # update the correct letters guessed
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            # only update the number of guesses
            # if you guess incorrectly
            num_guesses -= 1

        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(num_guesses))
        draw_hangman(num_guesses)
        # tell the user whether they have won or lost
    if num_guesses > 0:
        print("Congratulations! You correctly guessed the word {}".format(WORD))
    else:
        print("Sorry, you lost! Your word was {}".format(WORD))
