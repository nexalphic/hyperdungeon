import random

doortypes = {
    0: "worn",
    50: "good",
    70: "strong",
    90: "fortified",
    "last": "vault",
}
def genDoorstrength():
    door = []
    randDoortype = random.randrange(0, 100)
    for key in doortypes:
        if randDoortype <= key:
            door.append(doortypes[key])
            break

def genDoorstuck():
    randDoortype = random.randrange(0, 100)
    if randDoortype > 66:
        door.append("stuck")
    else:
        door.append("unstuck")

class Door(object):
    def __init__(self, doorStrength):
        self.doorStrength = genDoorstrength()
        self.doorStuck = genDoorstuck()


def generateRoom(level):
    room = []
    for i in random.randrange(0, 4):
        room.append(generateDoor())
