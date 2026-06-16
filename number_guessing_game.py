from random import randint

class Guess():
    
    def __init__(self):
        self.computer=randint(1,100)



print("🎉🎉WELCOME TO THE RANDOM GUESS🎉🎉")

print("════════════════════════════════════════════════════════════════════════════════════════")

print("Before we start lets know the rules : ")
print(" "*25, "Guess the number chosen by the computer between[1-100]. Keep trying until you get it right!")

print("════════════════════════════════════════════════════════════════════════════════════════")



print(" ▄︻デ══━一💥 Let's start! 💥💥💥💥💥")

print("════════════════════════════════════════════════════════════════════════════════════════")

game=Guess()
player=int(input("Enter your guess : "))
print("__________________________________________")

i=1

while(player!=game.computer):

    if(player>game.computer):
        print(" lower number please 🤔")
    
    else:
        print("Higher number please 🤔 ")

    player=int(input("Enter your guess : "))
    print("__________________________________________")
    

    i+=1


print("Your guess is right 🥳🥳🥳🥳")
print(f"It took {i} guesses 🎯🎯🎯🎯")
print("congrats🎊🎊🎉")

if i <= 5:
    print("Excellent! 🎉🥳🎊🎁")
elif i <= 10:
    print("Good!🏅🏅🏅🏅")
else:
    print("Keep practicing! 🤗🤗🤗")

