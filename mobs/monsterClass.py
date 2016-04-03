class monster:

    def setPlayer(self,sPlayer):
       self.player = sPlayer

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
        damageToTake =(dam-self.body)
        if((self.health-damageToTake)<=0):
            print (self.name, " has died!")
            self.health = 0
            self.alive = False
        else:
            print(self.name+" took " + str(damageToTake))
            self.health -=dam
    def act(self):
        if (self.alive):
            if(self.health>self.threshold):
                #print(self.player.name)
                self.player.takeDamage(self.calculateDamage())
            else:
                healing = 5 + (self.smarts*3)
                print(self.name, " is healing ", healing, " damage!")
                self.health+= healing
        else:
            print(self.name + "lies dead")



# really dumb goblins, easy to defeat
class Goblin(monster):
    def __init__(self,sName):
        self.name = sName
        self.body = 5
        self.punch = 5
        self.smarts = 2
        self.health = 30
        self.threshold = 5
        self.alive = True

    def act(self):
        if(self.alive):
            if(self.health>self.threshold):
                damage = self.calculateDamage()
                self.player.takeDamage(damage)

            else:
                print(self.name+ " is healing 10 HP!" )
                self.health+=10
        else:
            print(self.name + " lies on their arms dead")

    # This monster has the uniqe ability to raise a fallen comrade from the dead as a skellington warrior!
class Necromancer(monster):
    def __init__(self,sName,sListOfMonsters):
        self.name = sName
        self.body = 10
        self.punch = 3
        self.smarts = 7
        self.health = 100
        self.threshold = 50
        self.alive = True
        self.Allies = sListOfMonsters

    def act(self):





    #This class are the minions that the Necromancer can summon his side, weak but can swarm if not taken care of
class SkullWarrior(monster):
