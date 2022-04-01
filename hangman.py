# Importing Modules
import random

# Create word list
wordList = '''abruptly absurdabyss affix askew avenue awkward axiom 
              azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm 
              boxcar boxful crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves 
              embezzle equip espionage frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo 
              giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen 
              iatrogenic icebox joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki 
              kilobyte lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify 
              naphtha nightclub nowadays numbskull nymph onyx ovary oxidize subway swivel syndrome 
              thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth unknown 
              unworthy unzip uptown vaporize vixen vodka youthful yummy zephyr zigzag zigzagging 
              zilch zipper zodiac zombie'''.split()

# Create Hangman Pics
hangman = ['''
   _____
   |   |
       |
       |
       |
      ___''', '''
   _____
   |   |
   O   |
       |
       |
      ___''', '''
   _____
   |   |
   O   |
   |   |
       |
      ___''', '''
   _____
   |   |
   O/  |
   |   |
       |
      ___''', '''
   _____
   |   |
  \O/  |
   |   |
       |
      ___''', '''
   _____
   |   |
  \O/  |
   |   |
    \  |
      ___''', '''
   _____
   |   |
  \O/  |
   |   |
  / \  |
      ___''']

# Function to choose a random word
def getRandomWord(wordList):
    wordChose = random.randint(0, len(wordList) - 1)
    return wordList[wordChose]

# Function to show board
def displayBoard(missLetters, rightLetters, secretWord):
    print (hangman[len(missLetters)])
    print ()
    print ('Missed Letters: ' + missLetters)
    print ()
    
    # Show number of letters from random word
    blanks = '_' * len(secretWord) 

    # Change blanks from right letters
    for i in range(len(secretWord)): 
        if secretWord[i] in rightLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    print (blanks)
    print ()

# Function to ask for a guess and check it
def getGuess(lettersGuessed):
    while True:
        print ('Guess a letter')
        guess = input().lower()
        if len(guess) != 1:
            print ('Please enter only one letter.')
        elif guess in lettersGuessed:
            print ('You have already guessed that letter! Choose Again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print ('This is not a letter, please try again!')
        else:
            return guess

# Function to play the game again
def playAgain():
    print('Do you want to play again? (y)')
    return input().lower().startswith('y')

# Title of the game
print('===========')
print('--HANGMAN--')
print('===========')

# Set first variables parameters
missLetters = ''
rightLetters = ''
secretWord = getRandomWord(wordList)
finishGame = False

# Loop procedure of the game
while True:
    displayBoard(missLetters, rightLetters, secretWord)

    guess = getGuess(missLetters + rightLetters)

    if guess in secretWord:
        rightLetters += guess

        #Check if the player has won the game
        wonGame = True
        for i in range(len(secretWord)):
            if secretWord[i] not in rightLetters:
                wonGame = False
                break
        if wonGame is True:
            print('Congratulations!, You have won! The secret word is ' + secretWord)
            finishGame = True
    else:
        missLetters += guess

        #Check if the player has lost the game
        if len(missLetters) == len(hangman) - 1:
            displayBoard(missLetters, rightLetters, secretWord)
            print ('You Lost! The secret word is ' + secretWord)
            finishGame = True    

    # Check if the player wants to play again
    if finishGame is True:
        if playAgain() is True:
            finishGame = False
            missLetters = ''
            rightLetters = ''
            secretWord = getRandomWord(wordList)
        else:
            break
            