import random 
import time 
global number 
def intro():
    print("May i ask you your name?")
    global number 
    name = input("Enter ur name: ")
    print(name + ", we are going to play a number guessing game, I'm thinking of a number between 1 to 100")
    number= random.randint(1,101)
    if(number%2==0):
        x = 'even'
    else:
        x = 'odd'
    print("\n this is an", x , "number")
    time.sleep(.5)
    print("Go ahead and guess")
    guessestaken = 0 
    while guessestaken <6:
        time.sleep(.25)
        enter=input("enter you guess: ")
        try:
            guess = int(enter)
            if guessestaken<=100 and guess>=1:
                guessestaken = guessestaken + 1
                if guessestaken<6:
                    if guess<number:
                        print("the guess number u have entered is too low ")
                    elif guess>number:
                        print("the guess number u have entered is too high")
                    elif guess!=number:
                        time.sleep(.25)
                        print("try again!")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("that number isnt in the range ")

        except: #if a number wasn't entered
            print("I don't think that "+enter+" is a number. Sorry")
    if guess == number:
        guessestaken = str(guessestaken)
        print('Good job,',name, "! You guessed my number in",guessestaken,'guesses!')
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	print("Do you want to play again?")
	playagain=input()

