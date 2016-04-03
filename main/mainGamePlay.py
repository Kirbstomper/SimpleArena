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
testLevel.addEnemy([monsterClass.Goblin("Gobin Sukr"),monsterClass.Goblin("Gobin Gxudz"),monsterClass.Goblin("Goblin Grexut")])
testLevel.play()
UserPlayer.healForMatch()

print("You retire back to your room for the night tried but confident from todays victory.\n You hear screams from the outside, but by the morning they are silent to you.")

#Level 2. Includes a Necromancer who can summon shit
NecroFight = LevelClass.Level(UserPlayer)
NecroFight.setOpening("Today's opponent is a Necromancer and his minions.\n The rookie can't possibly win this fight.")
NecroFight.setEnding("TODAYS VICTOR IS "+ UserPlayer.name+". \n Who somehow killed the one who thrives on death.\n IS THIS PERSON NOT A MORTAL?")
NecroFight.addEnemy()