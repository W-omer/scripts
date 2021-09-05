import random

input("Do you want to Play a game? ")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger that 0. ")
        quit()
    
else:
    print('Please type a number next time. ')
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)


while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("You got it! ")
        break
    else:
        if user_guess > random_number:
            print("You were above the number! ")
        else:
            print("You were below the number")
    break

print("you got it in", guesses, "guesses")
