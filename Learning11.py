# Guess the number game using python

n = 18
number_of_guesses=1
print("Number of guesses is limited to only 9 times")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number:\n"))
    if guess_number<18:
        print("You enter less number please enter greater number:\n")
    elif guess_number>18:
        print("You enter greater number please input smaller number:\n")
    else:
        print("You Won\n")
        print(number_of_guesses, "number of guesses he took to finish.")
        break
    print(9-number_of_guesses, "no of guesses left")
    number_of_guesses=number_of_guesses+1

if(number_of_guesses>9):
    print("Game Over")