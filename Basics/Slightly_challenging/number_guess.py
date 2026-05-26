num=155

print("You have 5 chances to guess a 3 digit number")

chance=5
while chance>0:
    x=int(input("Guess the number:"))
    if x>num:
        print("Lower")
        chance-=1
    elif x<num:
        print("Higher")
        chance-=1
    else:
        print("Wooo You guessed the right one")
        break

print("Congratulations")