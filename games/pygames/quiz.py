print("Welcome to my computer quiz")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("okay! Let's play! ")
score = 0

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Wrong! ")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Wrong! ")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("Wrong! ")

print("You got " + str(score) + " questions correct")
print("you got " + str((score / 4) *100) + "%")