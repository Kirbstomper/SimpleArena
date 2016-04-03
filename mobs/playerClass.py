class player:
    health = 100
    magic = 90
    name = ""
    smarts = 2
    punch = 2
    body = 2
    exp = 0

    def __init__(self, sName):
        self.name = sName
        self.alive = True
        self.body = 5
        self.smarts = 5
        self.punch = 5
    #Heals yourself based on the formula
    def healSelf(self):
        if (self.magicCheck(30)):
            self.magic -=30
            self.health += (self.smarts*5)
        else:
            print("You don't have enough mana to heal, manage better")


    # Attacks a monster and deals damage to it
    def act(self,listOfMonsters):
        turnOver = False
        print("Please select your action for the turn")
        while(not turnOver):
            choice = int(input("1 : Fight\n2:Heal\n 3:Cry\n"))
            if(choice==1):
                self.chooseToAttack(listOfMonsters)
                turnOver=True
            elif choice == 2:
                self.healSelf()
                turnOver=True
            elif choice == 3:
                print("You cry, wasting a turn. Baby")
                turnOver=True
            else:
                print("Please enter a real choice")

    def chooseToAttack(self,monList):
        print("Select a monster to attack:")
        for x in range(0,len(monList)):
            print (x+1,monList[x].name,)
        choice = -1
        while(choice<0 or choice> len(monList)):
            choice = (int(input('?')))
        print("You attack:" ,monList[choice-1].name)
        self.attack(monList[choice-1])

    def attack(self,target):
        damage = (self.punch*10) - target.body
        target.takeDamage(damage)
       #simple function to check if enough mana to cast a spell

    #returns if you have enough mana to cast a spell/ability
    def magicCheck(self,val):
        return self.magic>=val

    def takeDamage(self,dam):
        if(self.health-dam <=0):
            self.health = 0
            print(self.name.upper()+" HAS DIED")
            self.alive = False
        else:
            self.health -=dam

    def levelUp(self):
        points = 3
        validIn = True
        while(points!=0):
            while(input):

                print("Please enter a stat to add a point to(s,p.or b) Points remaining:",points)
                stat = input("?")
                stat = str(stat).upper()[0]
                if(stat == 'S'):
                    self.smarts += 1
                    validIn = False
                if(stat == 'B'):
                    self.body += 1
                    validIn = False
                if (stat=='P'):
                    self.punch += 1
                    validIn = False
                print("Please enter an actual stat next time!")

            points-=1

        print("Punch:",self.punch,"Smarts:",self.smarts,"Body:",self.body)
