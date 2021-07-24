from random import randint # imports the random integer function from the random module

computer_guess = randint(1, 50) # stores the unknown number in a variable
chances = 5 # sets the chances available to the user to 5


def mainMenu(): # defines the main menu function, which will be prompted to the user every now and then
    global chances
    print('-' * 55)
    print("Guess the number from 1 up to 50, You have %d chances..." % chances)
    print('OR enter 404 to give up and show the answer...')
    print('-' * 55)
    user_value = int(input())  # stores the user's value

    return user_value

def hotCold(num,unknown): # defines the hot or cold function that will assist the user in guessing the number

    if num > unknown:
        if (num - 5) < unknown:
            result = 'Hotter'
        elif (num - 10) < unknown:
            result = 'bit hotter'
        else:
            result = 'Colder'
    elif num < unknown:
        if (num + 5) > unknown:
            result = 'Hotter'
        elif (num + 10) > unknown:
            result = 'bit hotter'
        else:
            result = 'Colder'
    else:
        result = 'Colder'

    return result

choice = mainMenu() # stores the choice made by the user from the main menu function into a variable

# Computation Section
while computer_guess != choice and choice != 404:  # this while loop will be executed till the specified condition

    # validates the range
    if choice > 50 or choice < 1:
        print('Be careful mate... Your guess is out of range')
        choice = mainMenu()
    else:
        # deducts the counter with each valid guess
        chances -= 1
        # if there are no more chances available, the loop gets interrupted and the code proceeds to the next lines
        if chances == 0:
            break
        tip = hotCold(choice, computer_guess) ## stores the result of the hot or cold function in a variable
        print('Try again... \"Hint: You are getting %s \"' % tip) ### prints the result of it
        choice = mainMenu() # prompts the user for another guess

# Check for the result based on the above computations
if computer_guess == choice and chances == 5:  # If the user wins from the first time
    print("\nYOU WIN")
    print('You guessed the number successfully!!!')
    print("CASINO")
elif computer_guess == choice:
    print("\nYOU WIN")
    print('You guessed the number successfully!!!')
elif choice == 404: # if the user gives up and wants to see the unknown number
    print('Sorry mate...')
    print('The unknown number was %d' % computer_guess)
    print('Thanks for your time')
else: # if the user failed to guess the number
    print("YOU LOSE GG MAN")
    print('The unknown number was %d' % computer_guess)
    print("\nThanks for your time, and I hope you have fun")

# developer's message to the user
print("Feel free to contact me if you face any issues.")