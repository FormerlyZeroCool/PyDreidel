import random
players = []
startingGelt = 10
class Object():
    pass
player = Object()
player.name = "a"
while len(player.name) > 0:
    print("press enter to skip.")
    player = Object()
    player.name = input("Next player name: ")
    player.gelt = startingGelt
    if len(player.name) > 0:
        players.append(player)
pot = 0

while len(players) > 1:
    input("Press enter to continue\n\n\n")
    players.reverse()
    for player in players:
        pot += 1
        player.gelt -= 1
        print(player.name,"gave one gelt to the pot")
    print()

    playersLost = 0
    for x in range(len(players)):
        player = players[x - playersLost]
        print("The pot has", pot, "gelt in it!\n")
        input("Press enter to spin " + player.name)
        spinValue = random.randint(1, 4)
        if spinValue == 1:
            print(player.name, "Spun a Gimel", end = ' ')
            player.gelt += pot
            pot -= pot
        elif spinValue == 2:
            print(player.name, "Spun a Shin", end = ' ')
            if(player.gelt > 0):
                player.gelt -= 1
                pot += 1
        elif spinValue == 3:
            print(player.name, "Spun a Hey", end = ' ')
            player.gelt += pot // 2
            pot -= pot // 2
        else:
            print(player.name, "Spun a Non", end = ' ')
        print("and has", player.gelt, "gelt!")
        if(player.gelt <= 0):
            print(player.name, "has lost!")
            players.remove(player)
            playersLost += 1
if(len(players) > 0):
    print(players[0].name, "Has won it all!")
