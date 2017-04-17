import random

doortypes = {
    0: "worn",
    50: "good",
    70: "strong",
    90: "fortified",
    "last": "vault",
}

def generateDoor():
    door = []
    randDoortype = random.randomrand(0, 100)
    randDoortype = random.randrange(0, 100)
    for key in doortypes:
        if randDoortype <= key:
            break

def generateRoom(level):
    for i in random.randrange(0, 4):

