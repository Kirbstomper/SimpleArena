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
                if(stat == 'B'):
                    self.body += 1
                if (stat=='P'):
                    self.punch +=1




class monster:
    health = 0
    body = 0
    smarts = 0
    name = ""
    description = ""

    def __init__(self,sName,sHealth, sBody,sSmarts,sPunch):
        self.name = sName
        self.body = sBody
        self.smarts = sSmarts
        self.punch = sPunch
        self.health = sHealth
    de