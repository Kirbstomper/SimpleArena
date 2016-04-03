from main import LevelClass
from mobs import playerClass
from mobs import monsterClass
UserPlayer = playerClass.player("Chris")
testLevel = LevelClass.Level(UserPlayer)

testLevel.setOpening("Welcome to the arena "+UserPlayer.name +",\n Here you will face many challeneges\n have a test against these goblins!")
testLevel.setEnding("Congratulations for completing this level!\n Enjoy more when I create them!")

testLevel.addEnemy([monsterClass.monster("Gobin1",30,5,5,5,10),monsterClass.monster("Gobin2",30,5,5,5,10),monsterClass.monster("Gobin3",30,5,5,5,10)])

testLevel.play()

