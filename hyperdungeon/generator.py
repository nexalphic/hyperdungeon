import random

doortypes = {
    0: "worn",
    50: "good",
    70: "strong",
    90: "fortified",
    101: "vault",
}
def genDoorstrength():
    randDoortype = random.randrange(0, 100)
    n = 0
    for key in doortypes:
        if randDoortype <= key:
            return (doortypes[n])
        else:
            n +=1

def genDoorstuck():
    randDoortype = random.randrange(0, 100)
    if randDoortype > 66:
        return "stuck"
    else:
        return "unstuck"

class Door():
    def __init__(self):
        self.doorStrength = genDoorstrength()
        self.doorStuck = genDoorstuck()


def generateRoom(level):
    room = []
    for i in range(0, random.randint(0, 4)):
        door = Door()
        room.append(door)
        return room

print generateRoom(1)[0].doorStrength
