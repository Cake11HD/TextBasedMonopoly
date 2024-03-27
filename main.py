## Sam, Ruairi, Mircea, Shreya, Victoria
## Computer Science Group Project

import random

# Base class for spaces
class Space:
    def __init__(self, name, index):
        self.name = name
        self.index = index

# Class for players
class Player:
    def __init__(self, name, location, properties, balance=1500, jailed=False):
        self.name = name
        self.balance = balance
        self.location = location
        self.properties = properties
        self.jailed = jailed

    # Add or remove money
    def makePayment(self, amount):
        self.balance += amount

# Base class for all property spaces
class Property(Space):
    def __init__(self, name, index, colour, value, owner, penaltyValue, owned=False):
        super().__init__(name, index)
        self.name = name
        self.colour = colour
        self.value = value
        self.owner = owner
        self.penaltyValue = penaltyValue
        self.owned = owned

# Chance class
class Chance(Space):
    def __init__(self, name, index):
        super().__init__(name, index)

    def generateCard(self):
        pass

# Station Class
class Station(Space):
    def __init__(self, name, index, price, owner, isOwned=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.price = price
        self.owner = owner
        self.isOwned = isOwned

# Community Chest Class
class CommunityChest(Space):
    def __init__(self, name, index):
        super().__init__(name, index)

    # Function to pull random card from deck and return it
    def generateCard(self):
        pass

# Go class
class Go(Space):
    def __init__(self, name, index, payout=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.payout = payout

# Free parking class (most useless space bro)
class FreeParking(Space):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.name = name
        self.index = index

# Utilities class
class Utilities(Space):
    def __init__(self, name, index, cost=150, isOwned=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.cost = cost
        self.isOwned = isOwned

# Jail class
class Jail(Space):
    def __init__(self, name, index, timeServable, bail):
        super().__init__(name, index)
        self.name = name
        self.timeServable = timeServable
        self.bail = bail

# Go to jail class
class GoToJail(Space):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.name = name
        self.index = index


### Working on getting this to work, being a dictionary at the moment, will change to 2d array
spaces = ['Go', Brown[0][0], 'Community Chest', Brown[1[1], Tax[0], Stations[0][0],
          Lblue[0][0], 'Chance', Lblue[1][1], Lblue[2][2], 'Jail', Pink[0][0], Utilities[0][0],
          Pink[1][1], Pink[2][2], Stations[1][1], Orange[0][0], 'Community Chest',
          Orange[1][1], Orange[2][2], 'Free Parking', Red[0][0], 'Chance', Red[1][1], Red[2][2],
          Stations[2][2], Yellow[0][0], Yellow[1][1], Utilities[1][1], Yellow[2][2], 'Go To Jail',
          Green[0][0], Green[1][1], 'Community Chest', Green[2][2], Stations[3][3], 'Chance',
          Dblue[0][0], Tax[1][1], Dblue[1][1]]
Brown = [["Old Kent Road","Whitechapel"],[60, 60]]
Lblue = [["The Angel Islington", "Euston Road", "Pentonville Road"],[100, 100, 120]]
Pink = [["Pall Mall","Whitehall", "Northumberland Avenue"],[140, 140, 160]]
Orange = [["Bow Street", "Marlborough Street", "Vine Street"],[180, 180, 200]]
Red = [["Strand", "Fleet Street", "Trafalgar Square"],[220, 220, 240]]
Yellow = [["Leicester Square", "Coventry Street", "Piccadilly"],[260, 260, 280]]
Green = [["Regent Street", "Oxford Street", "Bond Street"],[300, 300, 320]]
Dblue = {"Park Lane": 350, "Mayfair": 400} [[
Stations = {"King's Cross Station": 200, "Marylebone Station": 200, "Fenchurch Street Station": 200, "Liverpool Street Station": 200}
Tax = {"Income Tax": 200, "Luxury Tax": 100}
Utilities = {"Electric Company": 150, "Water Works": 150}
Misc = ("Go", "Chance", "Community Chest", "Free Parking", "Jail", "Go To Jail")


# Roll 2 dice function
def rollDice(rollCounter):
    # Roll die
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    rollCounter += 1
    total = roll1 + roll2
    # Check for double
    if roll1 != roll2:
        print(f'You rolled a {total}! ')
        canRoll = False
        return total
    else:
        print(f'You rolled a double! Move {total} spaces.')
        return total

# Move player function
def moveSpaces(moves, location):
    """Get the current player location index and add the number
    of moves to it. Loop if the index is greater than Mayfair"""
    pass

# Beginning of game loop
def GameLoop():
    # Find palyer count
    playerCount = int(input('How many players will there be? '))

    while True:
        # Go through each player
        for i in range(playerCount):

            rollCounter = 0
            canRoll = True
            while canRoll:
                moves = rollDice(rollCounter)

                pass

    # Roll dice

    # Calculate score

    # Move spaces

    # Check for Go

    # Check for payment

    # Next player

    pass


if __name__ == "__main__":
    GameLoop()

print("Hello World!")
