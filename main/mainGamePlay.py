from mobs import playerClass
from mobs import monsterClass
from main import LevelClass
from main import *
print("Welcome to simple area 2016!\n\n\n")
print("You have been taken captive by people unknown, please enter a name you wish to go by")
playerName = input(">")
print("You have a friend don't you? what is their name?")
friendName = input(">")
UserPlayer = playerClass.player(playerName)

print("Are you a strong one?, smart one?, or tough one?")
buff = input(">")
if(buff == "strong"):
    UserPlayer.punch+=5
if(buff == "smart"):
    UserPlayer.smarts+=5
if(buff == "tough"):
    UserPlayer.smart+=5

print("Thank you for your cooperation, may the odds in the arena be ever in your favor")
#Tutorial Level
testLevel = LevelClass.Level(UserPlayer)
testLevel.setOpening("Welcome to the arena "+UserPlayer.name +",\n Here you will face many challeneges\n have a test against these goblins!")
testLevel.setEnding("You survived? While I am impressed don't expect us to go easy on you the next time....")
testLevel.addEnemy([monsterClass.monster("Gobin Sukr",30,5,5,5,10),monsterClass.monster("Gobin Gxudz",30,5,5,5,10),monsterClass.monster("Goblin Grexut ",30,5,5,5,10)])
testLevel.play()



