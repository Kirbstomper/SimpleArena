class Level:
    openingStory = ""
    endingStory = ""
    LevelEnemies = []

    def __init__(self,player):
        self.openingStory = ""
        self.endingStory  = ""
        self.LevelEnemies = []
        self.player = player

    def setOpening(self,oText):
        self.openingStory = oText

    def setEnding(self,eText):
        self.endingStory=  eText

    def addEnemy(self,listOfEnemies):
        for x in listOfEnemies:
            self.LevelEnemies.append(x)
            x.setPlayer(self.player)
    def battle(self):
        while(True):
            print(self.player.name + ": Health:"+str(self.player.health) + "Mana:"+str(self.player.magic))
            self.player.act(self.LevelEnemies)
            for x in self.LevelEnemies:
                x.act()
            print("\n")

            # If all enemies are dead, returns to exit the function
            if (all(x.alive == False for x in self.LevelEnemies)):
                print("\n")
                return
            if(self.player.alive == False):
                self.setEnding("Such a sad fate, you have died. Try again some other day!")
                return

        #levels the player up at the end!
    def LevelPlayerUp(self):
        print("You leveled up!")
        self.player.levelUp()

    def play(self):
        print(self.openingStory)
        self.battle()
        #self.LevelPlayerUp()
        print(self.endingStory)
