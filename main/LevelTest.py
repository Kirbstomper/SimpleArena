from mobs import monsterClass
from mobs import playerClass

exampleMon = monsterClass.monster("Goblin",50,2,3,3,10)
ListOfMonsters = [exampleMon]
exUser = playerClass.player("Chris")
exampleMon.setPlayer(exUser)

for x in ListOfMonsters:
        x.setPlayer(exUser)
while (True):
    exUser.act(ListOfMonsters)
    for x in ListOfMonsters:
        x.act()

    print(exUser.health)