class monster:
    player = -1

    def setPlayer(sPlayer):
       player = sPlayer

    def __init__(self,sName,sHealth, sBody,sSmarts,sPunch,sThresh):
        self.name = sName
        self.body = sBody
        self.smarts = sSmarts
        self.punch = sPunch
        self.health = sHealth
        self.threshold = sThresh
        self.alive = True
        #Calculates the amount of damage to deal the player

    def calculateDamage(self):
        return self.punch*5
        #Deals damage to the player

    def takeDamage(self,dam):
        if(self.health-dam <=0):
            print (self.name, " has died!")
            self.health = 0
            self.alive = False
        else:
            self.health -=dam
    def act(self):
        if (self.alive):
            if(self.health>self.threshold):
                print(monster.player.name, " Took ")
                monster.player.takeDamage(self.calculateDamage()-monster.player.body*2)
            else:
                healing = 5 + (self.smarts*3)
                print(self.name, " is healing ", healing, " damage!")
                self.health+= healing
        else:
            print(self.name, " lies dead")