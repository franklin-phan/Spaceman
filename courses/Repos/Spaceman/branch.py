import random

letters_guessed = []
#display = ''   DOESNT NEED TO BE GLOBAL VARIABLE?
#This loads a word in the huge text document
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word
#Simple for loop to run through each character in secret word and the if statement desides if it is in letters guessed if it isnt then it returns true
def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return True
    return False
#Simple function to ask for user input
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
#This loops through each character in secret word and if the character is in letters guessed it inputs the character into display which is the blank/word the user sees, if it is not in letters guessed it displays a underscore for a place holder.
def get_guessed_word(secret_word, letters_guessed):
    display = ""
    for i in secret_word:
        if i in letters_guessed:
            display +=i
        else:
            display += "_"
    return display
#This one line function returns guess only if it is in secret word, so it asks if guess is in word.
def is_guess_in_word(guess, secret_word):
    return guess in secret_word
    #Function that asks the user if they want to play again, then follows the request.
def play_again(decision):
    if decision == ("YES"):
        #print("User wants to play again")
        letters_guessed.clear()
        secret_word = load_word()
        spaceman(secret_word)
    elif decision == ("NO"):
        print("Thank you for playing and have a nice day!")
    pass
#This function runs the spaceman game!
def spaceman(secret_word):
#This is for a strech challenge making the amount of guesses you have equal to the length of the secret word
    incorrect_guesses = len(secret_word)
    Game = True
#Welcome text line!
    print(f"Welcome to Space Man user! In this guessing game you have {incorrect_guesses} chances to guess the secret word!")

    while incorrect_guesses > 0 and incorrect_guesses <= len(secret_word) and is_word_guessed(secret_word, letters_guessed) and Game == True:
        print(get_guessed_word(secret_word, letters_guessed))

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            Game = False
            break
        #Asks user for a input changes it to lower case
        guess = user_input("Guess a letter! ").lower()
        print ('---------------------------------')
        
        if guess in secret_word:
            #This is so you can only guess one character!
                if len(guess) > 1:
                    print ("You may only guess 1 character!")
                    print ('---------------------------------')
                elif guess in letters_guessed:
                    print ("That letter has already been guessed! " + get_guessed_word(secret_word, letters_guessed))
                    print ('---------------------------------')
                else:
                    letters_guessed.append(guess)
                    print ('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                    print ('---------------------------------')
        else:
            if len(guess) > 1:
                    print ("You may only guess 1 character!")
                    print ('---------------------------------')
            elif guess in letters_guessed:
                print ("That letter has already been guessed! " + get_guessed_word(secret_word, letters_guessed))
                print ('---------------------------------')
            else:
                letters_guessed.append(guess)
                incorrect_guesses-= 1
                print ('That letter is not in the secret word :( ' + get_guessed_word(secret_word, letters_guessed))
                #This line tells you how many guesses you have left after each incorrect guess.
                print("You have " + (str(incorrect_guesses)) + " guesses left!")
                print ('---------------------------------')

    if not is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        decision = user_input("Would you like to play again? (Yes or No) ").upper()
        play_again(decision)
    #Because this is outside the big if tree if you didint win the game you lost.
    else: #incorrect_guesses == 0:
        print('Sorry, you ran out of guesses. The word was ' + secret_word)
        decision = user_input("Would you like to play again? (Yes or No) ").upper()
        play_again(decision)
    
# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
