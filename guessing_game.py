MAX_GUESS=101
import random
def super_guesser():
    print("vexillography\nmulticulturalism\n747")
    total_games=0
    best_guess=1000000000
    global_total_guesses=0
    play_again='y'
    while (str.lower(play_again[0]) == "y"):
        magic_number=random.randint(0, 101)
        print("Im thinking of a number between 1 and 100...")
        total_guesses=1
        print("Your guess? ", end='')
        guess=int(input())
        while(guess != magic_number):
            if guess < magic_number:
                total_guesses=total_guesses+1
                print("It's higher.")
                print("Your guess? ", end='')
                guess=int(input())
            if guess > magic_number:
                total_guesses=total_guesses+1
                print("It's lower.")
                print("Your guess? ", end='')
                guess=int(input())
            if (guess == magic_number):
                print("You got it right in ", total_guesses, "guesses!")
                print("Would you like to play again? ", end='')
                total_games=total_games+1
                if (total_guesses<best_guess):
                    best_guess=total_guesses
                play_again=input()
                global_total_guesses=global_total_guesses+total_guesses
        statistics(total_guesses, global_total_guesses, best_guess)
def statistics(total_games, global_total_guesses, best_guess):
    print("Overall results:")
    print("Total games   = ", total_games)
    print("Total guesses = ", global_total_guesses)
    print("Guesses/game  = ", (global_total_guesses/total_games))
    print("Best game     = ", best_guess)
def main():
    super_guesser()
main()
