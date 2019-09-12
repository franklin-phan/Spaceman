import random

    
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word
def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
            if counter == len(secret_word):
              return True
        return False
def get_guessed_word(secret_word, letters_guessed):
    display = ""
    for i in secret_word:
        if i in letters_guessed:
            display +=i
        else:
            display += "-"
    return display
def is_guess_in_word(guess, secret_word):
    return guess in secret_word

def spaceman(secret_word):
  next_game = True
  attempts = 7
  letters_guessed = []
  print(f"Welcome to Spaceman! You have 7 chances to guess the secret word!")
  print (get_guessed_word(secret_word,letters_guessed))

  while next_game and is_word_guessed(secret_word, letters_guessed) == False and attempts>0:
    #ASCII Astronaut from https://www.asciiart.eu/space/astronauts
  
    SPACEMAN = [
r"""\
         
     
    
   
  
   
  
    
   
    
    
        
                
         /-._/-._/
         \   `\  \
          `-._/._/
""",
r"""\
            
      
     
   
   
   
   
  
 


         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
""",
r"""\
        
      
     
   
   
   
   
  
 
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
""",
r"""\
        
    
    
   
    
     .- -;.__.
   .'=  *=| 
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
""",
r"""\
           
                     _
                   _/ \
                  |   |
                .-'-./
     .-'-;:__.'    =/
   .'=  *=|     _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
""",
r"""\
           
                     _
                   _/ \
                  |   |
                .-'-./
     .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \n
          `-._/._/
""",
r"""\
            _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/
"""
    ]
    # print(SPACEMAN[0])
    #TODO: show the player information about the game according to the project spec
   
   #TODO: Ask the player to guess one letter per round and check that it is only one letter
    guess = (input("\nPlease guess a letter: ")).lower()

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    if guess in secret_word:
        if len(guess) > 1: # check the input is only one letter
          print("That is more than one letter. Please try again.")
        elif guess in letters_guessed:
          print("You already guessed that letter.")
        else:
          letters_guessed.append(guess)
        print ('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
    else:
        if len(guess) > 1: # check the input is only one letter
          print("That is more than one letter. Please try again.")
        elif guess in letters_guessed:
          print("You already guessed that letter.")
        else:
          letters_guessed.append(guess)
          print(SPACEMAN[7-attempts])
          attempts-= 1
          print ('That letter is not in the secret word. ' + get_guessed_word(secret_word, letters_guessed))
           #This line tells you how many guesses you have left after each incorrect guess.
          print("You have " + (str(attempts)) + " guesses left!")
    
    #TODO: check if the game has been won or lost
  if is_word_guessed(secret_word, letters_guessed):
        print('Spacetacular Job! The spaceman lives another day! You correctly guessed the word '+ secret_word)
        response = input("\nWould you like to save another spaceman? ")
        if response in ("yes", "y"):
            next_game = True
            spaceman(load_word())
        else:
            next_game = False
            print("Thanks for playing! See you space cowboy.")
  else:
        print('The spaceman dies because you couldn\'t guess the word '+ secret_word +'. You\'re going to carry that weight.')
        response = input("\nWould you like to kill another spaceman? ")
        if response in ("yes", "y"):
            next_game = True
            spaceman(load_word())
        else:
            next_game = False
            print("Thanks for playing! See you space cowboy.")

#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())