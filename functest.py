import random 

def hi():
    print ("hi!")
def hello():
    print("hello!")
def Hey():
    print("Hey")
def joke():


    jokeNum = random.randint(0,3)
    if (jokeNum ==0):
        print("What do you call an alligator detective?")
        input()
        print("An investi-gator!")
    elif(jokeNum == 1):
        print("what did the scarecrow win an award?")
        input()
        print("Because he was outstanding in his field.")
    elif(jokeNum==2):
        print("why shouldn't you write with a broken pencil?")
        input()
        print("Because it's pointless.")


def game():
    t = ["Rock", "Paper", "Scissors"]

    computer = t[randint(0,2)]

    #set player to False
    player = False

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]


def intro():

    print("Welcome to the chat bot!")

def process_input(answer):

    if answer == "hello" or answer == "hi":
        hi()
    elif "hi" in answer:
        hello()
    elif answer == "what will you say?":
        Hey()
    elif "joke" in answer:
        joke()
    elif "game" in answer:
        game()
    else:
        print("That's nice")
def main():
        intro()

        while True:
            answer = input("(What would you say?)")
            process_input(answer)

        '''
            if(answer=="back"):
                print("I <3 Girls Who Code")
            break
        '''








# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
