import csv
import logging
import datetime
import time
from ast import Return

class Player: 
    def __init__(self, playerName, turns):
        self.playerName = playerName
        self.turns = turns
    def noOfTurns(self, turns):
        if turns <= 0:
            print("\n\nšŖ¦ šŖ¦  Michael got you!! You made too many wrong choices this Halloween night. šŖ¦ šŖ¦\n\n")
            logging.info(f"out of turns")
            game_ends = datetime.datetime.now()
            logging.info(f"Game started at {game_begins}")
            logging.info(f"Game ended at {game_ends}")
            logging.info(f"Total game time: {game_ends - game_begins}.")
            time.sleep(2)
            csv_file()
            exit()

logging.basicConfig(filename="halloween.log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

def csv_file():
    with open('halloween.log') as file:
        lines = file.read().splitlines()
        lines = [lines[x:x+2] for x in range(0, len(lines), 2)]
    
    with open('halloween.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)

def intro():
    global game_begins
    game_begins = datetime.datetime.now()
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š           It's Halloween 1978 in Haddonfield, IL, and as the local sheriff has claimed:                  š       ")
    print("š                                                                                                          š       ")
    print("š                            'Everyone's entitled to one good scare.'                                      š       ")
    print("š                                                                                                          š       ")
    print("š      Unfortunately, the scare you are about to experience will lead to a fight for your survival         š       ")
    print("š        from a disturbed patient named Michael Myers, who escaped Smith's Grove Sanitarium the            š       ")
    print("š          night before. Your Halloween horror is about to begin if you dare to continue . . .             š       ")
    print("š                                                                                                          š       ")
    print("š           If you decide to proceed, please provide your name so that we know what to place               š       ")
    print("š         on your gravestone. You know . . . in the event that your efforts are futile . . .               š       ")
    print("š                                                                                                          š       ")
    print("š                                        MUAH HA HA HA HA!                                                 š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

    logging.info(f"Requesting name for game.")
    global player
    player = Player(input("What is your name? "), 3)

    while True:
        if (len(player.playerName.strip())):
            break
        else:
            logging.info(f"No valid name provided.")
            logging.info(f"Requesting name for game again.")
            time.sleep(1)
            player = Player(input("You must provide a name. What is your name? "), 3)
            Return

    print(f"\nWelcome, {player.playerName}! Be warned - you must be ready for him. . . if you don't, it's your funeral.")

    response = input("\nDo you think you can survive the night with the evil and maniacal Michael Myers on the loose? Yes or No? ")

    while True:
        if response.lower() == 'yes':
            print("\n\nWonderful! Let's get started!")
            firstScenario()
        elif response.lower() == 'no':
            logging.info(f"You gave up before even starting.")
            game_ends = datetime.datetime.now()
            logging.info(f"Game started at {game_begins}")
            logging.info(f"Game ended at {game_ends}")
            logging.info(f"Total game time: {game_ends - game_begins}.")
            time.sleep(1)
            print(f"\nPoor, {player.playerName}. It's tragic, you NEVER go out. You gave up before even starting the game.") 
            print("\nHope you come back and play the entire game next time!\n")
            exit()
        else: 
            print("\nYou must answer Yes or No")
            response = input("\nDo you think you can survive the night with the evil and maniacal Michael Myers on the loose? Yes or No? ")
            Return
print("")

def firstScenario():
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š     It's Halloween night and your friend, Annie, has asked you to babysit Lindsey, the little girl       š       ")
    print("š       she is watching across the street. Annie wants to spend time with her boyfriend and because        š       ")
    print("š        you are such a great friend, you agree to help her out this time since you will also be           š       ")
    print("š                            babysitting your neighbor's kid, Tommy Doyle.                                 š       ")
    print("š                                                                                                          š       ")
    print("š      As the night goes on, Tommy claims that he sees the 'boogie man' across the street carrying         š       ")
    print("š                  a lifeless Annie, which sends him into a fit of hysterical crying.                      š       ")
    print("š                                                                                                          š       ")
    print("š                                       What will you do?                                                  š       ")
    print("š                                                                                                          š       ")
    print("š                      A: Do you believe Tommy and go check on your friend?                                š       ")
    print("š                                              OR                                                          š       ")
    print("š             B: Do you disregard Tommy's claim, since he is most likely paranoid from                     š       ")
    print("š                   the creepy Halloween movies he has been watching all night?                            š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            logging.info(f"Right choice made to believe Tommy.")
            time.sleep(1)
            print("\n\nGreat Choice! Let's keep surviving the night!")    
            secondScenario()
        elif response.lower() == 'b':
            logging.info(f"Wrong choice made to disregard Tommy's claim.")
            time.sleep(1)
            player.turns -= 1
            player.noOfTurns(player.turns)
            firstScenarioWrong()
            print("Let's try again!")
            firstScenario()
        else:
            logging.info(f"Invalid answer provided.")
            time.sleep(1) 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def firstScenarioWrong():
    logging.info(f"Provided response for wrong choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š                               This was not the best choice to make.                                      š       ")
    print("š                                                                                                          š       ")
    print("š            After murdering your friend, Michael continues his killing spree throughout the               š       ")
    print("š             neighborhood, increasing his death toll this Halloween night in Haddonfield.                 š       ")
    print("š                                                                                                          š       ")
    print("š                      It is recommended you make the right decision next time.                            š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   

def secondScenario():
    logging.info(f"Provided response for right choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                ")
    print("š                                                                                                          š       ")
    print("š     After you put the kids to bed, you walk across the street and knock on the front door, but no one    š       ")
    print("š       answers. You cautiously make your way to the backyard and see that the backdoor is wide open.      š       ")
    print("š         You make your way into the dark house and up the stairs. In one of the bedrooms, you see         š       ")
    print("š             Annie's motionless body on the bed. You want to check on Annie, but then you hear            š       ")
    print("š                                the floor boards squeek behind you.                                       š       ")
    print("š                                                                                                          š       ")
    print("š                                       What will you do?                                                  š       ")
    print("š                                                                                                          š       ")
    print("š                  A: Do you run to a nearby phone in the house to call for help?                          š       ")
    print("š                                              OR                                                          š       ")
    print("š                  B: Turn, run downstairs, and across the street back to safety?                          š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            logging.info(f"Wrong choice made to get to a nearby phone.")
            time.sleep(1)
            player.turns -= 1
            player.noOfTurns(player.turns)
            secondScenarioWrong()
            print("Let's try again!")
            secondScenario() 
        elif response.lower() == 'b':
            logging.info(f"Right choice made to run across the street.")
            time.sleep(1)
            print("\n\nGreat Choice! Let's keep surviving the night!") 
            thirdScenario() 
        else:
            logging.info(f"Invalid answer provided.")
            time.sleep(1) 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def secondScenarioWrong():
    logging.info(f"Provided response for wrong choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š                               This was not the best choice to make.                                      š       ")
    print("š                                                                                                          š       ")
    print("š            Reaching for a nearby phone, you quickly realize that the phone line is dead, and             š       ")
    print("š             the 'floor squeaker,' Michael, wastes no time swinging his knife, cutting your               š       ")
    print("š                                   shirt, and wounding your arm.                                          š       ")
    print("š                                                                                                          š       ")
    print("š             Tsk tsk. Your choices are costing you your wardrobe! You are not dead yet, so you            š       ")
    print("š                        still have a chance to make a better choice next time.                            š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

def thirdScenario():
    logging.info(f"Provided response for right choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š        As you return to the Doyle residence, you get into the house and lock the door behind you          š       ")
    print("š      As you catch your breath and try to compose yourself, you hear a curtain flutter behind you,        š       ")
    print("š      finding that the window has been left open. You quickly close the window and hastily attempt        š       ")
    print("š                  to secure the other rooms, but to your dismay, you learn that                           š       ")
    print("š                                 Michael is already in the house!                                         š       ")
    print("š                                                                                                          š       ")
    print("š                                       What will you do?                                                  š       ")
    print("š                                                                                                          š       ")
    print("š                      A: Do you run up the stairs to hide with the children?                              š       ")
    print("š                                              OR                                                          š       ")
    print("š              B: Run to the kitchen and grab a butcher knife to duel the masked madman?                   š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            logging.info(f"Right choice made to run upstairs with the children.")
            time.sleep(1)
            print("\n\nGreat Choice! Let's keep surviving the night!") 
            fourthScenario()   
        elif response.lower() == 'b':
            logging.info(f"Wrong choice made to fight Michael.")
            time.sleep(1)
            player.turns -= 1
            player.noOfTurns(player.turns)
            thirdScenarioWrong()
            print("Let's try again!")
            thirdScenario()
        else:
            logging.info(f"Invalid answer provided.")
            time.sleep(1) 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def thirdScenarioWrong():
    logging.info(f"Provided response for wrong choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š                               This was not the best choice to make.                                      š       ")
    print("š                                                                                                          š       ")
    print("š        You discover you're not as experienced with your weapon choice as Michael. He swiftly             š       ")
    print("š                  disarms and injures you again, causing a cut to your upper thigh.                       š       ")
    print("š                                                                                                          š       ")
    print("š                    Your choice has now left you between a rock and a dead place.                         š       ")
    print("š                        Choose better next time to keep your limbs intact!                                š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

def fourthScenario():
    logging.info(f"Provided response for right choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š     You effectively hide the children, but your own hiding spot in the closet is not the most ideal      š       ")
    print("š       Despite tying the closet doors shut with a tie you find, Michael begins breaking through the       š       ")
    print("š        doors. As he pulls his body into the closet to try to reach for you, you grab a hanger            š       ")
    print("š             and scratch him in the eye, which takes him aback. His vision is compromised,                š       ")
    print("š                             allowing you to escape from the closet.                                      š       ")
    print("š                                                                                                          š       ")
    print("š                You find a knitting needle and thrust it into his neck, which appears                     š       ")
    print("š                               to finally put his rampage to an end.                                      š       ")
    print("š                                                                                                          š       ")
    print("š                                       What will you do?                                                  š       ")
    print("š                                                                                                          š       ")
    print("š                     A: Do you grab the kids and run to the police station?                               š       ")
    print("š                                              OR                                                          š       ")
    print("š              B: Send the kids to a neighbor's house to contact the authorities while you                 š       ")
    print("š                               rest and wait for help to come?                                            š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            logging.info(f"Wrong choice made to run to the police station.")
            time.sleep(1)
            player.turns -= 1
            player.noOfTurns(player.turns)
            fourthScenarioWrong()
            print("Let's try again!")
            fourthScenario() 
        elif response.lower() == 'b':
            logging.info(f"Right choice made to send the kids for help.")
            time.sleep(1)
            print("\n\nGreat final choice! Now you can rest. . . but wait. . . ")
            conclusion() 
        else:
            logging.info(f"Invalid answer provided.")
            time.sleep(1) 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def fourthScenarioWrong():
    logging.info(f"Provided response for wrong choice.")
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š                               This was not the best choice to make.                                      š       ")
    print("š                                                                                                          š       ")
    print("š      The police station is all the way across town, and you don't get too far before the kids            š       ")
    print("š          get tired and become overly emotional to continue the journey. Michael somehow                  š       ")
    print("š              survives his injury and takes advantage of your slow pace, catching up to you.              š       ")
    print("š                                  Now three lives are indeed at stake.                                    š       ")
    print("š                                                                                                          š       ")
    print("š            The horrors of babysitting kids! Dragging them along was not the best choice.                 š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")

def conclusion():
    logging.info(f"Provided concluding paragraph for the game.")
    game_ends = datetime.datetime.now()
    logging.info(f"You survived with {player.turns} turns left.")
    logging.info(f"Game started at {game_begins}")
    logging.info(f"Game ended at {game_ends}")
    logging.info(f"Total game time: {game_ends - game_begins}.")
    csv_file()
    print("\nš š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š                 ")
    print("š                                                                                                          š       ")
    print("š                                  Ahh!! Michael is still alive!                                           š       ")
    print("š                                                                                                          š       ")
    print("š          He runs towards you, raising his arm to deliver one final, fatal swing of his knife.            š       ")
    print("š         However, Michael's psychiatrist from Smith's Grove Sanitarium, Dr. Loomis, is there to           š       ")
    print("š            the rescue with his Smith & Wesson Model 15. He uses the revolver on his patient              š       ")
    print("š                    sending him back flying through a second-floor bedroom window.                        š       ")
    print("š                                                                                                          š       ")
    print("š        It is over now. You can rest. You have successfully survived the night. You look out the          š       ")
    print("š                        broken window and see that Michael is. . . GONE!                                  š       ")
    print("š                                                                                                          š       ")
    print("š                         Never forget: 'You can't kill the boogie man!'                                   š       ")
    print("š                                                                                                          š       ")
    print("š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š š \n \n  ")   
    print("")
    exit()
intro()






        



