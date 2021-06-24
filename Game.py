import random

x = random.randint(1, 10)
t = 0
y = int(input("Guess the number from 1 up to 10, You have 5 chances...."))



if (y == 123321):
    t = -99
    print('BOOM Error(99T) Now you can try as many as you want')

while x != y:
    # some help
    if y == 123:
        print(t)
    if y == 123321:
        t = -99
        print('BOOM Error(99T) Now you can try as many as you want')

    if y > 10:
        print("Your number is more than 10 TRY AGAIN with less number")
        if y == 991:
            t = t
            t -= 1
        else:
            t -= 1
    elif y < 1:
        print("your number is less than 1 TRY AGAIN with bigger number")
        if t == 0:
            t = t
        else:
            t -= 1
    y = int(input("nop you didn't get it try again"))

    t += 1
    if t == 5:
        print("YOU LOSE GG MAN")
        break

if x == y and t == 0:
    print("YOU WIN")
    print("CASINO")
elif x == y:
    print("YOU WIN")
    print("you try {} times".format(t))

print("Thanks for your time, and I hope you have fun")
print("If you face any problem feel free to tell me")