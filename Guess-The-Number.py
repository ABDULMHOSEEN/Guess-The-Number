# Import randint
from random import *

# TAKE SOME INPUTS
# Take a random number and save it
computer_guess = randint(1, 10)
# set times as a number of guessing
times = 0
# set user value as an input
user_value = int(input("Guess the number from 1 up to 10, You have 5 chances..."))

# Do The processes
while computer_guess != user_value:
    # add 1 to the times
    times += 1
    # some help
    # if the user enter the password 123 print the number of times that has been tried
    if user_value == 123:
        times -= 1
        print("The number of trying is", times)
    # If the user value is == the password 123321 set times to -99
    elif user_value == 123321:
        times = -99
        print('BOOM Error(99T) Now you can try as many as you want')
    #If the user input == this password 991 so mines times by 1
    elif user_value == 991:
        times -= 2

    # Check if the value is in range
    # If the user value is bigger than 10 so print error and minos time by 1
    elif user_value > 10:
        print("Error: Your number is more than 10 TRY AGAIN with less number")
        times -= 1

    # If the number is less than 1 print error
    elif user_value < 1:
        print("Error: Your number is less than 1 TRY AGAIN with bigger number")
        times -= 1

    # Check how many times has the user
    if times == 5:  # If number of times == 5 stop
        break
    # ask the user for a new input
    user_value = int(input("You didn't get it try again..."))

# Check for win
if computer_guess == user_value and times == 0: # If the user win from the first time print win with CASINO
    print("\nYOU WIN")
    print("CASINO")
elif computer_guess == user_value:
    print("\nYOU WIN")
    print("You tried {} times".format(times + 1))
else:
    print("YOU LOSE GG MAN")
print("\nThanks for your time, and I hope you have fun")
print("If you face any problems feel free to tell me")
