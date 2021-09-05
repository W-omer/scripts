name = input("Type your name: ")
print("welcome", name, " to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Where do you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:").lower()
    if answer == "walk":
        print("You walked for many miles, ran out of water and you died of dehydration.")
    elif answer == "swim":
        print("You swim out to the middle before you feel something grab your foot, it pulls you down into the river where you drown.")


elif answer == "right":
    answer = input("you walk down a path, it grows darker as the forest becomes thicker. You come upon a stranger sitting by the road playing a Guitar. You can speak to him or you can keep walking, What will you do? ").lower()
    if answer == "walk":
        Print("You make it 5 steps before the stranger yells at you, he is offended that you have ignored him. You see his hands glow blue before the world becomes white. You are dead.")
    elif answer == "speak":
        print("The stranger smiles, he offers you a gift and you take it. It is a note saying you've won this game. Congradulations!")

else:
    print("Answer is invalid.")

replay = input("Play again? ")
if replay == "yes".lower():
    import chooseYourOwnAdventure.py
if replay == "no".lower():
    quit()
