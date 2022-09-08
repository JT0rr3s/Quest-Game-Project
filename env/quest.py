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
            print("\n\n🪦 🪦  Michael got you!! You made too many wrong choices this night. 🪦 🪦\n\n")
            logging.info(f"out of turns")
            time.sleep(2)
            create_csv()
            exit()

logging.basicConfig(filename="halloween.log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

def create_csv():
    with open('halloween.log') as file:
        lines = file.read().splitlines()
        lines = [lines[x:x+2] for x in range(0, len(lines), 2)]
    
    with open('halloween.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)

def intro():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃           It's Halloween 1978 in Haddonfield, IL, and as the local sheriff has claimed:                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                            'Everyone's entitled to one good scare.'                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃      Unfortunately, the scare you are about to experience will lead to a fight for your survival         🎃       ")
    print("🎃        from a disturbed patient named Michael Myers, who escaped Smith's Grove Sanitarium the            🎃       ")
    print("🎃          night before. Your Halloween horror is about to begin if you dare to continue . . .             🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃           If you decide to proceed, please provide your name so that we know what to place               🎃       ")
    print("🎃         on your gravestone. You know . . . in the event that your efforts are futile . . .               🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                        MUAH HA HA HA HA!                                                 🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

    global player
    global total
    player = Player(input("What is your name? "), 1)

    while True:
        if (len(player.playerName.strip())):
            break
        else:
            player = Player(input("You must provide a name. What is your name? "))
            Return

    print(f"\nWelcome, {player.playerName}! Be warned - you must be ready for him. . . if you don't, it's your funeral.")

    response = input("\nDo you think you can survive the night with the evil and maniacal Michael Myers on the loose? Yes or No? ")

    while True:
        if response.lower() == 'yes':
            print("\n\nWonderful! Let's get started!")
            firstScenario()
        elif response.lower() == 'no':
            print("\nGo home then! You're wasting my time!")
            exit()
        else: 
            print("\nYou must answer Yes or No")
            response = input("\nDo you think you can survive the night with the evil and maniacal Michael Myers on the loose? Yes or No? ")
            Return
print("")

def firstScenario():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃     It's Halloween night and your friend, Annie, has asked you to babysit Lindsey, the little girl       🎃       ")
    print("🎃       she is watching across the street. Annie wants to spend time with her boyfriend and because        🎃       ")
    print("🎃        you are such a great friend, you agree to help her out this time since you will also be           🎃       ")
    print("🎃                            babysitting your neighbor's kid, Tommy Doyle.                                 🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃      As the night goes on, Tommy claims that he sees the 'boogie man' across the street carrying         🎃       ")
    print("🎃                  a lifeless Annie, which sends him into a fit of hysterical crying.                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                       What will you do?                                                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                      A: Do you believe Tommy and go check on your friend?                                🎃       ")
    print("🎃                                              OR                                                          🎃       ")
    print("🎃             B: Do you disregard Tommy's claim, since he is most likely paranoid from                     🎃       ")
    print("🎃                   the creepy Halloween movies he has been watching all night?                            🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            print("\n\nGreat Choice! Let's keep surviving the night!")    
            secondScenario()
        elif response.lower() == 'b':
            player.turns -= 1
            player.noOfTurns(player.turns)
            firstScenarioWrong()
            print("Let's try again!")
            firstScenario()
        else: 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def firstScenarioWrong():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                               This was not the best choice to make.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃            After murdering your friend, Michael continues his killing spree throughout the               🎃       ")
    print("🎃             neighborhood, increasing his death toll this Halloween night in Haddonfield.                 🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                      It is recommended you make the right decision next time.                            🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   

def secondScenario():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                ")
    print("🎃                                                                                                          🎃       ")
    print("🎃     After you put the kids to bed, you walk across the street and knock on the front door, but no one    🎃       ")
    print("🎃       answers. You cautiously make your way to the backyard and see that the backdoor is wide open.      🎃       ")
    print("🎃         You make your way into the dark house and up the stairs. In one of the bedrooms, you see         🎃       ")
    print("🎃             Annie's motionless body on the bed. You want to check on Annie, but then you hear            🎃       ")
    print("🎃                                the floor boards squeek behind you.                                       🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                       What will you do?                                                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                  A: Do you run to a nearby phone in the house to call for help?                          🎃       ")
    print("🎃                                              OR                                                          🎃       ")
    print("🎃                  B: Turn, run downstairs, and across the street back to safety?                          🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            secondScenarioWrong()
            print("Let's try again!")
            secondScenario() 
        elif response.lower() == 'b':
            print("\n\nGreat Choice! Let's keep surviving the night!") 
            thirdScenario() 
        else: 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def secondScenarioWrong():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                               This was not the best choice to make.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃            Reaching for a nearby phone, you quickly realize that the phone line is dead, and             🎃       ")
    print("🎃             the 'floor squeaker,' Michael, wastes no time swinging his knife, cutting your               🎃       ")
    print("🎃                                   shirt, and wounding your arm.                                          🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃             Tsk tsk. Your choices are costing you your wardrobe! You are not dead yet, so you            🎃       ")
    print("🎃                        still have a chance to make a better choice next time.                            🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

def thirdScenario():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃        As you return to the Doyle residence, you get into th house and lock the door behind you          🎃       ")
    print("🎃      As you catch your breath and try to compose yourself, you hear a curtain flutter behind you,        🎃       ")
    print("🎃      finding that the window has been left open. You quickly close the window and hastily attempt        🎃       ")
    print("🎃                  to secure the other rooms, but to your dismay, you learn that                           🎃       ")
    print("🎃                                 Michael is already in the house!                                         🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                       What will you do?                                                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                      A: Do you run up the stairs to hide with the children?                              🎃       ")
    print("🎃                                              OR                                                          🎃       ")
    print("🎃              B: Run to the kitchen and grab a butcher knife to duel the masked madman?                   🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            print("\n\nGreat Choice! Let's keep surviving the night!") 
            fourthScenario()   
        elif response.lower() == 'b':
            thirdScenarioWrong()
            print("Let's try again!")
            thirdScenario()
        else: 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def thirdScenarioWrong():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                               This was not the best choice to make.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃        You discover you're not as experienced with your weapon choice as Michael. He swiftly             🎃       ")
    print("🎃                  disarms and injures you again, causing a cut to your upper thigh.                       🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                    Your choice has now left you between a rock and a dead place.                         🎃       ")
    print("🎃                        Choose better next time to keep your limbs intact!                                🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

def fourthScenario():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃     You effectively hide the children, but your own hiding spot in the closet is not the most ideal      🎃       ")
    print("🎃       Despite tying the closet doors shut with a tie you find, Michael begins breaking through the       🎃       ")
    print("🎃        doors. As he pulls his body into the closet to try to reach for you, you grab a hanger            🎃       ")
    print("🎃             and scratch him in the eye, which takes him aback. His vision is compromised,                🎃       ")
    print("🎃                             allowing you to escape from the closet.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                You find a knitting needle and thrust it into his neck, which appears                     🎃       ")
    print("🎃                               to finally put his rampage to an end.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                       What will you do?                                                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                     A: Do you grab the kids and run to the police station?                               🎃       ")
    print("🎃                                              OR                                                          🎃       ")
    print("🎃              B: Send the kids to a neighbor's house to contact the authorities while you                 🎃       ")
    print("🎃                               rest and wait for help to come?                                            🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

    response = input(f"{player.playerName}, choose wisely? A or B? ")

    while True:
        if response.lower() == 'a':
            fourthScenarioWrong()
            print("Let's try again!")
            fourthScenario() 
        elif response.lower() == 'b':
            print("\n\nGreat final choice! Now you can rest. . . but wait. . . ")
            conclusion() 
        else: 
            print(f"\nYou must answer A or B, {player.playerName}.")
            response = input(f"\nWhich do you choose? ")
            Return
print("")

def fourthScenarioWrong():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                               This was not the best choice to make.                                      🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃      The police station is all the way across town, and you don't get too far before the kids            🎃       ")
    print("🎃          get tired and become overly emotional to continue on the journey. Michael somehow               🎃       ")
    print("🎃              survives his injury and takes advantage of your slow pace, catching up to you. Now          🎃       ")
    print("🎃                          up to you. Now three lives are indeed at stake.                                 🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃            The horrors of babysitting kids! Dragging them along was not the best choice.                 🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")

def conclusion():
    print("\n🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃                 ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                                  Ahh!! Michael is still alive!                                           🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃          He runs towards you, raising his arm to deliver one final, fatal swing of his knife.            🎃       ")
    print("🎃         However, Michael's psychiatrist from Smith's Grove Sanitarium, Dr. Loomis, is there to           🎃       ")
    print("🎃            the rescue with his Smith & Wesson Model 15. He uses the revolver on his patient              🎃       ")
    print("🎃                    sending him back flying through a second-floor bedroom window.                        🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃        It is over now. You can rest. You have successfully survived the night. You look out the          🎃       ")
    print("🎃                        broken window and see that Michael is. . . GONE!                                  🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃                         Never forget: 'You can't kill the boogie man!'                                   🎃       ")
    print("🎃                                                                                                          🎃       ")
    print("🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 🎃 \n \n  ")   
    print("")
    exit()

intro()






        



