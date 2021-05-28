import random
weapons = ["Sword", "Fire"]
spells = ["Healing","Harming"]
shields = ["Armor","Shield", "Water"]

class Player1:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.weapon = 0
    self.shield = 0

  def damage(self):
      points = random.randint(10,35)
      self.health -= points

  def healing(self):
        points = random.randint(20, 30)
        self.health += points

  def selectWeapon(self):
        choice = int(input("Player 1,Choose your weapon 1-Sword, 2-Fire:  "))
        self.weapon = choice - 1
  
  def selectSpell(self):
        choice = int(input("Player 1, Choose your spell 1-Healing or 2-Harming:  "))
        self.spell = choice - 1

  def selectShield(self):
        choice = int(input("Player 1, Choose your shield 1-Armor, 2-Shield, or 3-Water:  "))
        self.shield = choice - 1

class Player2:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        self.shield = 0

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points

    def healing(self):
        points = random.randint(20, 30)
        self.health += points

    def selectWeapon(self):
        choice = int(input("Player 2, Choose your weapon 1-Sword or 2-Fire:  "))
        self.weapon = choice - 1

    def selectSpell(self):
        choice = int(input("Player 2, Choose your spell 1-Healing or 2-Harming:  "))
        self.spell = choice - 1


    def selectShield(self):
        choice = int(input("Player 2, Choose your shield 1-Armor, 2-Shield, or 3-Water:  "))
        self.shield = choice - 1

class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" %(self.round))  

    # Check if either or both Players is below zero health
    def checkWin(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.gameOver = True
            print("You Lose")
        elif opponent.health < 1 and player.health > 0:
            self.gameOver = True
            print("You Win")
        elif player.health < 1 and Player2.health < 1:
            self.gameOver = True
            print("*** Draw ***")


    def displayResult(self, player, opponent):
            print("%s used a %s, %s used a %s\n" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s caused damage to %s\n" %(player.name, opponent.name))
            print("%s used a %s, %s used a %s Shield\n" % (player.name, spells[player.spell], opponent.name, shields[opponent.shield]))

    def takeTurn(self, player, opponent):

        # Decision Array
        #
        #           Armour| Shield |  Water
        #           ______|________|_______
        # Sword:    False |  True  |  True
        # Spell:    True  |  False |  True   
        # Fire :    True  |  True  |  False

        decisionArray = [[False, True, True], [True, False, True], [True, True, False]]
        if decisionArray[player.weapon][opponent.shield]:
            opponent.damage()
            currentGame.displayResult(player, opponent)
        if decisionArray[player.spell][opponent.shield]:
            opponent.damage()
        if decisionArray[player.spell]:
            player.healing()
        
        else:
            print("\n%s used a %s, %s used a %s Shield" %(player.name, weapons[player.weapon], opponent.name, shields[opponent.shield]))
            print("%s blocked %s's attack - No Damage" %(opponent.name, player.name))


# Setup Game Objects
currentGame = Game()
human = Player1("Player1")
human2 = Player2("Player2")

players = [human, human2]

# Main Game Loop
while not currentGame.gameOver:
    for player in players:
        player.selectWeapon()
        player.selectShield()
        player.selectSpell()
    currentGame.newRound()
    currentGame.takeTurn(human, human2)
    currentGame.takeTurn(human2, human)
    print("%s's health = %d" %(human.name, human.health))
    print("%s's health = %d" %(human2.name, human2.health))
    currentGame.checkWin(human, human2)
