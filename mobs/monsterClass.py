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

    # This monster has the uniqe ability to raise a fallen comrade from the dead as a skull warrior!
class Necromancer(monster):
    def __init__(self,sName,sListOfMonsters):
        self.name = sName
        self.mana = 100
        self.body = 10
        self.punch = 3
        self.smarts = 7
        self.health = 100
        self.threshold = 50
        self.alive = True
        self.Allies = sListOfMonsters

    def act(self):

        if self.alive:
            # Loops to see who is dead, and revives the first person that he sees
            for x in self.Allies:
               # print(x.name)
                if(not x.alive)&(self.mana>10):
                    print(x.name + " has been reanimated as a skull man!!")
                    x = SkullWarrior()
                    print(x.name)
                    self.mana-=10


            # heals all allies 20 HP as his turn action NO MP NEEDED SUCKAS
            self.Allies.append(SkullWarrior())
            for x in self.Allies:
                x.health += 20
                x.setPlayer(self.player)



    #This class are the minions that the Necromancer can summon his side, weak but can swarm if not taken care of
class SkullWarrior(monster):

    def __init__(self):
        self.name = "Skull Warrior"
        self.body = 3
        self.smarts = 0
        self.punch = 3
        self.alive = True
        self.health = 10

    def act(self):
        if(self.alive):
            #print("ACTING")
            self.player.takeDamage(10)


class Manticore(monster):

    def __init__(self):
        self.name = "Mannticore"
        self.body = 10
        self.smarts = 3
        self.punch = 15
        self.alive = True
        self.health = 250
        self.poisonDealt = 0
        self.threshold = 100

        # Each turn the manticore adds a poison counter
    def act(self):
        if(self.alive):
            if(self.poisonDealt>0):
                print("Poison damage!")
                self.player.takeDamage(self.poisonDealt*10)
            #The manticore also has a rage mode!
            if(self.health<=self.threshold):
                print("The Manticore attacks with rage!")
                self.player.takeDamage(self.calculateDamage())

            self.player.takeDamage(self.calculateDamage())
            self.poisonDealt += 1



class Friend(monster):

    def __init__(self,sName):
        self.name = sName
        self.health = 400
        self.magic = 200
        self.body = 20
        self.smarts = 20
        self.punch = 25
        self.alive = True
        self.threshold = 100


    def act(self):
        if self.alive:
            print("YOU MUST DIE!")
            if (self.magic >= 50):
                self.magic -=50
                print(self.name + " has thrown a fire ball!")
                self.player.takeDamage(self.smarts*2)
            if (self.health <= self.threshold):
                print(self.player.name + " don't.... you... remember")
            if (self.health <= 50):
                print("we...should be...friends....")

