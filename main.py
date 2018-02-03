import json
from pprint import pprint
import winsound
from random import randint

def move(connections):
    global currCaveNum
    global caves
    global alive
    move_to = int(input("Which cave do you want to move to?"))
    winsound.PlaySound(caves[move_to][5], winsound.SND_FILENAME | winsound.SND_ASYNC)
    if move_to in connections:
        print("you  moved to cave " + str(move_to))
        currCaveNum = move_to
        if caves[currCaveNum][1]:
            print("You fell into the bottomless pit.")
            alive = False
        if caves[currCaveNum][2]:
            print("Before you die, you think you hear the wumpus burp. What bad manners it has.")
            alive = False
        if caves[currCaveNum][0]:
            print("This cave has bats. You are now going to be carried to a random, safe cave.")
            currCaveNum = random_cave()
    else:
       print("You cannot go there")

def shoot(connections, caves):
    shoot_to = int(input("Which cave do you want to shoot to?"))
    if shoot_to not in connections:
        print("You cannot shoot there. Try again")
        shoot(caves[currCaveNum][4], caves)
    if caves[shoot_to][2]:
        print("You shot the wumpus! You quickly escape and win.")
        caves[shoot_to][2] = False
    if caves[shoot_to][0]:
        print("You shot a bat and feel really bad. You promise to plan the funeral as soon as you kill the wumpus.")
        caves[shoot_to][0] = False


def random_cave():
    safeRandomCaveNumber = randint(0, 24)
    while 19 == safeRandomCaveNumber or 8 == safeRandomCaveNumber or 1 == safeRandomCaveNumber or 15 == safeRandomCaveNumber:
        safeRandomCaveNumber = randint(0, 24)
    return safeRandomCaveNumber

def warnings(connections, caves):
    for caveNum in connections:
        if caves[caveNum][0]:
            print("You hear bat's wings flapping.")
        if caves[caveNum][1]:
            print("You feel the pit's breeze.")
        if caves[caveNum][2]:
            print("You smell the wumpus.")

def decision():
    global caves
    global currCaveNum
    print("You are currently in cave " + str(currCaveNum))
    print(caves[currCaveNum][3])
    warnings(caves[currCaveNum][4], caves)
    print("you can go to caves " + str(caves[currCaveNum][4]) + " from here")

    Q = input("move or shoot? (type m for move and s for shoot)").lower()

    if Q == "m":



        move(caves[currCaveNum][4])

    elif Q == "s":

        shoot(caves[currCaveNum][4], caves)

    else:

        print("sorry I couldn't understand you. game over")

caves = json.load(open("caves.json", "r"))

pprint(caves)

#caves.append = [bat, pit, wumpus, text, [connections]]

#cave 19 has wumpus

#cave 8 has pit

#cave 1 has bats
              
#cave 15 has bats

currCaveNum = 0




print("""
YOU ARE A FAMOUS HUNTER DESCENDING DOWN INTO THE CAVES OF DARKNESS,
LAIR OF THE INFAMOUS MAN-EATING WUMPUS.  YOU ARE EQUIPPED WITH FIVE
BENT ARROWS, AND ALL YOUR SENSES.  THERE ARE TWENTY CAVES CONNECTED
BY TUNNELS, AND THERE ARE TWO OTHER KINDS OF HAZARDS:
        A) PITS, WHICH ARE BOTTOMLESS, AND USUALLY FATAL TO FALL
        INTO.  THERE ARE THREE SUCH PITS IN THE NETWORK.
        B) SUPER-BATS, WHICH IF YOU STUMBLE INTO THEIR ROOM WILL
        PICK YOU UP AND DROP YOU IN SOME RANDOM ROOM IN THE NETWORK.
        YOU MAY SHOOT SUPER-BATS, THERE IS ONE IN EACH OF THREE OR
        FOUR ROOMS WITHIN THE NETWORK.  THE SUPER-BATS GENERALLY STAY
        IN THEIR OWN ROOMS, EXCEPT WHEN DISPOSING OF INTRUDERS OR
        SCAVENGING FOR FOOD IN THE PITS.
IF YOU BLUNDER INTO THE SAME ROOM AS THE WUMPUS, YOU LOSE....
THE NORMALLY SLEEPING WUMPUS DOES NOT MOVE (HAVING GORGED HIMSELF UPON
A PREVIOUS HUNTER).  HOWEVER SEVERAL THINGS CAN WAKE HIM UP:
        1) WALKING INTO HIS ROOM,
        2) SHOOTING AN ARROW ANYWHERE IN THE NETWORK,
        3) TRIPPING OVER DEBRIS (CLUMSINESS),
        4) TURNING ON THE LIGHTS, IN ORDER TO SEE WHERE YOU ARE
        HEADED.
IF HE WAKES UP THERE'S A POSSIBILITY HE WILL MOVE, HOWEVER, HE'S TOO
LAZY TO MOVE MORE THAN ONE ROOM BETWEEN SNOOZES.  THE WUMPUS IS TOO
BIG TO BE PICKED UP BY SUPER-BATS AND HAS SUCKER FEET, SO HE DOESN'T
FALL INTO THE PITS.
YOU CAN SMELL THE WUMPUS FROM ONE ROOM AWAY.  YOU WILL
TREMBLE WITH FEAR WHEN HE MOVES ABOUT.  YOU CAN HEAR SUPER-BATS FROM
ONE ROOM AWAY, AND FEEL DRAFTS (FROM BOTTOMLESS PITS) FROM ONE ROOM
AWAY (AND TASTE THE FEAR...).
TO SHOOT AN ARROW TYPE 'SHOOT' INSTEAD OF A MOVE, AND THEN
SPECIFY WHICH ROOMS THE ARROW SHOULD PASS THROUGH.  YOU ARE STRONG
ENOUGH TO SHOOT IT THROUGH AS MANY AS ONE ROOM.  BENT ARROWS HAVE
NO PROBLEM ROUNDING CORNERS OF LESS THAN 743 DEGREES.  IF YOU
SPECIFY AN IMPOSSIBLE PATH THE ARROW WILL RICOCHET OFF THE WALLS OF
THE ROOM, LOSING SPEED, AND WILL EVENTUALLY COME TO REST IN ONE OF
THE ADJOINING ROOMS.  THE PATH MAY BE TERMINATED BY SPECIFYING ROOM 0.
EACH ROOM IS CONNECTED TO THREE OTHER ROOMS BY THREE TUNNELS A, B
AND C.  YOU MUST ALWAYS MOVE BETWEEN ROOMS BY SPECIFYING WHICH
TUNNEL YOU WISH TO EXPLORE.  YOU CAN ALWAYS RETRACE YOUR FOOT STEPS
BY MOVING BACK USING THE SAME TUNNEL DESIGNATOR.
IF YOU WISH TO SEE WHICH ROOMS ARE AT THE ENDS OF THE TUNNELS YOU
MAY TYPE 'LIGHTS ON' INSTEAD OF A MOVE.  THIS MAY BE AN UNHEALTHY
LUXURY HOWEVER BECAUSE THE LIGHT GIVES THE WUMPUS INSOMNIA.  TO
EXTINGUISH THE LIGHTS SIMPLY TYPE 'LIGHTS OFF'.
                GOOD LUCK HUNTING!!
                """)

alive = True

while alive and caves[19][2]:

    decision()


