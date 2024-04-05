#Jaden Martin
#Free Choice Assignment Hangman
#06/11/23

magic_word=input("Please enter the word being guessed: ")
blanked=[]
ASCII_ALPHA='abcdefghijklmnopqrstuvwxyz'
missed_letters=[]
win= False
guess=0
for i in range(0, len(magic_word)):
    if (magic_word[i].lower() in ASCII_ALPHA):
        blanked.append('_')
    else:
        blanked.append(magic_word[i])
print(''.join(blanked))
blanked=[]
while (guess < 6) & (win != True):
    guess_letter=input("Please guess a letter, or the word: ").lower()
    guess += 1
    print("You have "+ str(6-guess) + " guesses left.")
    print("You have missed these letters: "+ str(missed_letters))
    if (len(guess_letter) > 1):
        if (guess_letter == magic_word.lower()):
            win=True
            print("You have won!")
    else:
        ASCII_ALPHA=ASCII_ALPHA.replace(guess_letter, '/')
        if (guess_letter.lower() not in magic_word.lower()) | (guess_letter.lower() not in ASCII_ALPHA):
            missed_letters.append(guess_letter)
        for i in range(0, len(magic_word)):
            if (magic_word[i].lower() in ASCII_ALPHA):
                blanked.append('_')
            else:
                blanked.append(magic_word[i])
        hold=(''.join(blanked))
        print(hold)
        if (hold == magic_word):
            print("Congrats, you win!")
            win=True
        elif (guess > 6):
            print("You have lost.")
        else:
            blanked=[]
