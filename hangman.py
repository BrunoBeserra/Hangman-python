import random

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

def getRandomWord(wordList):
    wordChose = random.randint(0, len(wordList) - 1)
    return wordList[wordChose]

def displayBoard(missLetters, rightLetters, secretWord):
    print (hangman[len(missLetters)])
    print ()
    print ('Missed Letters: ' + missLetters)
    print ()
    
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in rightLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    print (blanks)
    print ()

def getGuess(alreadyGuessed):
    while True:
        print ('Guess a letter')
        guess = input().lower()
        if len(guess) != 1:
            print ('Please enter only one letter.')
        elif guess in alreadyGuessed:
            print ('You have already guessed that letter! Choose Again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print ('This is not a letter, please try again!')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (y)')
    return input().lower().startswith('y')

print('===========')
print('--HANGMAN--')
print('===========')

missLetters = ''
rightLetters = ''
secretWord = getRandomWord(wordList)
finishGame = False

while True:
    displayBoard(missLetters, rightLetters, secretWord)

    guess = getGuess(missLetters + rightLetters)

    if guess in secretWord:
        rightLetters += guess

        #Check if the player has won
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

        #Check if the player has lost
        if len(missLetters) == len(hangman) - 1:
            displayBoard(missLetters, rightLetters, secretWord)
            print ('You Lost! The secret word is ' + secretWord)
            finishGame = True    

    if finishGame is True:
        if playAgain() is True:
            finishGame = False
            missLetters = ''
            rightLetters = ''
            secretWord = getRandomWord(wordList)
        else:
            break
            