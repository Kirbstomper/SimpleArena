class player:
    health = 100
    magic = 0
    name = ""
    smarts = 0
    punch = 0
    body = 0
    exp = 0
    def __init__(self, sName):
        name = sName

    #Heals yourself based on the formula
    def HealSelf(self):
        if (self.magicCheck(30)):
            self.magic -=30
            self.health += (self.smarts*5)

    # Attacks a monster and deals damage to it
    def attack(self,target:monster):
        damage = (self.punch*10) - target.body
        target.takeDamage(damage)
       #simple function to check if enough mana to cast a spell

    #returns if you have enough mana to cast a spell/ability
    def magicCheck(self,val):
        return self.magic>=val

    def levelUp(self):
        points = 3
        input = True
        while(points!=0):
            while(input):

                print("Please enter a stat to add a point to(s,p.or b) Points remaining:",points)
                stat = input("?")
                stat = str(stat).upper()[0]
                if(stat == 'S'):
                    self.smarts +=1
                    input = False
                if(stat == 'B'):
                    self.body += 1
                    input = False
                if (stat=='P'):
                    self.punch +=1
                    input = False
                print("Please enter an actual stat next time!")

            points-=1

        print("Punch:",self.punch,"Smarts:",self.smarts,"Body:",self.body)

## The monster class base any extenstions done will be to add some challenge
class monster:

    player = -1

    def setPlayer(self,sPlayer):
       self.player = sPlayer

    def __init__(self,sName,sHealth, sBody,sSmarts,sPunch,sThresh):
        self.name = sName
        self.body = sBody
        self.smarts = sSmarts
        self.punch = sPunch
        self.health = sHealth
        self.threshold = sThresh

        #Calculates the amount of damage to deal the player

    def calculateDamage(self):
        return self.punch*5
        #Deals damage to the player

    def takeDamage(self):


    def act(self):
        if(self.health>self.threshold):
                print(player.name, " Took ")
                player.takedamage(self.calculateDamage()-player.body*2)
        else:
            healing = 5 + (self.smarts*3)
            print(self.name, " is healing ", healing, " damage!")
            self.health+= healing