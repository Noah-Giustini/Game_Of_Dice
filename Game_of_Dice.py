#   @author Marco Gonzalez
#   @author Noah Giustini
#   revision 1.0 <09/02/2018>

import random
import time

#this function handles the intro text to the game. explains all the rules and how to play
def intro():
    print('Hello Player!')
    time.sleep(1)
    print('\nYou are probably wondering who I am')
    time.sleep(2)
    print('\nI am The GameMaster')
    time.sleep(2)
    print('\nI will be watching over you over the course of this game')
    time.sleep(2)
    print('\nI guess you should know the rules of the game before we start...')
    time.sleep(2)
    print('\nIt is simple really, I give you a dice. And you choose to either roll it or keep it.')
    time.sleep(2)
    print('\nShould you roll it, you will gain a ability based on the number rolled')
    time.sleep(2)
    print('\nHowever should you choose to keep it, I roll a dice. \nEven means you keep the die, Odd means I take it away from you.')
    time.sleep(2)
    print('\nIf you manage to keep the dice, it doubles in power.')
    time.sleep(2)
    print('\nYou need a great sum of power to defeat me, a collective score of 20,\nI wish you good luck!')

#function to handle the rolling of the dice. generates a sudo random integer to simulate a dice roll and then returns it
def diceRoll() :
    mini,maxi = 1,6
    print('\nYou Rolled the Die')
    time.sleep(3)
    number = random.randint(mini,maxi)
    print('\nYou rolled a ' + str(number))
    time.sleep(2)
    return number

#function to handle the keeping of the dice. generates a sudo random integer to simulate a dice roll and returns it
def diceKeep() :  
    mini,maxi = 1,6
    print('\nYou Challenge the GameMaster')  
    time.sleep(3)
    print('\nThe GameMaster Rolls a Die')
    time.sleep(3)
    number = random.randint(mini,maxi)
    print('\nHe rolled a ' + str(number))
    return number

#function for the logic of the dice keep. takes parameter x as an integer and tests to see if it is odd or even. if odd returns 0 and if even returns twice the value of x
def keepLogic(x):
    if (((x + 1) % 2) == 0):
        print()
        print('Player earns 0 points')
        return 0
    else:
        print()
        print("Player earns ", 2*x,"points")
        return (2*x)

#function to handle the ending scene. takes a parameter of score as an integer and if score is greater than 20 then the player wins, otherwise the player loses.
def endScene(score):
    win = 20
    time.sleep(5)
    print('Counting Score.....')
    time.sleep(1)
    print('......')
    time.sleep(1)
    print('......')
    time.sleep(1)
    print("You scored: ",score)
    time.sleep(2)
    if score >= win:
        print('You Win!')
    else:
        print('You Lose!')

#the play function acts as the main function of the game. gives the player 6 turns to either roll or keep the dice. 
def play():
    turn = ["Turn 1","Turn 2","Turn 3","Turn 4","Turn 5","Final Turn"]
    playerScore = 0
    playerLastRoll = 0

    intro()
    for i in range(6):

        print()
        print(turn[i])
        while True:
            d1a = input ('\nDo you want to: A) Roll the die. B) Hold on to the Die. [A/B]? : ')
            if d1a in ['A' , 'B','a','b']:
            # If it was equal - break from while loop
                break

        if d1a in ["a","A"] :
            playerLastRoll = diceRoll() 
            playerScore += playerLastRoll
            print()
            print('Current Score',playerScore)

        elif d1a in ["b", "B"] :
            x = diceKeep()
            add = keepLogic(x)
            playerScore += add
            print()
            print("Current score: ", playerScore)
    endScene(playerScore)

#calling the main play function
play()
