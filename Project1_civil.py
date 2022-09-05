import random
random_number = random.randint(1,3)
def game_1(comp,user):
    if comp == user.lower():
        print("You tried well but This is a tie")
    else:
        if user.lower() == "stone":
            if comp == "scissor":
                print("Congrats, You Win, Lets win once more")
            elif comp == "paper":
                print("Sorry! You Loss this time, Lets try once more")
        elif user.lower() == "paper":
            if comp == "scissor":
                print("Sorry! You Loss this time, Lets try once more")
            elif comp == "stone":
                print("Congrats, You Win, Lets win once more")
        elif user.lower() == "scissor":
            if comp == "stone":
                print("Sorry! You Loss this time, Lets try once more")
            elif comp == "paper":
                print("Congrats, You Win, Lets win once more")
        else:
            print("oops! You don't choose anything from stone, paper, scissor")
print("Choose a thing between stone, paper, scissor\n")
user=input()
if random_number == 1:
    comp="stone"
elif random_number == 2:
    comp = "paper"
else:
    comp = "scissor"
print(f"Let the Computer to chose And computer choose {comp}")
a=game_1(comp,user)

